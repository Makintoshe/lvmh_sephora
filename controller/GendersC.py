from dao.GendersDAO import *
from model import ProductsM, OrdersM, OrderDetailsM, CustomersM, BodyPartsM, GendersM

class Genders:

    @staticmethod
    def visualiserGenders():
        '''
        Visualise tous les genres.
        @return: Liste de genres ou message d'erreur.
        '''
        try:

            gDAO = GendersDAO()

            gs: list[GendersM.Genders] = gDAO.trouverTout()

            if gs==None :
                return "ERROR"

            return gs

        except Exception as e:
            print(f'Erreur_GendersC.visualiserGenders() ::: {e}')

        return None

    @staticmethod
    def visualiserUnGenre(idG):
        '''
        Visualise un genre spécifique.
        @param idG: ID du genre.
        @return: Genre spécifique ou message d'erreur.
        '''
        try:

            gDAO = GendersDAO()

            g: GendersM.Genders = gDAO.trouverUn(idG)

            if g==None :
                return "ERROR"

            return g

        except Exception as e:
            print(f'Erreur_GendersC.visualiserUnGenre() ::: {e}')

        return None


    @staticmethod
    def ajouterUnGenre(idG, nameG):
        '''
        Ajoute un genre.
        @param idG: ID du genre.
        @param nameG: Nom du genre.
        @return: Statut de l'ajout du genre.
        '''
        try:

            gDAO = GendersDAO()

            objG = GendersM.Genders()

            objG.setGendersID(idG)
            objG.setGendersName(nameG)

            g: int = gDAO.insererUn(objG)

            if g==0 :
                return "ERROR"

            return "AJOUT Genre AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_GendersC.ajouterUnBP() ::: {e}')

        return None

    @staticmethod
    def modifierUnGenre(idG, nameG):
        '''
        Modifie un genre.
        @param idG: ID du genre.
        @param nameG: Nouveau nom du genre.
        @return: Statut de la modification du genre.
        '''
        try:

            gDAO = GendersDAO()
            objG = GendersM.Genders()

            objG.setGendersID(nameG)

            g: int = gDAO.modifierUn(idG, objG)

            if g==0 :
                return "ERROR"

            return "MODIFICATION DU GENRE AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_GendersC.modifierUnBP() ::: {e}')

        return None

    @staticmethod
    def supprimerUnGenre(idG):
        '''
        Supprime un genre.
        @param idG: ID du genre.
        @return: Statut de la suppression du genre.
        '''
        try:

            gDAO = GendersDAO()

            g: int = gDAO.supprimerUn(idG)

            if g==0 :
                return "ERROR"

            return "SUPPRESSION Genre AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_GendersC.supprimerUnBP() ::: {e}')

        return None