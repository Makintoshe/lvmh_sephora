class Genders:

    def __init__(self):
        self.__genders_id: int = None
        self.__genders_name: str = ""

    def setGendersID(self, genders_id: int) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut __genders_id.
        :param genders_id: L'identifiant du genre.
        :return: Rien.
        '''
        self.__genders_id = genders_id

    def getGendersID(self) -> int:
        '''
        Cette méthode permet de retourner l'identifiant du genre.
        :return: L'identifiant du genre.
        '''
        return self.__genders_id

    def setGendersName(self, genders_name: str) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut __genders_name.
        :param genders_name: Le nom du genre.
        :return: Rien.
        '''
        self.__genders_name = genders_name

    def getGendersName(self) -> str:
        '''
        Cette méthode permet de retourner le nom du genre.
        :return: Le nom du genre.
        '''
        return self.__genders_name
