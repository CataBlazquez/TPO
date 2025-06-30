from functools import reduce
import os
import json


def Importar_Archivos(habitacion, tipo):
    if habitacion=="dormitorio":
        if tipo=="matriz":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Dormitorio\matriz.txt", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "diccionario":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Dormitorio\diccionario.json", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "objetos":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Dormitorio\objetos.txt", "r+", encoding= "utf -8")
            return archivo
    elif habitacion=="living":
        if tipo=="matriz":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\living\matriz.txt", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "diccionario":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\living\diccionario.json", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "objetos":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\living\objetos.txt", "r+", encoding= "utf -8")
            return archivo
    elif habitacion=="cocina":
        if tipo=="matriz":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Cocina\matriz.txt", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "diccionario":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Cocina\diccionario.json", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "objetos":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Cocina\objetos.txt", "r+", encoding= "utf -8")
            return archivo
    elif habitacion=="baño":
        if tipo=="matriz":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Baño\matriz.txt", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "diccionario":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Baño\diccionario.json", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "objetos":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Baño\objetos.txt", "r+", encoding= "utf -8")
            return archivo
    elif habitacion=="oficina":
        if tipo=="matriz":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Oficina\matriz.txt", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "diccionario":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Oficina\diccionario.json", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "objetos":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Oficina\objetos.txt", "r+", encoding= "utf -8")
            return archivo
    elif habitacion=="patio":
        if tipo=="matriz":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Patio\matriz.txt", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "diccionario":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Patio\diccionario.json", "r+", encoding= "utf -8")
            return archivo
        elif tipo== "objetos":
            archivo=open(r"C:\Users\Cat\OneDrive\Desktop\TPO\Patio\objetos.txt", "r+", encoding= "utf -8")
            return archivo

def Eleccion_Personaje():
    print("👩Carla: Influencer en como balancear la vida con el estudio (esta reprobando todo)")
    print("👨Gabriel: Gymbro obsesionado con barritas de proteina")
    print("🐶Firulais: Guau Guau Guau")
    eleccion=input("Elige tu personaje: ").lower()
    while ((eleccion!="carla") and (eleccion!="gabriel") and (eleccion!="firulais")):
        print("No vale inventar personajes!!!")
        eleccion=input("Elige tu personaje: ").lower()
    if eleccion=='firulais':
        eligio_perro=input("Estas seguro que lo queres a firu? Si/No").lower()
        while eligio_perro=='si':
            print("Guau guau Guau")
            eligio_perro=input("Estas seguro que lo queres a firu? Si/No").lower()
        print("Sera re bueno Firu, pero no me parece la mejor idea para un juego como este. Por sus esfuerzos igual le damos un 🦴")
        print("Guau")
        print("De nada, Firu. Ahora si, elegi a tu personaje: ")
        print("👩Carla: Influencer en como balancear la vida con el estudio (esta reprobando todo)")
        print("👨Gabriel: Gymbro obsesionado con barritas de proteina")
        eleccion=input("Elige tu personaje: ").lower()
    return eleccion
def Inicio_Juego(personaje):
    print ("Mañana tengo que entregar el trabajo final de Programacion I y Edesur hizo una de las suyas mientras tenia el Word abierto y sin  el autoguardado."
    "Por suerte, mi amigo ya lo había imprimido (impreso o imprimido? A ver que dice la RAE… Ah cierto, no tengo WIFI")
    print ("Cuando llego a la casa de mi amigo, me doy cuenta que el tambien esta sin luz")
    print (
            """Despues de un pasillo larguisimo, llego a su departamento\n,
            1) Toco la puerta: \n
            2) Toco el timbre: \n
            3)Abro la puerta:""")
    opcion=int(input("¿Que opcion eliges?\n"))
    while opcion<0 and opcion>4:
        print("No vale inventar opciones")
        print (
            """Despues de un pasillo larguisimo, llego a su departamento\n,
            1) Toco la puerta: \n
            2) Toco el timbre: \n
            3)Abro la puerta:""")
        opcion=int(input("¿Que opcion eliges?\n"))
    if(opcion==1 or opcion==2):
        print("GUAUUUUUUUUU")
        print("Guau Guau Guau *sonido de rasqueteo en la puerta*")
        print("Este perro aprendio a abrir la puerta????")
    else: 
        print("¿Como van a dejar la puerta abierta? ¿Creen que viven en una sitcom?")
    matriz= Importar_Archivos("living", "matriz")
    matriz[6][2]=1
    ubicacion_personaje=(6,2)
    return ubicacion_personaje 
