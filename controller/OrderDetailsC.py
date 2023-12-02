from dao.OrderDetailsDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM

class OrderDetails:

    @staticmethod
    def consulterDetailCMD(idDetailCMD) -> OrderDetailsM.OrderDetail | str:
        '''
        Affiche un seul détail de commande.
        @param idDetailCMD: ID du détail de commande.
        @return: Détail de commande.
        '''

        try:
            ordetDAO = OrderDetailsDAO()

            un_od: OrderDetailsM.OrderDetail | None = ordetDAO.trouverUn(idDetailCMD)

            if un_od == None:
                return "Aucun détails!"

            return un_od

        except Exception as e:
            print(f'Erreur_OrderDetailsC.consulterDetailCMD() ::: {e}')

        return None

    @staticmethod
    def consulterCMD(idCMD)->list|str:
        '''
        Affiche tous les détails d'une commande.
        @param idCMD: ID de la commande.
        @return: Liste des détails de la commande.
        '''

        try:
            ordetDAO = OrderDetailsDAO()

            orderDetailsList: list = ordetDAO.trouverToutParUn(idCMD)

            if orderDetailsList==None:
                return "Aucune commande!"

            return orderDetailsList

        except Exception as e:
            print(f'Erreur_OrderDetailsC.consulterCMD() ::: {e}')

        return None

#####################################################################################

    @staticmethod
    def ajouterUnDetail(idOD, idO, pID, qty, totprice):
        '''
        Ajoute un détail de commande.
        @param idOD: ID du détail de commande.
        @param idO: ID de la commande.
        @param pID: ID du produit.
        @param qty: Quantité.
        @param totprice: Prix total.
        @return: Statut de l'ajout du détail de commande.
        '''
        try:

            ordetDAO = OrderDetailsDAO()

            objOD = OrderDetailsM.OrderDetail()

            objOD.setOrderDetailID(idOD)
            objOD.setOrderID(idO)
            objOD.setProductID(pID)
            objOD.setQuantity(qty)
            objOD.setTotalPrice(totprice)

            i: int = ordetDAO.insererUn(objOD)

            if i==0 :
                return "ERROR"

            return "AJOUT Order Details AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_OrderDetailsC.ajouterUnDetail() ::: {e}')

        return None

    @staticmethod
    def modifierUnDetail(idOD, idO, pID, qty, totprice):
        '''
        Modifie un détail de commande.
        @param idOD: ID du détail de commande.
        @param idO: ID de la commande.
        @param pID: ID du produit.
        @param qty: Quantité.
        @param totprice: Prix total.
        @return: Statut de la modification du détail de commande.
        '''
        try:

            ordetDAO = OrderDetailsDAO()
            objOD = OrderDetailsM.OrderDetail()

            objOD.setOrderID(idO)
            objOD.setProductID(pID)
            objOD.setQuantity(qty)
            objOD.setTotalPrice(totprice)

            i: int = ordetDAO.modifierUn(idOD, objOD)

            if i==0 :
                return "ERROR"

            return "MODIFICATION DU Order Details AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_OrderDetailsC.modifierUnDetail() ::: {e}')

        return None

    @staticmethod
    def supprimerUnDetail(idOD):
        '''
        Supprime un détail de commande.
        @param idOD: ID du détail de commande.
        @return: Statut de la suppression du détail de commande.
        '''
        try:

            ordetDAO = OrderDetailsDAO()

            i: int = ordetDAO.supprimerUn(idOD)

            if i==0 :
                return "ERROR"

            return "SUPPRESSION Order Details AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_OrderDetailsC.supprimerUnDetail() ::: {e}')

        return None