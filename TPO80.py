from functools import reduce
import os

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
def Inicio_Juego(personaje, inventario):
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
    matriz_living[6][2]=1
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
    
    matriz_habitacion=diccionario_matrices[nombre_habitacion]
    objetos_interactivos = []
    objetos_habitacion=diccionario_matrices["objetos "+nombre_habitacion]
    ubicacion_actual,coordenadas,direcciones=Ubicacion_Actual_Personaje(matriz_habitacion)
    fila_jugador,columna_jugador= ubicacion_actual
    objetos_adyacentes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for fila, columna in objetos_adyacentes: #cambia la vista del jugador y agrega a la lista los objetos que estan en jugador+-1
        nueva_fila = fila_jugador + fila 
        nueva_columna = columna_jugador + columna

        if 0 <= nueva_fila < len(matriz_habitacion) and 0 <= nueva_columna < len(matriz_habitacion[nueva_fila]): #si la nueva fila es menor al maximo de filas que hay (no cuentan las paredes) && si las columnas son menores al maximo de columnas en esa fila (no cuentan paredes)
            if matriz_habitacion[nueva_fila][nueva_columna] != -1: #muestra todo lo que no sea una pared
                if 0 <= nueva_fila < len(objetos_habitacion) and 0 <= nueva_columna < len(objetos_habitacion[nueva_fila]):
                    objeto = objetos_habitacion[nueva_fila][nueva_columna]
                    if objeto != 0:
                        objetos_interactivos.append(((nueva_fila, nueva_columna), objeto))
    print (objetos_interactivos)
    if objetos_interactivos :
        print("\nObjetos cercanos con los que puedes interactuar:")
        for i, (coordenadas, nombre_objeto) in enumerate(objetos_interactivos):
            print(f"{i + 1}. {nombre_objeto} (fila: {coordenadas[0]}, columna: {coordenadas[1]})")
        print(" Ver Objeto (1) || Agarrar Objeto (2)")
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
                    AgarrarObjeto(nombre_habitacion, nombre_objeto, inventario, coordenadas_objeto, objetos_habitacion)
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
    habitacion_actual= diccionario_matrices [nombre_habitacion]
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
        print("Puertas objetos_adyacentes:", adyacentes_con_puertas)
#eleccion de movimiento
    movimiento_elegido=input("¿Para donde te quieres mover?").lower()
    while(movimiento_elegido not in movimientos_posibles) and (movimiento_elegido not in adyacentes_con_puertas):
        print ("Movimiento invalido")
        movimiento_elegido=input("¿Para donde te quieres mover?").lower()
    habitacion_actual[fila_jugador][col_jugador]=0
    if movimiento_elegido=='w':
        if habitacion_actual[fila_jugador-1][col_jugador]==2:
            destino=Puertas((fila_jugador)-1,col_jugador, nombre_habitacion)
            Cambio_de_Habitacion(destino,ubicacion_personaje)
        habitacion_actual[fila_jugador-1][col_jugador]=1
    elif movimiento_elegido=='s':
        if habitacion_actual[fila_jugador+1][col_jugador]==2:
            destino=Puertas((fila_jugador)+1,col_jugador, nombre_habitacion)
            Cambio_de_Habitacion(destino, ubicacion_personaje)
        habitacion_actual[fila_jugador+1][col_jugador]=1
    elif movimiento_elegido=='a':
        if habitacion_actual[fila_jugador][col_jugador-1]==2:
            destino=Puertas(fila_jugador,(col_jugador)-1, nombre_habitacion)
            Cambio_de_Habitacion(destino, ubicacion_personaje)
        habitacion_actual[fila_jugador][col_jugador-1]=1
    elif movimiento_elegido=='d':
        if habitacion_actual[fila_jugador][col_jugador+1]==2:
            destino=Puertas(fila_jugador,(col_jugador)+1, nombre_habitacion)
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
    elif destino=="cuarto principal":
        Cuarto_Principal(inventario, ubicacion_personaje, personaje)
    elif destino=="afuera":
        Afuera(personaje, inventario)
    return destino
def Puertas(fila_jugador, col_jugador, nombre_habitacion):
    nombre_diccionario_puertas = "puertas " + nombre_habitacion
    if nombre_diccionario_puertas not in diccionario_puertas:
        print("ups, encontraste un bug 🐛, sentite bien con vos mismo")
        return None
    habitacion_puerta = diccionario_puertas[nombre_diccionario_puertas]
    for nombre_destino, info in habitacion_puerta.items():
        if "coordenada origen" not in info or "habitacion destino" not in info:
            continue  #salteamos entradas incompletas
        if info["coordenada origen"] == (fila_jugador, col_jugador):
            habitacion_destino = info["habitacion destino"]
            if "coordenada destino" not in info or info["coordenada destino"] is None:
                print("ups, encontraste un bug 🐛, sentite bien con vos mismo")
                return None
            coordenadas_destino = info["coordenada destino"]
            if habitacion_destino not in diccionario_matrices:
                print("ups, no existe la habitacion destino")
                return None
            matriz_destino = diccionario_matrices[habitacion_destino]
            matriz_destino[coordenadas_destino[0]][coordenadas_destino[1]] = 1
            matriz_origen = diccionario_matrices[nombre_habitacion]
            matriz_origen[fila_jugador][col_jugador] = 0
            return habitacion_destino

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
def Usar(nombre_objeto, habitacion_actual):
    clave = f"{nombre_objeto}+{habitacion_actual}"
    if clave not in diccionario_accciones_globales:
        print("Este objeto no tiene acciones disponibles.")
        return
    acciones = diccionario_accciones_globales[clave]
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
        Usar(eleccion, habitacion_actual)
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
    Opciones_Control_de_Personaje(personaje,inventario, nombre_habitacion )
    
def Cuarto_Principal(inventario, ubicacion_personaje, personaje):
    nombre_habitacion="cuarto principal"
    Opciones_Control_de_Personaje(personaje,inventario, nombre_habitacion ) 

def Oficina(inventario, ubicacion_personaje, personaje):
    nombre_habitacion="oficina"
    Opciones_Control_de_Personaje(personaje,inventario, nombre_habitacion )

