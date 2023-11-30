from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionBD

class modeleDAO(ABC):

    connect_objet = ConnexionBD().getConnexion()

    ### CRUD

    # INSERT

    @abstractmethod
    def insererUn(self, objIns)->int:
        pass

    @abstractmethod
    def insererToutList(self, objInsList)->int:
        pass

    # SELECT

    @abstractmethod
    def trouverUn(self, cleTrouv)->object:
        pass

    @abstractmethod
    def trouverTout(self)->list:
        pass

    @abstractmethod
    def trouverToutParUn(self, cleTrouv)->list:
        pass

    @abstractmethod
    def trouverToutParUnLike(self, cleTrouv)->list:
        pass

    # UPDATE

    @abstractmethod
    def modifierUn(self, cleAnc, objModif)->int:
        pass

    # DELETE

    @abstractmethod
    def supprimerUn(self, cleSup)->int:
        pass

    # SEANCE 4/5 :
    # 1.    La moyenne des dépenses effectuées par le client (PL/SQL)
    # 2.    CASE WHEN : filtrer par statut
    # 3.    RANK : classer les produits par prix croissant
    # 4.    @@ : faire une recherche plein texte

    @abstractmethod
    def depensesMoyennes(self)->float:
        pass

    @abstractmethod
    def filtrerCmdByStatus(self)->list:
        pass

    @abstractmethod
    def sortProductByPrice(self)->list:
        pass

    @abstractmethod
    def searchPleinText(self)->list:
        pass

    # SEANCE 6 :
    # 1.    User/Rôles
    # 2.    MD5 password
    # 3.    Indexation
    # 4.    Enum/DATE_TRUNC

    @abstractmethod
    def creerUser(self, pwd, usr)->object:
        pass

    @abstractmethod
    def creerRole(self, role)->int:
        pass

    @abstractmethod
    def attribuerRole(self, usr,role)->int:
        pass
