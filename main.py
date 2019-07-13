from src.data_generator import DataGenerator
from src.data_types.names import Name, FirstName, LastName


if __name__ == '__main__':
    d = DataGenerator({
        'name': Name(),
        'full_name': {
            'first_name': FirstName(),
            'last_name': LastName()
        }
    })
    print(d.generate_valid_data('a', {}))