def Cocina(inventario, ubicacion_personaje, personaje):
   nombre_habitacion="cocina"
   Opciones_Control_de_Personaje(personaje,inventario, nombre_habitacion )

def Baño(inventario, ubicacion_personaje, personaje):
    nombre_habitacion="baño"
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
puertas_living={
    #puertas desde el living
    "cuarto principal": {
       'coordenada origen': (0,1), #si el jugador llega a esa coordenada, es la puerta literal, entonces ahi se hace el cambio de habitacion
       'habitacion destino': 'cuarto principal',
       "coordenada destino": (5,5), #donde "aterriza" en el siguiente cuarto, el 0 se va a convertir en 1
       "estado puerta": "abierta",
    },
    "afuera" : {
        'coordenada origen': (7,2),
        "habitacion destino": "afuera",
    },
    "oficina": {
        'coordenada origen': (0,4),
       'habitacion destino': 'oficina',
       "coordenada destino": (4,2),
       "estado puerta": "abierta",
    },
    "baño": {
        'coordenada origen': (2,0),
       'habitacion destino': 'baño',
       "coordenada destino": (2,3),
       "estado puerta": "abierta",
    },
    "cocina": {
        'coordenada origen': (4,0),
       'habitacion destino': 'cocina',
       "coordenada destino": (2,3),
       "estado puerta": "abierta",
    }
}
puertas_cuarto_principal= {
    #puertas desde cuarto principal
    "living": {
        'coordenada origen': (5,4),
       'habitacion destino': 'living',
       "coordenada destino": (1,2),
       "estado puerta": "abierta",
        },
}
puerta_baño={#puertas desde el baño 
    "living": {
        "coordenada origen": (2,4),
       'habitacion destino': 'living',
       "coordenada destino": (2,1),
       "estado puerta": "abierta",
    }}
puerta_cocina={#puertas desde la cocina 
    "living": {
        'coordenada origen': (2,4),
       'habitacion destino': 'living',
       "coordenada destino": (4,1),
       "estado puerta": "abierta",
    }}
puertas_oficina={#puertas desde la oficina 
    "living": {
        'coordenada origen': (5,2),
       'habitacion destino': 'living',
       "coordenada destino": (1,5),
       "estado puerta": "abierta",
    },
    "patio": {
        'coordenada origen': (3,4),
       'habitacion destino': 'patio',
       "coordenada destino": (2,1),
       "estado puerta": "oculta",
    }}
puerta_patio={ #puerta desde el patio
    "oficina": {
        'coordenada origen': (2,0),
       'habitacion destino': 'oficina',
       "coordenada destino": (3,2),
       "estado puerta": "abierta",
    }}
"""Las matrices de objetos, van a indicar que hay en cada uno y cada uno tiene sus acciones especificas
    Si hay 0 es porque no hay nada, si hay algun objeto, se escribira tal objeto y sus acciones. Las puertas no cuentan como objetos.
    Puede haber objetos en puertas y paredes (afiches, cuadros, estantes)"""
"""La matriz de cada habitacion, tiene su forma arriba. Los cuadrados negros son las paredes, los blancos el piso. Si la matriz tiene 
un 1 es donde esta parado el jugador. Va a haber otra matriz con los objetos que tiene cada "celda". Si hay 0 es lugar donde puede caminar.
Si hay -1 esta prohibido caminar (ya sea porque hay una pared o un mueble), si hay un 2 es una puerta"""
# Definición de las matrices de objetos, habitaciones y sus diccionarios
matriz_living=[   [-1,2,-1,-1,2,-1],
               [-1,0,0,0,0,0,-1],
               [2,0,0,-1,-1,-1,0,-1],
               [-1,0,0,-1,-1,-1,0,-1],
               [2,0,0,0,0,0,0,-1],
               [-1,0,0,0,-1,-1,0,-1],
               [-1,-1,0,0,0,0,0,-1],
                  [-1,-1,2,-1,-1,-1,-1,-1],]
objetos_living=[[0,0,0,"cuadro",0,0,0,0],
                [0,0,0,0,0,0,0,0],
                ["chapa toilette",0,"alfombra","silla","mesa comedor","silla",0,0],
                [0,0,"alfombra","silla","mesa comedor","silla",0,"cartel prohibido"],
                ["Aca se hacen cosas ricas",0,"alfombra", 0,0,0,0,0],
                ["perchero",0,0,0,"sillon","sillon",0,"cuadro"],
                [0,"paraguero",0,0,0,0,0,0],
                [0,0,"llaves atras puerta",0,"television","television",0,0],]