def Afuera(personaje,inventario):
    #funcion por si se abre la puerta al exterior
    eleccion= input("Aun no has terminado, ¿Seguro que quieres irte? Si/No\n ").lower()
    while eleccion!='no' and eleccion!= 'si':
        print("Escribiste cualquiera, escribi bien")
        eleccion= input("Aun no has terminado, ¿Seguro que quieres irte? Si/No\n").lower()
    if eleccion=='si':
        exit()
    elif "no":
        ubicacion_personaje=(6,2)
        Living(inventario,ubicacion_personaje,personaje) 
def Ubicacion_Actual_Personaje(habitacion_actual):
    direcciones = ("w", "s", "a", "d") 
    # Primero buscamos la posición actual del jugador (el número 1)
    for fila in range(len(habitacion_actual)):
        for col in range(len(habitacion_actual[fila])):
            if habitacion_actual[fila][col] == 1:
                fila_jugador = fila
                col_jugador = col
    # Coordenadas relativas a la posición actual
    coordenadas = [
        (fila_jugador- 1, col_jugador),  # adelante (W)
        (fila_jugador + 1, col_jugador),  # atrás (S)
        (fila_jugador, col_jugador - 1),  # izquierda (A)
        (fila_jugador, col_jugador + 1)   # derecha (D)
    ]
    ubicacion_actual=(fila_jugador, col_jugador)
    return ubicacion_actual, coordenadas, direcciones
def Objetos_Cercanos_interactivos(personaje, inventario, nombre_habitacion):
    
    matriz_habitacion=Importar_Archivos(nombre_habitacion, "matriz")
    objetos_interactivos = []
    objetos_habitacion=Importar_Archivos(nombre_habitacion, "objetos")
    ubicacion_actual,coordenadas,direcciones=Ubicacion_Actual_Personaje(matriz_habitacion)
    fila_jugador,columna_jugador= ubicacion_actual
    objetos_adyacentes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for fila, columna in objetos_adyacentes: #cambia la vista del jugador y agrega a la lista los objetos que estan en jugador+-1
        nueva_fila = fila_jugador + fila 
        nueva_columna = columna_jugador + columna

        if 0 <= nueva_fila < len(matriz_habitacion) and 0 <= nueva_columna < len(matriz_habitacion[nueva_fila]): #si la nueva fila es menor al maximo de filas que hay (no cuentan las paredes) && si las columnas son menores al maximo de columnas en esa fila (no cuentan paredes)
            if matriz_habitacion[nueva_fila][nueva_columna] != 0: #muestra todo lo que no sea una pared
                if 0 <= nueva_fila < len(objetos_habitacion) and 0 <= nueva_columna < len(objetos_habitacion[nueva_fila]):
                    objeto = objetos_habitacion[nueva_fila][nueva_columna]
                    if objeto != 0:
                        objetos_interactivos.append(((nueva_fila, nueva_columna), objeto))
    print (objetos_interactivos)
    if objetos_interactivos :
        
        print("\nObjetos cercanos con los que puedes interactuar:")
        for i, (coordenadas, nombre_objeto) in enumerate(objetos_interactivos):
            print(f"{i + 1}. {nombre_objeto} (fila: {coordenadas[0]}, columna: {coordenadas[1]})")
    
        print(" Ver Objeto (1) || Interactuar con Objeto (2)")
        try:
            accion=int(input (">"))
            if accion not in [1, 2]:
                print("Opción no válida")
                return
            

            indice_objeto = int(input("Elige el número del objeto: ")) -1
            if 0 <= indice_objeto < len(objetos_interactivos):
                coordenadas_objeto, nombre_objeto = objetos_interactivos[indice_objeto]
                if accion==1:
                    VerObjeto(personaje, nombre_objeto, nombre_habitacion)
                elif accion==2:
                    if nombre_objeto!= "closet":
                        AgarrarObjeto(nombre_habitacion, nombre_objeto, inventario, coordenadas_objeto, objetos_habitacion)
                    else: 
                        Usar(nombre_objeto, nombre_habitacion, personaje, inventario)
            else:
                print("Número de objeto inválido.")
        except ValueError:
            print("Por favor, ingresa un número.")
        
    else:
        print("No hay objetos interesantes cerca.")
    return
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
def Mover  (nombre_habitacion):
    habitacion_actual= Importar_Archivos(nombre_habitacion, "matriz")
    ubicacion_personaje, coordenadas, direcciones =Ubicacion_Actual_Personaje(habitacion_actual)
    fila_jugador=ubicacion_personaje[0]
    col_jugador=ubicacion_personaje[1]
    # Recorremos los movimientos posibles segun la ubicacion del personaje
    movimientos_posibles = []
    for i in range(len(coordenadas)):
        f, c = coordenadas[i]
        if 0 <= f < len(habitacion_actual) and 0 <= c < len(habitacion_actual[0]) and habitacion_actual[f][c] == 0:
            movimientos_posibles.append(direcciones[i])
    adyacentes_con_puertas = []
    for i in range(len(coordenadas)):
        f, c = coordenadas[i]
        if 0 <= f < len(habitacion_actual) and 0 <= c < len(habitacion_actual[0]) and habitacion_actual[f][c] == 2:
            adyacentes_con_puertas.append(direcciones[i])
    print("el jugador esta en: ", fila_jugador,col_jugador)
    print("Movimientos posibles:", movimientos_posibles)
    if adyacentes_con_puertas!=[]:
        print("Buscar_Puertas objetos_adyacentes:", adyacentes_con_puertas)
