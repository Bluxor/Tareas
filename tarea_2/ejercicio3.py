
def palindrome_checker (frase:str) -> str:
    
    list(frase) #hago cada palabra un string
    #Como hago todo esto debajo en una sola linea?
    frase = frase.strip() #quito espacios de las orillas
    frase = frase.replace(" ","") #borro espacios
    frase = frase.lower() #todo minusculas
 
    alreves = frase[::-1]
    if(frase == alreves):
        print("True")
    else:
        print("False")

palindrome_checker("Anita lava la tina")
