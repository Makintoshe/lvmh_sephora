import model.InvoicesM
from dao.InvoicesDAO import *

class Invoices:

    @staticmethod
    def genererFacture(idFact):
        '''
        Génère une facture en fonction de l'ID fourni.
        @param idFact: ID de la facture.
        @return: Facture générée ou message d'erreur.
        '''
        try:

            invDAO = InvoicesDAO()

            facture: model.InvoicesM.Invoices = invDAO.trouverUn(idFact)

            if facture is None:
                return "ERROR"

            return facture

        except Exception as e:

            print(f"Erreur_InvoicesC.genererFacture() ::: {e}")

        return None

    @staticmethod
    def consulterdepensesmoyennes(idCust):
        '''
        Consulte les dépenses moyennes d'un client.
        @param idCust: ID du client.
        @return: Dépenses moyennes du client ou message d'erreur.
        '''
        try:

            invDAO = InvoicesDAO()

            depenses: float = invDAO.depensesMoyennes(idCust)

            if depenses is None:
                return "ERROR"

            return depenses

        except Exception as e:

            print(f"Erreur_InvoicesC.consulterdepensesmoyennes() ::: {e}")

        return None

    @staticmethod
    def visualiserFactures():
        '''
        Visualise toutes les factures.
        @return: Liste de factures ou message d'erreur.
        '''
        try:

            invDAO = InvoicesDAO()

            i: list[model.InvoicesM.Invoices] = invDAO.trouverTout()

            if i==None :
                return "ERROR"

            return i

        except Exception as e:
            print(f'Erreur_InvoicesC.visualiserFactures() ::: {e}')

        return None

    @staticmethod
    def visualiserUneFacture(idF):
        '''
        Visualise une facture spécifique en fonction de l'ID fourni.
        @param idF: ID de la facture.
        @return: Facture spécifique ou message d'erreur.
        '''
        try:

            invDAO = InvoicesDAO()

            i: model.InvoicesM.Invoices = invDAO.trouverUn(idF)

            if i==None :
                return "ERROR"

            return i

        except Exception as e:
            print(f'Erreur_InvoicesC.visualiserUneFacture() ::: {e}')

        return None


    @staticmethod
    def ajouterUnFacture(idI, idO, dates, totmont):
        '''
        Ajoute une nouvelle facture.
        @param idI: ID de la facture.
        @param idO: ID de la commande associée.
        @param dates: Date de la facture.
        @param totmont: Montant total de la facture.
        @return: Statut de l'ajout de la facture.
        '''
        try:

            iDAO = InvoicesDAO()

            objI = model.InvoicesM.Invoices()

            objI.setInvoiceID(idI)
            objI.setOrderID(idO)
            objI.setInvoiceDate(dates)
            objI.setTotalAmount(totmont)

            i: int = iDAO.insererUn(objI)

            if i==0 :
                return "ERROR"

            return "AJOUT Facture AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_InvoicesC.ajouterUneFacture() ::: {e}')

        return None

    @staticmethod
    def modifierUneFacture(idI, idO, dates, totmont):
        '''
        Modifie une facture existante.
        @param idI: ID de la facture.
        @param idO: Nouvel ID de la commande associée.
        @param dates: Nouvelle date de la facture.
        @param totmont: Nouveau montant total de la facture.
        @return: Statut de la modification de la facture.
        '''
        try:

            iDAO = InvoicesDAO()
            objI = Invoices()

            objI.setOrderID(idO)
            objI.setInvoiceDate(dates)
            objI.setTotalAmount(totmont)

            i: int = iDAO.modifierUn(idI, objI)

            if i==0 :
                return "ERROR"

            return "MODIFICATION DU Facture AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_InvoicesC.modifierUneFacture() ::: {e}')

        return None

    @staticmethod
    def supprimerUneFacture(idI):
        '''
        Supprime une facture en fonction de l'ID fourni.
        @param idI: ID de la facture.
        @return: Statut de la suppression de la facture.
        '''
        try:

            iDAO = InvoicesDAO()

            i: int = iDAO.supprimerUn(idI)

            if i==0 :
                return "ERROR"

            return "SUPPRESSION Facture AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_InvoicesC.supprimerUneFatcure() ::: {e}')

        return None