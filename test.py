import pytest
from python_homework_13 import Person, Employee, InvalidNameError, InvalidAgeError, InvalidIdError


@pytest.fixture
def example_person():
    return Person("Doe", "John", "Smith", 30)


@pytest.fixture
def example_employee():
    return Employee("Doe", "John", "Smith", 30, 123456)


def test_person_creation_with_valid_data(example_person):
    assert example_person.last_name == 'Doe'
    assert example_person.first_name == 'John'
    assert example_person.middle_name == 'Smith'
    assert example_person.age == 30


def test_person_creation_with_invalid_data():
    with pytest.raises(InvalidNameError):
        Person("", "John", "Smith", 30)


def test_person_creation_with_invalid_age():
    with pytest.raises(InvalidAgeError):
        Person("Doe", "John", "Smith", 0)


def test_person_birthday():
    person = Person("Doe", "John", "Smith", 30)
    person.birthday()
    assert person.age == 31


def test_employee_creation_with_valid_data(example_employee):
    assert example_employee.last_name == "Doe"
    assert example_employee.first_name == "John"
    assert example_employee.middle_name == "Smith"
    assert example_employee.age == 30
    assert example_employee.id == 123456


def test_employee_creation_with_invalid_id():
    with pytest.raises(InvalidIdError):
        Employee("Doe", "John", "Smith", 30, 99999)


def test_employee_get_level(example_employee):
    # Для id = 123456, сумма цифр равна 1 + 2 + 3 + 4 + 5 + 6 = 21
    # Остаток от деления 21 на 7 равен 0
    assert example_employee.get_level() == 0


def test_employee_get_age(example_employee):
    assert example_employee.get_age() == 30


#############################################

# Запускаем наш код с помощью: pytest test.py

#############################################