#eleccion de movimiento
    movimiento_elegido=input("¿Para donde te quieres mover?").lower()
    while(movimiento_elegido not in movimientos_posibles) and (movimiento_elegido not in adyacentes_con_puertas):
        print ("Movimiento invalido")
        movimiento_elegido=input("¿Para donde te quieres mover?").lower()
    habitacion_actual[fila_jugador][col_jugador]=0
    if movimiento_elegido=='w':
        if habitacion_actual[fila_jugador-1][col_jugador]==2:
            destino=Buscar_Puertas((fila_jugador)-1,col_jugador, nombre_habitacion)
            Cambio_de_Habitacion(destino,ubicacion_personaje)
        habitacion_actual[fila_jugador-1][col_jugador]=1
    elif movimiento_elegido=='s':
        if habitacion_actual[fila_jugador+1][col_jugador]==2:
            destino=Buscar_Puertas((fila_jugador)+1,col_jugador, nombre_habitacion)
            Cambio_de_Habitacion(destino, ubicacion_personaje)
        habitacion_actual[fila_jugador+1][col_jugador]=1
    elif movimiento_elegido=='a':
        if habitacion_actual[fila_jugador][col_jugador-1]==2:
            destino=Buscar_Puertas(fila_jugador,(col_jugador)-1, nombre_habitacion)
            Cambio_de_Habitacion(destino, ubicacion_personaje)
        habitacion_actual[fila_jugador][col_jugador-1]=1
    elif movimiento_elegido=='d':
        if habitacion_actual[fila_jugador][col_jugador+1]==2:
            destino=Buscar_Puertas(fila_jugador,(col_jugador)+1, nombre_habitacion)
            Cambio_de_Habitacion(destino, ubicacion_personaje)
        habitacion_actual[fila_jugador][col_jugador+1]=1
    return
def Cambio_de_Habitacion(destino, ubicacion_personaje):
    """Utiliza informacion del string destino para poder encontrar la habitacion a la que tiene que ir segun el diccionario de matrices y de puertas"""

    if destino=="cocina":
        Cocina(inventario,ubicacion_personaje, personaje )
    elif destino=="baño":
        Baño(inventario, ubicacion_personaje, personaje)
    elif destino=="living":
        Living(inventario, ubicacion_personaje, personaje)
    elif destino=="patio":
        Patio(inventario, ubicacion_personaje, personaje)
    elif destino=="oficina":
        Oficina (inventario, ubicacion_personaje, personaje)
    elif destino=="dormitorio":
        Dormitorio(inventario, ubicacion_personaje, personaje)
    elif destino=="afuera":
        Afuera(personaje, inventario)
    return destino
def Buscar_Puertas(fila_jugador, col_jugador, nombre_habitacion):
    with open (r"C:\Users\Cat\OneDrive\Desktop\TPO\puertas.json", "r") as f:
        puertas=json.load(f)
        if nombre_habitacion not in puertas:
            print("Hmmmm aca paso algo raro...")
            return None
        for destino, info in puertas[nombre_habitacion].items():
            if info.get("coordenada origen") == [fila_jugador, col_jugador]:
                return {
                    "habitacion destino": info["habitacion destino"],
                    "coordenada destino": info.get("coordenada destino"),
                    "estado puerta": info.get("estado puerta", "abierta"),
                    "nombre destino": destino
                }

    return None

