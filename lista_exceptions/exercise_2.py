def evaluation():
    while True:
        review = input("Type a number from 0 to 10 to give a review of the product: ")
        try:
            review = int(review)
            assert review >= 0 and review <= 10
            break
        except ValueError:
            print("The informed number is invalid.")
        except AssertionError:
            print("The informed number is out of permitted range.")
        except BaseException:
            print("Unexpected error.")
    print(f"Evaluation: {review}")
def main():
    evaluation()
main()