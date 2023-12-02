import model.ProductsM
from dao.OrdersDAO import *
from dao.OrderDetailsDAO import *
from dao.InvoicesDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, InvoicesM
class Orders:

    @staticmethod
    def passerCMD(idCMD, customer_id, order_date, status, order_details : list[dict]):
        """
        Passer une commande.
        @param idCMD: Identifiant de la commande.
        @param customer_id: Identifiant du client.
        @param order_date: Date de la commande.
        @param status: Statut de la commande.
        @param order_details: Liste des détails de la commande.
        @return: Statut de la commande.
        """
        try:

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

            o_res = oDAO.insererUn(oM)

            # ajout des détails DE LA COMMANDE

            odDAO = OrderDetailsDAO()

            liste_order_details = []

            for od in order_details:
                #odM.setOrderDetailID(od["order_detail_id"])
                odM.setProductID(od["product_id"])
                odM.setOrderID(idCMD)
                odM.setQuantity(od["quantity"])
                odM.setTotalPrice(od["price"])

                liste_order_details.append(odM)

            od_res = odDAO.insererToutList(liste_order_details)

            # créer une facture

            iDAO = InvoicesDAO()

            montant_tot = 0

            for od in liste_order_details:

                prix = od.getTotalPrice()
                montant_tot += prix

            iM = InvoicesM.Invoices()

            #iM.setInvoiceID(invoices_id)
            iM.setOrderID(idCMD)
            iM.setInvoiceDate(order_date)
            iM.setTotalAmount(montant_tot)

            i_res = iDAO.insererUn(iM)

            if o_res!=1 and od_res==1 or i_res==1:
                return "COMMANDE PASSEE AVEC SUCCES !!!"

            return "ERROR"

        except Exception as e:
            print(f'Erreur_OrderC.passerCMD() ::: {e}')

        return None

    @staticmethod
    def annulerCMD(idCMD):
        """
        Annuler une commande.
        @param idCMD: Identifiant de la commande à annuler.
        @return: Statut de l'annulation.
        """
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
        """
        Actualiser une commande.
        @param idCMD: Identifiant de la commande à actualiser.
        @param date_maj: Date de la mise à jour.
        @param status: Nouveau statut de la commande.
        @return: Statut de l'actualisation.
        """
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
        """
        Visualiser une commande par son identifiant.
        @param idCMD: Identifiant de la commande à visualiser.
        @return: Commande au format JSON.
        """
        try:

            odDAO = OrdersDAO()

            cmd: OrdersM.Orders() = odDAO.trouverUn(idCMD)

            if cmd==None :
                return "ERROR"

            return cmd

        except Exception as e:
            print(f'Erreur_OrderC.visualiserCMD() ::: {e}')

        return None

    @staticmethod
    def visualiserCMDCustom(idCustomer):
        """
        Visualiser les commandes d'un client.
        @param idCustomer: Identifiant du client.
        @return: Liste des commandes du client.
        """
        try:

            odDAO = OrdersDAO()

            cmds: list[OrdersM.Orders()] = odDAO.trouverToutParUn(idCustomer)

            if cmds==None :
                return "ERROR"

            return cmds

        except Exception as e:
            print(f'Erreur_OrderC.visualiserCMDCustom() ::: {e}')

        return None

    @staticmethod
    def visualiserCMDByStatus(idCustomer, statut):
        """
        Visualiser les commandes d'un client par statut.
        @param idCustomer: Identifiant du client.
        @param statut: Statut des commandes à filtrer.
        @return: Liste des commandes au format JSON.
        """
        try:

            odDAO = OrdersDAO()

            cmds: list[OrdersM.Orders] = odDAO.filtrerCmdByStatus(statut, idCustomer)

            if cmds==None :
                return "ERROR"

            return cmds

        except Exception as e:
            print(f'Erreur_OrderC.visualiserCMDByStatus() ::: {e}')

        return None

####

