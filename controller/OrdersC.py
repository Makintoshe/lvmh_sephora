import model.ProductsM
from dao.OrdersDAO import *
from dao.OrderDetailsDAO import *
from dao.InvoicesDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, InvoicesM
class Orders:

    @staticmethod
    def passerCMD(idCMD,customer_id, order_date, status, invoices_id, order_detail : list[OrderDetail]):

        try:

            pM = ProductsM.Products()
            cM = CustomersM.Customers()
            oM = OrdersM.Orders()
            odM = OrderDetailsM.OrderDetail()

            # création de la commande

            oDAO = OrdersDAO()

            oM.setOrderID(idCMD)

            cM.setCustomerID(customer_id)
            oM.setCustomerID(cM)

            oM.setOrderDate(order_date)
            oM.setStatus(status)

            o_res: int = oDAO.insererUn(oM)

            # ajout des détails DE LA COMMANDE

            odDAO = OrderDetailsDAO()

            od_res: int = odDAO.insererToutList(order_detail)

            # créer une facture

            iDAO = InvoicesDAO()

            montant_tot = 0

            for od in order_detail:

                prix = od.getTotalPrice()
                montant_tot += prix

            iM = InvoicesM.Invoices()

            iM.setOrderID(invoices_id)
            iM.setOrderID(idCMD)
            iM.setInvoiceDate(order_date)
            iM.setTotalAmount(montant_tot)

            i_res: int = iDAO.insererUn(iM)

            if o_res==1 and od_res==1 and i_res==1:
                return "COMMANDE PASSEE AVEC SUCCES !!!"

            return "ERROR"

        except Exception as e:
            print(f'Erreur_OrderC.passerCMD() ::: {e}')

        return None

    @staticmethod
    def annulerCMD(idCMD):

        try:

            odDAO = OrdersDAO()

            cmd: int = odDAO.supprimerUn(idCMD)

            if cmd==0 :
                return "ERROR"

            return "ANNULATION AVEC SUCCES !!!"

        except Exception as e:
            print(f'Erreur_OrderC.annulerCMD() ::: {e}')

        return None


    @staticmethod
    def actualiserCMD(idCMD, date_maj, status):

        try:

            oM = OrdersM.Orders()

            oM.setOrderDate(date_maj)
            oM.setStatus(status)

            odDAO = OrdersDAO()

            cmd: int = odDAO.modifierUn(idCMD, oM)

            if cmd==0 :
                return "ERROR"

            return "ANNULATION AVEC SUCCES !!!"

        except Exception as e:
            print(f'Erreur_OrderC.actualiserCMD() ::: {e}')

        return None

    @staticmethod
    def visualiserCMD(idCMD):

        try:

            odDAO = OrdersDAO()

            cmd: OrdersM.Orders() = odDAO.trouverUn(idCMD)

            if cmd!=None :
                return "ERROR"

            return cmd

        except Exception as e:
            print(f'Erreur_OrderC.visualiserCMD() ::: {e}')

        return None

    @staticmethod
    def visualiserCMDCustom(idCustomer):

        try:

            odDAO = OrdersDAO()

            cmds: list[OrdersM.Orders()] = odDAO.trouverToutParUn(idCustomer)

            if cmds!=None :
                return "ERROR"

            return cmds

        except Exception as e:
            print(f'Erreur_OrderC.visualiserCMDCustom() ::: {e}')

        return None

    @staticmethod
    def visualiserCMDByStatus(idCustomer, statut):

        try:

            odDAO = OrdersDAO()

            cmds: list[OrdersM.Orders()] = odDAO.filtrerCmdByStatus(statut, idCustomer)

            if cmds!=None :
                return "ERROR"

            return cmds

        except Exception as e:
            print(f'Erreur_OrderC.visualiserCMDByStatus() ::: {e}')

        return None

