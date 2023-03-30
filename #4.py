#
#  Reto #4
#  ÁREA DE UN POLÍGONO
#  Fecha publicación enunciado: 24/01/22
#  Fecha publicación resolución: 31/01/22
#  Dificultad: FÁCIL
# 
#  Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#  - La función recibirá por parámetro sólo UN polígono a la vez.
#  - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  - Imprime el cálculo del área de un polígono de cada tipo.

def area(num : int):
    area_1 : int = 4
    area_2 : int = 22
    
    if num == 1:
        result = area_1**2  
        print(result)

    if num == 2:
        result = area_1 * area_2 
        print(result)

    if num == 3:
        result = (area_1 * area_2)/2
        print(result)
    
    if num > 3 or num < 1:
        print('That number is not in the range')


def main():
    enunc = '1) cuadrado, 2) rectangulo, 3)triangulo'
    question = int(input(enunc + '\n>> '))
    area(question)


if __name__ == "__main__":
    main()

# Finish 30/3/23
