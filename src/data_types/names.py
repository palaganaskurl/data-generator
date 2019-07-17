from random import choice

from src.data_types.base import Data


class Name:
    instance = str

    @property
    def invalid_name(self):
        invalid_names = [
            '',
            '    ',
            99,
            69,
            68
        ]

        return choice(invalid_names)


class FullName(Data, Name):
    def generate_valid_data(self):
        return self.faker.name()

    def generate_invalid_data(self):
        return self.invalid_name


class FirstName(Data, Name):
    # TODO: Gender based name
    def generate_valid_data(self):
        return self.faker.first_name()

    def generate_invalid_data(self):
        return self.invalid_name


class LastName(Data, Name):
    # TODO: Gender based name
    def generate_valid_data(self):
        return self.faker.last_name()

    def generate_invalid_data(self):
        return self.invalid_name
