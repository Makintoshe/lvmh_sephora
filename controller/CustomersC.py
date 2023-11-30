from dao.CustomersDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, BodyPartsM, GendersM

class Customers:

    @staticmethod
    def visualiserCustomers():

        try:

            cDAO = CustomersDAO()

            cs: list[CustomersM.Customers] = cDAO.trouverTout()

            if cs!=None :
                return "ERROR"

            return cs

        except Exception as e:
            print(f'Erreur_CustomersC.visualiserCustomers() ::: {e}')

        return None