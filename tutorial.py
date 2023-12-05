#Piedra, papel y tijeras
# Importar elección aletoria
import random

#crear variables del juego
options: ["Piedra, Papel, Tijera"]

#numero de turnos
num_turnos: 5

#Iniciar el juego
for turno in range(num_turnos):
    print(f"turno {turno + 1}")

#Menu de seleccion:jugador
    options_jugador = input("Piedra, Papel, Tijera").lower()

#Menu de seleccion: Bot
    options_bot= random.choices(options)
    print(f"El Bot elige: {options_bot}")

#Logica en el juego
    if options_jugador in options:
        if options_jugador == options_bot:
           print ("Empate!")
        elif (
            (options_jugador == "piedra" and options_bot == "tijera")
            or (options_jugador == "papel" and options_bot == "piedra")
            or (options_jugador == "tijera" and options_bot == "papel")
        ):
            print("¡Haz Ganado!")    
        else : 
            (print("El bot gana."))
    else:
        print("Elección no válida. Elige piedra, papel o tijera.")

# Fin del juego
print("Juego terminado.")
