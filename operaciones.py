# =====================================
# Nombre: operaciones.py
# Autor: Alvin  Gil
# Fecha: 20/03/2026
# Descripción: Clase con operaciones matemáticas
# =====================================
import math
from datetime import datetime

class OperacionesMatematicas:
    # Suma
    def suma(self, a, b):
        return a + b

    # Resta
    def resta(self, a, b):
        return a - b 

    # Multiplicación
    def multiplicacion(self, a, b):
        return a * b

    # División
    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "No se puede dividir entre 0"
            

    # Número primo
    def num_primos(self, n):
        if n <= 1:
            return f"{n} no es primo"
        if n == 2:
            return f"{n} es un número primo"
        for i in range(2, n):
            if n % i == 0:
                return f"{n} no es primo"
            
        return f"{n} es un número primo"
    
   # Factorial paso a paso
    def factorial(self, n):
        if n < 0:
            return "No existe factorial de números negativos"
        else:
            resultado = 1
            print(f"Calculando {n}!:")
            for i in range(1, n + 1):
                resultado *= i
            return resultado

    # potencias
    def potencia(self,base,exponente):
        return base ** exponente 
    
    def numero_impar(self,n):
        return n % 2 != 0

    def numero_par(self,n):
        return n % 2 == 0
    
    def area_triangulo(self,base,altura):
    	return (base * altura) / 2
    
    def area_cuadrado(self,lado):
        return lado ** 2

    def radianes_grados(self):
        pi = 3.141592653589793
        radianes = pi 
        return radianes * 180 / pi

    def grados_radianes(self,grados):
    	pi = 3.141592653589793
    	return grados * pi / 180

    # Función para convertir Fahrenheit a Celsius

    def fahrenheit_to_celsius(self,f):
    	return (f-32) * 5 / 9

    # Funcion para convertir Celcius a Fahrenheit

    def celsius_to_fahrenheit(self,c):
        return (c * 9 / 5) + 32

    # Funcion para convertir Celcius a Fahrenheit

    def kelvin_to_celsius(self,k):
    	return k - 273.15
    # Funcion para convertir Celcius a Fahrenheit

    def kelvin_to_fahrenheit(self, k):
    	return (k - 273.15) * 9 / 5 + 32

    # Funcion para convertir Celcius a kelvin

    def celsius_to_kelvin(self,c):
    	return c + 273.15

    #  Funcion para convertir fahrenheit a kelvin

    def fahrenheit_to_kelvin(self,f):
    	return (f-32) * 5 / 9 + 273.15

    # Funcion para imprimir la serie de fibonacci
    def fibonacci(self,n):
        a,b = 0,1 
        for _ in range(n):
            print(a, end="")
            a,b = b, a + b 
    
    # metros a centimetros
    def metros_to_centimetros(self,metros):
        return metros * 100
    
    # cm a metros
    def centimetros_to_metros(self,cm):
        return cm / 100

    # km a metros
    def km_to_metros(self,km):
    	return km * 1000

    # metros a km 
    def metros_to_km(self,metros):
        return round(metros / 1000)

    # calcular imc 
    def imc(self,peso, altura):
        peso = float(peso)
        altura = float(altura)
        imc_valor = peso / (altura ** 2)
        if imc_valor < 18.5:
            categoria = "bajo peso"
        elif 18.5 <= imc_valor < 25:
            categoria = "peso normal"
        elif 25 <= imc_valor < 30:
            categoria = "sobrepeso"
        else:
            categoria = "obesidad"
        return f"IMC: {imc_valor:.2f} - {categoria}"
    
    # logaritmo natural
    def logaritmo_natural(self,n):
        return math.log(n)
    
    # logaritmo con base 10 
    def logaritmo_base10(self,n):
        return math.log10(n)

    # logaritmo con base 
    def logaritmo_base(self,n,base):
        return math.log(n,base)

    # funcion para sacar seno 
    def seno(self,n):
        radianes = math.radians(n)
        return math.sin(radianes)
    
    # funcion para sacar residuo
    def residuo(self,a,b):
        return a % b 

    # precio de galon de gasolina
    def pricefuelgallon(self,lt):
        return round(lt * 3.785, 2)

    # hora actual
    def hora_actual(self):
        hora = datetime.now()
        hora_formateada = hora.strftime("%H:%M:%S")
        return hora_formateada




    	
# testear
# numeros = OperacionesMatematicas()
# resultado = numeros.hora_actual()
# print(resultado)











			

	 	