def VerObjeto(personaje, objeto,nombre_habitacion):
    try:
        descripcion = diccionario_objetos[nombre_habitacion][objeto][personaje]
        print(descripcion)
    except KeyError:
        print(f" El objeto '{objeto}' no se puede ver o no existe en '{nombre_habitacion}'")
def AgarrarObjeto(nombre_habitacion, nombre_objeto, inventario, coordenadas_objeto, objetos_habitacion):
    if nombre_habitacion in diccionario_objetos:
        dicc_hab = diccionario_objetos.get(nombre_habitacion, {})
        if nombre_objeto in dicc_hab:
            if dicc_hab[nombre_objeto]["inventario"]:
                respuesta = input(f"¿Quieres guardar '{nombre_objeto}' en tu inventario? (si/no) ").lower()
                if respuesta == "si":
                    inventario.append(nombre_objeto)
                    objetos_habitacion[coordenadas_objeto[0]][coordenadas_objeto[1]] = 0
                    print(f"{nombre_objeto} fue añadido al inventario.")
                else:
                    print("No se guardo el objeto.")
            else:
                print("No se puede guardar ese objeto en el inventario.")
        else:
            print("Ese objeto no se puede agarrar.")
def Usar(nombre_objeto, habitacion_actual, personaje, inventario,):
    palabras=[nombre_objeto, habitacion_actual]
    clave =" ".join(palabras)

    acciones = diccionario_accciones_globales[clave]
    if clave not in diccionario_accciones_globales:
        print("Este objeto no tiene acciones disponibles.")
        return  
    elif clave=="closet":
        print("Que queres hacer?")
        print(" || ".join(acciones.keys())) #Muestra las acciones disponibles para el objeto
        eleccion = input("> ").lower()
        while eleccion not in acciones:
            print("Opcion no valida")
            eleccion = input(">").lower()    
        if eleccion=="intentar abrir caja fuerte": #algunos objetos tienen acciones que son funciones
            resultado=Cajas_Fuertes(ubicacion_personaje=(5,4),nombre_habitacion= "dormitorio" )
        else:
            print(acciones[eleccion])

    print("Que queres hacer?")
    print(" || ".join(acciones.keys())) #Muestra las acciones disponibles para el objeto
    eleccion = input("> ").lower()
    while eleccion not in acciones:
        print("Opcion no valida")
        eleccion = input(">").lower()

    resultado = acciones[eleccion]
    if callable(resultado): #algunos objetos tienen acciones que son funciones
        resultado() 
    else:
        print(resultado)
def Inventario(inventario, habitacion_actual):
    if not inventario:
        print("El inventario esta vacio")
        return
    print("Inventario:")
    for i, objeto in enumerate(inventario, 1):
        print(f"{i}. {objeto}") #imprime como una lista numerada
    eleccion = input("Que objeto queres usar?").lower()
    if eleccion in inventario:
        Usar(eleccion, habitacion_actual, personaje, inventario)
    else:
        print("Etse objeto no esta en el inventario")
def Mensajear():
    # funcion para los wpp
    print("Intentas enviar un mensaje...")
    pass
def Hojas():
    pass

def Opciones_Control_de_Personaje(personaje,inventario,nombre_habitacion):
    print("\n¿Qué quieres hacer ahora?")
    print("MOVER (1) || VER INVENTARIO (2) || VER OBJETOS CERCANOS (3) ||SALIR (4)") 
    decision = int(input("> "))
    while decision<0 or decision>5:
        print("Opción no válida.")
        print("\n¿Qué quieres hacer ahora?")
        print("MOVER (1) || VER INVENTARIO (2) || VER OBJETOS CERCANOS (3) ||SALIR (4)") 
        decision = int(input("> "))
    while decision!=4:
        try:
            if decision == 1:
                Mover(nombre_habitacion)
            elif decision== 2:
                print("Inventario:", inventario)
            elif decision==3:
                Objetos_Cercanos_interactivos(personaje,inventario,nombre_habitacion)
            elif decision== 4: 
                break
            print("\n¿Qué quieres hacer ahora?")
            print("MOVER (1) || VER INVENTARIO (2) || VER OBJETOS CERCANOS (3) ||SALIR (4)") 
            decision = int(input("> "))
        except ValueError:
            print ("Error de valor")
            print("\n¿Qué quieres hacer ahora?")
            print("MOVER (1) || VER INVENTARIO (2) || VER OBJETOS CERCANOS (3) ||SALIR (4)") 
  
