from asciiFigures import *
import time

logoLines = logo.splitlines()
for line in logoLines:
    print(line)
    time.sleep(0.09)

print("Ingresa la palabra correcta sin espacios")


adivinanzas = [
    
    {"adivinanza": "¿Qué cosa es la que enriquece a todos sin empobrecer a nadie?", 
     "respuesta": ["cultura", "educación", "educacion"], 
     "pistas": [cultura, cultura2]},

    {"adivinanza": "Tiene cuello pero no cabeza, brazos pero no manos", 
     "respuesta": ["camisa", "camiseta"],
     "pistas": [camisa1, f"Se usa para cubrir el torso \n{camisa2}"]},

    {"adivinanza": "Blanco por dentro, verde por fuera, si quieres que te lo diga, espera", 
     "respuesta": ["pera"],
     "pistas": [frutas1, frutas2]},

     
    {"adivinanza": "Tengo un cuello largo y no tengo cabeza, sin alas vuelo y sin plumas nado ¿Quién soy? ", 
     "respuesta": ["cisne"], 
     "pistas": [f"Es un ave alta \n{ave1}",  f"Está en los lagos \n{ave2}"]},

     
    {"adivinanza": "Camina sin pies y vuela sin alas ¿Qué es?", 
     "respuesta": ["tiempo"], 
     "pistas": [f"Transcurre linealmente y no para \n{tiempo1}", f"Está en los relojes \n{tiempo2}", "Esta en los relojes"]}

]
contadorCorrectas = 0

for lista in adivinanzas:
    print("\n", lista["adivinanza"])
    intentos_restantes = 3
    count = 0

    while intentos_restantes > 0:
        respuesta = input("\nIntenta adivinar: ")

        if respuesta.lower() in [ans.lower() for ans in lista["respuesta"]]:
            print("\n¡Correcto! Has adivinado.")
            contadorCorrectas += 1
            break

        else:
            print("\nLo siento, respuesta incorrecta.")
            intentos_restantes -= 1

            if intentos_restantes > 0:
                print("\nPista:")
                pista = lista["pistas"][count]
                drawLinesPista = pista.split("\n")

                for line in drawLinesPista:
                    print(line)
                    time.sleep(0.09)

                count += 1

            else:
                print("\nLo siento, has agotado tus intentos. La respuesta correcta era:", lista["respuesta"])

cantidadAdivinanzas = len(adivinanzas)

print(f"\nTuviste {contadorCorrectas}/{cantidadAdivinanzas} respuestas correctas")
if contadorCorrectas == cantidadAdivinanzas:
    print("\n¡Enhorabuena, pudiste resolver todas las adivinanzas!\n")
else:
    print("\nTe puede ir mejor la proxima vez, vuélvelo a intentar\n")