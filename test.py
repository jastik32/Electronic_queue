def is_valids_fio(user_name:str):
    list_user_name = user_name.split()
    is_all_correct = True

    for element in list_user_name:
        if not element.isalpha():
            is_all_correct = False
            break

    return is_all_correct


def get_user_fio():

    while True:
        user_name = input("Введите фио: ")

        if is_valids_fio(user_name):

            return user_name

name = get_user_fio()
print(name)



