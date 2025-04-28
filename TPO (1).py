import emoji
from functools import reduce
"""El diccionario de puertas, se va a leer con el primer elemento siendo las coordenadas de la puerta, y la ubicacion actual. """   
puertas_living={
    #puertas desde el living
   (0,2): {
       'lugar de la puerta': "living",
       'habitacion destino': 'cuarto principal',
       "coordenada destino": (5,4),
       "estado puerta": "abierta",
    },
    (7,2) : {
        'lugar de la puerta':"living",
        "habitacion destino": "afuera" 
    },
    (0,4): {
       'lugar de la puerta':"living",
       'habitacion destino': 'oficina',
       "coordenada destino": (4,2),
       "estado puerta": "abierta",
    },
    (2,0): {
       'lugar de la puerta':"living",
       'habitacion destino': 'baño',
       "coordenada destino": (2,3),
       "estado puerta": "abierta",
    },
    (4,0): {
       'lugar de la puerta':"living",
       'habitacion destino': 'cocina',
       "coordenada destino": (2,3),
       "estado puerta": "abierta",
    },
    (3,7): {
       'lugar de la puerta':"living",
       'habitacion destino': 'cuarto_extra',
       "coordenada destino": (2,1),
       "estado_puerta": "abierta",
    }
}
puertas_cuarto_principal= {
    #puertas desde cuarto principal
    (6,4): {
     ' ': "cuarto principal",
       ' ': 'living',
       "coordenada destino": (1,2),
       "estado puerta": "abierta",
        },
    (5,6): {
     ' ': "cuarto principal",
       ' ': 'closet',
       "coordenada destino": (2,1),
       "estado puerta": "abierta",
        }
}
puerta_closet= {#puertas desde el closet 
    (2,0):{
     ' ': "closet",
       ' ': 'cuarto principal',
       "coordenada destino": (5,5),
       "estado puerta": "abierta",
    }}
puerta_baño={#puertas desde el baño 
    (2,4): {
     ' ': "baño",
       ' ': 'living',
       "coordenada destino": (2,1),
       "estado puerta": "abierta",
    }}
puerta_cocina={#puertas desde la cocina 
    (2,4): {
     ' ': "cocina",
       ' ': 'living',
       "coordenada destino": (4,1),
       "estado puerta": "abierta",
    }}
puertas_oficina={#puertas desde la oficina 
    (5,2): {
     ' ': "oficina",
       ' ': 'living',
       "coordenada destino": (1,4),
       "estado puerta": "abierta",
    },
    (4,4): {
     ' ': "oficina",
       ' ': 'cuarto oculto',
       "coordenada destino": (3,1),
       "estado puerta": "oculta",
    }}
puerta_cuarto_oculto={#puerta desde el cuarto oculto
    (3,0): {
     ' ': "cuarto oculto",
       ' ': 'oficina',
       "coordenada destino": (4,3),
       "estado puerta": "oculta",
    }}
puerta_cuarto_extra={#puerta desde cuarto extra
    (2,0): {
       'lugar de la puerta':"cuarto extra",
       'habitacion destino': 'living',
       "coordenada destino": (3,6),
       "estado puerta": "abierta",
}}
"""Las matrices de objetos, van a indicar que hay en cada uno y cada uno tiene sus acciones especificas
    Si hay 0 es porque no hay nada, si hay algun objeto, se escribira tal objeto y sus acciones. Las puertas no cuentan como objetos.
    Puede haber objetos en puertas y paredes (afiches, cuadros, estantes)"""

"""La matriz de cada habitacion, tiene su forma arriba. Los cuadrados negros son las paredes, los blancos el piso. Si la matriz tiene 
un 1 es donde esta parado el jugador. Va a haber otra matriz con los objetos que tiene cada "celda". Si hay 0 es lugar donde puede caminar.
Si hay -1 esta prohibido caminar (ya sea porque hay una pared o un mueble), si hay un 2 es una puerta"""
# Definición de las matrices de objetos y habitaciones
matriz_living=[[-1,2,-1,-1,2,-1],
               [-1,0,0,0,0,0,-1],
               [2,0,0,-1,-1,-1,0,-1],
               [-1,0,0,-1,-1,-1,0,2],
               [2,0,0,0,0,0,0,-1],
               [-1,0,0,0,-1,-1,0,-1],
               [-1,-1,0,0,0,0,0,-1],
               [-1,2,-1,-1,-1,-1],]
