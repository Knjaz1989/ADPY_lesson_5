def get_info():
    print("""
        p - (people) - команда, которая запрашивает номер документа и выводит имя человека, которому он принадлежит.
        s - (shelf) - команда, которая запрашивает номер документа и выводитт номер полки, на которой он находится.
        ss - (show shelves) -  команда, показывает все полки и их содержимое.
        as - (add shelf) - команда, которая запрашивает номер новой полки и добавит ее в перечень.
        l - (list) - команда, которая выводит список всех документов.
        a - (add) - команда, которая добавляет новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
        d - (delete) - команда, которая запрашивает номер документа и удаляет его из каталога и из перечня полок.
        m - (move) - команда, которая запрашивает номер документа и целевую полку и перемещает его с текущей полки на целевую. """)

def get_name():
    num = input("Введите номер документа: ")
    for i in documents:
        if num == i["number"]:
            print("-", i['name'])
            return i['name']
    else:
        print("Такого документа нет в каталоге!")
        return

def get_shelf():
    num = input("Введите номер документа: ")
    for shelf in directories:
        if num in directories[shelf]:
            print("Документ находится на полке №", shelf)
            return shelf
    else:
        print("Такого документа нет в каталоге!")
        return

def print_doc():
    for i in documents:
        print("-", i["type"], '"' + i["number"] + '"', '"' + i['name'] + '"')

def add_doc():
    num = input("Введите номер документа: ")
    t = input("Введите тип документа: ")
    n = input("Введите имя владельца: ")
    s = input("Укажите номер полки: ")
    if s not in directories.keys():
        print("К сожалению такой полки не существует!")
    else:
        directories[s].append(num)
        documents.append({"type": t, "number": num, "name": n})
        print("Документ добавлен!")

def show_shelves():
    for i in directories:
        print (i + " = " + '; '.join(directories[i]))

def delete_doc():
    num = input("Введите номер документа, который надо удалить: ")
    for n_doc in directories:
        if num in directories[n_doc]:
            directories[n_doc].remove(num)
            for i in range(len(documents)):
                if n_doc in documents[i]['number']:
                    del documents[i]
                    break
            print("Документ удален!")
            break
    else:
        print("Такого документа нет!")

def add_shelf():
    while True:
        sh = input("Введите номер полки, которую хотите добавить: ")
        if sh == "q":
            break
        elif sh in directories:
            print("Такая полка уже существует!")
        else:
            directories[sh] = []
            print(f"Полка {sh} добавлена.")
            break

def move_doc():
    num = input("Введите номер документа: ")
    for i in directories:
        if num in directories[i]:
            shelf_first = i
            shelf_second = input("Укажите полку, в которую надо переместить: ")
            if shelf_second not in directories:
                print("Такой полки не существует!")
            elif shelf_second == shelf_first:
                print("Этот документ уже находится в требуемой полке")
            else:
                directories[shelf_second].append(num)
                directories[shelf_first].remove(num)
                print("Документ перенесен!")
            break
    else:
        print("Такого документа нет!")

dict_of_commands = {"p": get_name,
                    "s": get_shelf,
                    "l": print_doc,
                    "a": add_doc,
                    "ss": show_shelves,
                    "as": add_shelf,
                    "m": move_doc,
                    "i": get_info,
                    "d": delete_doc}
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

if __name__ == '__main__':
    while True:
        letter = input("Введите команду (q = выход, i = инфо по всем командам): ").lower()
        if letter == "q":
            print("До новых встреч!")
            break
        elif letter not in dict_of_commands:
            print("Такой команды не существует!", end=" ")
        else:
            dict_of_commands[letter]()

