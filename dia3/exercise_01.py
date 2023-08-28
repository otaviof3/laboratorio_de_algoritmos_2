import random
def generate(bingo,numbers):
    repeats = []
    for line in range(5):
        bingo.append([])
        while len(bingo[line]) < 5:
            number = random.randint(0,99)
            if number not in numbers:
                bingo[line].append(number)
                numbers.append(number)
            else:
                repeats.append(number)
    for bingo_line in bingo:
        print(bingo_line)
    print(repeats)
def main():
    bingo = []
    numbers = []
    generate(bingo,numbers)
main()