from datetime import date
from model import CustomersM
class Orders:

    def __init__(self):
        self.__order_id: int = None
        self.__customer_id: CustomersM = None
        self.__order_date: date = None
        self.__status: str = ""

    def setOrderID(self, order_id: int) -> None:
        self.__order_id = order_id

    def getOrderID(self) -> int:
        return self.__order_id

    def setCustomerID(self, customer_id: CustomersM) -> None:
        self.__customer_id = customer_id

    def getCustomerID(self) -> CustomersM:
        return self.__customer_id

    def setOrderDate(self, order_date: date) -> None:
        self.__order_date = order_date

    def getOrderDate(self) -> date:
        return self.__order_date

    def setStatus(self, status: str) -> None:
        self.__status = status

    def getStatus(self) -> str:
        return self.__status
