import emoji
"""El diccionario de puertas, se va a leer con el primer elemento siendo las coordenadas de la puerta, y la ubicacion actual. """
puertas={
   ((0,1),"living"): {
       "habitacion_destino" : "cuarto principal"
       "coordenada_destino"()
   }
}

# living=[["⬛⬛⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬜⬛"]
# ["⬛⬜⬜⬜⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛⬛⬛"]]
"""La matriz de cada habitacion, tiene su forma arriba. Los cuadrados negros son las paredes, los blancos el piso. Si la matriz tiene 
un 1 es donde esta parado el jugador. Va a haber otra matriz con los objetos que tiene cada "celda". Si hay 0 es lugar donde puede caminar.
Si hay -1 esta prohibido caminar (ya sea porque hay una pared o un mueble), si hay un 2 es una puerta"""
    
# matriz_living=[[-1,2,-1,-1,2,-1],#La primera y la ultima fila tiene un elemento menos porque son las paredes y tienen las esquinas
#     [-1,0,0,0,0,0,-1-1],
#     [2,0,0,-1,-1,-1,0,-1], #no se puede caminar en el medio por los muebles
#     [-1,0,0,-1,-1,-1,0,2],
#     [2,0,0,0,0,0,0,-1],
#     [-1,0,0,0,-1,-1,0,-1],
#      [-1,-1,0,0,0,0,0,-1],
#     [-1,2,-1,-1,-1,-1,]]
"""Las matrices de objetos, van a indicar que hay en cada uno y cada uno tiene sus acciones especificas
    Si hay 0 es porque no hay nada, si hay algun objeto, se escribira tal objeto y sus acciones. Las puertas no cuentan como objetos.
    Puede haber objetos en puertas y paredes (afiches, cuadros, estantes)"""
# objetos_living=[[0,0,"cuadro",0,"En reunion, no entrar!",0],
#     [0,0,0,0,0,0,"cucha perro",0],
#     ["chapa que dice toilette",0,"alfombra","silla","mesa comedor","silla",0,0]     
#     [0,0,"alfombra","silla","mesa comedor","silla",0,"cartel prohibido pasar"]                
#     ["Aca se hacen cosas ricas",0,"alfombra", 0,0,0,0,0]
#     ["perchero",0,0,0,"sillon","sillon,",0,"cuadro"] 
#     [0,"paraguero",0,0,0,0,0,0]
#     [0,"coso para colgar las llaves atras de la puerta principal",0,"television","television",0]]

# for fila in range (0, len(cuarto)):
#     for columna in range (0,len(cuarto[fila])):
#         print(f"{cuarto[fila][columna]")
# cocina=[["⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛"]]

# matriz_cocina=[[-1,-1,-1],
#                [-1,0,0,-1,-1],#pared, vacio, vacio, heladera, pared
#                [-1,-1,0,0,2], #pared, horno y puerta a living
#                [-1,0,0,0,-1],
#                [-1,-1,-1]]

# baño=[["⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛"]]

# matriz_baño=[[-1,-1,-1],
#             [-1,-1,0,-1,-1],#pared, primera parte de la bañera, nada, inodoro, pared
#             [-1,-1,-1,0,2],#pared, segunda parte bañera, lavamanos, nada, puerta a living
#             [-1,-1,-1] #pared, espejo, pared
# ]

# cuarto_principal=[["⬛⬛⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛⬛⬛"]]

# matriz_cuarto_principal=[[-1,-1,-1,-1,-1],#pared del cuarto
#                         [-1,-1,-1,-1,-1,-1,-1],#pared, mesa de luz, camax3, mesa de luz, pared
#                         [-1,0,-1,-1,-1,0,-1],
#                         [-1,0,-1,-1,-1,0,-1],
#                         [-1,-1,0,0,0,0,-1],#pared, mesa de maquillaje, vacio
#                         [-1,-1,-1,-1, 0,0,2],#pared, mesa de maquillaje, zapatero, vacio y puerta a closet
#                         [-1,-1,-1,2,-1]]#pared y puerta a living


# closet=[["⬛⬛⬛"],
#["⬛⬜⬛"],
# ["⬛⬜⬛"],
# ["⬛⬛⬛"]]

# matriz_closet=[[-1,],
#                [-1,0,-1],
#                [2,0,-1]
#                [-1]]

# oficina=[["⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛"]]

# matriz_oficina=[[-1,-1,-1],
#                 [-1,-1,-1,-1,-1],#paredes y escritorio
#                 [-1,0,-1,0,-1], #paredes y silla
#                 [-1,0,0,-1,-1],#paredes y biblioteca 
#                 [-1,0,0,-1,2],#paredes y biblioteca con puerta oculta
#                 [-1,2,-1]
# ]

# cuarto_oculto=[["⬛⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛⬛"]]

# matriz_cuarto_oculto=[[-1,-1,-1,-1], #lo dejo vacio porque no se me ocurre que poner
#                       [-1,0,0,0,0,-1],
#                       [-1,0,0,0,0,-1],
#                       [2,0,0,0,0,-1],
#                       [-1,0,0,0,0,-1],
#                       [-1,-1,-1,-1]]