def Living (inventario, ubicacion_personaje, personaje):
    nombre_habitacion=str("living")
    print(f"\nEstás en el {nombre_habitacion}. Observas alrededor...")
    Opciones_Control_de_Personaje(personaje,inventario,nombre_habitacion)

def Patio(inventario, ubicacion_personaje, personaje):
    nombre_habitacion="patio"
    print(f"\nEstás en el {nombre_habitacion}. Observas alrededor...")
    Opciones_Control_de_Personaje(personaje,inventario, nombre_habitacion )
    
def Dormitorio(inventario, ubicacion_personaje, personaje):
    nombre_habitacion="dormitorio"
    print(f"\nEstás en el {nombre_habitacion}. Observas alrededor...")
    Opciones_Control_de_Personaje(personaje,inventario, nombre_habitacion ) 

def Oficina(inventario, ubicacion_personaje, personaje):
    nombre_habitacion="oficina"
    print(f"\nEstás en el {nombre_habitacion}. Observas alrededor...")
    Opciones_Control_de_Personaje(personaje,inventario, nombre_habitacion )

def Cocina(inventario, ubicacion_personaje, personaje):
   nombre_habitacion="cocina"
   print(f"\nEstás en el {nombre_habitacion}. Observas alrededor...")
   Opciones_Control_de_Personaje(personaje,inventario, nombre_habitacion )

def Baño(inventario, ubicacion_personaje, personaje):
    nombre_habitacion="baño"
    print(f"\nEstás en el {nombre_habitacion}. Observas alrededor...")
    # Definir una tupla con los elementos del estante y sus características
    estante_baño = (
    ("Jabón", "líquido"),
    ("Shampoo", "para cabello seco"),
    ("Acondicionador", "hidratante"),
    ("Pasta de dientes", "blanqueadora"),
    ("Cepillo de dientes", "suave"),
    ("Desodorante", "antitranspirante"),
    ("Pañuelitos", "extra suave"),
    ("Toalla", "de algodón"),
    ("Perfume", "floral"),
    ("Crema para manos", "nutritiva"),
    ("Gel capilar", "no graso"),
    ("Esponja", "exfoliante"),
    ("Labial", "rojo"),
    ("Mascara de pestañas", "tono negro"),
    ("Agua Micelar", "libre de Parabenos"),
    ("Delineador", "líquido"),
    ("Llave", "abre puerta")
    )

    # Mostrar los elementos del estante y sus características
    print("Elementos del estante en el baño y sus características:")
    for i, (elemento, caracteristica) in enumerate(estante_baño):
        print(f"{i + 1}. {elemento}: {caracteristica}")

    # Preguntar al usuario si desea tomar algo
    respuesta = input('¿Desea tomar algo del estante? seleccione "Si" o "No": ')

    if respuesta.lower() == 'si':
        elementos_tomados = []
        estante_lista = list(estante_baño)
        
        while True:
            seleccion = int(input("Seleccione el número del elemento que desea tomar (ingrese -1 para finalizar): "))
            if seleccion == -1:
                break
            if 1 <= seleccion <= len(estante_lista):
                elemento_tomado = estante_lista[seleccion - 1]
                elementos_tomados.append(elemento_tomado)
                estante_lista[seleccion - 1] = ("", "")  # Llenar el espacio con vacío
            else:
                print("Selección no válida. Intente nuevamente.")
        
        # Convertir la lista de nuevo a tupla
        estante_baño = tuple(estante_lista)
        
        # Mostrar los elementos tomados y los elementos restantes
        print("Has tomado los siguientes elementos:")
        for elemento, caracteristica in elementos_tomados:
            print(f"- {elemento}: {caracteristica}")
        
        print("Elementos restantes en el estante:")
        for i, (elemento, caracteristica) in enumerate(estante_baño):
            if elemento is not None:
                print(f"{i + 1}. {elemento}: {caracteristica}")
            else:
                print(f"{i + 1}. [Vacío]")
    else:
        print("No has tomado ningún elemento.")
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

