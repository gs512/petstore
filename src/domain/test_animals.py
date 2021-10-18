import pytest
import uuid
from datetime import date, datetime
from domain.animals import Animal, ChippedAnimal

def test_animal_model_init():
    
    dog = Animal(name='tom', price=10, type='dog',
                description='3 legged dog', date_of_birth=date.fromisoformat('2020-11-18'),
                is_refundable=False, date_of_sale=date.fromisoformat('2021-11-18'),
                date_of_option=date.fromisoformat('2020-10-18'),
                is_chipped=True)
    assert dog.name == 'tom'
    assert dog.price == 10
    assert dog.type == 'dog'
    assert dog.description == '3 legged dog'
    assert dog.date_of_birth == date.fromisoformat('2020-11-18')
    assert dog.is_refundable == False
    assert dog.date_of_sale == date.fromisoformat('2021-11-18')
    assert dog.date_of_option == date.fromisoformat('2020-10-18')
    assert dog.is_chipped == True
