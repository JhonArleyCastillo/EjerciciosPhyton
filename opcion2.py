import random
name = input (" Ingrese su nombre ").capitalize()
op = ["piedra", "papel", "tijeras"]
sep = "-" * 15 
while True:
    user = input(name +" "+ "Elije: piedra, papel o tijeras:"+" ").lower()
    if user not in op:
        print(name +" "+" Movimiento no valido")
        continue
    pc= random.choice(op)
    print(" la PC ha seleccionado "+ pc)
    if user == pc:
        print("Empate!, ambos eligieron "+ user)
    elif user == "tijeras" and pc == "papel":
        print(name+" "+"Ganaste,"+ user +" ganas en contra de "+ pc)
    elif user == "papel" and pc == "piedra":
        print(name+" "+"Ganaste, "+ user +" ganas en contra de "+ pc)
    elif user == "piedra" and pc == "tijeras":
       print(name+" "+"Ganaste, "+ user +" ganas en contra de "+ pc)
    else:
        print(name +" "+"Perdiste, "+ user + " pierde contra" +" "+(pc))
        print (sep +" Fin del juego "+ sep)