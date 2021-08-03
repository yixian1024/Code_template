# parser.py
import yaml
import logging

logger = logging.getLogger(__name__)

class food:

    def __init__(self, iso_dict):
        try:
            self.apple = iso_dict['apple']
            self.chocolate = iso_dict['chocolate']
        except KeyError as e:
            logging.warning(f'KeyError in iso : {e}')


class OBJ:

    def __init__(self, yaml_file):
        try:
            with open(yaml_file, 'r') as f:
                data = yaml.load(f, Loader=yaml.BaseLoader)
        except OSError as e:
            logging.error('Could not open/read file: {}'.format(yaml_file))
            raise e
        try:
            # iso parameters
            food_dict = data['food']
            self.food = food(food_dict)
        except KeyError as e:
            raise e