import datetime
import os
import random

beauty_data_base_name = "beauty_data_base.txt"
data_base_name = "data_base.csv"

dict_doctors_code = {"1": "Окулист", "2": "Дантист", "3": "Венеролог", "4": "Гастроэнтеролог"}


def get_clear_console():
    return os.system('cls')


def get_current_data():
    current_data = datetime.datetime.now()
    current_data = f"{current_data.day}-{current_data.month}-{current_data.year}"
    return current_data


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_waiting_time():
    waiting_time = random.randint(1, 24)
    print(f"Ожидайте! Примерное время ожидания ответа: {waiting_time} часа(ов)")


def get_heder():
    return "ФИО;Пол;Дата рождения;Номер карты;Врач;Дата"


def show_instruction_to_reception_to_doctor():
    print(
        """Добро пожаловать в нашу больницу! Пожалуйста, укажите ваше ФИО, номер банк. карты, дату рождения, пол и укажите врача.""")


def is_new_data_base(file_name: str):
    try:
        file_size = os.path.getsize(file_name)
        return file_size == 0
    except:
        return True


def add_data_to_db(data: dict):
    line = ""
    sep = ";"
    if is_new_data_base(data_base_name):
        heder = get_heder()
        line = f"{heder}\n"

    line += f"{data['фио']}{sep}{data['пол']}{sep}{data['дата рождения']}{sep}{data['номер карты']}{sep}{data['выбор врача']}{sep}{get_current_data()}\n"
    with open(data_base_name, "a", encoding="cp1251") as file:
        file.write(line)


def get_correct_fio(user_name: str):
    for elements in user_name:
        for letter in elements:
            pass


def is_valids_fio(user_name: str):
    list_user_name = user_name.split()

    is_all_correct = True

    if user_name != "":

        for element in list_user_name:

            if not element.isalpha():
                is_all_correct = False
                break

        return is_all_correct


def get_user_fio():
    while True:
        user_name = input("Введите фио: ")
        user_name = user_name.title()

        if is_valids_fio(user_name):
            return user_name

        print("Это не фио!")


def get_selection_doctor():
    counter_users_to_individual_doctor = 0
    while True:
        print(f"{'=' * 120}")
        print("Выберите врача")
        print(f"{'=' * 120}")
        print("1-Окулист, 2-Дантист, 3-Венеролог, 4-Гастроэнтеролог")
        doctor_number = input("-> ")

        if is_valids_doctor(doctor_number):
            return decryption_doctors_number(doctor_number)

        print("Такого врача нет!")


def decryption_doctors_number(doctor_number: str):
    return dict_doctors_code[doctor_number]


def is_valids_doctor(doctor):
    return doctor in dict_doctors_code.keys()


def is_valids_date_of_birth(date_of_birth: str):
    try:
        datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        return True
    except:
        return False


def get_date_of_birth():
    while True:
        date_of_birth = input("Введите дату рождения(год-месяц-день): ")
        date_of_birth = processing_user_date_of_birth(date_of_birth)

        if is_valids_date_of_birth(date_of_birth):
            return date_of_birth
        else:
            print("Вы ввели некорректную дату рождения!")


def processing_user_date_of_birth(date_of_birth: str):
    if date_of_birth.count("-") == 2:
        return date_of_birth

    for char in (":", ";", ".", ",", "/", " "):
        if char in date_of_birth:
            date_of_birth = date_of_birth.replace(char, "-")

    return date_of_birth


def get_user_bank_card_number():
    while True:
        user_card_number = input("Введите номер карты: ")

        if is_valids_card_number(user_card_number):
            return user_card_number

        print("Некорректный формат карты!")


def is_valids_card_number(user_card_number: str):
    result_all = False
    try:
        result_summ_even = is_summ_card_number_is_even(user_card_number)
        result_count_space_is_three = user_card_number.count(" ") == 3
        result_all_char_is_int = user_card_number.replace(" ", "").isdigit()
        result_count_numbers_is_sixteen = len(user_card_number.replace(" ", "")) == 16
        # without_spaces = ' '.join(user_card_number[i:i + 4] for i in range(0, len(user_card_number), 4))
        result_all = (
                result_count_space_is_three and result_summ_even and result_all_char_is_int and result_count_numbers_is_sixteen)


    except:
        pass

    return result_all


def is_summ_card_number_is_even(user_card_number: str):
    global card_number
    card_number = user_card_number.replace(" ", "")

    summ_ = 0

    for element in card_number:
        summ_ += int(element)

    return summ_ % 2 == 0


def get_user_data():
    fio = get_user_fio()
    sex = get_user_sex()
    date = get_date_of_birth()
    card = get_user_bank_card_number()
    doctor = get_selection_doctor()
    dict_data = {"фио": fio, "пол": sex, "дата рождения": date, "номер карты": card, "выбор врача": doctor}

    return dict_data


def get_user_sex():
    while True:
        user_sex = input("Введите пол(в формате М/Ж): ")
        user_sex = user_sex.upper()

        if is_valids_sex(user_sex):
            return user_sex

        print("Такого варианта выбора пола нет!")


def is_valids_sex(user_sex: str):
    user_sex = user_sex.lower()
    return user_sex in ('м', 'ж')


def show_goodbye_message():
    print("Спасибо, что выбрали нашу клинику! Будьте здоровы!")


def main():
    heder = get_heder()
    len_heder = len(heder)
    while True:
        print(f"{'=' * 120}")
        show_instruction_to_reception_to_doctor()
        print(f"{'=' * 120} \n")
        user_data = get_user_data()
        print(f"{'=' * 120} ")
        show_goodbye_message()
        show_waiting_time()
        print(f"{'=' * 120}")
        # print(f"\n")
        # print(f"{'=' * 120}")
        add_data_to_db(user_data)
        print(f"\n")
        # get_clear_console()


# адекватный вывод доделать +
# попробовать сломать программу не верным польз. вводом +
# написать доп. скрипт(новый файл), который будет считывать базу данных и красиво выводить ее в консоль +-
# данные, которые должны быть выведены в консоль(user_data, кол-во посетителей того или иного доктора и общее кол-во посетителей)
# написать еще один скрипт, который будет конвертировать txt базу данных в csv базу данных +-
# csv файл должен корректно открываться в excel
# сделать все выводы в консоль более красивыми +
if __name__ == "__main__":
    main()
