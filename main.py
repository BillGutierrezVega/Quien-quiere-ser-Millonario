import random
import time

#Constantes de colores 
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0;m'
NEGRITA = '\033[1m'
B_BLUE = '\033[1;34m'

#Iniciamos la variable en True y Variable para saber cuantos intentos vamos
iniciar_trivia = True  
intentos = 1  

#funcion de validacion para saber si es un número lo que ingrese el usuario
def sies_numero(cadena):
  try:
    int(cadena)
    return True
  except ValueError:
    return False

print (NEGRITA+"          Bienvenido a ¿Quién quiere ser Programador(Python)?"+ '\033[0m')
print(GREEN+"Cualquier parecido con ¿Quién quiere ser Millonario? es pura coinsidencia\n"+RESET)

print("Comenzamos en:")
#Un temporizador antes de empezar
for tiempo_inicio in range(5,0,-1):
  print(tiempo_inicio)
  time.sleep(1) 

print("Nuestro objetivo es tratar de obtener su IQ mediante estas preguntas y las veces que las respondas")
#Datos personales
print("\nDatos personales")
nombre = input("=>Ingrese su nombre: ")
edad = input("=>Ingrese su edad: ")
if sies_numero(edad):
  time.sleep(1)
else:
  edad = input("=>Ingrese una edad válida: ")  
  
#Lista para saber el promedio 
promedio = []  

