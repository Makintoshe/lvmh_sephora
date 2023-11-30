
class Brands:

    # un attribut de classe, est une valeur partagée par toutes les instances de la classe
    # ici nous n'avons pas.

    def __init__(self):
        '''
        le constructeur de notre méthode, contrairement à d'autres langages,
        en python, un attribut d'instance est un attribut pur le uqel chaque
        instance de la classe ou objet de type de cette classe,
        possède sa propre copie ou description des valeurs des atributs.
        '''
        self.__brand_id: int = None
        self.__brand_name: str = ""

    def setBrandId(self, brandId: int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__brand_id = brandId

    def getBrandId(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__brand_id

    def setBrandName(self, brandName: str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandName>
        :param brandName: le nom de la marque
        :return: rien
        '''
        self.__brand_name = brandName

    def getBrandName(self) -> str:
        '''
        cette méthode permet de retourner le nom d'une marque
        :return: le nom d'une marque
        '''
        return self.__brand_name