dicc_objetos_living={
    "cuadro":{
        "carla":"*Carla analiza el cuadro buscando detalles estéticos y si podría ser un buen fondo para sus fotos.*",
        "gabriel":"*Gabriel mira el cuadro sin mucho interés, pensando en si tendrá suficientes calorías para su próxima rutina.*",
        "usar": False,
        "inventario" : False, 
    },
    "cucha perro":{
        "carla":"*Carla se acerca a la cucha, pensando si Firulais tendrá algún secreto de belleza canino.*",
        "gabriel":"Gabriel revisa la cucha por si acaso Firulais escondió alguna barrita de proteína.",
        "usar": False,
        "inventario" : False, 
    },
    "chapa toilette":{
        "carla":"Una chapa... quizás tenga un estilo vintage interesante para una storie de Insta.",
        "gabriel":"Gabriel ignora la chapa, enfocado en encontrar algo más útil.",
        "usar": False,
        "inventario" : False, 
    },
    "alfombra":{
        "carla":"Que linda alfombra",
        "gabriel":"Una alfombra comun",
        "usar": True, # alfombra living, abajo deberia haber una hoja
        "inventario" : False, 
    },
    "silla":{
        "carla":"*Carla evalúa si la silla es cómoda para tomarse una selfie.*",
        "gabriel":"Gabriel prueba la firmeza de la silla.",
        "usar": False,
        "inventario" : False, 
    },
    "mesa comedor":{
        "carla":"*Carla se pregunta si la mesa sería un buen lugar para un unboxing.*",
        "gabriel":"Gabriel se pregunta si la mesa será lo suficientemente resistente para apoyar pesas.",
        "usar": False,
        "inventario" : False, 
    },
    "Cartel: 'Aca se hacen cosas ricas'":{
        "carla":"Mmm, quizás haya algún snack rico y me tome un break.",
        "gabriel":"Gabriel olfatea el aire: '¿Proteína casera?'",
        "usar": False,
        "inventario" : False, 
    },
    "perchero":{
        "carla":"*Carla revisa las prendas, buscando inspiración para su próximo outfit.*",
        "gabriel":"Gabriel mira el perchero, buscando alguna toalla para secarse el sudor.",
        "usar": False,
        "inventario" : False, 
    },
    "sillon":{
        "carla":"Ay, este es como el sillon que hice canje por una storie en insta!",
        "gabriel":"Gabriel se sienta brevemente, evaluando si el sillón ofrece buen soporte lumbar.",
        "usar": False,
        "inventario" : False, 
    },
    "paraguero":{
        "carla":"*Carla mira los paraguas, pensando si alguno podría ser un accesorio de moda inesperado.*",
        "gabriel":"Gabriel mira los paraguas, pensando si alguno podría servir como improvisada barra de dominadas",
        "usar": False,
        "inventario" : False, 
    },
    "llaves atras puerta":{
        "carla":"*Carla examina el llavero buscando alguna llave que parezca importante o tenga un diseño interesante.*",
        "gabriel":"Gabriel mira las llaves sin darle mucha importancia.",
        "usar": False,
        "inventario" : False, 
    },
    "television":{
        "carla":"*Carla mira la televisión apagada, pensando en qué serie estará de moda*",
        "gabriel":"Gabriel mira la televisión apagada, pensando en qué canal pasarán competencias de fuerza.",
        "usar": False,
        "inventario" : False, 
    },

}
matriz_cocina=[[-1,-1,-1],
               [-1,0,0,-1,-1],#pared, vacio, vacio, heladera, pared
               [-1,-1,0,0,2], #pared, horno y puerta a living
               [-1,0,0,0,-1],
               [-1,-1,-1],]
objetos_cocina = [["pared","pared","pared"],
                  ["pared", "mesada", "comida perro" ,"heladera","pared"],
                  ["pared","cocina",0 ,0 ,0],
                  ["pared", "alacena", "mesada", "mesada", "pared"],
                  ["pared", "pared", "pared",]]
