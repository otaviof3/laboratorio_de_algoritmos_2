def first(message):
    while True:
        first_side = input(message)
        try:
            first_side = float(first_side)
            highest_value = first_side
            break
        except ValueError:
            print("Informe um valor válido.")
        except BaseException:
            print("Erro inesperado.")
    return first_side, highest_value
def other_sides(message,highest_value):
    while True:
        side = input(message)
        try:
            side = float(side)
            if highest_value < side:
                highest_value = side
            break
        except ValueError:
            print("Informe um valor válido.")
        except BaseException:
            print("Erro inesperado.")
    return side, highest_value
def validate(highest_value,side_one,side_two):
    try:
        if side_one + side_two < highest_value:
            raise ValueError
        else:
            return True
    except ValueError:
        print("O triângulo informado é inválido.")
        return False
def triangle_type(first_side,second_side,third_side,highest_value):
    if highest_value == first_side:
        check = validate(highest_value,second_side,third_side)
    elif highest_value == second_side:
        check = validate(highest_value,first_side,third_side)
    elif highest_value == third_side:
        check = validate(highest_value,first_side,second_side)
    if check == True:
        if first_side == second_side == third_side:
            print("O triângulo é equilátero.")
        elif first_side == second_side or first_side == third_side or second_side == third_side:
            print("O triângulo é isósceles")
        else:
            print("O triângulo é escaleno.")
def values():
    first_side, highest_value = first("Primeiro lado do triângulo: ")
    second_side, highest_value = other_sides("Segundo lado do triângulo: ",highest_value)
    third_side, highest_value = other_sides("Terceiro lado do triângulo: ",highest_value)
    return first_side,second_side,third_side,highest_value
def main():
    first_side,second_side,third_side,highest_value = values()
    triangle_type(first_side,second_side,third_side,highest_value)
main()