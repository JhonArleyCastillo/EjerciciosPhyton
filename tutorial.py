##Juego Piedra Papel o Tijeras##
import random

options = ('piedra','papel','tijera') 
print ("Inicia el juego")
name = input("Escribe tu nombre" +" ")
user = input(name +" "+ 'Elije Piedra, Papel, Tijera ')
user = user.lower()
computer = random.choice(options)

if not user in options:
  print('opcion invalida')
  
print('user = >',user)
print('computer => ',computer)

if user == computer:
  print('empate !')
elif user == 'piedra':
  if computer == 'tijera':
    print('piedra gana a tijera')
    print(name +' ' +' win')
  else:
    print('papel gana a  piedra ')
    print( 'computer win ')
elif user == 'papel':
  if computer == 'piedra':
    print('papel gana a piedra')
    print(name +' '+' win')
  else:
    print('tijera gana a  papel ')
    print( 'computer win ')
elif user == 'tijera':
  if computer == 'papel':
    print('tijera gana a papel')
    print(name +' '+' win')
  else:
    print('piedra gana a tijera ')
    print( 'computer win ')

#Piedra, papel y tijeras
# Importar elección aletoria
#import random

#crear variables del juego
#options: ["Piedra, Papel, Tijera"]

#numero de turnos
#num_turnos: 5

#Iniciar el juego
#for turno in range(num_turnos):
#    print(f"turno {turno + 1}")

#Menu de seleccion:jugador
#    options_jugador = input("Piedra, Papel, Tijera").lower()

#Menu de seleccion: Bot
#    options_bot= random.choices(options)
#    print(f"El Bot elige: {options_bot}")

#Logica en el juego
#    if options_jugador in options:
#        if options_jugador == options_bot:
#           print ("Empate!")
#        elif (
#            (options_jugador == "piedra" and options_bot == "tijera")
#            or (options_jugador == "papel" and options_bot == "piedra")
#            or (options_jugador == "tijera" and options_bot == "papel")
#        ):
#            print("¡Haz Ganado!")    
#        else : 
#            (print("El bot gana."))
#    else:
#        print("Elección no válida. Elige piedra, papel o tijera.")

# Fin del juego
#print("Juego terminado.")

