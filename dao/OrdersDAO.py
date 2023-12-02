from dao import ModelDAO
from model.OrdersM import Orders
from model.CustomersM import Customers

class OrdersDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet OrdersDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Orders) -> int:
        '''
        Insère un objet dans la table Orders.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO orders (order_id, customer_id, order_date, status) 
                       VALUES ((SELECT MAX(order_id)+1 as order_id FROM orders), %s, %s, %s);'''
            self.cur.execute(query, (objIns.getCustomerID().getCustomerID(),
                                     objIns.getOrderDate(), objIns.getStatus()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_OrdersDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def insererToutList(self, objInsList: list[Orders]) -> int:
        '''
        Insère une liste d'objets dans la table Orders.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        pass

    def trouverUn(self, cleTrouv) -> Orders:
        '''
        Trouve un objet dans la table Orders par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM orders WHERE order_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                order = Orders()
                order.setOrderID(res[0])
                customer = Customers()
                customer.setCustomerID(res[1])
                order.setCustomerID(customer)
                order.setOrderDate(res[2])
                order.setStatus(res[3])

                return order
            else:
                return None
        except Exception as e:
            print(f"Erreur_OrdersDAO.trouverUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverTout(self) -> list[Orders]:
        '''
        Récupère tous les enregistrements de la table Orders.

        :return: Une liste d'objets Orders.
        '''
        try:
            query = '''SELECT * FROM orders;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            orders_list = []

            if len(res) > 0:
                for r in res:
                    order = Orders()
                    order.setOrderID(r[0])
                    customer = Customers()
                    customer.setCustomerID(r[1])
                    order.setCustomerID(customer)
                    order.setOrderDate(r[2])
                    order.setStatus(r[3])

                    orders_list.append(order)

                return orders_list

            else:
                return None
        except Exception as e:
            print(f"Erreur_OrdersDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUn(self, cleTrouv) -> list[Orders]:
        '''
        Récupère toutes commandes d'un client.

        :param cleTrouv: La clé du client.
        :return: Une liste d'objets Orders.
        '''
        try:
            query = '''SELECT * FROM brands WHERE customer_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_b = []

            if len(res)>0:

                for r in res:
                    o = Orders()

                    o.setOrderID(r[0])
                    o.se(r[1])

                    liste_b.append(o)

                return liste_b

            else:

                return None
        except Exception as e:
            print(f"Erreur_OrdersDAO.trouverToutParUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUnLike(self, cleTrouv) -> list[Orders]:
        '''
        Récupère tous les enregistrements de la table Orders par une clé similaire.

        :param cleTrouv: La clé de recherche similaire.
        :return: Une liste d'objets Orders.
        '''
        pass

    def modifierUn(self, cleAnc, objModif: Orders) -> int:
        '''
        Modifie un enregistrement dans la table Orders.

        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE orders SET order_date = %s, status = %s WHERE order_id = %s;'''
            self.cur.execute(query, (objModif.getOrderDate(), objModif.getStatus(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_OrdersDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()


    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table Orders.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''DELETE FROM orders WHERE order_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_OrdersDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def depensesMoyennes(self) -> float:
        pass

    def filtrerCmdByStatus(self, statut, idCust) -> list:
        try:
            query = f'''SELECT o.order_id, o.order_date,
                          CASE 
                            WHEN o.status = 'Expédiée' THEN 'vous pouvez encore annuler'
                            WHEN o.status = 'Livrée' THEN 'impossible de modifier ou annuler'
                            WHEN o.status = 'Annulée' THEN 'aucune possibilité'
                            WHEN o.status = 'En attente' THEN 'vous pouvez encore modifier ou annuler'
                            ELSE 'contactez le service client'
                          END
                   FROM orders o
                   WHERE o.status=%s AND o.customer_id=%s;'''

            self.cur.execute(query, (statut,idCust))
            res = self.cur.fetchall()

            liste_s = []

            if len(res) > 0:
                for r in res:
                    o = Orders()

                    o.setOrderID(r[0])
                    o.setOrderDate(r[1])
                    o.setStatus(r[2])  # Utilisez l'index 2 pour récupérer la colonne calculée

                    liste_s.append(o)

                return liste_s
            else:
                return None
        except Exception as e:
            print(f"Erreur_OrdersDAO.filtrerCmdByStatus() ::: {e}")
        finally:
            self.cur.close()

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