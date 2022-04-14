# Suma de una lista
# Declarar lista vacía
lista = []
# Input para que el usuario introduzca los elementos y longitud de la lista
numElementos = int(input("Introduce el número de elementos en el arreglo: "))
# If else para limitar un máximo de 1000 elementos en la lista
if numElementos <= 1000:
    for i in range(0, numElementos):
        elementos=int(input("Introduce los elementos del arreglo: "))
        lista.append(elementos)
    print(lista)
    print("La suma de los elementos de la lusta es: ",sum(lista))
else:
    print("Introduce un número menor a 1000.")