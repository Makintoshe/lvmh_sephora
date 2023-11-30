from model import GendersM, BrandsM, BodyPartsM

class Products:

    def __init__(self):
        self.__product_id: int = None
        self.__product_name: str = ""
        self.__brand_id: BrandsM.Brands = None
        self.__body_part_id: BodyPartsM.Body_parts = None
        self.__gender_id: GendersM.Genders = None
        self.__price: float = None
        self.__stock_quantity: int = None

    def setProductID(self, product_id: int) -> None:
        self.__product_id = product_id

    def getProductID(self) -> int:
        return self.__product_id

    def setProductName(self, product_name: str) -> None:
        self.__product_name = product_name

    def getProductName(self) -> str:
        return self.__product_name

    def setBrandID(self, brand_id: BrandsM.Brands) -> None:
        self.__brand_id = brand_id

    def getBrandID(self) -> BrandsM.Brands:
        return self.__brand_id

    def setBodyPartID(self, body_part_id: BodyPartsM.Body_parts) -> None:
        self.__body_part_id = body_part_id

    def getBodyPartID(self) -> BodyPartsM.Body_parts:
        return self.__body_part_id

    def setGenderID(self, gender_id: GendersM.Genders) -> None:
        self.__gender_id = gender_id

    def getGenderID(self) -> GendersM.Genders:
        return self.__gender_id

    def setPrice(self, price: float) -> None:
        self.__price = price

    def getPrice(self) -> float:
        return self.__price

    def setStockQuantity(self, stock_quantity: int) -> None:
        self.__stock_quantity = stock_quantity

    def getStockQuantity(self) -> int:
        return self.__stock_quantity
