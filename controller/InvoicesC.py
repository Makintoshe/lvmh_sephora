import model.InvoicesM
from dao.InvoicesDAO import *

class Invoices:

    @staticmethod
    def genererFacture(idFact):

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

        try:

            invDAO = InvoicesDAO()

            depenses: float = invDAO.depensesMoyennes(idCust)

            if depenses is None:
                return "ERROR"

            return depenses

        except Exception as e:

            print(f"Erreur_InvoicesC.consulterdepensesmoyennes() ::: {e}")

        return None