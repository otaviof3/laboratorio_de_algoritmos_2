def add(matriz1,matriz2):
    matriz_added = []
    for line in range(len(matriz1)):
        matriz_added.append([])
        for column in range (len(matriz1[line])):
            plus = matriz1[line][column] + matriz2[line][column]
            matriz_added[line].append(plus)
    return matriz_added
def main():
    matriz1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    matriz2 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    matriz_added = add(matriz1,matriz2)
    print("Final matriz:", matriz_added)
main()