def control_f():
    my_file = open("words.txt", "r")
    words = my_file.readlines()
    line = 1
    result = input("Word to find: ")
    for word in words:
        if word.find(result) != -1:
            print(f"Word {result} found in line > {line}")
            line += 1
        else:
            line += 1
    my_file.close()
def main():
    control_f()
main()
