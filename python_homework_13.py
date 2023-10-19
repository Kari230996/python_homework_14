class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(
            f'Invalid name: {value}. Name should be a non-empty string.')


class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(
            f'Invalid age: {value}. Age should be a positive integer.')


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(
            f'Invalid id: {value}. Id should be a 6-digit positive integer between 100000 and 999999.')


class Person:
    def __init__(self, last_name: str, first_name: str, middle_name: str, age: int):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str) or not value:
            raise InvalidNameError(value)
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) or not value:
            raise InvalidNameError(value)
        self._first_name = value

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        if not isinstance(value, str) or not value:
            raise InvalidNameError(value)
        self._middle_name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise InvalidAgeError(value)
        self._age = value

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, id):
        super().__init__(last_name, first_name, middle_name, age)
        self.id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if isinstance(value, int) and (100000 <= value <= 999999):
            self._id = value
        else:
            raise InvalidIdError(value)

    def get_level(self):
        return sum(int(digit) for digit in str(self.id)) % 7
