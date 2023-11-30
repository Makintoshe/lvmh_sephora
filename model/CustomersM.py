class Customers:

    def __init__(self):
        self.__customer_id: int = None
        self.__customer_name: str = ""
        self.__email: str = ""
        self.__phone_number: str = ""

    def setCustomerID(self, customer_id: int) -> None:
        self.__customer_id = customer_id

    def getCustomerID(self) -> int:
        return self.__customer_id

    def setCustomerName(self, customer_name: str) -> None:
        self.__customer_name = customer_name

    def getCustomerName(self) -> str:
        return self.__customer_name

    def setEmail(self, email: str) -> None:
        self.__email = email

    def getEmail(self) -> str:
        return self.__email

    def setPhoneNumber(self, phone_number: str) -> None:
        self.__phone_number = phone_number

    def getPhoneNumber(self) -> str:
        return self.__phone_number