#Un condicional para saber cuantos intentos vamos
while iniciar_trivia == True:
  print("Su número de intentos es: ", intentos)
  print ("\nAqui pondremos a prueba tus conocimientos\n")
  
  puntaje = 0
  print()
  print("Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa que creas sea la correcta y presionando 'Enter' para enviar tu respuesta:")
  print("Comienzas con"+RED ,puntaje, RESET+"puntos\n")
  
  #Preguna 1
  print (B_BLUE+"1.- ¿Qué es una tupla?"+RESET)
  print ("a) "+BLACK+"Una lista ordenada"+RESET)
  print ("b) "+BLACK+"Una lista desordenada"+RESET)
  print ("c) "+BLACK+"Una lista mutable"+RESET)
  print ("d) "+BLACK+"Una lista inmutable"+RESET)
  #Limitando las respuestas a (a,b,c,d)
  respuesta_1 = input("\nTu respuesta: ")
  print()
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  #Verificando si la respuesta es la correcta
  if respuesta_1 == "a":
    print("Incorrecto!", nombre, "Una tupla es una lista inmutable")
  #restamos puntos de manera aleatoria entre 1 y 10
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "b":
    print("Incorrecto!", nombre, "Una tupla es una lista inmutable")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "c":
    print("Incorrecto!", nombre, "Una tupla es una lista inmutable")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  else:
    print("Muy bien", nombre, "!")
    puntaje += 10
  
  if puntaje <= 15:
    print("Su puntaje actual es de"+RED , puntaje, RESET)
  elif puntaje > 15 and puntaje <= 30:
    print("Su puntaje actual es de"+YELLOW , puntaje,RESET)
  else:
    print("Su puntaje actual es de"+GREEN, puntaje, RESET)
  print()

  #Pregunta 2
  print (B_BLUE+"2.- Se puede decir de Python que: "+RESET)
  print ("a) "+BLACK+"Es débilmente tipado"+RESET)
  print ("b) "+BLACK+"Es fuertemente tipado"+RESET)
  print ("c) "+BLACK+"Es dinámicamente tipado"+RESET)
  print ("d) "+BLACK+"b y c son correctas"+RESET)
  #Limitando las respuestas a (a,b,c,d)
  respuesta_1 = input("\nTu respuesta: ")
  print()
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  #Verificando si la respuesta es la correcta
  if respuesta_1 == "a":
    print("Incorrecto!", nombre, "Python es un lenguaje de programación fuertemente tipado y dinamicamente tipado")
  #restamos puntos de manera aleatoria entre 1 y 5
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "b":
    print("Incorrecto!", nombre, "Python es un lenguaje de programación fuertemente tipado y dinamicamente tipado")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "c":
    print("Incorrecto!", nombre, "Python es un lenguaje de programación fuertemente tipado y dinamicamente tipado")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  else:
    print("Muy bien", nombre, "!")
    puntaje += 10
  if puntaje <= 15:
    print("Su puntaje actual es de"+RED , puntaje, RESET)
  elif puntaje > 15 and puntaje <= 30:
    print("Su puntaje actual es de"+YELLOW , puntaje,RESET)
  else:
    print("Su puntaje actual es de"+B_BLUE, puntaje, RESET)

  #Pregunta 3
  print (B_BLUE+"3.- Para que se usa 'def' "+RESET)
  print ("a) "+BLACK+"Parte de la sintaxis para crear una función"+RESET)
  print ("b) "+BLACK+"Parte de la sintaxis para crear una tupla"+RESET)
  print ("c) "+BLACK+"Parte de la sintaxis para crear una variable"+RESET)
  print ("d) "+BLACK+"Parte de la sintaxis para crear una lista"+RESET)
  #Limitando las respuestas a (a,b,c,d)
  respuesta_1 = input("\nTu respuesta: ")
  print()
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  #Verificando si la respuesta es la correcta
  if respuesta_1 == "d":
    print("Incorrecto!", nombre, "En Python se usa la palabra reservada 'def' para definir una función")
  #restamos puntos de manera aleatoria entre 1 y 5
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "b":
    print("Incorrecto!", nombre, "En Python se usa la palabra reservada 'def' para definir una función")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "c":
    print("Incorrecto!", nombre, "En Python se usa la palabra reservada 'def' para definir una función")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  else:
    print("Muy bien", nombre, "!")
    puntaje += 10
  if puntaje <= 15:
    print("Su puntaje actual es de"+RED , puntaje, RESET)
  elif puntaje > 15 and puntaje <= 30:
    print("Su puntaje actual es de"+YELLOW , puntaje,RESET)
  else:
    print("Su puntaje actual es de"+GREEN, puntaje, RESET)

  #Pregunta 4
  print (B_BLUE+"4.- Como se escriben los comentarios en Python"+RESET)
  print ("a) "+BLACK+"En Python no se puede escribir comentarios"+RESET)
  print ("b) "+BLACK+"En python se usa // para escribir comentarios"+RESET)
  print ("c) "+BLACK+"En Python se usa # para escribir comentarios"+RESET)
  print ("d) "+BLACK+"En Python se usa /* y */ para escribir comentarios"+RESET)
  #Limitando las respuestas a (a,b,c,d)
  respuesta_1 = input("\nTu respuesta: ")
  print()
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  #Verificando si la respuesta es la correcta
  if respuesta_1 == "a":
    print("Incorrecto!", nombre, "En Python se usa # para escribir comentarios")
  #restamos puntos de manera aleatoria entre 1 y 5
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "b":
    print("Incorrecto!", nombre, "En Python se usa # para escribir comentarios")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "d":
    print("Incorrecto!", nombre, "En Python se usa # para escribir comentarios")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  else:
    print("Muy bien", nombre, "!")
    puntaje += 10
  if puntaje <= 15:
    print("Su puntaje actual es de"+RED , puntaje, RESET)
  elif puntaje > 15 and puntaje <= 30:
    print("Su puntaje actual es de"+YELLOW , puntaje,RESET)
  else:
    print("Su puntaje actual es de"+B_BLUE, puntaje, RESET)

  #Pregunta 5
  print (B_BLUE+"5.- ¿Python es un lenguaje de programación de bajo nivel?"+RESET)
  print ("a) "+BLACK+"Si, Python es un lenguaje de programación de bajo nivel"+RESET)
  print ("b) "+BLACK+"No, Python es un lenguaje de programación de alto nivel"+RESET)
  print ("c) "+BLACK+"No, Python es un lenguaje de programación en código máquina"+RESET)
  print ("d) "+BLACK+"Ninguna de las anteriores"+RESET)
  #Limitando las respuestas a (a,b,c,d)
  respuesta_1 = input("\nTu respuesta: ")
  print()
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d.\nIngresa nuevamente tu respuesta: ")
  #Verificando si la respuesta es la correcta
  if respuesta_1 == "a":
    print("Incorrecto!", nombre, "Python es un lenguaje de programación de alto nivel")
  #restamos puntos de manera aleatoria entre 1 y 5
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "c":
    print("Incorrecto!", nombre, "Python es un lenguaje de programación de alto nivel")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  elif respuesta_1 == "d":
    print("Incorrecto!", nombre, "Python es un lenguaje de programación de alto nivel")
    restapuntos = random.randint(1,10)
    puntaje -= restapuntos
  else:
    print("Muy bien", nombre, "!")
    puntaje += 10
  if puntaje <= 15:
    print("\nGracias por jugar", nombre ,"espero se haya divertido su puntaje final es:"+RED , puntaje, RESET)
  elif puntaje > 15 and puntaje <= 30:
    print("\nGracias por jugar", nombre ,"espero se haya divertido su puntaje final es:"+YELLOW , puntaje,RESET)
  else:
    print("\nGracias por jugar", nombre ,"espero se haya divertido su puntaje final es:"+B_BLUE, puntaje, RESET)

  print("\n¿Desea intentarlo nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  #agregamos uno al contador de intentos
  intentos += 1
  #Añadimos a la lista del promedio
  promedio.append(puntaje)
  print()
  #Reiniciamos el puntaje
  puntaje = 0
  print()
  print("------------------------------------------")
  print()
  if repetir_trivia != "si": 
   #Los resultados
   print("Su número de intentos es: ", intentos-1)
   print("El resultado de cada uno de sus intentos es:")
   i=1
   for inten in promedio:
    print("En su intento",i,"obtuvo: ",inten,"puntos")
    i+=1
   i=0
   edad = float(edad)
   prom_fin = sum(promedio)/len(promedio)
   print("Su promedio de todos sus intentos es(edad mental): ", prom_fin)
   print("IQ = (edad mental/edad cronológica)*100")
   IQ = (prom_fin/edad)*100
   print("Finalmente su IQ(apróximado) es: ", IQ)
   print("\nNota: Si el promedio final es negativo o muy bajo el valor de su IQ es muy impreciso")
   print("\nEspero" ,nombre, "que lo hayas pasado bien, hasta pronto!")
    

   #cambiamos su valor a False para que ya no se repita
   iniciar_trivia = False  