def mostrar_objetos(diccionario):
    for idx, elemento in enumerate(diccionario, 1): #index, enumera como lista
        print(f"{idx}. {elemento}")
    return list(diccionario.keys()) #devuelve como una lista

def elegir_objeto(diccionario):
    objetos = mostrar_objetos(diccionario)
    texto=("Elige un objeto por su número:\n> ")
    while True:
        try:
            eleccion_num = int(input(texto)) - 1
            if 0 <= eleccion_num < len(objetos):
                return objetos[eleccion_num]
            else:
                print("Número fuera de rango.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def realizar_accion(objeto, acciones_dicc):
    acciones = acciones_dicc.get(objeto, {})
    if not acciones:
        print("No hay acciones disponibles para este objeto.")
        return
    print(f"Acciones disponibles: {', '.join(acciones.keys())}")
    accion = input("¿Qué acción deseas realizar?\n> ").strip().lower()
    while accion not in acciones:
        print("Acción no válida. Intenta nuevamente.")
        accion = input("> ").strip().lower()
    print(acciones[accion])

def interactuar_baño(personaje):

    while True:
        print("\n¿Dónde quieres interactuar?")
        print("1. Objetos del baño")
        print("2. Estante del baño")
        print("3. Salir del baño")
        opcion = input("> ")
        if opcion == "1":
            print("\nObjetos disponibles en el baño:")
            eleccion = elegir_objeto(dicc_objetos_baño)
            print(dicc_objetos_baño[eleccion][personaje])
            realizar_accion(eleccion, acciones_generales_baño)
        elif opcion == "2":
            print("\nObjetos disponibles en el estante del baño:")
            eleccion = elegir_objeto(dicc_objetos_estante_baño)
            print(dicc_objetos_estante_baño[eleccion][personaje])
            realizar_accion(eleccion, acciones_generales_estante_baño)
        elif opcion == "3":
            print("Saliste del baño.")
            break
        else:
            print("Opción no válida.")

def registrar_interaccion(nombre, objeto, resultado):
    try:
        ruta = "log.txt"
        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre} interactuó con {objeto}: {resultado}\n")
    except Exception as e:
        print("No se pudo guardar el registro.")

"""El diccionario de puertas, se va a leer con el primer elemento siendo las coordenadas de la puerta, y la ubicacion actual. """   
inventario=[]

def Cajas_Fuertes(ubicacion_personaje, nombre_habitacion):
    if ubicacion_personaje==(5,6) and nombre_habitacion=="dormitorio":
        print("Hay una caja fuerte con un candado de 3 numeros, que queres hacer?")
        print ("Ingresa los 3 numeros juntos, por ejemplo 123")
        contraseña=int(input("Contraseña: "))
        while contraseña!=653: #reloj, pelota, anteojos
            print("Contraseña incorrecta, intenta de nuevo")
            print("Quieres volver a intentar? Si/No")
            eleccion=input(">").lower()
            if eleccion=="si":
               contraseña=int(input("Contraseña: ")) 
            elif eleccion=="no":
                print("Volviendo al dormitorio")
                return
            else:
                print("Respuesta no valida, volviendo al dormitorio")
                return
        if contraseña==653:
            print("Contraseña correcta, la caja fuerte se abre")
            print ("encuentras una hoja del TP")
        return
    elif ubicacion_personaje==(1,4) and nombre_habitacion=="patio":
        print("Hay una caja fuerte con un candado de 3 numeros, que queres hacer?")
        print ("Ingresa los 3 numeros juntos, por ejemplo 123")
        contraseña=int(input("Contraseña: "))
        while contraseña!=236: #arboles, lapidas, lapidas+pozos
            print("Contraseña incorrecta, intenta de nuevo")
            print("Quieres volver a intentar? Si/No")
            eleccion=input(">").lower()
            if eleccion=="si":
               contraseña=int(input("Contraseña: ")) 
            elif eleccion=="no":
                print("Volviendo al patio")
                return
            else:
                print("Respuesta no valida, volviendo al patio")
                return
        if contraseña==236:
            print("Contraseña correcta, la caja fuerte se abre")
            print ("encuentras una hoja del TP")
        return

"""--------------------------------------------------------------------------------------------------------------------------"""    
#main 

personaje=Eleccion_Personaje()
ubicacion_personaje=Inicio_Juego(personaje, inventario )
Living(inventario, ubicacion_personaje,personaje)








