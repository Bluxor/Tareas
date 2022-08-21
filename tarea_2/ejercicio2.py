# Ejercicio 2

frase = input("Escribe tu frase: ")
palabras = frase.split() #hace la frase un array de palabras
dic = {} #inicializo diccionario
for i in palabras:
    if i not in dic.keys():
        #asigno el diccionario a 0 la primera vez
        dic[i]=0
    dic[i] = dic[i]+1
    # le sumo a los keys +1 cada vez que se repite el key
for key, value in dic.items():
    print(f"la palabra \"{key}\" se repite {value} veces") 
    #imprimo la frase rotando los keys y sus valores
