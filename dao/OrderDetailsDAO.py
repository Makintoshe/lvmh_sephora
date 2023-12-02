from dao import ModelDAO
from model.OrderDetailsM import OrderDetail
from model.OrdersM import Orders
from model.ProductsM import Products

class OrderDetailsDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet OrdersDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: OrderDetail) -> int:
        '''
        Insère un objet dans la table OrderDetails.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO order_details (order_id, order_detail_id, product_id, quantity, total_price) 
                       VALUES(%s, %s, %s, %s, %s);'''
            self.cur.execute(query, (objIns.getOrderID(), objIns.getOrderID(), objIns.getProductID(),
                                     objIns.getQuantity(), objIns.getTotalPrice()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_OrderDetailsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def insererToutList(self, objInsList: list[OrderDetail])->int:
        '''
        Insère une liste d'objets dans la table OrderDetails.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            for obj in objInsList:
                query = '''INSERT INTO order_details(order_detail_id, order_id, product_id, quantity, total_price) 
                           VALUES( (SELECT MAX(order_detail_id)+1 as order_detail_id FROM order_details), %s, %s, %s, %s);'''
                self.cur.execute(query, (obj.getOrderID(), obj.getProductID(), obj.getQuantity(), obj.getTotalPrice()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_OrderDetailsDAO.insererToutList() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def trouverUn(self, cleTrouv) -> OrderDetail:
        '''
        Trouve un objet dans la table OrderDetails par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM order_details WHERE order_detail_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                order_detail = OrderDetail()
                order_detail.setOrderDetailID(res[0])
                o = Orders()
                o.setOrderID(res[1])
                order_detail.setOrderID(o)
                p = Products()
                p.setProductID(res[2])
                order_detail.setProductID(p)
                order_detail.setQuantity(res[3])
                order_detail.setTotalPrice(res[4])

                return order_detail
            else:
                return None
        except Exception as e:
            print(f"Erreur_OrderDetailsDAO.trouverUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverTout(self) -> list[OrderDetail]:
        '''
        Récupère tous les enregistrements de la table OrderDetails.

        :return: Une liste d'objets OrderDetails.
        '''
        try:
            query = '''SELECT * FROM order_details;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_order_details = []

            if len(res) > 0:
                for r in res:
                    order_detail = OrderDetail()
                    order_detail.setOrderDetailID(r[0])
                    o = Orders()
                    o.setOrderID(res[1])
                    order_detail.setOrderID(o)
                    p = Products()
                    p.setProductID(res[2])
                    order_detail.setProductID(p)
                    order_detail.setQuantity(r[3])
                    order_detail.setTotalPrice(r[4])

                    liste_order_details.append(order_detail)

                return liste_order_details
            else:
                return None
        except Exception as e:
            print(f"Erreur_OrderDetailsDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUn(self, cleTrouv) -> list[OrderDetail]:
        '''
        Récupère tous les enregistrements de la table OrderDetails par une clé spécifique.

        :param cleTrouv: La clé de recherche.
        :return: Une liste d'objets OrderDetails.
        '''
        try:
            query = '''SELECT * FROM order_details WHERE order_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_order_details = []

            if len(res) > 0:
                for r in res:
                    order_detail = OrderDetail()
                    order_detail.setOrderDetailID(r[0])
                    o = Orders()
                    o.setOrderID(res[1])
                    order_detail.setOrderID(o)
                    p = Products()
                    p.setProductID(res[2])
                    order_detail.setProductID(p)
                    order_detail.setQuantity(r[3])
                    order_detail.setTotalPrice(r[4])

                    liste_order_details.append(order_detail)

                return liste_order_details
            else:
                return None
        except Exception as e:
            print(f"Erreur_OrderDetailsDAO.trouverToutParUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUnLike(self, val) -> list[OrderDetail]:
        '''
        Récupère tous les enregistrements de la table OrderDetails par une clé similaire.

        :param val: La clé de recherche similaire.
        :return: Une liste d'objets OrderDetails.
        '''
        try:
            query = '''SELECT * FROM order_details WHERE order_id LIKE %s;'''
            self.cur.execute(query, (val,))
            res = self.cur.fetchall()

            liste_order_details = []

            if len(res) > 0:
                for r in res:
                    order_detail = OrderDetail()
                    order_detail.setOrderDetailID(r[0])
                    o = Orders()
                    o.setOrderID(res[1])
                    order_detail.setOrderID(o)
                    p = Products()
                    p.setProductID(res[2])
                    order_detail.setProductID(p)
                    order_detail.setQuantity(r[3])
                    order_detail.setTotalPrice(r[4])

                    liste_order_details.append(order_detail)

                return liste_order_details
            else:
                return None
        except Exception as e:
            print(f"Erreur_OrderDetailsDAO.trouverToutParUnLike() ::: {e}")
        finally:
            self.cur.close()

    def modifierUn(self, cleAnc, objModif: OrderDetail) -> int:
        '''
        Modifie un enregistrement dans la table OrderDetails.

        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE order_details SET order_id = %s, product_id = %s, quantity = %s, total_price = %s
                           WHERE order_detail_id = %s;'''
            self.cur.execute(query, (objModif.getOrderID(), objModif.getProductID(),
                                     objModif.getQuantity(), objModif.getTotalPrice(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_OrderDetailsDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table OrderDetails.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''DELETE FROM order_details WHERE order_detail_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_OrderDetailsDAO.supprimerUn() ::: {e}")
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
