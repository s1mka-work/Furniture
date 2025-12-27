class NoncorrectInputException(Exception):
    def __init__(self, value):
        self.value = value
class HeightOutOfRangeException(Exception):
    def __init__(self, value):
        self.value = value
class WidthOutOfRangeException(Exception):
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
        if value > 0:
            self._height = value
        else:
            raise NoncorrectInputException(value)

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NoncorrectInputException(value)

    def get_elements(self):
        pass

class TurnWindow(Window):
    def __init__(self, height, width):
        super().__init__(height, width)

    @Window.height.setter
    def height(self, value):
        if not 280 <= value <= 2400:
            raise HeightOutOfRangeException(value)
        super(TurnWindow, TurnWindow).height.fset(self, value)
    @Window.width.setter
    def width(self, value):
        if not 280 <= value <= 1300:
            raise WidthOutOfRangeException(value)
        super(TurnWindow, TurnWindow).width.fset(self, value)

    def get_elements(self):
        result = {}
        base = TurnWindowBaseElements.get_base_elements()

        if self.width <= 700:
            height_items = TurnWindowHeightManager.get_height(self.height)
            for key, value in height_items.items():
                if key not in result:
                    result[key] = value
                else:
                    result[key] = result[key] + value
        elif self.width > 700:
            height_items = TurnWindowWidthManager.get_height(self.height)
            width_items = TurnWindowWidthManager.get_width(self.width)
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

class TurnWindowBaseElements:
    @staticmethod
    def get_base_elements():
        return {
            'ВР': 1,
            'ШВП': 1,
            'ВС': 1,
            'НР': 1,
            'НС': 1,
            'Комплект декоративных накладок': 1,
            'Оконная ручка': 1
        }

