from dao import ModelDAO
from model.GendersM import Genders

class GendersDAO(ModelDAO.modeleDAO):
    def __init__(self):
        '''
        Initialise l'objet GendersDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Genders) -> int:
        '''
        Insère un objet dans la table Genders.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO genders (gender_id, gender_name) 
                       VALUES (%s, %s);'''
            self.cur.execute(query, (objIns.getGendersID(), objIns.getGenderName()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_GendersDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def insererToutList(self, objInsList: list[Genders] = []) -> int:
        '''
        Insère une liste d'objets dans la table Genders.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        # Non codée
        pass

    def trouverUn(self, cleTrouv) -> Genders:
        '''
        Trouve un objet dans la table Genders par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM genders WHERE gender_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                gender = Genders()
                gender.setGendersID(res[0])
                gender.setGendersName(res[1])
                return gender
            else:
                return None
        except Exception as e:
            print(f"Erreur_GendersDAO.trouverUn() ::: {e}")

    def trouverTout(self) -> list[Genders]:
        '''
        Récupère tous les enregistrements de la table Genders.

        :return: Une liste d'objets Genders.
        '''
        try:
            query = '''SELECT * FROM genders;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            genders_list = []

            if res:

                for row in res:
                    g = Genders()

                    g.setGendersID(row[0])

                    g.setGendersName(row[1])

                    genders_list.append(g)

                return genders_list

            else:

                return None

        except Exception as e:
            print(f"Erreur_GendersDAO.trouverTout() ::: {e}")

    def trouverToutParUn(self, cleTrouv) -> list[Genders]:
        '''
        Récupère tous les enregistrements de la table Genders par une clé spécifique.

        :param cleTrouv: La clé de recherche.
        :return: Une liste d'objets Genders.
        '''
        pass

    def trouverToutParUnLike(self, cleTrouv) -> list[Genders]:
        '''
        Récupère tous les enregistrements de la table Genders par une clé similaire.

        :param cleTrouv: La clé de recherche similaire.
        :return: Une liste d'objets Genders.
        '''
        try:
            query = '''SELECT * FROM genders WHERE gender_name LIKE %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            genders_list = []

            if res:

                for row in res:
                    g = Genders()

                    g.setGendersID(row[0])

                    g.setGendersName(row[1])

                    genders_list.append(g)

                return genders_list

            else:

                return None

        except Exception as e:
            print(f"Erreur_GendersDAO.trouverToutParUnLike() ::: {e}")

    def modifierUn(self, cleAnc, objModif: Genders) -> int:
        '''
        Modifie un enregistrement dans la table Genders.

        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE genders SET gender_name = %s WHERE gender_id = %s;'''
            self.cur.execute(query, (objModif.getGenderName(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_GendersDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table Genders.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''DELETE FROM genders WHERE gender_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_GendersDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def depensesMoyennes(self) -> float:
        pass

    def filtrerCmdByStatus(self) -> list:
        pass

    def sortProductByPrice(self) -> list:
        pass

    def searchPleinText(self) -> list:
        pass

    def creerUser(self, pwd, usr) -> object:
        pass

    def creerRole(self, role) -> int:
        pass

    def attribuerRole(self, usr, role) -> int:
        pass