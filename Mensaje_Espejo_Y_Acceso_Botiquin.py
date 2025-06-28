from functools import reduce

def procesar_mensaje(mensaje):
    # Extraer cada tercera letra usando slice
    extraer_letra = mensaje[::3]
    
    # Inicializar variables
    palabras = []
    mensaje_en_construcción = ""
    
    # Iterar sobre cada carácter en el mensaje extraído
    for caracter in extraer_letra:
        if caracter.isupper() and mensaje_en_construcción:
            # Si el carácter es mayúscula y mensaje_en_construcción no está vacío, agregar mensaje_en_construcción a la lista de palabras
            palabras.append(mensaje_en_construcción)
            mensaje_en_construcción = caracter
        else:
            # De lo contrario, agregar el carácter a mensaje_en_construcción
            mensaje_en_construcción += caracter
    
    # Agregar la última palabra a la lista
    if mensaje_en_construcción:
        palabras.append(mensaje_en_construcción)
    
    # Convertir el mensaje resultante a minúsculas menos la primera letra que debe ir en mayúscula
    mensaje_descifrado = " ".join(palabras).lower().capitalize()
    
    return mensaje_descifrado

# Mensaje cifrado
mensaje_cifrado = "LasazuHoyolijayasiDdhesolosTipporEyesolteeasiEsenooEmelosBotorotusisoqueunainonahDipemaPriroaisameseparaposososAceunoxyximalosipaocasum"

#Mostrar mensaje Cifrado
print(mensaje_cifrado) 
# Solicitar al usuario si desea descifrar el mensaje
respuesta = input('Desea descifrar el mensaje: seleccione "Si" o "No": ')

if respuesta.lower() == 'si':
    resultado = procesar_mensaje(mensaje_cifrado)
    print(f"Mensaje descifrado: {resultado}")
    
    # Lista de números
    numeros = [2, 3, 5, 9, 11, 17, 22, 31, 39]
    
    # Mostrar la lista de números al usuario
    print(f"Estos números te ayudaran a acceder al botiquín: {numeros}")
    
    # Preguntar al usuario si desea sumar o multiplicar los números
    operacion = input('Para abrir el botiquín, necesitaras la clave de acceso. Seleccione "sumar" o "multiplicar" para obtener una clave: ')
    
    if operacion.lower() == 'sumar':
        suma = sum(numeros)
        print(f"La clave generada es: {suma}. Podes abrir el botiquín.")
    elif operacion.lower() == 'multiplicar':
        producto = reduce(lambda x, y: x * y, numeros)
        print(f"La clave generada es: {producto}. No abre el botiquín.")
    else:
        print("La operación no es válida.")
else:
    print("Operación cancelada.")
