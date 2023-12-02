from datetime import date
from model.InvoicesM import Invoices
from dao import ModelDAO
from dao.OrdersDAO import Orders

class InvoicesDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet InvoicesDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Invoices) -> int:
        '''
        Insère un objet dans la table Invoices.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO invoices (invoice_id, order_id, invoice_date, total_amount) 
                       VALUES ((SELECT MAX(invoice_id)+1 as invoice_id FROM invoices), %s, %s, %s);'''
            self.cur.execute(query, (objIns.getOrderID(), objIns.getInvoiceDate(), objIns.getTotalAmount()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_InvoicesDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def insererToutList(self, objInsList: list[Invoices]) -> int:
        '''
        Insère une liste d'objets dans la table Invoices.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO invoices (invoices_id, order_id, invoice_date, total_amount) 
                       VALUES (%s, %s, %s, %s);'''
            self.cur.executemany(query, [(obj.getInvoiceID(), obj.getOrderID(), obj.getInvoiceDate(), obj.getTotalAmount()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_InvoicesDAO.insererToutList() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def trouverUn(self, cleTrouv) -> Invoices:
        '''
        Trouve un objet dans la table Invoices par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM invoices WHERE invoice_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                invoice = Invoices()
                invoice.setInvoiceID(res[0])
                o = Orders()
                o.setOrderID(res[1])
                invoice.setOrderID(o)
                invoice.setInvoiceDate(res[2])
                invoice.setTotalAmount(res[3])

                return invoice
            else:
                return None
        except Exception as e:
            print(f"Erreur_InvoicesDAO.trouverUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverTout(self) -> list[Invoices]:
        '''
        Récupère tous les enregistrements de la table Invoices.

        :return: Une liste d'objets Invoices.
        '''
        try:
            query = '''SELECT * FROM invoices;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_invoices = []

            if len(res) > 0:
                for r in res:
                    invoice = Invoices()
                    invoice.setInvoiceID(r[0])
                    o = Orders()
                    o.setOrderID(res[1])
                    invoice.setOrderID(o)
                    invoice.setInvoiceDate(r[2])
                    invoice.setTotalAmount(r[3])
                    liste_invoices.append(invoice)

                return liste_invoices
            else:
                return None
        except Exception as e:
            print(f"Erreur_InvoicesDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUn(self, cleTrouv) -> list[Invoices]:
        '''
        Récupère tous les enregistrements de la table Invoices par une clé spécifique.

        :param cleTrouv: La clé de recherche.
        :return: Une liste d'objets Invoices.
        '''
        try:
            query = '''SELECT * FROM invoices WHERE order_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_invoices = []

            if len(res) > 0:
                for r in res:
                    invoice = Invoices()
                    invoice.setInvoiceID(r[0])
                    invoice.setOrderID(r[1])
                    invoice.setInvoiceDate(r[2])
                    invoice.setTotalAmount(r[3])
                    liste_invoices.append(invoice)

                return liste_invoices
            else:
                return None
        except Exception as e:
            print(f"Erreur_InvoicesDAO.trouverToutParUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUnLike(self, cleTrouv) -> list[Invoices]:
        '''
        Récupère tous les enregistrements de la table Invoices par une clé similaire.

        :param cleTrouv: La clé de recherche similaire.
        :return: Une liste d'objets Invoices.
        '''
        try:
            query = '''SELECT * FROM invoices WHERE order_id LIKE %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_invoices = []

            if len(res) > 0:
                for r in res:
                    invoice = Invoices()
                    invoice.setInvoiceID(r[0])
                    o = Orders()
                    o.setOrderID(res[1])
                    invoice.setOrderID(o)
                    invoice.setInvoiceDate(r[2])
                    invoice.setTotalAmount(r[3])
                    liste_invoices.append(invoice)

                return liste_invoices
            else:
                return None
        except Exception as e:
            print(f"Erreur_InvoicesDAO.trouverToutParUnLike() ::: {e}")
        finally:
            self.cur.close()

    def modifierUn(self, cleAnc, objModif: Invoices) -> int:
        '''
        Modifie un enregistrement dans la table Invoices.

        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE invoices SET order_id = %s, invoice_date = %s, total_amount = %s 
                       WHERE invoice_id = %s;'''
            self.cur.execute(query, (objModif.getOrderID(), objModif.getInvoiceDate(), objModif.getTotalAmount(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_InvoicesDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table Invoices.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''DELETE FROM invoices WHERE invoice_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_InvoicesDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def depensesMoyennes(self, idCustomer) -> float:
        '''
        Calcule la moyenne des dépenses effectuées par les clients.

        :return: La moyenne des dépenses.
        '''
        try:
            query = f'''SELECT depenses_moyenne({idCustomer});'''
            self.cur.execute(query)
            res = self.cur.fetchone()

            if res:
                return res
            else:
                return None
        except Exception as e:
            print(f"Erreur_InvoicesDAO.depensesMoyennes() ::: {e}")
        finally:
            self.cur.close()

    def filtrerCmdByStatus(self, status: str) -> list[Invoices]:
        '''
        Filtrage des commandes par statut.

        :param status: Le statut à filtrer.
        :return: Une liste de commandes filtrée.
        '''
        pass

    def sortProductByPrice(self) -> list[Invoices]:
        '''
        Trie les commandes par prix total.

        :return: Une liste de commandes triées.
        '''
        pass

    def searchPleinText(self, query: str) -> list[Invoices]:
        '''
        Effectue une recherche plein texte.

        :param query: La requête de recherche.
        :return: Une liste de résultats de recherche.
        '''
        pass



    def creerUser(self, pwd, usr) -> object:
        '''
        Crée un nouvel utilisateur.

        :param pwd: Le mot de passe de l'utilisateur.
        :param usr: Le nom d'utilisateur.
        :return: L'objet utilisateur créé.
        '''
        pass

    def creerRole(self, role) -> int:
        '''
        Crée un nouveau rôle.

        :param role: Le rôle à créer.
        :return: Le nombre de lignes affectées.
        '''
        pass

    def attribuerRole(self, usr, role) -> int:
        '''
        Attribue un rôle à un utilisateur.

        :param usr: L'utilisateur auquel attribuer le rôle.
        :param role: Le rôle à attribuer.
        :return: Le nombre de lignes affectées.
        '''
        pass