from dataclasses import dataclass, field
from datetime import datetime, date
from domain import PetstoreEntity
from domain.animals import Animal, ChippedAnimal

@dataclass
class Room(PetstoreEntity):
    id_: int = field(compare=False, init=False, default=None)
    showroom_display: list
    animal_list: list
    sold_animal_list: list
    optioned_animal_list: list
    warehouse_setup: dict = field(default_factory={'dog': 15, 'cat': 30, 'bird': 30})
    showroom_setup: dict = field(default_factory={'dog': 5, 'cat': 10, 'bird': 15})

    def display_warehouse_inventory(self):
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
        if not pet.id_ in self.optioned_animal_list:
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


    def display_showroom_inventory(self):
        return {'pets':self.showroom_display,
        'setup': self.showroom_setup
        }

    def sell_animal(self, pet:Animal):
        if pet not in self.animal_list:
            return False
        if pet.id_ in self.showroom_display:
            self.showroom_display.remove(pet.id_)
            self.showroom_setup[pet.type]+=1
            
        if pet.id_ in self.optioned_animal_list:
            self.optioned_animal_list.remove(pet.id_)
        
        self.sold_animal_list.append(pet)
        self.animal_list.remove(pet)
        pet.date_of_sale = date.today()
        return True

    def option_animal(self, pet:Animal):
        if pet not in self.animal_list:
            return False
        if pet.id_ not in self.showroom_display:
            return False
        pet.date_of_option = date.today()
        return True
        

    def remove_animal(self, pet:Animal):
        if pet.type not in self.warehouse_setup.keys():
            return False
        if pet not in self.animal_list:
            return False

        self.remove_animal_from_showroom(pet)
        if pet._id in self.optioned_animal_list:
            self.optioned_animal_list.remove(pet._id)

        self.animal_list.remove(pet)
        self.warehouse_setup[pet.type]-=1
        
        return True
