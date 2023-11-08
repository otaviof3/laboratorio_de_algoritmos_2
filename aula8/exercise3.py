def copy_file():
    input_filename = input("File to open (include file extension like .txt): ")
    try:
        my_file = open(input_filename, "r")
        file_lines = my_file.read()
        copy_name = "copia_" + input_filename
        copied_file = open(copy_name, "w")
        copied_file.write(file_lines)
        my_file.close()
        copied_file.close()
    except FileNotFoundError:
        print("File not found.")
def main():
    copy_file()
main()