objetos_living=[[0,0,"cuadro",0,"En reunion, no entrar!",0],
                [0,0,0,0,0,0,"cucha perro",0],
                ["chapa toilette",0,"alfombra","silla","mesa comedor","silla",0,0],
                [0,0,"alfombra","silla","mesa comedor","silla",0,"cartel prohibido"],
                ["Aca se hacen cosas ricas",0,"alfombra", 0,0,0,0,0],
                ["perchero",0,0,0,"sillon","sillon",0,"cuadro"],
                [0,"paraguero",0,0,0,0,0,0],
                [0,"llaves atras puerta",0,"television","television",0],]
matriz_cocina=[[-1,-1,-1],
               [-1,0,0,-1,-1],#pared, vacio, vacio, heladera, pared
               [-1,-1,0,0,2], #pared, horno y puerta a living
               [-1,0,0,0,-1],
               [-1,-1,-1],]
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
matriz_cuarto_principal=[[-1,-1,-1,-1,-1],#pared del cuarto
                        [-1,-1,-1,-1,-1,-1,-1],#pared, mesa de luz, camax3, mesa de luz, pared
                        [-1,0,-1,-1,-1,0,-1],
                        [-1,0,-1,-1,-1,0,-1],
                        [-1,-1,0,0,0,0,-1],#pared, mesa de maquillaje, vacio
                        [-1,-1,-1,-1, 0,0,2],#pared, mesa de maquillaje, zapatero, vacio y puerta a closet
                        [-1,-1,-1,2,-1],]#pared y puerta a living
matriz_closet=[[-1,],
               [-1,0,-1],
               [2,0,-1],
               [-1],]
matriz_oficina=[[-1,-1,-1],
                [-1,-1,-1,-1,-1],#paredes y escritorio
                [-1,0,-1,0,-1], #paredes y silla
                [-1,0,0,-1,-1],#paredes y biblioteca 
                [-1,0,0,-1,2],#paredes y biblioteca con puerta oculta
                [-1,2,-1],]
matriz_cuarto_oculto=[[-1,-1,-1,-1], #lo dejo vacio porque no se me ocurre que poner
                      [-1,0,0,0,0,-1],
                      [-1,0,0,0,0,-1],
                      [2,0,0,0,0,-1],
                      [-1,0,0,0,0,-1],
                      [-1,-1,-1,-1],]
matriz_cuarto_extra=[[-1,-1,-1],
                    [-1,0,-1,-1,-1],#paredes y ropero 
                    [2,0,0,0,-1],#puerta, , pared 
                    [-1,0,0,0,-1],
                    [-1,-1,-1,-1,-1],]#paredes, cama
objetos_cocina = [[-1,-1,-1],
                  ["ventana", "mesada", "comida perro" ,"heladera",-1],
                  [-1,"cocina",0 ,0 ,2],
                  [-1, "alacena", "mesada", "mesada", -1],
                  [-1, -1, -1,],]
