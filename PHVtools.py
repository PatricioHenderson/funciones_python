
import random
import statistics
def imprimir_nombre(nombre, apellido):
    print("Nombre: {} Apellido {}" .format(nombre,apellido))
    #print("Nombre : {} \nApellido {}" )
    # En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    # print(.....)


def promedio(numeros):
    if len(numeros) == 0:
        print("No hay numeros en la lista")
    else:
        #Realizo el calculo de dos formas para corroborar que llego al mismo resultado
        sumatoria_numeros = sum(numeros) 
        cantidad_numeros = len(numeros)
        promedio_2 = sumatoria_numeros / cantidad_numeros
        promedio = statistics.mean(numeros)
        return(promedio)
    #return  promedio 
    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
    # Cuando termine de implementar está función borrar "pass"

def ordenar(numeros):
    if len(numeros) == 0: 
        print("No hay numeros en la lista")
    else:        
        lista_orden = sorted(numeros, reverse=True)
        #Ordenamos de mayor a menor para ver si funciona o solo imprime la misma lista por defecto
        return  (lista_orden)
def lista_aleatoria(inicio, fin, cantidad):
    lista = []
    while len(lista) < cantidad:
         numero = random.randrange(inicio, fin+1)
         lista.append(numero)
    return(lista)

def contar(lista):
    buscado = int(input("Introducir número a buscar repetición: "))
    repetido = lista.count(buscado)
    return(repetido)