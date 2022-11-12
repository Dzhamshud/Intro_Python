from func import read_data, calculate, print_data


def my_func():
    data = read_data()
    answer = calculate(data)
    print_data(answer)



if __name__ == '__main__':  # запуск модуля по вызову
    my_func()


