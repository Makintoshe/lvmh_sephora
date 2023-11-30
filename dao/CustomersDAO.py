from dao import ModelDAO
from model.CustomersM import Customers

class CustomersDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet CustomersDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Customers) -> int:
        '''
        Insère un objet dans la table Customers.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO customers (customer_id, customer_name, email, phone_number) 
                           VALUES (%s, %s, %s, %s);'''
            self.cur.execute(query, (objIns.getCustomerID(), objIns.getCustomerName(), objIns.getEmail(),
                                     objIns.getPhoneNumber()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_CustomersDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def insererToutList(self, objInsList: list[Customers]) -> int:
        '''
        Insère une liste d'objets dans la table Customers.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO customers (customer_id, customer_name, email, phone_number) 
                           VALUES (%s, %s, %s, %s);'''
            self.cur.executemany(query, [(obj.getCustomerID(), obj.getCustomerName(), obj.getEmail(), obj.getPhoneNumber()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_CustomersDAO.insererToutList() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def trouverUn(self, cleTrouv) -> Customers:
        '''
        Trouve un objet dans la table Customers par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM customers WHERE customer_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                customer = Customers()
                customer.setCustomerID(res[0])
                customer.setCustomerName(res[1])
                customer.setEmail(res[2])
                customer.setPhoneNumber(res[3])

                return customer
            else:
                return None
        except Exception as e:
            print(f"Erreur_CustomersDAO.trouverUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverTout(self) -> list[Customers]:
        '''
        Récupère tous les enregistrements de la table Customers.

        :return: Une liste d'objets Customers.
        '''
        try:
            query = '''SELECT * FROM customers;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_customers = []

            if len(res) > 0:
                for r in res:
                    customer = Customers()
                    customer.setCustomerID(r[0])
                    customer.setCustomerName(r[1])
                    customer.setEmail(r[2])
                    customer.setPhoneNumber(r[3])

                    liste_customers.append(customer)

                return liste_customers
            else:
                return None
        except Exception as e:
            print(f"Erreur_CustomersDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUn(self, cleTrouv) -> list[Customers]:
        '''
        Récupère tous les enregistrements de la table Customers par une clé spécifique.

        :param cleTrouv: La clé de recherche.
        :return: Une liste d'objets Customers.
        '''
        try:
            query = '''SELECT * FROM customers WHERE customer_name = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_customers = []

            if len(res) > 0:
                for r in res:
                    customer = Customers()
                    customer.setCustomerID(r[0])
                    customer.setCustomerName(r[1])
                    customer.setEmail(r[2])
                    customer.setPhoneNumber(r[3])

                    liste_customers.append(customer)

                return liste_customers
            else:
                return None
        except Exception as e:
            print(f"Erreur_CustomersDAO.trouverToutParUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUnLike(self, val) -> list[Customers]:
        '''
        Récupère tous les enregistrements de la table Customers par une clé similaire.

        :param val: La clé de recherche similaire.
        :return: Une liste d'objets Customers.
        '''
        try:
            query = '''SELECT * FROM customers WHERE customer_name LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_customers = []

            if len(res) > 0:
                for r in res:
                    customer = Customers()
                    customer.setCustomerID(r[0])
                    customer.setCustomerName(r[1])
                    customer.setEmail(r[2])
                    customer.setPhoneNumber(r[3])

                    liste_customers.append(customer)

                return liste_customers
            else:
                return None
        except Exception as e:
            print(f"Erreur_CustomersDAO.trouverToutParUnLike() ::: {e}")
        finally:
            self.cur.close()

    def modifierUn(self, cleAnc, objModif: Customers) -> int:
        '''
        Modifie un enregistrement dans la table Customers.

        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE customers SET customer_name = %s, email = %s, phone_number = %s
                           WHERE customer_id = %s;'''
            self.cur.execute(query, (objModif.getCustomerName(), objModif.getEmail(), objModif.getPhoneNumber(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_CustomersDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table Customers.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''DELETE FROM customers WHERE customer_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_CustomersDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def depensesMoyennes(self) -> float:
        pass

    def filtrerCmdByStatus(self) -> list:
        pass

    def sortProductByPrice(self) -> list:
        pass

    def searchPleinText(self) -> list:
        pass

    def creerUser(self, pwd, usr) -> object:
        pass

    def creerRole(self, role) -> int:
        pass

    def attribuerRole(self, usr, role) -> int:
        pass