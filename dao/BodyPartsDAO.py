from dao import ModelDAO
from model.BodyPartsM import Body_parts  # Assurez-vous d'importer la classe BodyParts appropriée

class BodyPartsDAO(ModelDAO.modeleDAO):
    def __init__(self):
        '''
        Initialise l'objet BodyPartsDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insererUn(self, objIns: Body_parts) -> int:
        '''
        Insère un objet dans la table BodyParts.

        :param objIns: L'objet à insérer dans la table.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''INSERT INTO body_parts (body_part_id, body_part_name) 
                       VALUES (%s, %s);'''
            self.cur.execute(query, (objIns.getBodyPartId(),objIns.getBodyPartName(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_BodyPartsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def insererToutList(self, objInsList: list[Body_parts] = []) -> int:
        '''
        Insère une liste d'objets dans la table BodyParts.

        :param objInsList: La liste d'objets à insérer.
        :return: Le nombre de lignes affectées.
        '''
        # Non codée
        pass

    def trouverUn(self, cleTrouv) -> Body_parts:
        '''
        Trouve un objet dans la table BodyParts par clé.

        :param cleTrouv: La clé de recherche.
        :return: L'objet trouvé.
        '''
        try:
            query = '''SELECT * FROM body_parts WHERE body_part_id = %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchone()

            if res:
                body_part = Body_parts()
                body_part.setBodyPartId(res[0])
                body_part.setBodyPartName(res[1])
                return body_part
            else:
                return None
        except Exception as e:
            print(f"Erreur_BodyPartsDAO.trouverUn() ::: {e}")

    def trouverTout(self) -> list[Body_parts]:
        '''
        Récupère tous les enregistrements de la table BodyParts.

        :return: Une liste d'objets BodyParts.
        '''
        try:
            query = '''SELECT * FROM body_parts;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_bp = []

            if len(res)>0:

                for r in res:
                    bp = Body_parts()

                    bp.setBodyPartId(r[0])
                    bp.setBodyPartName(r[1])

                    liste_bp.append(bp)

                return liste_bp

            else:

                return None

        except Exception as e:
            print(f"Erreur_BodyPartsDAO.trouverTout() ::: {e}")

    def trouverToutParUn(self, cleTrouv) -> list[Body_parts]:
        '''
        Récupère tous les enregistrements de la table BodyParts par une clé spécifique.

        :param cleTrouv: La clé de recherche.
        :return: Une liste d'objets BodyParts.
        '''
        pass

    def trouverToutParUnLike(self, cleTrouv) -> list[Body_parts]:
        '''
        Récupère tous les enregistrements de la table BodyParts par une clé similaire.

        :param cleTrouv: La clé de recherche similaire.
        :return: Une liste d'objets BodyParts.
        '''
        try:
            query = '''SELECT * FROM body_parts WHERE body_part_name LIKE %s;'''
            self.cur.execute(query, (cleTrouv,))
            res = self.cur.fetchall()

            liste_bp = []

            if len(res)>0:

                for r in res:
                    bp = Body_parts()

                    bp.setBodyPartId(r[0])
                    bp.setBodyPartName(r[1])

                    liste_bp.append(bp)

                return liste_bp

            else:

                return None

        except Exception as e:
            print(f"Erreur_BodyPartsDAO.trouverTout() ::: {e}")

    def modifierUn(self, cleAnc, objModif: Body_parts) -> int:
        '''
        Modifie un enregistrement dans la table BodyParts.

        :param cleAnc: La clé de l'enregistrement à
        :param cleAnc: La clé de l'enregistrement à modifier.
        :param objModif: Les nouvelles données à mettre à jour.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = '''UPDATE body_parts SET body_part_name = %s WHERE body_part_id = %s;'''
            self.cur.execute(query, (objModif.getBodyPartName(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_BodyPartsDAO.modifierUn() ::: {e}")
            self.cur.connection.rollback()
            return 0

    def supprimerUn(self, cleSup) -> int:
        '''
        Supprime un enregistrement de la table BodyParts.

        :param cleSup: La clé de l'enregistrement à supprimer.
        :return: Le nombre de lignes affectées.
        '''
        try:
            query = f'''DELETE FROM body_parts WHERE body_part_id = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as e:
            print(f"Erreur_BodyPartsDAO.supprimerUn() ::: {e}")
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