from main import data_base_name


def selection_actions():
    print("[1] Показать базу данных"
          "[2] Выйти ")
    mod = input("Выберите действие ->")
    if mod == "1":
        ...


def get_data_from_data_base():
    with open(data_base_name, "r", encoding="cp1251") as file:
        data = file.readlines()

    return data


def get_redact_data_from_show():
    data = get_data_from_data_base()
    heder = get_heder_from_table(data[0])
    border_up = "=" * len(heder)
    border_down = "-" * len(heder)

    list_lines = [border_up, heder, border_down]

    for i in range(1, len(data)):
        split_line = data[i].replace("\n", "").split(";")
        line = f"|{split_line[0]:^35}|{split_line[1]:^7}|{split_line[2]:^17}|{split_line[3]:^27}|{split_line[4]:^18}|"
        list_lines.append(line)

    # list_lines.append(border_down)
    return list_lines
    return "\n".join(list_lines)


def get_heder_from_table(heder: str):
    list_heder = heder.replace("\n", "").split(";")
    heder = f"|{list_heder[0]:^35}|{list_heder[1]:^7}|{list_heder[2]:^17}|{list_heder[3]:^27}|{list_heder[4]:^18}|"
    return heder


def show_data_from_data_base():
    list_lines = get_redact_data_from_show()
    border = "=" * len(list_lines[0])
    for i in range(len(list_lines)):
        ...
    ...

    print(get_redact_data_from_show())


def main():
    show_data_from_data_base()


if __name__ == "__main__":
    main()
