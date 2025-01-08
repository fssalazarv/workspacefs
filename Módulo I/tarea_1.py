#ejercicio 1

print("hola mundo")

#ejercicio 2

nombre=input("ingrese su nombre: ") # input

print("Hola", nombre) # output

#ejercicio 3

edad=int(input("ingrese su edad: ")) # input

if edad>=18:
   print("Es mayor de edad")
else:
    print("No es mayor de edad")

#ejercicio 4    

numero = int(input("Ingrese un número entero positivo: "))

# Validar que el número sea positivo
if numero > 0:
        # Calcular la suma de 1 hasta el número ingresado
        suma = (numero * (numero + 1)) / 2
        
        print(f"La suma de los números desde 1 hasta {numero} es {suma}.")
else:
        print("Por favor, ingrese un número entero positivo.")

#ejercicio 5

numero = int(input("Ingrese un número entero: "))  # Convertir a entero

if numero % 2 == 0:  # Verificar si el número es divisible entre 2
    
    print("El número", numero,  "es par.")
else:
    print(f"El número {numero} es impar.")