def bank():
    cash = []
    withdraw = int(input("Withdraw amount: "))
    while withdraw % 10 != 0:
        withdraw = int(input("Withdraw valid amount: "))
    while withdraw > 0:
        if withdraw >= 100:
            cash.append(100)
            withdraw -= 100
        elif withdraw >= 50 and withdraw < 100:
            cash.append(50)
            withdraw -= 50
        elif withdraw >= 20 and withdraw < 50:
            cash.append(20)
            withdraw -= 20
        elif withdraw >= 10 and withdraw < 20:
            cash.append(10)
            withdraw -= 10
    return cash
def delivery(cash):
    count100 = 0
    count50 = 0
    count20 = 0
    count10 = 0
    for i in cash:
        if i == 100:
            count100 += 1
        elif i == 50:
            count50 += 1
        elif i == 20:
            count20 += 1
        else:
            count10 += 1
    if count100 == 1:
        print(f"{count100} R$100,00 banknote.")
    elif count100 > 0:
        print(f"{count100} R$100,00 banknotes.")
    if count50 == 1:
        print(f"{count50} R$50,00 banknote.")
    elif count50 > 0:
        print(f"{count50} R$50,00 banknotes.")
    if count20 == 1:
        print(f"{count20} R$20,00 banknote.")
    elif count20 > 0:
        print(f"{count20} R$20,00 banknotes.")
    if count10 == 1:
        print(f"{count10} R$10,00 banknote.")
    elif count10> 0:
        print(f"{count10} R$10,00 banknotes.")
def main():
    cash = bank()
    delivery(cash)
main()