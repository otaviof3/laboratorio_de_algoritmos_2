def reverse_txt(index, reversed_file, lines):
    print(index)
    if index >= 0:
        reversed_file.write(lines[index])
        reverse_txt(index - 1, reversed_file, lines)
def reverse_file():
    my_file = open("lyrics.txt", "r")
    reversed_file = open("reverse_lyrics.txt", "w")
    lines = my_file.readlines()
    reverse_txt(len(lines) - 1, reversed_file, lines)
    my_file.close()
    reversed_file.close()
def main():
    reverse_file()
main()
