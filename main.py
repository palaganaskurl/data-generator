from src.data_generator import ValidDataGenerator, InvalidDataGenerator
from src.data_types.names import FullName, FirstName, LastName


if __name__ == '__main__':
    # d = ValidDataGenerator({
    #     'name': Name(),
    #     'full_name': {
    #         'first_name': FirstName(),
    #         'last_name': LastName(),
    #         'others': {
    #             'suffix': Name()
    #         }
    #     },
    #     'full_name_xd': {
    #         'first_name': FirstName(),
    #         'last_name': LastName(),
    #         'others': {
    #             'suffix': Name()
    #         }
    #     }
    # })
    # import pprint
    # pprint.pprint(d.generate_valid_data_for_create())
    d = InvalidDataGenerator({
        'name': FullName(),
        'full_name': {
            'first_name': FirstName(),
            'last_name': LastName(),
            'others': {
                'suffix': FullName()
            }
        },
        'full_name_xd': {
            'first_name': FirstName(),
            'last_name': LastName(),
            'others': {
                'suffix': FullName()
            }
        }
    })
    import pprint
    x = d.generate_invalid_data_for_create()
    pprint.pprint(x)
    d.print_to_json(x)
