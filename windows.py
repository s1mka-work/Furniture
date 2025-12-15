class OutOfRangeException(Exception):
    def __init__(self, value):
        self.value = value

class Window:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        if 280 <= value <= 2400:
            self._height = value
        else:
            raise OutOfRangeException(value)

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if 0 < value <= 1300:
            self._width = value
        else:
            raise OutOfRangeException(value)

    def get_elements(self):
        pass

class TurnWindow(Window):
    def get_elements(self):
        result = {}
        base = BaseElements.get_base_elements()

        if self.width <= 700:
            height_items = HeightManager.get_height(self.height)
            for key, value in height_items.items():
                if key not in result:
                    result[key] = value
                else:
                    result[key] = result[key] + value
        elif self.width > 700:
            height_items = WidthManager.get_height_if_width(self.height)
            width_items = WidthManager.get_width(self.width)
            for key, value in height_items.items():
                if key not in result:
                    result[key] = value
                else:
                    result[key] = result[key] + value
            for key, value in width_items.items():
                if key not in result:
                    result[key] = value
                else:
                    result[key] = result[key] + value

        for key, value in base.items():
            if key not in result:
                result[key] = value
            else:
                result[key] = result[key] + value
        return result

class BaseElements:
    @staticmethod
    def get_base_elements():
        return {
            'Петлевая группа': 1,
            'Комплект декоративных накладок': 1,
            'Оконная ручка': 1
        }

class HeightManager:
    rules = [
        {
            'min': 280,
            'max': 400,
            'elements': {
                'ПР 1': 1,
                'Ответка': 2,
                'СП': 0
            }
        },
        {
            'min': 401,
            'max': 600,
            'elements': {
                'ПР 2': 1,
                'Ответка': 2,
                'СП': 0
            }
        },
        {
            'min': 601,
            'max': 800,
            'elements': {
                'ПР 3': 1,
                'Ответка': 2,
                'СП': 1
            }
        },
        {
            'min': 801,
            'max': 1000,
            'elements': {
                'ПР 4': 1,
                'Ответка': 3,
                'СП': 1
            }
        },
        {
            'min': 1001,
            'max': 1200,
            'elements': {
                'ПР 5': 1,
                'Ответка': 3,
                'СП': 1
            }
        },
        {
            'min': 1201,
            'max': 1400,
            'elements': {
                'ПР 6': 1,
                'Ответка': 3,
                'СП': 2
            }
        },
        {
            'min': 1401,
            'max': 1600,
            'elements': {
                'ПР 7': 1,
                'Ответка': 3,
                'СП': 2
            }
        },
        {
            'min': 1601,
            'max': 1800,
            'elements': {
                'ПР 8': 1,
                'Ответка': 3,
                'СП': 2
            }
        },
        {
            'min': 1801,
            'max': 2000,
            'elements': {
                'ПР 9': 1,
                'Ответка': 4,
                'СП': 2
            }
        },
        {
            'min': 2001,
            'max': 2200,
            'elements': {
                'ПР 10': 1,
                'Ответка': 4,
                'СП': 3
            }
        },
        {
            'min': 2201,
            'max': 2400,
            'elements': {
                'ПР 11': 1,
                'Ответка': 4,
                'СП': 3
            }
        }
    ]
    @staticmethod
    def get_height(height):
        for rule in HeightManager.rules:
            if rule['min'] <= height <= rule['max']:
                return rule['elements']
        return {}

class WidthManager:
    height_rule = [
        {
            'min': 500,
            'max': 800,
            'elements': {
                'ПОП 1': 1,
                'Ответка': 0
            }
        },
        {
            'min': 801,
            'max': 1200,
            'elements': {
                'ПОП 2': 1,
                'Ответка': 1
            }
        },
        {
            'min': 1201,
            'max': 1400,
            'elements': {
                'ПОП 3': 1,
                'Ответка': 1
            }
        },
        {
            'min': 1401,
            'max': 1600,
            'elements': {
                'ПОП 4': 1,
                'Ответка': 2
            }
        },
        {
            'min': 1601,
            'max': 2000,
            'elements': {
                'ПОП 5': 1,
                'Ответка': 2
            }
        },
        {
            'min': 2001,
            'max': 2400,
            'elements': {
                'ПОП 6': 1,
                'Ответка': 3
            }
        }
    ]
    @staticmethod
    def get_height_if_width(height):
        for rule in WidthManager.height_rule:
            if rule['min'] <= height <= rule['max']:
                return rule['elements']
        return {}

    width_rule = [
        {
            'min': 701,
            'max': 1000,
            'elements': {
                'УП 1': 2,
                'Ответка': 3,
                'ВШ 90': 1,
                'НЗ': 1,
                'НП': 1
            }
        },
        {
            'min': 1001,
            'max': 1300,
            'elements': {
                'УП 2': 2,
                'Ответка': 5,
                'ВШ 90': 1,
                'НЗ': 1,
                'НП': 1
            }
        }
    ]
    @staticmethod
    def get_width(width):
        for rule in WidthManager.width_rule:
            if rule['min'] <= width <= rule['max']:
                return rule['elements']
        return {}

class Catalog:
    catalog_rule = {
        'Приводы': ['ПР 1', 'ПР 2', 'ПР 3', 'ПР 4', 'ПР 5', 'ПР 6', 'ПР 7', 'ПР 8', 'ПР 9', 'ПР 10', 'ПР 11',
                    'ПОП 1', 'ПОП 2', 'ПОП 3', 'ПОП 4', 'ПОП 5', 'ПОП 6'],
        'Вспомогательные элементы': ['УП 1', 'УП 2', 'ВШ 90', 'НЗ', 'НП', 'Ответка', 'СП'],
        'База': ['Петлевая группа', 'Комплект декоративных накладок', 'Оконная ручка']
    }
    @staticmethod
    def get_category(element):
        for rule, value in Catalog.catalog_rule.items():
            if element in value:
                return rule
        return None

class Output:
    output_rule = {
        'Приводы': {},
        'Вспомогательные элементы': {},
        'База': {}
    }
    @staticmethod
    def create_structure(result_dict):
        for key, value in result_dict.items():
            category = Catalog.get_category(key)
            Output.output_rule[category][key] = value

    @staticmethod
    def output_structure():
        for key in Output.output_rule:
            print(key.upper())
            for el, value in Output.output_rule[key].items():
                print(f'- {el}: {value}')
