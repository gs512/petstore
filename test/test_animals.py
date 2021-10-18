import pytest
import uuid
from datetime import date, datetime
from src.domain.animals import Animal, ChippedAnimal


def test_animal_model_init():
    code = uuid.uuid4()
    dog = Animal(id_=code, name='tom', price=10, type='dog',
                description='3 legged dog', date_of_birth=date.fromisoformat('2020-11-18'),
                is_refundable=False, date_of_sale=date.fromisoformat('2021-11-18'),
                date_of_option=date.fromisoformat('2020-10-18'),
                is_chipped=True)
    assert dog.id_ == code
    assert dog.name == 'tom'
    assert dog.price == 10
    assert dog.type == 'dog'
    assert dog.description == '3 legged dog'
    assert dog.date_of_birth == date.fromisoformat('2020-11-18')
    assert dog.is_refundable == False
    assert dog.date_of_sale == date.fromisoformat('2021-11-18')
    assert dog.date_of_option == date.fromisoformat('2020-10-18')
    assert dog.is_chipped == True

# def test_can_allocate_if_available_greater_than_required():
#     large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)
#     assert large_batch.can_allocate(small_line)

# def test_cannot_allocate_if_available_smaller_than_required():
#     small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
#     assert small_batch.can_allocate(large_line) is False

# def test_can_allocate_if_available_equal_to_required():
#     batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
#     assert batch.can_allocate(line)

# def test_cannot_allocate_if_skus_do_not_match():
#     batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
#     different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
#     assert batch.can_allocate(different_sku_line) is False