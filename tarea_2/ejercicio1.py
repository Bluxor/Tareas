from numpy import *

#Ejercicio 1
def fb (entero:int) -> int:

    ans = [""] #inicializo el array

    for i in range(entero):
        ans1 = [("Fizz"*(i%3<1)+(i%5<1)*"Buzz" or i)]
        ans = concatenate([ans,ans1])

    print(ans)
print(fb(16))
# duda: python no reconoce arrays? tengo que inicializarlo a fuerza?


# Ejercicio 2
def cuenta (input):
    string = input
    palabras = string.split()
    contador = {}
    for i in contador:
        contador[i] = palabras.count(i)
    for key, value in contador.items():
        print(f"la palabra \"{key}\" se repite {value} times")

print(cuenta("pepe pecas pica papas con un pico pica papas pepe pecas"))








  #for i in range(entero):
        #if (i % 5 == 0) and (i % 3 == 0):
         #   print("FizzBuzz")
        #elif i % 5 == 0:
         #   print("Buzz")
        #elif i % 3 == 0:
         #   print("Fizz")
        #else:
         #   print(i)




# 