diccionario_matrices= {
    "living": matriz_living,
    "objetos living": objetos_living,
    "cocina": matriz_cocina,
    "baño": matriz_baño,
    "objetos baños" : objetos_baño,
    "cuarto principal": matriz_cuarto_principal,
    "closet": matriz_closet,
    "oficina": matriz_oficina,
    "cuarto oculto": matriz_cuarto_oculto,
    "cuarto extra": matriz_cuarto_extra,
    "objetos cocina" :objetos_cocina,
}
diccionario_puertas={
    "puertas living" : puertas_living,
    "puertas closet" : puerta_closet,
    "puertas baño" : puerta_baño,
    "puertas cocina" : puerta_cocina,
    "puertas cuarto extra" : puerta_cuarto_extra,
    "puertas cuarto oculto" : puerta_cuarto_oculto,
    "puertas cuarto principal" : puertas_cuarto_principal,
    "puertas oficina" : puertas_oficina, 
}
def Eleccion_Personaje():
    print(emoji.emojize(":woman:Carla: Influencer en como balancear la vida con el estudio (esta reprobando todo)"))
    print(emoji.emojize(":man: Gabriel: Gymbro obsesionado con barritas de proteina"))
    print(emoji.emojize(":dog_face: Firulais: Guau Guau Guau"))
    eleccion=input("Elige tu personaje: ").lower()
    while ((eleccion!="carla") and (eleccion!="gabriel") and (eleccion!="firulais")):
        print("No vale inventar personajes!!!")
        eleccion=input("Elige tu personaje: ").lower()
    if eleccion=='firulais':
        eligio_perro=input("Estas seguro que lo queres a firu? Si/No").lower()
        while eligio_perro=='si':
            print("Guau guau Guau")
            eligio_perro=input("Estas seguro que lo queres a firu? Si/No").lower()
        print(emoji.emojize("Sera re bueno Firu, pero no me parece la mejor idea para un juego como este. Por sus esfuerzos igual le damos un :bone:"))
        print("Guau")
        print("De nada, Firu. Ahora si, elegi a tu personaje: ")
        print(emoji.emojize(":woman:Carla: Influencer en como balancear la vida con el estudio (esta reprobando todo)"))
        print(emoji.emojize(":man: Gabriel: Gymbro obsesionado con barritas de proteina"))
        eleccion=input("Elige tu personaje: ").lower()
    return eleccion

def Inicio_Juego(personaje, inventario):
    print (emoji.emojize("Mañana tengo que entregar el trabajo final de Programacion I y Edesur hizo una de las suyas mientras tenia el Word abierto y sin  el autoguardado."
    "Por suerte, mi amigo ya lo había imprimido (impreso o imprimido? A ver que dice la RAE… Ah cierto, no tengo WIFI:crying_face:).", language='alias'))
    print ("Cuando llego a la casa de mi amigo, me doy cuenta que el tambien esta sin luz")
    print (emoji.emojize(
            """Despues de 6 pisos por escalera, llego a su departamento\n,
            1) Toco la puerta:raised_fist_light_skin_tone: \n
            2) Toco el timbre:bell: \n
            3)Abro la puerta:door:"""))
    opcion=int(input("¿Que opcion eliges?\n"))
    while opcion<0 and opcion>4:
        print("No vale inventar opciones")
        print (emoji.emojize(
            """Despues de 6 pisos por escalera, llego a su departamento\n,
            1) Toco la puerta:raised_fist_light_skin_tone: \n
            2) Toco el timbre:bell: \n
            3)Abro la puerta:door:"""))
        opcion=int(input("¿Que opcion eliges?\n"))
    if(opcion==1 or opcion==2):
        print("GUAUUUUUUUUU")
        print("Guau Guau Guau *sonido de rasqueteo en la puerta*")
        print("Este perro aprendio a abrir la puerta????")
    else: 
        print("¿Como van a dejar la puerta abierta? ¿Creen que viven en una sitcom?")
    matriz_living[6][2]=1
    return 

def Afuera():
    #funcion por si se abre la puerta al exterior
    eleccion= input("Aun no has terminado, ¿Seguro que quieres irte? Si/No").lower()
    while eleccion!='no' and eleccion!= 'si':
        print("Escribiste cualquiera, escribi bien")
        eleccion= input("Aun no has terminado, ¿Seguro que quieres irte? Si/No").lower()
    if eleccion=='si':
        exit()
    else:
        return
    
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

