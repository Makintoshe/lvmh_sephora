from dao.BodyPartsDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, BodyPartsM

class Body_parts:

    @staticmethod
    def visualiserBP():

        try:

            bpDAO = BodyPartsDAO()

            bps: list[BodyPartsM.Body_parts] = bpDAO.trouverTout()

            if bps!=None :
                return "ERROR"

            return bps

        except Exception as e:
            print(f'Erreur_Body_partsC.visualiserBP() ::: {e}')

        return None

    @staticmethod
    def visualiserUnBP(idBP):

        try:

            bpDAO = BodyPartsDAO()

            bp: BodyPartsM.Body_parts = bpDAO.trouverUn(idBP)

            if bp!=None :
                return "ERROR"

            return bp

        except Exception as e:
            print(f'Erreur_Body_partsC.visualiserUnBP() ::: {e}')

        return None


    @staticmethod
    def ajouterUnBP(idBP, nameBP):

        try:

            bpDAO = BodyPartsDAO()
            objBP = BodyPartsM.Body_parts()

            objBP.setBodyPartId(idBP)
            objBP.setBodyPartName(nameBP)

            bp: int = bpDAO.insererUn(objBP)

            if bp!=1 :
                return "ERROR"

            return "AJOUT BP AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_Body_partsC.ajouterUnBP() ::: {e}')

        return None

    @staticmethod
    def modifierUnBP(idBP, nameBP):

        try:

            bpDAO = BodyPartsDAO()
            objBP = BodyPartsM.Body_parts()

            objBP.setBodyPartName(nameBP)

            bp: int = bpDAO.modifierUn(idBP, objBP)

            if bp!=1 :
                return "ERROR"

            return "MODIFICATION DE BP AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_Body_partsC.modifierUnBP() ::: {e}')

        return None

    @staticmethod
    def supprimerUnBP(idBP, nameBP):

        try:

            bpDAO = BodyPartsDAO()

            bp: int = bpDAO.supprimerUn(idBP)

            if bp!=1 :
                return "ERROR"

            return "SUPPRESSION BP AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_Body_partsC.supprimerUnBP() ::: {e}')

        return None