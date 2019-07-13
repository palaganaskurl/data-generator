from random import choice


class DataGenerator:
    def __init__(self, properties):
        """
        Properties = {
            'first_name': Name()
        }
        """
        self.properties = properties

    def generate_valid_data(self, method, valid_data, data=None):
        if data is None:
            data = self.properties

        for property_name, requirements in data.items():
            if isinstance(requirements, dict):
                self.generate_valid_data(method, valid_data, data=requirements)
            else:
                try:
                    valid_data[property_name] = getattr(requirements, 'generate_valid_data')()
                except AttributeError as e:
                    raise e

        return valid_data

    def generate_invalid_data(self):
        # add missing parameters chance
        # add percentage on nested values invalid parent instance
        pass

    def generate_mixed_data(self):
        # add missing parameters chance
        # add valid/invalid ratio
        pass


class InvalidValue:
    classes = [
        list,
        dict,
        bool,
        str
    ]

    def get_random_invalid_value(self, not_this_instance):
        self.classes.remove(not_this_instance)

        return choice(self.classes)
