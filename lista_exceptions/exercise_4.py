def create_list_and_index():
    class_list = ["Jardel","Otávio","Michel","Cristian","Vitor","Gabriel Costa","Nicolas","José","Lucas Descovi","Lucas Feldmann","Pedro","Antonio","Andrey","Gabriel Roggia","Gabriel Tessele","Matheus","Arthur"]
    while True:
        index = input("Type the index of wanted element: ")
        try:
            index = int(index)
            break
        except ValueError:
            print("Invalid value informed.")
        except BaseException:
            print("Unexpected error.")
    return class_list,index
def find_element(class_list,index):
    try:
        print(f"Element: {class_list[index]}")
    except IndexError:
        print("Invalid index informed.")
def main():
    class_list,index = create_list_and_index()
    find_element(class_list,index)
main()