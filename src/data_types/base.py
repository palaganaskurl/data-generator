from abc import ABCMeta, abstractmethod
from faker import Faker


class Data(metaclass=ABCMeta):
    faker = Faker()

    @abstractmethod
    def generate_valid_data(self):
        raise NotImplementedError