dicc_objetos_cocina = {
    "pared": {
        "carla": "Carla observa la pared, pensando en cómo quedaría un mural de recetas.",
        "gabriel": "Gabriel mira la pared, buscando manchas de salsa o humedad.",
        "usar": False,
        "inventario": False,
    },
    "mesada": {
        "carla": "Carla revisa la mesada, buscando utensilios para preparar algo dulce.",
        "gabriel": "Gabriel limpia la mesada para dejarla lista para cocinar.",
        "usar": True, #key mesada cocina
        "inventario": False,
    },
    "comida perro": {
        "carla": "Carla sonríe al ver el plato de Firulais, pensando si la comida será gourmet.",
        "gabriel": "Gabriel revisa si Firulais ya comió o necesita más comida.",
        "usar": True, #key comida perro cocina
        "inventario": False,
    },
    "heladera": {
        "carla": "Carla abre la heladera buscando algo fresco para un snack.",
        "gabriel": "Gabriel revisa la heladera para ver si hay suficiente proteína.",
        "usar": True, #key heladera cocina
        "inventario": False,
    },
    "cocina": {
        "carla": "Carla piensa en preparar una receta nueva en la cocina.",
        "gabriel": "Gabriel prende la hornalla para cocinar huevos.",
        "usar": True, #key cocina cocina
        "inventario": False,
    },
    "alacena": {
        "carla": "Carla revisa la alacena buscando ingredientes para una torta.",
        "gabriel": "Gabriel busca arroz y fideos en la alacena.",
        "usar": True, # key alacena cocina
        "inventario": False,
    },
    
}
dicc_objetos_heladera_cocina = {
    "Leche": {
        "carla": "Carla piensa en hacerse un licuado con la leche.",
        "gabriel": "Gabriel revisa si la leche tiene suficiente proteína.",
        "usar": True,
        "inventario": False,
    },
    "Huevos": {
        "carla": "Carla imagina una tortilla para el desayuno.",
        "gabriel": "Gabriel cuenta los huevos para ver si puede hacer omelette.",
        "usar": True,
        "inventario": True,
    },
    "Queso": {
        "carla": "Carla piensa en preparar una picada con el queso.",
        "gabriel": "Gabriel corta una feta de queso para su sándwich.",
        "usar": True,
        "inventario": True,
    },
    "Manteca": {
        "carla": "Carla busca la manteca para untar unas tostadas.",
        "gabriel": "Gabriel derrite un poco de manteca para cocinar.",
        "usar": True,
        "inventario": True,
    },
    "Jugo de naranja": {
        "carla": "Carla se sirve un vaso de jugo bien frío.",
        "gabriel": "Gabriel toma jugo para hidratarse después de entrenar.",
        "usar": True,
        "inventario": True,
    },
    "Frutas": {
        "carla": "Carla elige una manzana para una merienda saludable.",
        "gabriel": "Gabriel come una naranja para recuperar energía.",
        "usar": True,
        "inventario": True,
    },
    "Sobras de comida": {
        "carla": "Carla revisa si las sobras sirven para un almuerzo rápido.",
        "gabriel": "Gabriel calienta las sobras para no perder tiempo cocinando.",
        "usar": True,
        "inventario": False,
    },
    "Agua mineral": {
        "carla": "Carla se sirve un vaso de agua bien fría.",
        "gabriel": "Gabriel toma agua para mantenerse hidratado.",
        "usar": True,
        "inventario": True,
    },
}
acciones_generales_heladera_cocina = {
    "Leche": {
        'revisar': "Una bolsa de leche abierta.",
        'usar': "Te servís un vaso de leche.",
    },
    "Huevos": {
        'revisar': "Media docena de huevos.",
        'usar': "Usás los huevos para cocinar.",
    },
    "Queso": {
        'revisar': "Un trozo de queso cremoso.",
        'usar': "Cortás un poco de queso.",
    },
    "Manteca": {
        'revisar': "Un poco de manteca en su envoltorio.",
        'usar': "Usás la manteca para untar o cocinar.",
    },
    "Jugo de naranja": {
        'revisar': "Una botella de jugo de naranja.",
        'usar': "Te servís un vaso de jugo.",
    },
    "Frutas": {
        'revisar': "Manzanas y naranjas frescas.",
        'comer': "Comés una fruta.",
    },
    "Sobras de comida": {
        'revisar': "Un tupper con sobras de la cena de anoche.",
        'comer': "Calentás y comés las sobras.",
    },
    "Agua mineral": {
        'revisar': "Una botella de agua mineral fría.",
        'usar': "Te servís un poco de agua.",
    },
}
dicc_objetos_alacena_cocina = {
    "Aceite de oliva": {
        "carla": "Carla piensa en usar el aceite de oliva para una ensalada gourmet.",
        "gabriel": "Gabriel revisa si el aceite sirve para cocinar pollo.",
        "usar": True,
        "inventario": True,
    },
    "Sal fina": {
        "carla": "Carla agrega un poco de sal fina a su receta.",
        "gabriel": "Gabriel revisa si hay suficiente sal para sazonar.",
        "usar": True,
        "inventario": True,
    },
    "Azúcar rubia": {
        "carla": "Carla usa el azúcar rubia para endulzar su café.",
        "gabriel": "Gabriel piensa en preparar avena con azúcar rubia.",
        "usar": True,
        "inventario": True,
    },
    "Harina 000": {
        "carla": "Carla planea hacer una torta con la harina 000.",
        "gabriel": "Gabriel revisa si hay harina suficiente para panqueques.",
        "usar": True,
        "inventario": True,
    },
    "Arroz largo fino": {
        "carla": "Carla piensa en preparar una ensalada de arroz.",
        "gabriel": "Gabriel cocina arroz para acompañar el pollo.",
        "usar": True,
        "inventario": True,
    },
    "Fideos tirabuzón": {
        "carla": "Carla elige los fideos tirabuzón para una pasta rápida.",
        "gabriel": "Gabriel hierve los fideos para la cena.",
        "usar": True,
        "inventario": True,
    },
    "Lentejas secas": {
        "carla": "Carla prepara una sopa de lentejas.",
        "gabriel": "Gabriel cocina lentejas para sumar proteína.",
        "usar": True,
        "inventario": True,
    },
    "Café instantáneo": {
        "carla": "Carla se prepara un café instantáneo para la tarde.",
        "gabriel": "Gabriel toma café para despertarse.",
        "usar": True,
        "inventario": True,
    },
    "Té verde": {
        "carla": "Carla disfruta de una taza de té verde.",
        "gabriel": "Gabriel prueba el té verde aunque prefiere café.",
        "usar": True,
        "inventario": True,
    },
    "Yerba con palo": {
        "carla": "Carla prepara un mate con la yerba.",
        "gabriel": "Gabriel ceba mate para compartir.",
        "usar": True,
        "inventario": True,
    },
    "Galletitas dulces": {
        "carla": "Carla come unas galletitas dulces con su té.",
        "gabriel": "Gabriel se come unas galletitas de postre.",
        "usar": True,
        "inventario": True,
    },
    "Cacao en polvo": {
        "carla": "Carla usa el cacao en polvo para hacer chocolatada.",
        "gabriel": "Gabriel mezcla cacao en polvo con leche.",
        "usar": True,
        "inventario": True,
    },
    "Mermelada de frutilla": {
        "carla": "Carla unta mermelada de frutilla en una tostada.",
        "gabriel": "Gabriel agrega mermelada a su pan integral.",
        "usar": True,
        "inventario": True,
    },
    "Enlatados atún": {
        "carla": "Carla abre una lata de atún para una ensalada.",
        "gabriel": "Gabriel come atún directo de la lata.",
        "usar": True,
        "inventario": True,
    },
    "Especias orégano": {
        "carla": "Carla espolvorea orégano en su pizza casera.",
        "gabriel": "Gabriel usa orégano para condimentar la comida.",
        "usar": True,
        "inventario": True,
    },
    "Pan integral": {
        "carla": "Carla prepara una tostada de pan integral.",
        "gabriel": "Gabriel come pan integral con queso.",
        "usar": True,
        "inventario": True,
    },
    "Servilletas doble hoja": {
        "carla": "Carla usa una servilleta para limpiar la mesa.",
        "gabriel": "Gabriel agarra una servilleta para no ensuciarse.",
        "usar": True,
        "inventario": True,
    },
}
acciones_generales_alacena_cocina = {
    "Aceite de oliva": {
        'revisar': "Una botella de aceite de oliva, casi llena.",
        'usar': "Podés usar el aceite para cocinar.",
    },
    "Sal fina": {
        'revisar': "Un paquete de sal fina, bien cerrado.",
        'usar': "Podés usar la sal para sazonar la comida.",
    },
    "Azúcar rubia": {
        'revisar': "Un frasco con azúcar rubia.",
        'usar': "Podés usar el azúcar para endulzar.",
    },
    "Harina 000": {
        'revisar': "Un paquete de harina 000.",
        'usar': "Podés usar la harina para hacer masa.",
    },
    "Arroz largo fino": {
        'revisar': "Un paquete de arroz largo fino.",
        'usar': "Podés cocinar arroz.",
    },
    "Fideos tirabuzón": {
        'revisar': "Un paquete de fideos tirabuzón.",
        'usar': "Podés hervir los fideos.",
    },
    "Lentejas secas": {
        'revisar': "Un paquete de lentejas secas.",
        'usar': "Podés cocinar las lentejas.",
    },
    "Café instantáneo": {
        'revisar': "Un frasco de café instantáneo.",
        'usar': "Podés preparar café.",
    },
    "Té verde": {
        'revisar': "Un paquete de té verde.",
        'usar': "Podés preparar té.",
    },
    "Yerba con palo": {
        'revisar': "Un paquete de yerba con palo.",
        'usar': "Podés preparar un mate.",
    },
    "Galletitas dulces": {
        'revisar': "Un paquete de galletitas dulces.",
        'comer': "Comés unas galletitas.",
    },
    "Cacao en polvo": {
        'revisar': "Un frasco de cacao en polvo.",
        'usar': "Podés preparar chocolate.",
    },
    "Mermelada de frutilla": {
        'revisar': "Un frasco de mermelada de frutilla.",
        'usar': "Podés untar la mermelada en pan.",
    },
    "Enlatados atún": {
        'revisar': "Una lata de atún.",
        'abrir': "Abrís la lata de atún.",
    },
    "Especias orégano": {
        'revisar': "Un frasco de orégano.",
        'usar': "Podés usar el orégano para condimentar.",
    },
    "Pan integral": {
        'revisar': "Un paquete de pan integral.",
        'comer': "Comés una rebanada de pan.",
    },
    "Servilletas doble hoja": {
        'revisar': "Un paquete de servilletas doble hoja.",
        'usar': "Podés usar una servilleta.",
    },
}
matriz_baño=[[-1,-1,-1],
            [-1,-1,0,-1,-1],#pared, primera parte de la bañera, nada, inodoro, pared
            [-1,-1,-1,0,2],#pared, segunda parte bañera, lavamanos, nada, puerta a living
            [-1,-1,-1],] #pared, espejo, pared
