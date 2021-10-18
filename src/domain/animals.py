from dataclasses import dataclass, field
from datetime import datetime, date
from domain.uuids import UUID
import uuid

@dataclass
class Animal(UUID):
    name: str = field(init=True)
    type: str = field(init=True)
    description: str = field(init=True)
    price: float = 500.0
    date_of_birth: datetime = field(default=None)
    is_refundable: bool = field(default=True)
    date_of_sale: datetime = field(default=None)
    date_of_option: datetime = field(default=None)
    is_chipped: bool = field(default=True)

    def has_been_sold(self):
        self.date_of_sale = date.today()
    
    
@dataclass
class ChippedAnimal(Animal):
    date_of_chip: datetime = field(default=None)
    chip_id: uuid.UUID = field(default=None)
    is_chipped: bool = field(default=False)

    def is_chipable(self):
        today = date.today()
        diff_in_months = (today.year - self.date_of_birth.year) * 12
        diff_in_months += today.month - self.date_of_birth.month
        return diff_in_months >= 2

