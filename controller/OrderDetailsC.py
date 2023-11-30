from dao.OrderDetailsDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM

class OrderDetails:

    @staticmethod
    def consulterDetailCMD(idDetailCMD)->OrderDetailsM.OrderDetail:

        try:
            ordetDAO = OrderDetailsDAO()

            un_od: OrderDetailsM.OrderDetail = ordetDAO.trouverUn(idDetailCMD)

            if un_od==None:
                return "Aucun détails!"

            return un_od

        except Exception as e:
            print(f'Erreur_OrderDetailsC.consulterDetailCMD() ::: {e}')

        return None

    @staticmethod
    def consulterCMD(idCMD)->list:

        try:
            ordetDAO = OrderDetailsDAO()

            orderDetailsList: list = ordetDAO.trouverToutParUn(idCMD)

            if orderDetailsList==None:
                return "Aucune commande!"

            return orderDetailsList

        except Exception as e:
            print(f'Erreur_OrderDetailsC.consulterCMD() ::: {e}')

        return None

