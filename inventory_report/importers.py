from typing import Dict, Type
from inventory_report.product import Product
from abc import ABC, abstractmethod
import json

class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path


    @abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path, "r") as file:
            data = json.load(file)

        products = []    
        for item in data:
            product = Product(
                item.get("id", ""),
                item.get("product_name", ""),
                item.get("company_name", ""),
                item.get("manufacturing_date", ""),
                item.get("expiration_date", ""),
                item.get("serial_number", ""),
                item.get("storage_instructions", "")
            )
            products.append(product)

        return products

class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