def Living (personaje, inventario):
    nombre_habitacion=str("living")
    print(f"\nEstás en el {nombre_habitacion}. Observas alrededor...")
    Opciones_Control_de_Personaje(personaje,inventario,nombre_habitacion)
    
def Objetos_Cercanos_interactivos(inventario, nombre_habitacion):
    
    matriz_habitacion=diccionario_matrices[nombre_habitacion]
    objetos_interactivos = []
    objetos_habitacion=diccionario_matrices["objetos "+nombre_habitacion]
    
    ubicacion_actual,coordenadas,direcciones=Ubicacion_Actual_Personaje(matriz_habitacion)
    fila_jugador,columna_jugador= ubicacion_actual
    adyacentes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for df, dc in adyacentes:
        nueva_fila = fila_jugador + df
        nueva_columna = columna_jugador + dc

        if 0 <= nueva_fila < len(matriz_habitacion) and 0 <= nueva_columna < len(matriz_habitacion[nueva_fila]):
            if matriz_habitacion[nueva_fila][nueva_columna] != -1: # No es una pared
                if 0 <= nueva_fila < len(objetos_habitacion) and 0 <= nueva_columna < len(objetos_habitacion[nueva_fila]):
                    objeto = objetos_habitacion[nueva_fila][nueva_columna]
                    if objeto != 0:
                        objetos_interactivos.append(((nueva_fila, nueva_columna), objeto))

    if objetos_interactivos:
        print("\nObjetos cercanos con los que puedes interactuar:")
        for i, (coordenadas, nombre_objeto) in enumerate(objetos_interactivos):
            print(f"{i+1}. {nombre_objeto} (en fila: {coordenadas[0]}, columna: {coordenadas[1]})")
        print("Ver Objeto || Agarrar Objeto")
        accion=input (">").lower()
        if "ver objeto" in accion or "agarrar objeto" in accion:
            try:
                indice_objeto = int(input("Elige el número del objeto: ")) - 1
                if 0 <= indice_objeto < len(objetos_interactivos):
                    coordenadas_objeto, nombre_objeto = objetos_interactivos[indice_objeto]
                    if "ver" in accion:
                        VerObjeto(personaje, nombre_objeto)
                    elif "agarrar" in accion:
                        AgarrarObjeto(personaje, nombre_objeto, inventario, coordenadas_objeto, objetos_habitacion)
                else:
                    print("Número de objeto inválido.")
            except ValueError:
                print("Por favor, ingresa un número.")
        elif accion == "mover":
            Mover(matriz_habitacion)
            # Después de mover, la función Living debería ser llamada de nuevo
            Living(personaje, inventario, matriz_habitacion, objetos_habitacion, nombre_habitacion)
        elif "inventario" in accion:
            print("Tu inventario:", inventario)
        elif "usar" in accion:
            objeto_a_usar = input("¿Qué objeto del inventario quieres usar? ").lower()
            UsarObjeto(personaje, objeto_a_usar, inventario, matriz_habitacion, objetos_habitacion)
        else:
            print("Acción no reconocida.")
    else:
        print("No hay objetos interesantes cerca.")
    Opciones_Control_de_Personaje(personaje, inventario, nombre_habitacion)

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

def Inventario(inventario):
    for objeto in inventario:
        print(objeto)
    return 
    
#en todo esta escrito como baño pero por la ñ escribimos toilette
def Toilette(personaje, inventario, matriz_habitacion, objetos_habitacion):
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
                estante_lista[seleccion - 1] = (None, None)  # Llenar el espacio con vacío
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
        print("Puertas adyacentes:", adyacentes_con_puertas)
