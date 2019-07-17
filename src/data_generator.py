from random import choice

import simplejson as json
from dotty_dict import dotty


class DataGenerator:
    def __init__(self, properties: dict):
        self.properties = properties

    # noinspection PyMethodMayBeStatic
    def print_to_json(self, generated_data, filename='json_data.json'):
        with open(filename, 'w') as f:
            json.dump(generated_data, f, indent=4)


class ValidDataGenerator(DataGenerator):
    def generate_valid_data_for_create(self, parent='', valid_data=None, data=None):
        valid_data = valid_data or dotty()
        data = data or self.properties
        parent = parent or ''

        for property_name, requirements in data.items():
            if isinstance(requirements, dict):
                if property_name in self.properties.keys():
                    parent = ''

                parent += property_name + '.'
                self.generate_valid_data_for_create(
                    valid_data=valid_data,
                    data=requirements,
                    parent=parent
                )
            else:
                try:
                    valid_data[parent + property_name] = getattr(requirements, 'generate_valid_data')()
                except AttributeError as e:
                    raise e

        return valid_data.to_dict()


class InvalidDataGenerator(DataGenerator):
    def __init__(self, properties, missing_key_chance=.3, value_invalid_instance_chance=1):
        super().__init__(properties)

        self.missing_key_chance = round(missing_key_chance * 100)
        self.value_invalid_instance_chance = round(value_invalid_instance_chance * 100)

    def generate_invalid_data_for_create(self, parent='', valid_data=None, data=None):
        valid_data = valid_data or dotty()
        data = data or self.properties
        parent = parent or ''

        for property_name, requirements in data.items():
            if isinstance(requirements, dict):
                if property_name in self.properties.keys():
                    parent = ''

                parent += property_name + '.'
                self.generate_invalid_data_for_create(
                    valid_data=valid_data,
                    data=requirements,
                    parent=parent
                )
            else:
                try:
                    missing_key_chance = self._generate_chance(self.missing_key_chance)
                    missing_key = choice(missing_key_chance)

                    if missing_key:
                        continue

                    invalid_instance_chance = self._generate_chance(self.value_invalid_instance_chance)
                    invalid_instance = choice(invalid_instance_chance)

                    if invalid_instance:
                        valid_instance = getattr(requirements, 'instance')
                        generate_invalid_data_instance = getattr(requirements, 'generate_invalid_data_instance')
                        valid_data[parent + property_name] = generate_invalid_data_instance(valid_instance)
                    else:
                        parent_value = valid_data.get(parent[:-1])

                        if isinstance(parent_value, dict):
                            valid_data[parent + property_name] = getattr(requirements, 'generate_invalid_data')

                except AttributeError as e:
                    raise e

        return valid_data.to_dict()

    # noinspection PyMethodMayBeStatic
    def _generate_chance(self, invalid_chance):
        return [True] * invalid_chance + [False] * (100 - invalid_chance)


class MixedDataGenerator(DataGenerator):
    pass
