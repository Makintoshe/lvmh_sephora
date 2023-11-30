from dao.BrandsDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, BodyPartsM, GendersM, BrandsM

class Brands:

    @staticmethod
    def visualiserBrands():

        try:

            bDAO = BrandsDAO()

            cs: list[BrandsM.Brands] = bDAO.trouverTout()

            if cs==None :
                return "ERROR"

            return cs

        except Exception as e:
            print(f'Erreur_BrandsC.visualiserBrands() ::: {e}')

        return None