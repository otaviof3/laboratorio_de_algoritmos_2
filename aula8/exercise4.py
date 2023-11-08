def validate_ip(line):
    numbers = line.split(".")
    if len(numbers) != 4:
        return False
    first_number = True
    for number in numbers:
        print(number)
        if first_number == True:
            try:
                num = int(number)
                print(num)
                if num <= 0 or num > 255:
                    return False
                first_number = False
            except ValueError:
                return False
        else:
            try:
                num = int(number)
                if num < 0 or num > 255:
                    return False
            except ValueError:
                return False
    return True
def separate_ip():
    my_file = open("ip_address.txt", "r")
    invalid = open("invalid_address.txt", "w")
    valid = open("valid_address.txt", "w")
    lines = my_file.read().splitlines()
    for line in lines:
        validation = validate_ip(line)
        if validation == True:
            valid.write(f"{line}\n")
        else:
            invalid.write(f"{line}\n")
def main():
    separate_ip()
main()