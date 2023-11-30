class Body_parts:

    # un attribut de classe, est une valeur partagée par toutes les instances de la classe
    # ici nous n'avons pas.

    def __init__(self):
        '''
        le constructeur de notre méthode, contrairement à d'autres langages,
        en python, un attribut d'instance est un attribut pur le uqel chaque
        instance de la classe ou objet de type de cette classe,
        possède sa propre copie ou description des valeurs des atributs.
        '''
        self.__body_part_id: int = None
        self.__body_part_name: str = ""

    def setBodyPartId(self, bodyPartId: int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut __body_part_id
        :param bodyPartId: l'identifiant d'une partie du corps
        :return: rien
        '''
        self.__body_part_id = bodyPartId

    def getBodyPartId(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une partie du corps
        :return: l'id d'une partie du corps
        '''
        return self.__body_part_id

    def setBodyPartName(self, bodyPartName: str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut bodyPartName
        :param bodyPartName: le nom de la partie du corps
        :return: rien
        '''
        self.__body_part_name = bodyPartName

    def getBodyPartName(self) -> str:
        '''
        cette méthode permet de retourner le nom d'une partie du corps
        :return: le nom d'une partie du corps
        '''
        return self.__body_part_name


