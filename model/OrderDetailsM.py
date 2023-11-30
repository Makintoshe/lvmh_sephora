from model.OrdersM import Orders
from model.ProductsM import Products

class OrderDetail:

    def __init__(self):
        self.__order_detail_id: int = None
        self.__order_id: Orders = None
        self.__product_id: Products = None
        self.__quantity: int = None
        self.__total_price: float = None

    def setOrderDetailID(self, order_detail_id: int) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut __order_detail_id.
        :param order_detail_id: L'identifiant du détail de la commande.
        :return: Rien.
        '''
        self.__order_detail_id = order_detail_id

    def getOrderDetailID(self) -> int:
        '''
        Cette méthode permet de retourner l'identifiant du détail de la commande.
        :return: L'identifiant du détail de la commande.
        '''
        return self.__order_detail_id

    def setOrderID(self, order_id: Orders) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut __order_id.
        :param order_id: L'objet Orders associé à ce détail de commande.
        :return: Rien.
        '''
        self.__order_id = order_id

    def getOrderID(self) -> Orders:
        '''
        Cette méthode permet de retourner l'objet Orders associé à ce détail de commande.
        :return: L'objet Orders associé à ce détail de commande.
        '''
        return self.__order_id

    def setProductID(self, product_id: Products) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut __product_id.
        :param product_id: L'objet Products associé à ce détail de commande.
        :return: Rien.
        '''
        self.__product_id = product_id

    def getProductID(self) -> Products:
        '''
        Cette méthode permet de retourner l'objet Products associé à ce détail de commande.
        :return: L'objet Products associé à ce détail de commande.
        '''
        return self.__product_id

    def setQuantity(self, quantity: int) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut __quantity.
        :param quantity: La quantité associée à ce détail de commande.
        :return: Rien.
        '''
        self.__quantity = quantity

    def getQuantity(self) -> int:
        '''
        Cette méthode permet de retourner la quantité associée à ce détail de commande.
        :return: La quantité associée à ce détail de commande.
        '''
        return self.__quantity

    def setTotalPrice(self, total_price: float) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut __total_price.
        :param total_price: Le prix total associé à ce détail de commande.
        :return: Rien.
        '''
        self.__total_price = total_price

    def getTotalPrice(self) -> float:
        '''
        Cette méthode permet de retourner le prix total associé à ce détail de commande.
        :return: Le prix total associé à ce détail de commande.
        '''
        return self.__total_price
