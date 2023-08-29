def sum_matriz(matriz):
    added = 0
    for line in range(len(matriz)):
        for column in range (len(matriz[line])):
            if column < line:
                added = added + matriz[line][column]
    print("The sum is",added)
def main():
    matriz = [
        [2,0,99,5,5],
        [1,2,100,50,20],
        [1,1,2,10,30],
        [1,1,1,2,80],
        [1,1,1,1,2]
    ]
    sum_matriz(matriz)
main()