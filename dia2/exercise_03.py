def add(matriz):
    result = 0
    for line in range(len(matriz)):
        higher = matriz[line][0]
        for column in range (len(matriz[line])):
            if matriz[line][column] > higher:
                higher = matriz[line][column]
        result = result + higher
    return result
def main():
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    result = add(matriz)
    print("Result:",result)
main()
