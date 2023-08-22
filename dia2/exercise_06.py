def transpose(matriz):
    transposed_matriz = []
    for line in range(len(matriz)):
        transposed_matriz.append([])
        for column in range (len(matriz[line])):
            transposed_matriz[line].append(matriz[column][line])
    if matriz == transposed_matriz:
        print("Symmetrical.")
    else:
        print("Not symmetrical.")
def main():
    matriz = [
        [1,2,3],
        [2,5,6],
        [3,6,9]
    ]
    transpose(matriz)
main()