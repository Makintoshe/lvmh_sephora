from dao.GendersDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, BodyPartsM, GendersM

class Genders:

    @staticmethod
    def visualiserGenders():

        try:

            gDAO = GendersDAO()

            gs: list[GendersM.Genders] = gDAO.trouverTout()

            if gs!=None :
                return "ERROR"

            return gs

        except Exception as e:
            print(f'Erreur_GendersC.visualiserGenders() ::: {e}')

        return None