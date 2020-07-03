lista = []
salida = "No"

def agregarcontacto():
    nuevo_contacto = {}
    nuevo_contacto['Nombre'] = input("Ingresa contacto: ")
    lista.append(nuevo_contacto)

while (salida == "No"):
    entrada=input("Escribe la acción a efectuar: ")
    if entrada == "Nuevo":
        agregarcontacto()
        print("Contacto agregado")
    elif entrada == "Mostrar":
        print(lista[:])
    elif entrada == "salir":
       exit()
    else:
        print("opcion no valida ")
        