objetos_baño = [
                ["llave ducha", "espejo", -1],
                [-1, "bañera", "lavamanos" ,0 , "inodoro", -1],
                [-1, "bañera", 0 , 0 , -1],
                [-1,2,"estante"],
                ]
dicc_objetos_baño = {
    "llave ducha": {
        "carla": "Carla revisa la llave de la ducha, pensando en un baño relajante.",
        "gabriel": "Gabriel verifica si la ducha funciona bien para después de entrenar.",
        "usar": True,
        "inventario": False,
    },
    "espejo": {
        "carla": "Carla se mira en el espejo y se arregla el pelo.",
        "gabriel": "Gabriel se mira en el espejo y se acomoda la remera.",
        "usar": False,
        "inventario": False,
    },
    "bañera": {
        "carla": "Carla sueña con un baño de burbujas.",
        "gabriel": "Gabriel piensa en usar la bañera para relajar los músculos.",
        "usar": True,
        "inventario": False,
    },
    "lavamanos": {
        "carla": "Carla se lava las manos con jabón perfumado.",
        "gabriel": "Gabriel se lava la cara para despertarse.",
        "usar": True,
        "inventario": False,
    },
    "inodoro": {
        "carla": "Carla revisa si hay papel higiénico.",
        "gabriel": "Gabriel se asegura de que el inodoro funcione.",
        "usar": True,
        "inventario": False,
    },
    "estante": {
        "carla": "Carla revisa el estante buscando cremas y perfumes.",
        "gabriel": "Gabriel busca desodorante en el estante.",
        "usar": True,
        "inventario": False,
    },
}
acciones_generales_estante_baño = {
    "Shampoo": {
        'revisar': "Una botella de shampoo casi llena.",
        'usar': "Te lavás el pelo con shampoo.",
    },
    "Acondicionador": {
        'revisar': "Una botella de acondicionador.",
        'usar': "Usás el acondicionador para suavizar el pelo.",
    },
    "Jabón": {
        'revisar': "Una pastilla de jabón perfumado.",
        'usar': "Te lavás las manos con jabón.",
    },
    "Crema hidratante": {
        'revisar': "Un pote de crema hidratante.",
        'usar': "Te ponés crema en las manos.",
    },
    "Perfume": {
        'revisar': "Un frasco de perfume.",
        'usar': "Te perfumás un poco.",
    },
    "Desodorante": {
        'revisar': "Un desodorante en aerosol.",
        'usar': "Usás el desodorante.",
    },
    "Toalla": {
        'revisar': "Una toalla limpia y suave.",
        'usar': "Te secás con la toalla.",
    },
    "Cepillo de dientes": {
        'revisar': "Un cepillo de dientes de cerdas suaves.",
        'usar': "Te lavás los dientes.",
    },
    "Pasta dental": {
        'revisar': "Un tubo de pasta dental casi vacío.",
        'usar': "Ponés pasta dental en tu cepillo y te lavás los dientes.",
    },
}
acciones_generales_baño = {
    "llave ducha": {
        'abrir': "Abrís la llave de la ducha y sale agua.",
        'cerrar': "Cerrás la llave de la ducha.",
    },
    "espejo": {
        'mirar': "Te ves reflejado en el espejo.",
        'limpiar': "Limpiás el espejo y queda reluciente.",
    },
    "bañera": {
        'llenar': "Llenás la bañera con agua caliente.",
        'vaciar': "Vaciás la bañera.",
    },
    "lavamanos": {
        'usar': "Usás el lavamanos para lavarte.",
        'revisar': "El lavamanos está limpio y tiene jabón.",
    },
    "inodoro": {
        'usar': "Usás el inodoro.",
        'revisar': "El inodoro está limpio y tiene papel.",
    },
    "estante": {
        'abrir': "Abrís el estante y ves varios productos.",
        'revisar': "Hay cremas, perfumes y otros artículos de higiene.",
        'tomar': "Podés tomar algo del estante.",
    },
}
dicc_objetos_estante_baño = {
    "Shampoo": {
        "carla": "Carla elige el shampoo con aroma a frutos rojos.",
        "gabriel": "Gabriel busca el shampoo anticaspa.",
        "usar": True,
        "inventario": True,
    },
    "Acondicionador": {
        "carla": "Carla usa el acondicionador para dejar su pelo suave.",
        "gabriel": "Gabriel no suele usar acondicionador, pero lo mira curioso.",
        "usar": True,
        "inventario": True,
    },
    "Jabón": {
        "carla": "Carla toma el jabón perfumado.",
        "gabriel": "Gabriel agarra el jabón para lavarse las manos.",
        "usar": True,
        "inventario": True,
    },
    "Crema hidratante": {
        "carla": "Carla se pone un poco de crema hidratante en las manos.",
        "gabriel": "Gabriel se pregunta si la crema sirve para después de afeitarse.",
        "usar": True,
        "inventario": True,
    },
    "Perfume": {
        "carla": "Carla se pone un poco de perfume.",
        "gabriel": "Gabriel huele el perfume y decide no usarlo.",
        "usar": True,
        "inventario": True,
    },
    "Desodorante": {
        "carla": "Carla revisa si el desodorante es antitranspirante.",
        "gabriel": "Gabriel usa el desodorante después de entrenar.",
        "usar": True,
        "inventario": True,
    },
    "Toalla": {
        "carla": "Carla toma una toalla limpia.",
        "gabriel": "Gabriel agarra una toalla para secarse.",
        "usar": True,
        "inventario": True,
    },
    "Cepillo de dientes": {
        "carla": "Carla busca su cepillo de dientes rosa.",
        "gabriel": "Gabriel revisa si su cepillo está seco.",
        "usar": True,
        "inventario": True,
    },
    "Pasta dental": {
        "carla": "Carla pone un poco de pasta dental en su cepillo.",
        "gabriel": "Gabriel revisa si queda suficiente pasta dental.",
        "usar": True,
        "inventario": True,
    },
}
matriz_cuarto_principal=[[-1,-1,-1,-1,-1],#pared del cuarto
                        [-1,-1,-1,-1,-1,-1,-1],#pared, mesa de luz, camax3, mesa de luz, pared
                        [-1,0,-1,-1,-1,0,-1],
                        [-1,0,-1,-1,-1,0,-1],
                        [-1,-1,0,0,0,0,-1],#pared, mesa de maquillaje, vacio
                        [-1,-1,-1,-1, 0,0,-1],#pared, mesa de maquillaje, zapatero, vacio y pared
                        [-1,-1,-1,2,-1],]#pared y puerta a living