#eleccion de movimiento
    movimiento_elegido=input("¿Para donde te quieres mover?").lower()
    while(movimiento_elegido not in movimientos_posibles) and (movimiento_elegido not in adyacentes_con_puertas):
        print ("Movimiento invalido")
        movimiento_elegido=input("¿Para donde te quieres mover?").lower()
    habitacion_actual[fila_jugador][col_jugador]=0
    if movimiento_elegido=='w':
        if habitacion_actual[fila_jugador-1][col_jugador]==2:
            destino=Puertas((fila_jugador)-1,col_jugador, nombre_habitacion)
            Cambio_de_Habitacion(destino)
        habitacion_actual[fila_jugador-1][col_jugador]=1
    elif movimiento_elegido=='s':
        if habitacion_actual[fila_jugador+1][col_jugador]==2:
            destino=Puertas((fila_jugador)+1,col_jugador, nombre_habitacion)
            Cambio_de_Habitacion(destino)
        habitacion_actual[fila_jugador+1][col_jugador]=1
    elif movimiento_elegido=='a':
        if habitacion_actual[fila_jugador][col_jugador-1]==2:
            destino=Puertas(fila_jugador,(col_jugador)-1, nombre_habitacion)
            Cambio_de_Habitacion(destino)
        habitacion_actual[fila_jugador][col_jugador-1]=1
    elif movimiento_elegido=='d':
        if habitacion_actual[fila_jugador][col_jugador+1]==2:
            destino=Puertas(fila_jugador,(col_jugador)+1, nombre_habitacion)
            Cambio_de_Habitacion(destino)
        habitacion_actual[fila_jugador][col_jugador+1]=1
    return

def Cambio_de_Habitacion(destino):
    """Utiliza informacion del string destino para poder encontrar la habitacion a la que tiene que ir segun el diccionario de matrices y de puertas"""

    if destino=="cocina":
        Cocina()
    elif destino=="baño":
        Toilette()
    elif destino=="living":
        Living()
    return destino

def Puertas(fila_puerta,col_puerta, nombre_habitacion):
   coordenadas_puerta=(fila_puerta,col_puerta)
   habitacion_puerta=(diccionario_puertas["puertas "+ nombre_habitacion])
   info_habitacion=habitacion_puerta[coordenadas_puerta]
   habitacion_destino=info_habitacion["habitacion destino"]
   matriz_destino = diccionario_matrices[habitacion_destino]

   habitacion_actual=diccionario_matrices[nombre_habitacion]
   for fila in range(len(habitacion_actual)):
    for col in range(len(habitacion_actual[fila])):
        if habitacion_actual[fila][col] == 1:
            habitacion_actual[fila][col] = 0
   coordenadas_destino=info_habitacion["coordenada destino"]
   fila_destino,col_destino=coordenadas_destino
   matriz_destino[fila_destino][col_destino]=1
   nombre_habitacion=str(habitacion_destino)
   return nombre_habitacion
   
