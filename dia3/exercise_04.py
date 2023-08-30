def multiply_line(matriz):
    higher_line = 1
    for line in range(0,len(matriz)):
        line_product = 1
        for column in range(0,len(matriz[line])):
            line_product = line_product * matriz[line][column]
        if line == 0:
            higher_line = line_product
        elif line_product > higher_line:
            higher_line = line_product
    return higher_line

def multiply_column(matriz):
    higher_column = 1
    for line in range(0,len(matriz)):
        column_product = 1
        for column in range(0,len(matriz[line])):
            column_product = column_product * matriz[column][line]
        if line == 0:
            higher_column = column_product
        elif column_product > higher_column:
            higher_column = column_product
    return higher_column

def multiply_diagonal(matriz):
    diagonal = 1
    for line in range(0,len(matriz)):
        for column in range(0,len(matriz[line])):
            if line == column:
                diagonal = diagonal * matriz[line][column]
    return diagonal

def highest(higher_line,higher_column,diagonal):
    if higher_line >= higher_column:
        if higher_line >= diagonal:
            print(higher_line)
        else:
            print(diagonal)
    elif higher_column >= diagonal:
        print(higher_column)
    else:
        print(diagonal)

def main():
    matriz = [
        [2,1,1,1,1],
        [1,2,1,1,1],
        [1,1,2,1,1],
        [1,1,1,2,1],
        [1,1,1,1,2]
    ]
    higher_line = multiply_line(matriz)
    higher_column = multiply_column(matriz)
    diagonal = multiply_diagonal(matriz)
    highest(higher_line,higher_column,diagonal)

main()