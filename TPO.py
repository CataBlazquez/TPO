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
    ubicacion_actual=[fila_jugador, col_jugador]
    return ubicacion_actual, coordenadas, direcciones

def Living (personaje, inventario, matriz_living, objetos_living):

    pass
    
def Mover  (habitacion_actual):
    ubicacion_personaje, coordenadas, direcciones =Ubicacion_Actual_Personaje(habitacion_actual)
    fila_jugador=ubicacion_personaje[0]
    col_jugador=ubicacion_personaje[1]
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

def VerObjeto(personaje, nombre_objeto):
    #funcion para poder ver cada objeto en el juego
    print(f"\n{personaje} está mirando {nombre_objeto}.")
    #Esto es temporal hasta ver diccionarios
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

def UsarObjeto(personaje, objeto_a_usar, inventario, matriz_habitacion, objetos_habitacion):
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
    pass

def Hojas():
    pass

def Opciones_Control_de_Personaje(personaje,inventario,habitacion_actual):
    while True:
        print("\n¿Qué quieres hacer ahora?")
        print("MOVER || VER INVENTARIO || VER OBJETOS CERCANOS || USAR OBJETO ||") 
        decision = input("> ").lower()
        if decision == "mover":
            Mover(habitacion_actual)
            break # Vuelve a la función de la habitación para la nueva posición
        elif "inventario" in decision:
            print("Inventario:", inventario)
        elif "ver objetos cercanos":
            # Vuelve a llamar a Living para mostrar e interactuar con objetos
            Living(personaje, inventario, habitacion_actual, objetos_living) # pasar la matriz de objetos correcta
            break
        elif "usar objeto":
            objeto_a_usar = input("¿Qué objeto quieres usar de tu inventario? ").lower()
            UsarObjeto(personaje, objeto_a_usar, inventario, habitacion_actual, objetos_living) # pasar las matrices correctas
        else:
            print("Opción no válida.")

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
