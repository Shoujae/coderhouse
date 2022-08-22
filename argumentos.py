#lo primeo que hay que hacer es importar la libreria sys
import sys

nombre=sys.argv[1]


print(f"Hola {nombre}!")

if len(sys.argv) !=3:
    print("Error necesito 2 argumentos")
else:
    palabra=sys.argv[1]
    cantidad=int(sys.argv[2])

    for i in range(cantidad):    
        print(palabra)