def VerObjeto(personaje, nombre_habitacion, inventario):
    for objeto in inventario:
        print(objeto)
    nombre_objeto=input("Que objeto quieres mirar?").lower
    while nombre_objeto not in inventario:
        print("ese objeto no esta en la lista")
        nombre_objeto=input("Que objeto quieres mirar?").lower
    
    #funcion para poder ver cada objeto en el juego
    print(f"\n{personaje} está mirando {nombre_objeto}.")
    #Esto es temporal hasta ver diccionarios!
    if personaje == "carla":
        if nombre_objeto == "cuadro":
            print("Carla analiza el cuadro buscando detalles estéticos y si podría ser un buen fondo para sus fotos.")
        elif nombre_objeto == "cucha perro":
            print("Carla se acerca a la cucha, pensando si Firulais tendrá algún secreto de belleza canino.")
        elif nombre_objeto == "chapa toilette":
            print("Carla piensa: 'Una chapa... quizás tenga un estilo vintage interesante para una historia de Instagram.'")
        elif nombre_objeto == "alfombra":
            print(f"Carla mira la alfombra, pensando en si combina con la decoración.")
        elif nombre_objeto == "silla":
            print(f"Carla evalúa si la silla es cómoda para tomarse una selfie.")
        elif nombre_objeto == "mesa comedor":
            print(f"Carla se pregunta si la mesa sería un buen lugar para un unboxing.")
        elif nombre_objeto == "cartel prohibido":
            print("Carla sonríe de forma traviesa: 'Los carteles están para romperse, ¿no?'")
        elif nombre_objeto == "Aca se hacen cosas ricas":
            print("Carla piensa: 'Mmm, quizás encuentre algún snack delicioso para una pausa en su ajetreada vida.'")
        elif nombre_objeto == "perchero":
            print("Carla revisa las prendas, buscando inspiración para su próximo outfit.")
        elif nombre_objeto == "sillon":
            print("Carla prueba el sillón, pensando en la foto perfecta para promocionar la comodidad.")
        elif nombre_objeto == "paraguero":
            print("Carla mira los paraguas, pensando si alguno podría ser un accesorio de moda inesperado.")
        elif nombre_objeto == "llaves atras puerta":
            print("Carla examina el llavero buscando alguna llave que parezca importante o tenga un diseño interesante.")
        elif nombre_objeto == "television":
            print("Carla mira la televisión apagada, pensando en qué serie estará de moda.")
    elif personaje == "gabriel":
        if nombre_objeto == "cuadro":
            print("Gabriel mira el cuadro sin mucho interés, pensando en si tendrá suficientes calorías para su próxima rutina.")
        elif nombre_objeto == "cucha perro":
            print("Gabriel revisa la cucha por si acaso Firulais escondió alguna barrita de proteína.")
        elif nombre_objeto == "chapa toilette":
            print("Gabriel ignora la chapa, enfocado en encontrar algo más útil.")
        elif nombre_objeto == "alfombra":
            print("Gabriel patea la alfombra ligeramente, sin encontrar nada.")
        elif nombre_objeto == "silla":
            print("Gabriel prueba la firmeza de la silla.")
        elif nombre_objeto == "mesa comedor":
            print("Gabriel se pregunta si la mesa será lo suficientemente resistente para apoyar pesas.")
        elif nombre_objeto == "cartel prohibido":
            print("Gabriel asiente: 'Reglas son reglas, mejor no pasar.'")
        elif nombre_objeto == "Aca se hacen cosas ricas":
            print("Gabriel olfatea el aire: '¿Proteína casera?'")
        elif nombre_objeto == "perchero":
            print("Gabriel mira el perchero, buscando alguna toalla para secarse el sudor.")
        elif nombre_objeto == "sillon":
            print("Gabriel se sienta brevemente, evaluando si el sillón ofrece buen soporte lumbar.")
        elif nombre_objeto == "paraguero":
            print("Gabriel mira los paraguas, pensando si alguno podría servir como improvisada barra de dominadas.")
        elif nombre_objeto == "llaves atras puerta":
            print("Gabriel mira las llaves sin darle mucha importancia.")
        elif nombre_objeto == "television":
            print("Gabriel mira la televisión apagada, pensando en qué canal pasarán competencias de fuerza.")
    return

def AgarrarObjeto(personaje, nombre_objeto, inventario, coordenadas_objeto, objetos_habitacion):
    print(f"\n{personaje} intenta agarrar {nombre_objeto}.")
    if nombre_objeto == "chapa toilette":
        print(f"{personaje} toma la chapa y la guarda en su inventario.")
        inventario.append(nombre_objeto)
        objetos_habitacion[coordenadas_objeto[0]][coordenadas_objeto[1]] = 0 # El objeto desaparece de la habitación
    elif nombre_objeto == "alfombra":
        if personaje == "gabriel":
            print("Gabriel intenta levantar la alfombra con esfuerzo, pero no encuentra nada interesante debajo.")
        elif personaje == "carla":
            print("Carla levanta la alfombra con cuidado, revisando si hay alguna pista oculta.")
            # agregar lógica para encontrar algo debajo de la alfombra según el personaje
    elif nombre_objeto == "llaves atras puerta":
        print(f"{personaje} desengancha las llaves.")
        inventario.append(nombre_objeto)
        objetos_habitacion[coordenadas_objeto[0]][coordenadas_objeto[1]] = 0
    # Agrega más lógica para otros objetos que se pueden agarrar y cómo afecta a cada personaje