objetos_cuarto_principal=[["pared","pared","pared","pared","pared","pared","pared"],#pared del cuarto
                        ["pared","mesa de luz1","cama","cama","cama","mesa de luz2","pared"],#pared, mesa de luz, camax3, mesa de luz, pared
                        ["pared",0,"cama","cama","cama",0,"pared"],
                        ["pared",0,"cama1","cama","cama2",0,"pared"],
                        ["pared","mesa",0,0,0,0,"pared"],#pared, mesa de maquillaje, vacio
                        ["pared","mesa","zapatero","zapatero", 0,0,"closet"],#pared, mesa de maquillaje, zapatero, vacio y pared
                        ["pared","pared","pared","pared",2,"pared","pared"],]#pared y puerta a living
dicc_objetos_cuarto_principal={ 
    "pared": {
        'carla': "me encanta el color de la pared, es como un verde musgo", #lo que ve Carla
       'gabriel': "una pared nomas", #lo que ve gabriel
       'usar': False, # si el objeto puede usarse
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    },
    "closet": {
        'carla': "Un poco chico el closet, y muy desordenado!", #lo que ve Carla
       'gabriel': "Que buena coleccion de camisetas de futbol!", #lo que ve gabriel
       'usar': False, # si el objeto puede usarse
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    },
    "mesa de luz1": {
        'carla': "una mesa de luz con 2 cajones, estilo nordico, del lado izquierdo de la cama", #lo que ve Carla
       'gabriel': "una mesa de luz con 2 cajones, del lado izquierdo de la cama", #lo que ve gabriel
       'usar': True, # si el objeto puede usarse
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    },
    "mesa de luz2": {
        'carla': "una mesa de luz con 2 cajones, estilo nordico, del lado derecho de la cama", #lo que ve Carla
       'gabriel': "una mesa de luz con 2 cajones, del lado derecho de la cama", #lo que ve gabriel
       'usar': True, # si el objeto puede usarse
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    }, 
    "cama": {
        'carla': "una cama queen, sin hacer, cuanto se mueve el dueño de casa eh", #lo que ve Carla
       'gabriel': "una cama grande...jajaj ni el dueño de casa hace la cama, con razon es mi amigo", #lo que ve gabriel
       'usar': False, # key, cama cuarto principal
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    },  
    "cama1": {
        'carla': "la esquina inferior izquierda de la cama... parece que hubiera algo entre el somier y el colchon", #lo que ve Carla
       'gabriel': "la esquina inferior izquierda de la cama... parece que hubiera algo entre la cama y el colchon", #lo que ve gabriel
       'usar': True, # key, cama1 cuarto principal
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    }, 
    "cama2": {
        'carla': "la esquina inferior derecha de la cama... parece que hubiera algo abajo de la cama... un monstruo? jsjs", #lo que ve Carla
       'gabriel': "la esquina inferior derecha da de la cama... parece que hubiera algo abajo de la cama...", #lo que ve gabriel
       'usar': True, # key, cama2 cuarto principal
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    }, 
    "mesa": {
        'carla': "Que desorden, una mesa llena de cosas", #lo que ve Carla
       'gabriel': "Una mesa llena de boludeces", #lo que ve gabriel
       'usar': True, # key, mesa cuarto principal
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    }, 
    "zapatero": {
        'carla': "Un zapatero lleno de botines", #lo que ve Carla
       'gabriel': "EUUU altas llantas", #lo que ve gabriel
       'usar': False, # key, mesa cuarto principal
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    }, 
    
}
matriz_oficina=[[-1,-1,-1],
                [-1,-1,-1,-1,-1],#paredes y escritorio
                [-1,0,-1,0,-1], #paredes y silla
                [-1,0,0,-1,-1],#paredes y biblioteca 
                [-1,0,0,-1,2],#paredes y biblioteca con puerta oculta
                [-1,2,-1],]
objetos_oficina=[[-1,-1,-1],
                [-1,-1,"escritorio",-1,-1],
                [-1,0,"silla",0,-1], 
                ["cuadro",0,0,-1,"biblioteca"],
                [-1,0,0,-1,"biblioteca"],
                [-1,2,-1],]
