def avg(matriz):
    average = 0
    for line in range(len(matriz)):
        line_average = 0
        for column in range (len(matriz[line])):
            line_average = line_average + matriz[line][column]
            average = average + matriz[line][column]
        print(f"Line {(matriz[line])} average:",line_average / 3)
    return average
def main():
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    average = avg(matriz)
    print("Total average:",average / 9)
main()
