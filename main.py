from windows import *
windows = []
output = {}

def main():
    list_windows(count_windows())
    dict_windows()
    output_windows()
    get_in_file()

def count_windows():
    count = int(input('Введите количество окон: '))
    return count

def list_windows(count):
    counter = 0
    while counter < count:
        try:
            height = int(input('Введите высоту окна: '))
            width = int(input('Введите ширину окна: '))
            window = Window(height, width)
        except (ValueError, OutOfRangeException):
            print('Ошибка! Введите число от 280 до 2400')
            continue
        else:
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
    for key, value in output.items():
        print(f'{key}: {value}')

def get_in_file():
    with open('C:/test/test_file.txt', 'w', encoding='utf-8') as file:
        for key, value in output.items():
            file.write(f'{key}: {value}\n')

if __name__ == '__main__':
    main()
