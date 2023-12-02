from dao import ModelDAO
import model.BrandsM
import model.BodyPartsM
from model.ProductsM import Products


class ProductsDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialise l'objet ProductsDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Products) -> int:
        '''
        Insère un objet dans la table Products.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO products(product_id, product_name, brand_id, body_part_id, gender_id, price, stock_quantity) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            self.cur.execute(query, (objIns.getProductID(),objIns.getProductName(),
                                     objIns.getBrandID(), objIns.getBodyPartID(),
                                     objIns.getGenderID(), objIns.getPrice(), objIns.getStockQuantity()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_ProductsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0
        finally:
            self.cur.close()

    def insererToutList(self, objInsList: list[Products] = []) -> int:
        '''
        Insère une liste d'objets dans la table Products.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        pass

    def trouverUn(self, cleTrouv) -> Products:
        '''
        Trouve un objet dans la table Products par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM products WHERE product_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                product = Products()
                product.setProductID(res[0])
                product.setProductName(res[1])
                product.setPrice(res[2])
                return product
            else:
                return None
        except Exception as e:
            print(f"Erreur_ProductsDAO.trouverUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverTout(self) -> list[Products]:
        '''
        Récupère tous les enregistrements de la table Products.

        :return: Une liste d'objets Products.
        '''
        try:
            query = '''SELECT * FROM products;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            products_list = []

            if len(res) > 0:
                for r in res:
                    product = Products()
                    product.setProductID(r[0])
                    product.setProductName(r[1])
                    product.setPrice(r[2])
                    products_list.append(product)
                return products_list
            else:
                return None
        except Exception as e:
            print(f"Erreur_ProductsDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUn(self, cleTrouv) -> list[Products]:
        '''
        Récupère tous les enregistrements de la table Products par une clé spécifique.

        :param cleTrouv: La clé de recherche.
        :return: Une liste d'objets Products.
        '''
        try:
            query = '''SELECT * FROM products WHERE product_name = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_produits = []

            if len(res) > 0:
                for r in res:
                    produit = Products()
                    produit.setProductID(r[0])
                    produit.setProductName(r[1])
                    produit.setPrice(r[2])
                    # Ajouter d'autres attributs au besoin
                    liste_produits.append(produit)

                return liste_produits

            else:
                return None

        except Exception as e:
            print(f"Erreur_ProductsDAO.trouverToutParUn() ::: {e}")
        finally:
            self.cur.close()

    def trouverToutParUnLike(self, cleTrouv) -> list[Products]:
        '''
        Récupère tous les enregistrements de la table Products par une clé similaire.

        :param cleTrouv: La clé de recherche similaire.
        :return: Une liste d'objets Products.
        '''
        try:
            query = '''SELECT * FROM products WHERE product_name LIKE %s;'''
            self.cur.execute(query, (f"%{cleTrouv}%",))
            res = self.cur.fetchall()

            liste_produits = []

            if len(res) > 0:
                for r in res:
                    produit = Products()
                    produit.setProductID(r[0])
                    produit.setProductName(r[1])
                    produit.setPrice(r[2])
                    # Ajouter d'autres attributs au besoin
                    liste_produits.append(produit)

                return liste_produits

            else:
                return None

        except Exception as e:
            print(f"Erreur_ProductsDAO.trouverToutParUnLike() ::: {e}")
        finally:
            self.cur.close()

    def modifierUn(self, cleAnc, objModif: Products) -> int:
        '''
        Modifie un enregistrement dans la table Products.

        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE products SET product_name = %s, product_price = %s, stock_quantity = %s WHERE product_id = %s;'''
            self.cur.execute(query, (objModif.getProductName(), objModif.getPrice(), objModif.getStockQuantity(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0

        except Exception as e:
            print(f"Erreur_ProductsDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table Products.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''DELETE FROM products WHERE product_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0

        except Exception as e:
            print(f"Erreur_ProductsDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def depensesMoyennes(self) -> float:
        '''
        Calcule la moyenne des dépenses pour les produits.

        :return: La moyenne des dépenses.
        '''
        pass

    def filtrerCmdByStatus(self) -> list[Products]:
        '''
        Filtrage des produits par statut.

        :return: Une liste de produits filtrée.
        '''
        pass

    def sortProductByPrice(self) -> list[Products]:
        '''
        Trie les produits par prix.

        :return: Une liste de produits triés.
        '''
        try:
            query = '''SELECT product_name, stock_quantity, price, RANK() OVER (ORDER BY price)
                        FROM products;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_produits = []

            if len(res) > 0:
                for r in res:
                    produit = Products()
                    produit.setProductName(r[0])
                    produit.setStockQuantity(r[1])
                    produit.setPrice(r[2])
                    produit.setProductID(r[3])
                    liste_produits.append(produit)

                return liste_produits

            else:
                return None

        except Exception as e:
            print(f"Erreur_ProductsDAO.sortProductByPrice() ::: {e}")
        finally:
            self.cur.close()

    def searchPleinText(self, keyword) -> list[Products]:
        '''
        Effectue une recherche plein texte.

        :param keyword: Le mot-clé de recherche.
        :return: Une liste de résultats de recherche.
        '''
        try:
            query = '''SELECT * FROM products WHERE product_name @@ %s;'''
            self.cur.execute(query, (f"'{keyword}'",))
            res = self.cur.fetchall()

            liste_produits = []

            if len(res) > 0:
                for r in res:
                    produit = Products()
                    produit.setProductID(r[0])
                    produit.setProductName(r[1])
                    produit.setPrice(r[5])
                    produit.setStockQuantity(r[6])
                    liste_produits.append(produit)

                return liste_produits

            else:
                return None

        except Exception as e:
            print(f"Erreur_ProductsDAO.searchPleinText() ::: {e}")
        finally:
            self.cur.close()

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

    #######################################################################################################################

    def catalogueProduits(self)->list[dict]:
        '''
        Récupère le produit et ses descriptions de façon explicite.

        :return: Une liste .
        '''
        try:
            query = '''SELECT p.product_name, b.brand_name, bp.body_part_name, g.gender_name, p.price, p.stock_quantity
             FROM products p, brands b, body_parts bp, genders g
             WHERE p.brand_id=b.brand_id
             AND p.body_part_id=bp.body_part_id;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            catprods_list = []
            if len(res) > 0:
                for r in res:
                    un_prod = {
                        'product_name': r[0],
                        'brand_name': r[1],
                        'body_part': r[2],
                        'gender_name': r[3],
                        'price': r[4],
                        'stock_quantity': r[5]
                    }
                    catprods_list.append(un_prod)
                return catprods_list
            else:
                return None
        except Exception as e:
            print(f"Erreur_ProductsDAO.catalogueProduits() ::: {e}")
        finally:
            self.cur.close()