dicc_objetos_oficina = {
    "pared": {
        "carla": "Que horrible color tiene la pared",
        "gabriel": "la pared tiene manchas de humedad...",
        "usar": False,
        "inventario": False,
    },
    "escritorio": {
        "carla": "Este escritorio es parecido al de papá",
        "gabriel": "Podría poner una PC Gamer y viciar toda la noche",
        "usar": True,
        "inventario": False,
    },
    "silla": {
        "carla": "una silla cómoda, ideal para hacer vivos en tiktok mientras me maquillo",
        "gabriel": "una silla giratoria con ruedas... puedo usarla para moverme de un lado a otro",
        "usar": True,
        "inventario": False,
    },
    "cuadro": {
        "carla": "un cuadro abstracto que no entiendo pero me gusta. Creo que podría pintar uno igual",
        "gabriel": "una pintura moderna, probablemente sea muy cara",
        "usar": False,
        "inventario": False,
    },
    "biblioteca": {
        "carla": "¿No hay revistas de moda o maquillaje en esta biblioteca?",
        "gabriel": "No veo ningún comic o manga",
        "usar": True,
        "inventario": False,
    },
    "puerta oculta": {
        "carla": "parece una biblioteca... pero hay algo raro en ella",
        "gabriel": "hay una rendija, como si se pudiera abrir...",
        "usar": True,
        "inventario": False,
    }
}
matriz_patio=[[-1,-1,-1,-1],
                      [-1,-1,-1,-1,-1,-1],
                      [2,0,0,-1,0,-1],
                      [-1,0,-1,0,0,-1],
                      [-1,0,0,0,-1,-1],
                      [-1,-1,-1,-1],]
objetos_patio=[["enredadera","pared","pared","pared"],
                      ["enredadera","cucha perro","arbol","pozo","cobertizo", "pared"],
                      ["puerta",0,"lapida1","arbol",0,"pared"],
                      ["placa","banco","pozo","lapida2",0,"pared"],
                      ["enredadera","lapida3",0,0,"pozo","pared"],
                      ["enredadera","enredadera","pared","pared"],]
