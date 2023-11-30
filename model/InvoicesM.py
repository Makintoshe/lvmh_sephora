from datetime import date
from model.OrdersM import Orders

class Invoices:

    def __init__(self):
        self.__invoice_id: int = None
        self.__order_id: Orders = None
        self.__invoice_date: date = None
        self.__total_amount: float = None

    def setInvoiceID(self, invoice_id: int) -> None:
        self.__invoice_id = invoice_id

    def getInvoiceID(self) -> int:
        return self.__invoice_id

    def setOrderID(self, order_id: Orders) -> None:
        self.__order_id = order_id

    def getOrderID(self) -> Orders:
        return self.__order_id

    def setInvoiceDate(self, invoice_date: date) -> None:
        self.__invoice_date = invoice_date

    def getInvoiceDate(self) -> date:
        return self.__invoice_date

    def setTotalAmount(self, total_amount: float) -> None:
        self.__total_amount = total_amount

    def getTotalAmount(self) -> float:
        return self.__total_amount