# cuarto_extra=[["⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛"]]

# matriz_cuarto_extra=[[-1,-1,-1],
#                     [-1,0,-1,-1,-1],#paredes y ropero 
#                     [2,0,0,0,-1],#puerta, , pared 
#                     [-1,0,0,0,-1],
#                     [-1,-1,-1,-1,-1]#paredes, cama
# ]


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


def Inicio_Juego(personaje,matriz_living):
    inventario=[]
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


def Living (personaje, inventario, matriz_living, objetos_living):

    pass
    
def Mover  (habitacion_actual):
    direcciones = ["w", "s", "a", "d"] 
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
    # Recorremos 
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
    if adyacentes_con_puertas!=[]:
        print("Puertas adyacentes:", adyacentes_con_puertas)

    print("el jugador esta en: ", fila_jugador,col_jugador)
    print("Movimientos posibles:", movimientos_posibles)
    movimiento_elegido=input("¿Para donde te quieres mover?").lower()
    while movimiento_elegido not in movimientos_posibles:
        print ("Movimiento invalido")
        movimiento_elegido=input("¿Para donde te quieres mover?").lower()
    habitacion_actual[fila_jugador][col_jugador]=0
    if movimiento_elegido=='w':
        if habitacion_actual[fila_jugador-1][col_jugador]==2:
            Puertas(habitacion_actual,(fila_jugador)-1,col_jugador)
        habitacion_actual[fila_jugador-1][col_jugador]=1
    elif movimiento_elegido=='s':
        if habitacion_actual[fila_jugador+1][col_jugador]==2:
            Puertas(habitacion_actual,(fila_jugador)+1,col_jugador)
        habitacion_actual[fila_jugador+1][col_jugador]=1
    elif movimiento_elegido=='a':
        if habitacion_actual[fila_jugador][col_jugador-1]==2:
            Puertas(habitacion_actual,fila_jugador,(col_jugador)-1)
        habitacion_actual[fila_jugador][col_jugador-1]=1
    elif movimiento_elegido=='d':
        if habitacion_actual[fila_jugador][col_jugador+1]==2:
            Puertas(habitacion_actual,fila_jugador,(col_jugador)+1)
        habitacion_actual[fila_jugador][col_jugador+1]=1
    return

def Puertas(habitacion_actual, habitacion_siguiente, puerta_fila,puerta_columna):
    pass
    
def Mensajear():
    pass

def Hojas():
    pass

def Opciones_Control_de_Personaje(personaje,inventario,habitacion_actual):
    print("MOVER || VER INVENTARIO || MANDAR MENSAJE AL DUEÑO DE CASA || USAR...  ||")
    decision=input("¿Que quieres hacer?\n").lower()
    if decision=='mover':
        Mover()
    elif decision=='inventario' or decision=='ver inventario':
        pass
    elif decision =='mandar mensaje al dueño de casa' or decision=='mensaje' or decision=='mandar mensaje':
        pass
    pass

def Ver():
    pass
# print("Elige para donde moverte: ", Mover_Izquierda,Mover_Adelante,Mover_Atras,Mover_Derecha)
#     movimiento=input("Opcion: ")
# # def Opciones_de_Control_del_Personaje (personaje, inventario):

"""--------------------------------------------------------------------------------------------------------------------------"""    
#main 
matriz_living=[[-1,2,-1,-1,2,-1],#La primera y la ultima fila tiene un elemento menos porque son las paredes y tienen las esquinas
    [-1,0,0,0,0,0,-1-1],
    [2,0,0,-1,-1,-1,0,-1], #no se puede caminar en el medio por los muebles
    [-1,0,0,-1,-1,-1,0,2],
    [2,0,0,0,0,0,0,-1],
    [-1,0,0,0,-1,-1,0,-1],
     [-1,-1,0,0,0,0,0,-1],
    [-1,2,-1,-1,-1,-1,]]
"""Las matrices de objetos, van a indicar que hay en cada uno y cada uno tiene sus acciones especificas
    Si hay 0 es porque no hay nada, si hay algun objeto, se escribira tal objeto y sus acciones. Las puertas no cuentan como objetos.
    Puede haber objetos en puertas y paredes (afiches, cuadros, estantes)"""
objetos_living=[[0,0,"cuadro",0,"En reunion, no entrar!",0],
    [0,0,0,0,0,0,"cucha perro",0],
    ["chapa que dice toilette",0,"alfombra","silla","mesa comedor","silla",0,0] ,    
    [0,0,"alfombra","silla","mesa comedor","silla",0,"cartel prohibido pasar"],                
    ["Aca se hacen cosas ricas",0,"alfombra", 0,0,0,0,0],
    ["perchero",0,0,0,"sillon","sillon,",0,"cuadro"], 
    [0,"paraguero",0,0,0,0,0,0],
    [0,"coso para colgar las llaves atras de la puerta principal",0,"television","television",0]]

inventario=[]
personaje=Eleccion_Personaje()
Inicio_Juego(personaje,matriz_living )
Living(personaje,inventario, matriz_living, objetos_living)