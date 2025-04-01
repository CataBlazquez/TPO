import emoji

# # Imprimir cada emoji
# for emoji in emojis:
#     print(emoji)

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

# baño=[["⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛"]]

# cuarto_principal=[["⬛⬛⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛⬛⬛"]]

# closet=[["⬛⬛⬛⬛"],
# ["⬛⬜⬜⬛"],
# ["⬛⬛⬛⬛"]]

# oficina=[["⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛"]]


# cuarto_oculto=[["⬛⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛⬛"]]

# cuarto_extra=[["⬛⬛⬛⬛⬛⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬜⬜⬜⬜⬛"],
# ["⬛⬛⬛⬛⬛⬛"]]


# def Eleccion_Personaje():
#     print(emoji.emojize(":woman:Carla: Influencer en como balancear la vida con el estudio (esta reprobando todo)"))
#     print(emoji.emojize(":man: Gabriel: Gymbro obsesionado con barritas de proteina"))
#     print(emoji.emojize(":dog_face: Firulais: Guau Guau Guau"))
#     eleccion=input("Elige tu personaje: ").lower
#     while (eleccion!='carla' or eleccion!='gabriel'or eleccion!='firulais'):
#         print("No vale inventar personajes!!!")
#         eleccion=input("Elige tu personaje: ").lower
#     if eleccion=='firulais':
#         eligio_perro=input("Estas seguro que lo queres a firu? Si/No").lower
#         while eligio_perro=='si':
#             print("Guau guau Guau")
#             eligio_perro=input("Estas seguro que lo queres a firu? Si/No").lower
#         print(emoji.emojize("Sera re bueno Firu, pero no me parece la mejor idea para un juego como este. Por sus esfuerzos igual le damos un :bone:"))
#         print("Guau")
#         print("De nada, Firu. Ahora si, elegi a tu personaje: ")
#         print(emoji.emojize(":woman:Carla: Influencer en como balancear la vida con el estudio (esta reprobando todo)"))
#         print(emoji.emojize(":man: Gabriel: Gymbro obsesionado con barritas de proteina"))
#         eleccion=input("Elige tu personaje: ").lower
#     return eleccion


def Inicio_Juego(personaje,matriz_living):
    inventario=[]
    print (emoji.emojize("Mañana tengo que entregar el trabajo final de Programacion I y Edesur hizo una de las suyas mientras tenia el Word abierto y sin  el autoguardado."
    "Por suerte, mi amigo ya lo había imprimido (impreso o imprimido? A ver que dice la RAE… Ah cierto, no tengo WIFI:crying_face:).", language='alias'))
    print ("Cuando llego a la casa de mi amigo, me doy cuenta que el tambien esta sin luz")
    print (emoji.emojize("Despues de 6 pisos por escalera, llego a su departamento\n", "1) Toco la puerta:raised_fist_light_skin_tone: \n", "2) Toco el timbre:bell: \n", "3)Abro la puerta:door:\n"))
    opcion=int(input("¿Que opcion eliges?\n"))
    while opcion<0 and opcion>4:
        print("No vale inventar opciones")
        print (emoji.emojize("Despues de 6 pisos por escalera, llego a su departamento\n", "1) Toco la puerta:raised_fist_light_skin_tone: \n", "2) Toco el timbre:bell: \n", "3)Abro la puerta:door:\n"))
        opcion=int(input("¿Que opcion eliges?\n"))
    if(opcion==1 or opcion==2):
        print("GUAUUUUUUUUU")
        print("Guau Guau Guau *sonido de rasqueteo en la puerta*")
        print("Este perro aprendio a abrir la puerta????")
    else: 
        print("¿Como van a dejar la puerta abierta? ¿Creen que viven en una sitcom?")
    matriz_living[6][2]=1
    Living(personaje,inventario,posicion_personaje)

# def Living (personaje, inventario,posicion_personaje, matriz_living, objetos_living):
#     Opciones()

def Mover  (matriz_ubicacion_de_habitacion_actual, matriz_de_cambio_de_habitacion):
    """La ubicacion del personaje habla para donde puede moverse adelante (W), izquierda (A), derecha (D), atras (S) 
    Hay que comprobar si es posible moverse para algun lado de esos o si hay alguna puerta."""
    Mover_Adelante=None
    Mover_Izquierda=None
    Mover_Derecha=None
    Mover_Atras=None
    Puerta_Adelante=None
    puerta_Izquierda=None
    puerta_Derecha=None
    puerta_Atras=None
    ubicacion_actual_fila=0
    for fila in range (0, len(matriz_ubicacion_de_habitacion_actual)):
        for columna in range (0,len(matriz_ubicacion_de_habitacion_actual[fila])):
            if matriz_ubicacion_de_habitacion_actual[fila][columna]==(1):
                ubicacion_actual_columna=columna
                ubicacion_actual_fila=fila
    if(matriz_ubicacion_de_habitacion_actual[ubicacion_actual_fila-1][ubicacion_actual_columna]==0):  #si lo que esta delante del personaje es 0 es posible avanzar
        Mover_Adelante=True
    elif (matriz_ubicacion_de_habitacion_actual[ubicacion_actual_fila-1][ubicacion_actual_columna]==2):#Adelante hay una puerta
        Puerta_Adelante=True
    if(matriz_ubicacion_de_habitacion_actual[ubicacion_actual_fila+1][ubicacion_actual_columna]==0):  #si lo que esta detras del personaje es 0 es posible avanzar
        Mover_Atras=True
    elif (matriz_ubicacion_de_habitacion_actual[ubicacion_actual_fila+1][ubicacion_actual_columna]==2):#Detras hay una puerta
        Puerta_Atras=True
    if(matriz_ubicacion_de_habitacion_actual[ubicacion_actual_fila][ubicacion_actual_columna-1]==0):  #si lo que esta a la izquierda del personaje es 0 es posible avanzar
        Mover_Izquierda=True
    elif (matriz_ubicacion_de_habitacion_actual[ubicacion_actual_fila][ubicacion_actual_columna-1]==2):#A la izquierda hay una puerta
        puerta_Izquierda=True
    if(matriz_ubicacion_de_habitacion_actual[ubicacion_actual_fila][ubicacion_actual_columna+1]==0):  #si lo que esta a la derecha del personaje es 0 es posible avanzar
        Mover_Derecha=True
    elif (matriz_ubicacion_de_habitacion_actual[ubicacion_actual_fila][ubicacion_actual_columna+1]==2):#A la derecha hay una puerta
        Puerta_Derecha=True
    
           

    


def Opciones_de_Control_del_Personaje (personaje, inventario, posicion_personaje):
    
