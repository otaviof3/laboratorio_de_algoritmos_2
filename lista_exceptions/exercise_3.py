class NegativeNumberError(Exception):
    pass
def number():
    while True:
        num = input("Type a number: ")
        try:
            num = float(num)
            break
        except ValueError:
            print("Invalid number informed.")
        except BaseException:
            print("Unexpected error.")
    return num
def calculate_square_root(num):
    try:
        if num < 0:
            raise NegativeNumberError
        square_root = num ** (1/2)
        return square_root
    except NegativeNumberError:
        print("The square root of a negative number isn't a real number.")
        return "End of program."
    except BaseException:
        print("Unexpected error.")
        return "End of program."
def main():
    num = number()
    print(calculate_square_root(num))
main()