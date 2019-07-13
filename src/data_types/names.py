from src.data_types.base import Data


class Name(Data):
    def generate_valid_data(self):
        return self.faker.name()


class FirstName(Data):
    # TODO: Gender based name
    def generate_valid_data(self):
        return self.faker.first_name()


class LastName(Data):
    # TODO: Gender based name
    def generate_valid_data(self):
        return self.faker.last_name()


if __name__ == '__main__':
    print(Name().generate_valid_data())
