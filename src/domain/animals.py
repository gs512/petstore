import uuid
from dataclasses import dataclass, field
from datetime import datetime, date
from domain import PetstoreEntity

@dataclass
class Animal(PetstoreEntity):
    name: str = field(init=True)
    type: str = field(init=True)
    description: str = field(init=True)
    price: float = 500.0
    date_of_birth: datetime = field(default=None)
    is_refundable: bool = field(default=True)
    date_of_sale: datetime = field(default=None)
    date_of_option: datetime = field(default=None)
    is_chipped: bool = True

    def can_be_chipped(self)->bool:
        return False

    def set_date_of_sale(self, date_of_sale:datetime=None):
        if date_of_sale is None:
            date_of_sale = date.today()
        self.date_of_sale = date_of_sale

    def set_date_of_option(self, date_of_option:datetime=None):
        if date_of_option is None:
            date_of_option = date.today()
        self.date_of_option = date_of_option
    
    def set_date_of_birth(self, date_of_birth:datetime=None):
        if date_of_birth is None:
            date_of_birth = date.today()
        self.date_of_birth = date_of_birth
    
@dataclass
class ChippedAnimal(Animal):
    is_chipped: bool = False
    date_of_chip: datetime = field(default=None)
    chip_id: uuid.UUID = field(default=None)

    def can_be_chipped(self)->bool:
        if self.date_of_birth is None:
            return False
        today = date.today()
        diff_in_months = (today.year - self.date_of_birth.year) * 12
        diff_in_months += today.month - self.date_of_birth.month
        return diff_in_months >= 2

    def set_date_of_chip(self, date_of_chip:datetime=None)->bool:
        if not self.can_be_chipped():
            return False
        if date_of_chip is None:
            date_of_chip = date.today()
        self.date_of_chip = date_of_chip
        return True

    def set_chip(self, chip_id:uuid.uuid4, date_of_chip=None)->bool:
        if not self.can_be_chipped():
            return False
        if chip_id is None:
            return False
        
        self.chip_id = chip_id
        self.set_date_of_chip(date_of_chip)
        self.is_chipped = True
        return True
