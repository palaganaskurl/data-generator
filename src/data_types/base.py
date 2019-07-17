from abc import ABCMeta, abstractmethod
from random import choice

from faker import Faker


class Data(metaclass=ABCMeta):
    faker = Faker()

    @abstractmethod
    def generate_valid_data(self):
        raise NotImplementedError

    @abstractmethod
    def generate_invalid_data(self):
        raise NotImplementedError

    def generate_invalid_data_instance(self, valid_instance):
        instances = {
            bool: self.faker.pybool(),
            float: self.faker.pydecimal(),
            int: self.faker.pyint(),
            list: self.faker.pylist(6, True, 'str', 'float', 'int', 'decimal', 'uri', 'email')
        }

        if valid_instance in instances:
            del instances[valid_instance]

        return choice(list(instances.values()))