class TurnWindowHeightManager:
    turn_window_height_rules = [
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
        for rule in TurnWindowHeightManager.turn_window_height_rules:
            if rule['min'] <= height <= rule['max']:
                return rule['elements']
        return {}

class TurnWindowWidthManager:
    turn_window_width_rules = [
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
    def get_height(height):
        for rule in TurnWindowWidthManager.turn_window_width_rules:
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
        for rule in TurnWindowWidthManager.width_rule:
            if rule['min'] <= width <= rule['max']:
                return rule['elements']
        return {}

class TransomWindow(Window):
    def __init__(self, height, width):
        super().__init__(height, width)

    @Window.height.setter
    def height(self, value):
        if 280 <= value <= 1300:
            super(TransomWindow, TransomWindow).height.fset(self, value)
        else:
            raise HeightOutOfRangeException(value)
    @Window.width.setter
    def width(self, value):
        if 280 <= value <= 2400:
            super(TransomWindow, TransomWindow).width.fset(self, value)
        else:
            raise WidthOutOfRangeException(value)

    def get_elements(self):
        result = {}
        base = TransomWindowBaseElements.get_base_elements()
        width_items = TransomWindowWidthManager.get_width(self.width)
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

class TransomWindowBaseElements:
    @staticmethod
    def get_base_elements():
        return {
            'ВР': 2,
            'ШВП': 2,
            'ВС': 2,
            'ФП': 2,
            'КДНВ': 2,
            'ФН': 2,
            'Оконная ручка': 1
        }

class TransomWindowWidthManager:
    transom_window_width_rules = [
        {
            'min': 280,
            'max': 400,
            'elements': {
                'ПР 1': 1,
                'Ответка': 2,
                'СП': 0,
                'ВР': 0,
                'ШВП': 0,
                'ВС': 0,
                'ФП': 0,
                'КДНВ': 0,
                'ФН': 0
            }
        },
        {
            'min': 401,
            'max': 600,
            'elements': {
                'ПР 2': 1,
                'Ответка': 2,
                'СП': 0,
                'ВР': 0,
                'ШВП': 0,
                'ВС': 0,
                'ФП': 0,
                'КДНВ': 0,
                'ФН': 0
            }
        },
        {
            'min': 601,
            'max': 800,
            'elements': {
                'ПР 3': 1,
                'Ответка': 2,
                'СП': 1,
                'ВР': 0,
                'ШВП': 0,
                'ВС': 0,
                'ФП': 0,
                'КДНВ': 0,
                'ФН': 0
            }
        },
        {
            'min': 801,
            'max': 1000,
            'elements': {
                'ПР 4': 1,
                'Ответка': 3,
                'СП': 1,
                'ВР': 0,
                'ШВП': 0,
                'ВС': 0,
                'ФП': 0,
                'КДНВ': 0,
                'ФН': 0
            }
        },
        {
            'min': 1001,
            'max': 1200,
            'elements': {
                'ПР 5': 1,
                'Ответка': 3,
                'СП': 0,
                'ВР': 1,
                'ШВП': 1,
                'ВС': 1,
                'ФП': 1,
                'КДНВ': 1,
                'ФН': 0
            }
        },
        {
            'min': 1201,
            'max': 1400,
            'elements': {
                'ПР 6': 1,
                'Ответка': 3,
                'СП': 0,
                'ВР': 1,
                'ШВП': 1,
                'ВС': 1,
                'ФП': 1,
                'КДНВ': 1,
                'ФН': 0
            }
        },
        {
            'min': 1401,
            'max': 1600,
            'elements': {
                'ПР 7': 1,
                'Ответка': 3,
                'СП': 2,
                'ВР': 1,
                'ШВП': 1,
                'ВС': 1,
                'ФП': 1,
                'КДНВ': 1,
                'ФН': 0
            }
        },
        {
            'min': 1601,
            'max': 1800,
            'elements': {
                'ПР 8': 1,
                'Ответка': 3,
                'СП': 0,
                'ВР': 2,
                'ШВП': 2,
                'ВС': 2,
                'ФП': 2,
                'КДНВ': 2,
                'ФН': 1
            }
        },
        {
            'min': 1801,
            'max': 2000,
            'elements': {
                'ПР 9': 1,
                'Ответка': 4,
                'СП': 0,
                'ВР': 2,
                'ШВП': 2,
                'ВС': 2,
                'ФП': 2,
                'КДНВ': 2,
                'ФН': 1
            }
        },
        {
            'min': 2001,
            'max': 2200,
            'elements': {
                'ПР 10': 1,
                'Ответка': 4,
                'СП': 0,
                'ВР': 3,
                'ШВП': 3,
                'ВС': 3,
                'ФП': 3,
                'КДНВ': 3,
                'ФН': 1
            }
        },
        {
            'min': 2201,
            'max': 2400,
            'elements': {
                'ПР 11': 1,
                'Ответка': 4,
                'СП': 0,
                'ВР': 3,
                'ШВП': 3,
                'ВС': 3,
                'ФП': 3,
                'КДНВ': 3,
                'ФН': 2
            }
        }
    ]

    @staticmethod
    def get_width(width):
        for rule in TransomWindowWidthManager.transom_window_width_rules:
            if rule['min'] <= width <= rule['max']:
                return rule['elements']
        return {}

class Catalog:
    catalog_rule = {
        'Приводы': ['ПР 1', 'ПР 2', 'ПР 3', 'ПР 4', 'ПР 5', 'ПР 6', 'ПР 7', 'ПР 8', 'ПР 9', 'ПР 10', 'ПР 11',
                    'ПОП 1', 'ПОП 2', 'ПОП 3', 'ПОП 4', 'ПОП 5', 'ПОП 6'],
        'Вспомогательные элементы': ['УП 1', 'УП 2', 'ВШ 90', 'НЗ', 'НП', 'Ответка', 'СП', 'ФН'],
        'База': [{'Петлевая группа': ['ВР', 'ШВП', 'ВС', 'ФП', 'КДНВ', 'НР', 'НС']}, 'Комплект декоративных накладок', 'Оконная ручка']
    }
    @staticmethod
    def get_category(element):
        for rule, value in Catalog.catalog_rule.items():
            for item in value:
                if isinstance(item, str):
                    if element == item:
                        return rule
                elif isinstance(item, dict):
                    for key, el in item.items():
                        if element in el:
                            return rule
        return {}

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