dicc_objetos_patio={ 
    "enredadera": {
        'carla': "que linda enredadera🌿🌿, me encantaria que en mi casa haya una asi", #lo que ve Carla
       'gabriel': "una planta que cubre la pared🌿🌿", #lo que ve gabriel
       'usar': False, # si el objeto puede usarse
       'inventario': False, #si el objeto puede ser guardado en inventario o no  
    },
    "pared": {
        'carla': "ay alguien deberia darle una mano de pintura a esta pared",
       'gabriel': "una pared descascarada",
       'usar': False, 
       'inventario': False,
    }, 
    "cucha perro": {
        'carla': "aww la casita de firu",
       'gabriel': "alta home la de firu",
       'usar': False, 
       'inventario': False,
    }, 
    "arbol":{
        'carla': "un arbol de limones frescos🌲🍋",
        'gabriel': "un arbol de limones frescos🌲🍋",
        'usar': False,
        'inventario':False, 
    },
    "pozo": {
        'carla': "una gran montaña de tierra... parece que alguien planto algo hace poco.",
        'gabriel': "un monticulo de tierra. Parece que alguien enterro algo hace poco tiempo.",
        'usar': False,
        'inventario':False, 
    },
    "cobertizo": {
        'carla': "un cobertizo. Parece cerrado pero no tiene manija... que raro ", #adentro del cobertizo hay una caja con un candado numerico
        'gabriel': "un cobertizo. No tiene manija, pero deberia poder abrirse ",
        'usar': False, #cuando se accione la placa, se cambiara a true y podra entrar
        'inventario':False, 
    },
    "lapida1": {
        'carla': "Una lapida? Muy creepy para un patio... A ver que dice... 🪦Ruben Grabal 29/08/1934-18/10/2009 \"Amado padre, marido y segundo lugar de la mejor pizza del mundo mundial\" ", 
        'gabriel': "Eso es una lapida?? 😳😳,🪦Ruben Grabal 29/08/1934-18/10/2009 \" Amado padre, marido y segundo lugar de la mejor pizza del mundo mundial\" ",
        'usar': False,
        'inventario':False, 
    },
    "placa": {
        'carla': "Que es eso? Detras de la enredadera? ", 
        'gabriel': "Hay algo detras de la enredadera? ",
        'usar': True, #placa patio es el key que hay que usar
        'inventario':False, 
    },
    "banco": {
        'carla': "Un banco para poder sentarme un rato y mirar todo el patio ", 
        'gabriel': "Un banco para sentarse y mirar todo el patio",
        'usar': True, #banco patio es el key que hay que usar
        'inventario':False, 
    },
    "lapida2": {
        'carla': "Otra lapida?? A ver que dice esta...🪦 Maria Dolores Grimaldi de Grabal 7/10/1939-25/06/2014 \" Amada madre y ganadora de la mejor pizza del mundo mundial \" ", 
        'gabriel': "Otra lapida?? A ver que dice...🪦 Maria Dolores Grimaldi de Grabal 7/10/1939-25/06/2014 \" Amada madre y ganadora de la mejor pizza del mundo mundial \" ", 
        'usar': False,
        'inventario':False, 
    },
    "lapida3": {
        'carla': "Otra lapida mas? Pero que es esto? El cementerio de Chacarita? A ver que dice esta...🪦 Pedro Grabal 06/10/1987- 12/05/2007 \"Amado hermano y catador de pizzas \" ", 
        'gabriel': "Otra lapida mas? Esto no parece muy legal que digamos... A ver que dice...🪦 Pedro Grabal 06/10/1987- 12/05/2007 \"Amado hermano y catador de pizzas \" ", 
        'usar': False,
        'inventario':False, 
    },
    
}
diccionario_matrices= {
    "living": matriz_living,
    "objetos living": objetos_living,
    "cocina": matriz_cocina,
    "objetos cocina": objetos_cocina,
    "baño": matriz_baño,
    "objetos baños" : objetos_baño,
    "cuarto principal": matriz_cuarto_principal,
    "objetos cuarto principal": objetos_cuarto_principal,
    "oficina": matriz_oficina,
    "objetos oficina": objetos_oficina,
    "patio": matriz_patio,
    "objetos patio": objetos_patio,
}
diccionario_puertas={
    "puertas living" : puertas_living,
    "puertas baño" : puerta_baño,
    "puertas cocina" : puerta_cocina,
    "puertas patio" : puerta_patio,
    "puertas cuarto principal" : puertas_cuarto_principal,
    "puertas oficina" : puertas_oficina, 
}
diccionario_objetos={
    "living": dicc_objetos_living,
    "patio": dicc_objetos_patio,
    "baño": dicc_objetos_baño,
    "cocina":dicc_objetos_cocina ,
    "cuarto principal": dicc_objetos_cuarto_principal, 
    "oficina": dicc_objetos_oficina,
}
diccionario_accciones_globales={
    ("placa patio"): {
        'mover enredadera': "hay una placa detras de la enredadera",
        'leer': "\"Gracias por siempre empujarme a ser mejor\"",
        'empujar': "La placa se metio para dentro de la pared... y ese ruido? Parece como que se haya abierto una puerta",
        'tirar': "No puedo tirar de la placa, esta atornillada a la pared"
    },
    ("banco patio"): {
        'sentarse': "Al fin puedo descansar un poco",
        'apreciar la vista sentado': "Wow, la enredadera si que esta crecida, lo mismo como los 2 arboles de limones, hay 3 lapidas y por algun motivo 3 monticulos de tierra nuevos...",
        'disociar': "...",
    },
    ("llaves atras puerta living"): {
        'guardar en inventario': inventario.append("llaves living"),
        'ver': "una llave roja, una electronica y una dorada", 
    },
    ("escritorio oficina"): {
        'abrir cajón': "El cajón está vacío... o eso parece.",
        'revisar': "Hay mucha basura y cosas viejas guardadas.",
    },
    ("silla oficina"): {
        'sentarse': "Girás un poco.",
        'moverse': "Te deslizás por la oficina como si fuera una pista de hielo.",
        'guardar en inventario': "No podés llevar la silla de la casa de tu amigo.",
        },
    ("cuadro oficina"): {
        'mirar': "Es un cuadro abstracto, con formas que parecen moverse si lo mirás mucho tiempo.",
        'tocar': "La pintura está seca, pero hay algo raro en el marco...",
        },
    ("biblioteca oficina"): {
        'revisar libros': "Muchos libros de derecho, historia y... ¿una novela romántica?",
        'empujar': "¡Click! Algo se movió detrás...",
        },
    ("puerta oculta oficina"): {
        'abrir': "La biblioteca se corre revelando una puerta secreta.",
        'entrar': "Pasás por la puerta oculta hacia otra habitación...",
        },
    ("pared oficina"): {
        'golpear': "Suena hueco en algunas partes.",
        'mirar': "Pared blanca con manchas de humedad.",
        },
    ("mesa cuarto principal"): {
        "ver": "hay 3 anteojos de Tommy, 6 relojes de marca y 5 figuritas del mundial"        
        },
    ("cama2 cuarto principal"): {
        "ver": "la esquina de la cama",    
        "mirar abajo de la cama": "esta una de las hojas del TP!",
        },
    ("cama1 cuarto principal"): {
        "ver": "la esquina de la cama",   
        "levantar el colchon": "uyy que pesado... Que es eso?? Una hoja con estos dibujos? ⌚⚽🕶",
        },
    ("mesa de luz1 cuarto principal"): {
        "abrir primer cajon": "A ver que hay... NONONONOOON aca no hay nada importante!!!",      
        "abrir segundo cajon": "algunos comics de Batman y unas revistas viejas",
        },
    ("mesa de luz2 cuarto principal"): {
        "abrir primer cajon": "Que miedo abrir los cajones de la mesa de luz de alguien... Ah esta bien, solo hay unas flores y un rosario",      
        "abrir segundo cajon": "Una caja fuerte... que raro, tiene 3 numeros",
        },
    ("mesada cocina"): {
        'revisar': "Hay algunos utensilios y migas de pan sobre la mesada.",
        'limpiar': "Limpiás la mesada, ahora está reluciente.",
    },
    ("comida perro cocina"): {
        'revisar': "Un plato con comida para Firulais.",
        'servir': "Le servís comida a Firulais. ¡Está feliz!",
    },
    ("heladera cocina"): {
        'abrir': "Abrís la heladera. Hay algunas cosas para picar.",
        'revisar': "Ves leche, huevos y un poco de queso.",
    },
    ("cocina cocina "): {
        'prender': "Encendés la hornalla, lista para cocinar.",
        'revisar': "La cocina está limpia y lista para usar.",
    },
    ("alacena cocina"): {
        'abrir': "Abrís la alacena y ves varios alimentos.",
        'revisar': "Hay paquetes de arroz, fideos, azúcar y más.",
        'tomar': "Podés tomar algo de la alacena.",
    },
    ("llave ducha baño"): {
        'abrir': "Abrís la llave de la ducha y sale agua.",
        'cerrar': "Cerrás la llave de la ducha.",
    },
    ("espejo baño"): {
        'mirar': "Te ves reflejado en el espejo.",
        'limpiar': "Limpiás el espejo y queda reluciente.",
    },
    ("bañera baño"): {
        'llenar': "Llenás la bañera con agua caliente.",
        'vaciar': "Vaciás la bañera.",
    },
    ("lavamanos baño"): {
        'usar': "Usás el lavamanos para lavarte.",
        'revisar': "El lavamanos está limpio y tiene jabón.",
    },
    ("inodoro baño"): {
        'usar': "Usás el inodoro.",
        'revisar': "El inodoro está limpio y tiene papel.",
    },
    ("estante baño"): {
        'abrir': "Abrís el estante y ves varios productos.",
        'revisar': "Hay cremas, perfumes y otros artículos de higiene.",
        'tomar': "Podés tomar algo del estante.",
    },
}

"""--------------------------------------------------------------------------------------------------------------------------"""    
#main 

personaje=Eleccion_Personaje()
ubicacion_personaje=Inicio_Juego(personaje, inventario )
Living(inventario, ubicacion_personaje,personaje)









