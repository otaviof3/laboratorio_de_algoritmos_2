def main():  
    my_list = [1,2,3,4,5,6]
    reversed_list = invert_list(my_list)
    print(reversed_list)
def invert_list(my_list):
    reversed_list = []
    index = len(my_list) - 1
    while (index >= 0):
        print(f"Index >",index)
        reversed_list.append(my_list[index])
        index -= 1
    return reversed_list
main()
