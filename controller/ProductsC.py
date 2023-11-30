import dao.ProductsDAO
import model.ProductsM
from model.ProductsM import *
from dao.ProductsDAO import *
#from model.ProductsM import *

class Products:

    @staticmethod
    def ajouterProd(prodObj: Products)->int:

        try:

            prodDAO = ProductsDAO()

            addProd: int = prodDAO.insererUn(prodObj)

            if addProd==0:
                return "ERROR"

            return "INSERTION PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f"Erreur_ProductsC.ajouterProd() ::: {e}")

        return None

    @staticmethod
    def modifierProd(prodId, name, price, qty)->int:

        try:

            prodDAO = ProductsDAO()

            prod = model.ProductsM.Products()

            prod.setPrice(price)
            prod.setStockQuantity(qty)
            prod.setProductName(name)

            modProd: int = prodDAO.modifierUn(prodId, prod)

            if modProd==0:
                return "ERROR"

            return "MISE A JOUR PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f"Erreur_ProductsC.modifierProd() ::: {e}")

        return None


    @staticmethod
    def consulterUnProd(prodName: str)->Products:

        try:

            prodDAO = ProductsDAO()

            modProd: model.ProductsM.Products = prodDAO.trouverUn(prodName)

            if modProd==0:
                return "ERROR"

            return "MISE A JOUR PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f"Erreur_ProductsC.modifierProd() ::: {e}")

        return None

    def consulterUnProdbyId(prodId: int)->Products:

        try:

            prodDAO = ProductsDAO()

            modProd: model.ProductsM.Products = prodDAO.trouverUn(prodId)

            if modProd==0:
                return "ERROR"

            return "MISE A JOUR PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f"Erreur_ProductsC.modifierProd() ::: {e}")

        return None

    @staticmethod
    def consulterCatalogueProd()->list[Products]:

        try:

            prodDAO = ProductsDAO()

            listProds: list[model.ProductsM.Products] = prodDAO.trouverTout()

            if listProds==None:
                return "ERROR"

            return listProds

        except Exception as e:

            print(f"Erreur_ProductsC.modifierProd() ::: {e}")

        return None

    @staticmethod
    def supprimerProd(prodId)->int:

        try:

            prodDAO = ProductsDAO()

            delProd: int = prodDAO.supprimerUn(prodId)

            if delProd==0:
                return "ERROR"

            return "SUPPRESSION PRODUIT AVEC SUCCES"

        except Exception as e:

            print(f'Erreur_ProductC.supprimerProd() ::: {e}')


    @staticmethod
    def filtrerProdByPrice()->list[Products]:

        try:

            prodDAO = ProductsDAO()

            listProds: list[model.ProductsM.Products] = prodDAO.sortProductByPrice()

            if listProds==None:
                return "ERROR"

            return listProds

        except Exception as e:

            print(f"Erreur_ProductsC.filtrerProdByPrice() ::: {e}")

        return None

    @staticmethod
    def search_product_by_name(keyword) -> list[Products]:

        try:

            prodDAO = ProductsDAO()

            listProds: list[model.ProductsM.Products] = prodDAO.searchPleinText(keyword)

            if listProds==None:
                return "ERROR"

            return listProds

        except Exception as e:

            print(f"Erreur_ProductsC.search_product_by_name() ::: {e}")

        return None