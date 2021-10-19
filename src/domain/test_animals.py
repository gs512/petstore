import pytest
import uuid
from datetime import date, datetime
from domain.animals import Animal, ChippedAnimal

dog = Animal(name='tom', price=10, type='dog',
            description='3 legged dog', date_of_birth=date.fromisoformat('2020-11-18'),
            is_refundable=False, date_of_sale=date.fromisoformat('2021-11-18'),
            date_of_option=date.fromisoformat('2020-10-18'))

chipped_cat = ChippedAnimal(name='skip', price=10, type='cat',
            description='chipped cat', date_of_birth=date.fromisoformat('2020-11-18'),
            is_refundable=False, date_of_sale=date.fromisoformat('2021-11-18'),
            date_of_option=date.fromisoformat('2020-10-18'))

def test_animal_model_init():
    assert dog.name == 'tom'
    assert dog.price == 10
    assert dog.type == 'dog'
    assert dog.description == '3 legged dog'
    assert dog.date_of_birth == date.fromisoformat('2020-11-18')
    assert dog.is_refundable == False
    assert dog.date_of_sale == date.fromisoformat('2021-11-18')
    assert dog.date_of_option == date.fromisoformat('2020-10-18')
    assert dog.is_chipped == True

def test_animal_copy():
    dog_copy = dog
    assert dog.id_ == dog_copy.id_

def test_animal_chip():
    assert dog.is_chipped == True
    assert dog.can_be_chipped() == False

def test_chipped_animal_chip():
    assert chipped_cat.is_chipped == False
    assert chipped_cat.can_be_chipped() == True

def test_chipped_animal_setchip():
    chip_id = uuid.uuid4()
    assert chipped_cat.set_chip(chip_id) == True
    assert chipped_cat.is_chipped == True
    assert chipped_cat.chip_id == chip_id
    assert chipped_cat.date_of_chip == date.today()

    chipped_cat.set_date_of_birth(date.today())
    assert chipped_cat.can_be_chipped() == False
    with pytest.raises(Exception) as e_info:
        chipped_cat.set_chip(chip_id)
