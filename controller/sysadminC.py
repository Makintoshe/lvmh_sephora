from dao.sysadminDAO import *

class SysAdmin:

    @staticmethod
    def creerUnUser(pwd, usr):

        try:

            sDAO = sysadmin()

            sys: int = sDAO.creerUser(pwd, usr)

            if sys!=1 :
                return "ERROR"

            return "CREATION D'UN NOUVEAU USER AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_sysadminC.creerUSER() ::: {e}')

        return None

    @staticmethod
    def creerUnRole(role):

        try:

            sDAO = sysadmin()

            sys: int = sDAO.creerRole(role)

            if sys!=1 :
                return "ERROR"

            return "CREATION D'UN NOUVEAU USER AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_sysadminC.creerUnRole() ::: {e}')

        return None

    @staticmethod
    def privilege_Role(privileges, tables, roles):

        try:

            sDAO = sysadmin()

            sys: int = sDAO.attribuerPriviliege(privileges, tables, roles)

            if sys!=1 :
                return "ERROR"

            return "ATTRIBUTION DE(S) PRIVILEGE(S) A UN ROLE AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_sysadminC.privilege_Role() ::: {e}')

        return None

    @staticmethod
    def attribution_Role(usr, roles):

        try:

            sDAO = sysadmin()

            sys: int = sDAO.attribuerRole(usr, roles)

            if sys!=1 :
                return "ERROR"

            return "ATTRIBUTION DE(S) ROLE(S) A UN USER AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_sysadminC.privilege_Role() ::: {e}')

        return None