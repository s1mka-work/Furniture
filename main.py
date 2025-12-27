from windows import *
windows = []
output = {}

def main():
    list_windows(count_windows())
    dict_windows()
    output_windows()
    print(Output.output_rule)

def count_windows():
    count = int(input('Введите количество окон: '))
    return count

def list_windows(count):
    counter = 0
    while counter < count:
        try:
            window_type = input('Введите тип окна: ')
            height = int(input('Введите высоту окна: '))
            width = int(input('Введите ширину окна: '))
        except (ValueError, HeightOutOfRangeException):
            print('Ошибка! Введите число от 280 до 2400')
            continue
        except (ValueError, WidthOutOfRangeException):
            print('Ошибка! Введите число от 280 до 1300')
        else:
            if window_type.lower() == 'поворотное':
                window = TurnWindow(height, width)
                windows.append(window)
            elif window_type.lower() == 'фрамуга':
                window = TransomWindow(height, width)
                windows.append(window)
            counter += 1

def dict_windows():
    for window in windows:
        res = window.get_elements()
        for key, value in res.items():
            if key not in output:
                output[key] = value
            else:
                output[key] = output[key] + value

def output_windows():
    Output.create_structure(output)
    Output.output_structure()

if __name__ == '__main__':
    main()
