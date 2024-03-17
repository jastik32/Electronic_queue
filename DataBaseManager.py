dict_current_data_base = {"1": "База данных", "2": "База данных по дате"}


def show_data_base_info():
    print("[1]Показать базу данных\n[2]Показать базу данных по дате")
    choise = input("Укажите выбор: ")

    if is_valid_data_base(choise):
        return decryption_current_data_base(choise)  # сделать защиту от неверного ввода +

    print("Такого варианта нет")


def decryption_current_data_base(numbers: str):
    return dict_current_data_base[numbers]


def is_valid_data_base(current):
    return current in dict_current_data_base.keys()


def show_current_data_base(choise: str):
    if choise == "1":
        show_data_base()
    elif choise == "2":
        data = input("Введите дату в формате day-mouth-year: ")


def get_data_base_range(*date_birth):
    start_range = ""
    end_range = ""
    start_index = 0
    end_index = 0
    if len(date_birth) == 1:
        start_range = date_birth[0]
        end_range = date_birth[0]
    elif len(date_birth) == 2:
        start_range = date_birth[0]
        end_range = date_birth[1]
    else:
        raise Exception("ф-ция принимает 1 или 2 аргумента, долбаеб")

    is_start_index_find = False

    for i in range(len(data_base)):

        data = data_base[i].split(";")[-1].replace("\n", "")

        if data == start_range and not is_start_index_find:
            start_index = i
            is_start_index_find = True

        if data == end_range:
            end_index = i - 1

    return start_index, end_index


def get_patients_counter():
    counter_patients = 0
    while get_data_from_data_base():
        counter_patients += 1
    return counter_patients


def get_data_from_data_base():
    with open(Data_Base_Name, "r", encoding="cp1251") as file:
        return file.readlines()


def get_border(char_sep: str, len_line: int):
    border = f"|{char_sep * (len_line - 2)}|"
    return border


def show_data_base(db_arg=[]):
    if len(db_arg) == 0:
        data_base_local = data_base.copy()
    else:
        data_base_local = db_arg.copy()

    heder = get_processing_line(data_base_local[0])
    len_border = len(heder)
    border_heder = get_border("=", len_border)
    border_line = get_border("-", len_border)
    print(border_heder)
    print(heder)
    print(border_heder)

    counter = 0
    count_line_before_border = 3
    for i in range(1, len(data_base)):
        counter += 1
        line = get_processing_line(data_base[i])

        print(line)
        # print(counter)
        if counter == count_line_before_border:
            counter = 0
            print(border_line)


def show_sorted_data_base(data_base: "Data_Base_Name"):
    # if data_base[5] ==
    pass


def get_processing_line(row_line: str):
    row_line = row_line.replace("\n", "").split(";")
    line = f"|{row_line[0]:^37}|{row_line[1]:^9}|{row_line[2]:^19}|{row_line[3]:^29}|{row_line[4]:^20}|"
    return line


def main():
     show_data_base()
     show_data_base_info()
     show_current_data_base(choise=str, data_=Data_Base_Name)
    # get_patients_counter()
     a, b = get_data_base_range("19.12.2023", "21.12.2023")
    print(a, b)


Data_Base_Name = "data_base.csv"
data_base = get_data_from_data_base()

if __name__ == "__main__":
    main()