def UsarObjeto(personaje, inventario):
    Inventario(inventario)
    print("Que objeto quieres usar?")
    objeto_a_usar=input(">").lower()
    print(f"\n{personaje} intenta usar {objeto_a_usar}.")
    if objeto_a_usar in inventario:
        if objeto_a_usar == "chapa toilette":
            print(f"{personaje} se pregunta para qué podría servir esta chapa...")
            # agregar lógica específica para usar la chapa en algún lugar
        elif objeto_a_usar == "llaves atras puerta":
            print("¿Dónde intentas usar estas llaves?")
            # lógica para intentar usar las llaves en puertas u otros objetos
    else:
        print("No tienes ese objeto en tu inventario.")

def Mensajear():
    # funcion para los wpp
    print("Intentas enviar un mensaje...")
    pass

def Hojas():
    pass

def Opciones_Control_de_Personaje(personaje,inventario,nombre_habitacion):
    while True:
        print("\n¿Qué quieres hacer ahora?")
        print("MOVER || VER INVENTARIO || VER OBJETOS CERCANOS || USAR OBJETO ||") 
        decision = input("> ").lower()
        if decision == "mover":
            Mover(nombre_habitacion)
        elif "inventario" in decision:
            print("Inventario:", inventario)
        elif "ver objetos cercanos":
            Objetos_Cercanos_interactivos(inventario,nombre_habitacion)
        elif "usar objeto":
            UsarObjeto(personaje, inventario, nombre_habitacion) 
        else:
            print("Opción no válida.")
    

def Cocina():
    alacena_cocina = (
    ("Aceite", "de oliva"),
    ("Sal", "fina"),
    ("Azúcar", "rubia"),
    ("Harina", "000"),
    ("Arroz", "largo fino"),
    ("Fideos", "tirabuzón"),
    ("Lentejas", "secas"),
    ("Café", "instantáneo"),
    ("Té", "verde"),
    ("Yerba", "con palo"),
    ("Galletitas", "dulces"),
    ("Cacao", "en polvo"),
    ("Mermelada", "de frutilla"),
    ("Enlatados", "atún"),
    ("Especias", "orégano"),
    ("Pan", "integral"),
    ("Servilletas", "doble hoja")
    )

    print("Elementos de la alacena de cocina y sus características:")
    for i, (elemento, caracteristica) in enumerate(alacena_cocina):
        print(f"{i + 1}. {elemento}: {caracteristica}")

    respuesta = input('¿Desea tomar algo de la alacena? seleccione "Si" o "No": ')

    if respuesta.lower() == 'si':
        elementos_tomados = []
        alacena_lista = list(alacena_cocina)
        
        while True:
            seleccion = int(input("Seleccione el número del elemento que desea tomar (ingrese -1 para finalizar): "))
            if seleccion == -1:
                break
            if 1 <= seleccion <= len(alacena_lista):
                elemento_tomado = alacena_lista[seleccion - 1]
                elementos_tomados.append(elemento_tomado)
                alacena_lista[seleccion - 1] = (None, None)  # Llenar el espacio con vacío
            else:
                print("Selección no válida. Intente nuevamente.")
        
    
        alacena_cocina = tuple(alacena_lista)
        
    
        print("\nHas tomado los siguientes elementos:")
        for elemento, caracteristica in elementos_tomados:
            print(f"- {elemento}: {caracteristica}")
        
        print("\nElementos restantes en la alacena:")
        for i, (elemento, caracteristica) in enumerate(alacena_cocina):
            if elemento is not None:
                print(f"{i + 1}. {elemento}: {caracteristica}")
            else:
                print(f"{i + 1}. [Vacío]")
    else:
        print("No has tomado ningún elemento.")
"""--------------------------------------------------------------------------------------------------------------------------"""    
#main 


inventario=[]
personaje=Eleccion_Personaje()
Inicio_Juego(personaje, inventario )
Living(personaje,inventario)
