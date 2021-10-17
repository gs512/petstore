from dataclasses import dataclass, field
import uuid
from datetime import datetime, date
from animals import Animal, ChippedAnimal

@dataclass
class UUID():
    id_: int = field(compare=False, init=False, default=None)

    def __post_init__(self):
        if self.id_ is None:
            self.id_ = uuid.uuid4()

@dataclass
class Room(UUID):
    id_: int = field(compare=False, init=False, default=None)
    showroom_display: list
    animal_list: list
    sold_animal_list: list
    warehouse_setup: dict = field(default_factory={'dog': 15, 'cat': 30, 'bird': 30})
    showroom_setup: dict = field(default_factory={'dog': 5, 'cat': 10, 'bird': 15})

    def send_warehouse_inventory(self):
        return {'pets':[pet._id for pet in self.animal_list],
        'setup': self.warehouse_setup
        }

    def move_animal_to_showroom(self, pet:Animal):
        if pet not in self.animal_list:
            return False
        if self.showroom_setup[pet.type] == 0:
            return False
        if not pet.is_chipped:
            return False
        if pet.id_ not in self.showroom_display:
            self.showroom_display.append(pet.id_)
            self.showroom_setup[pet.type]-=1
        return True


    def remove_animal_from_showroom(self, pet:Animal):
        if pet not in self.animal_list:
            return False
        if pet.id_ not in self.showroom_display:
            return  False
        
        self.showroom_display.remove(pet.id_)
        self.showroom_setup[pet.type]+=1
        return True


    def add_animal_to_warehouse(self, pet:Animal):
        if pet.type not in self.warehouse_setup.keys():
            return False
        if pet in self.animal_list:
            return False
        if self.warehouse_setup[pet.type] == 0:
            return False
        self.animal_list.append(pet)
        self.warehouse_setup[pet.type]-=1
        return True


    def send_showroom_inventory(self):
        return {'pets':self.showroom_display,
        'setup': self.showroom_setup
        }


    def sell_animal(self, pet:Animal):
        if pet not in self.animal_list:
            return False
        if pet not in self.animal_list:
            return False
        if pet.id_ not in self.showroom_display:
            return False
        
        self.sold_animal_list.append(pet)
        self.animal_list.remove(pet)
        self.showroom_display.remove(pet.id_)
        self.showroom_setup[pet.type]+=1
        # trigger sale message
        return True
