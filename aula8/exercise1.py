def calculate_avg():
    my_file = open("numbers.txt", "r")
    content = my_file.read()
    file_numbers = content.split(",")
    amount = 0
    sum_of_numbers = 0
    for num in file_numbers:
        amount += 1
        num = float(num)
        sum_of_numbers += num
    my_file.close()
    return sum_of_numbers / amount
def main():
    print(calculate_avg())
main()
