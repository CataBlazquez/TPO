# Definición de la matriz del living y la de objetos
matriz_living=[[-1,2,-1,-1,2,-1],
               [-1,0,0,0,0,0,-1],
               [2,0,0,-1,-1,-1,0,-1],
               [-1,0,0,-1,-1,-1,0,2],
               [2,0,0,0,0,0,0,-1],
               [-1,0,0,0,-1,-1,0,-1],
               [-1,-1,0,0,0,0,0,-1],
               [-1,2,-1,-1,-1,-1]]

objetos_living=[[0,0,"cuadro",0,"En reunion, no entrar!",0],
                [0,0,0,0,0,0,"cucha perro",0],
                ["chapa toilette",0,"alfombra","silla","mesa comedor","silla",0,0],
                [0,0,"alfombra","silla","mesa comedor","silla",0,"cartel prohibido"],
                ["Aca se hacen cosas ricas",0,"alfombra", 0,0,0,0,0],
                ["perchero",0,0,0,"sillon","sillon",0,"cuadro"],
                [0,"paraguero",0,0,0,0,0,0],
                [0,"llaves atras puerta",0,"television","television",0]]

def Living (personaje, inventario, matriz_habitacion, objetos_habitacion, nombre_habitacion="living"):
    print(f"\nEstás en el {nombre_habitacion}. Observas alrededor...")

    # Encuentra la posición del jugador
    for fila in range(len(matriz_habitacion)):
        for columna in range(len(matriz_habitacion[fila])):
            if matriz_habitacion[fila][columna] == 1:
                fila_jugador = fila
                columna_jugador = columna
                break
        else:
            continue
        break

    objetos_interactuables = []
    adyacentes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for df, dc in adyacentes:
        nueva_fila = fila_jugador + df
        nueva_columna = columna_jugador + dc

        if 0 <= nueva_fila < len(matriz_habitacion) and 0 <= nueva_columna < len(matriz_habitacion[nueva_fila]):
            if matriz_habitacion[nueva_fila][nueva_columna] != -1: # No es una pared
                if 0 <= nueva_fila < len(objetos_habitacion) and 0 <= nueva_columna < len(objetos_habitacion[nueva_fila]):
                    objeto = objetos_habitacion[nueva_fila][nueva_columna]
                    if objeto != 0:
                        objetos_interactuables.append(((nueva_fila, nueva_columna), objeto))

    if objetos_interactuables:
        print("\nObjetos cercanos con los que puedes interactuar:")
        for i, (coordenadas, nombre_objeto) in enumerate(objetos_interactuables):
            print(f"{i+1}. {nombre_objeto} (en fila: {coordenadas[0]}, columna: {coordenadas[1]})")

        accion = input("¿Qué deseas hacer? (VER OBJETO/AGARRAR OBJETO/MOVER/INVENTARIO/USAR...) ").lower()

        if "ver objeto" in accion or "agarrar objeto" in accion:
            try:
                indice_objeto = int(input("Elige el número del objeto: ")) - 1
                if 0 <= indice_objeto < len(objetos_interactuables):
                    coordenadas_objeto, nombre_objeto = objetos_interactuables[indice_objeto]
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

    Opciones_Control_de_Personaje(personaje, inventario, matriz_habitacion)

def VerObjeto(personaje, nombre_objeto):
    print(f"\n{personaje} está mirando {nombre_objeto}.")
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

def Mover(matriz_habitacion):
    direcciones = ["w", "s", "a", "d"]
    # Encuentra la posición actual del jugador
    for fila in range(len(matriz_habitacion)):
        for col in range(len(matriz_habitacion[fila])):
            if matriz_habitacion[fila][col] == 1:
                fila_jugador = fila
                col_jugador = col
                break
        else:
            continue
        break

    coordenadas = [(fila_jugador - 1, col_jugador), (fila_jugador + 1, col_jugador),
                   (fila_jugador, col_jugador - 1), (fila_jugador, col_jugador + 1)]
    movimientos_posibles = []
    adyacentes_con_puertas = []

    for i in range(len(coordenadas)):
        f, c = coordenadas[i]
        if 0 <= f < len(matriz_habitacion) and 0 <= c < len(matriz_habitacion[0]):
            if matriz_habitacion[f][c] == 0:
                movimientos_posibles.append(direcciones[i])
            elif matriz_habitacion[f][c] == 2:
                adyacentes_con_puertas.append(direcciones[i])

    if adyacentes_con_puertas:
        print("Puertas adyacentes:", adyacentes_con_puertas)
    print("Tu posición actual: fila", fila_jugador, "columna", col_jugador)
    print("Movimientos posibles:", movimientos_posibles)

    movimiento_elegido = input("¿Para dónde te quieres mover? (w/a/s/d) ").lower()
    while movimiento_elegido not in movimientos_posibles:
        print("Movimiento inválido.")
        movimiento_elegido = input("¿Para dónde te quieres mover? (w/a/s/d) ").lower()

    matriz_habitacion[fila_jugador][col_jugador] = 0
    if movimiento_elegido == 'w':
        if matriz_habitacion[fila_jugador - 1][col_jugador] == 2:
            # llamar a la función para cambiar de habitación
            print("¡Entras por la puerta de arriba!")
            # Puertas(matriz_habitacion, (fila_jugador) - 1, col_jugador)
        matriz_habitacion[fila_jugador - 1][col_jugador] = 1
    elif movimiento_elegido == 's':
        if matriz_habitacion[fila_jugador + 1][col_jugador] == 2:
            print("¡Entras por la puerta de abajo!")
            # Puertas(matriz_habitacion, (fila_jugador) + 1, col_jugador)
        matriz_habitacion[fila_jugador + 1][col_jugador] = 1
    elif movimiento_elegido == 'a':
        if matriz_habitacion[fila_jugador][col_jugador - 1] == 2:
            print("¡Entras por la puerta de la izquierda!")
            # Puertas(matriz_habitacion, fila_jugador, (col_jugador) - 1)
        matriz_habitacion[fila_jugador][col_jugador - 1] = 1
    elif movimiento_elegido == 'd':
        if matriz_habitacion[fila_jugador][col_jugador + 1] == 2:
            print("¡Entras por la puerta de la derecha!")
            # Puertas(matriz_habitacion, fila_jugador, (col_jugador) + 1)
        matriz_habitacion[fila_jugador][col_jugador + 1] = 1
    return

def Puertas(habitacion_actual, puerta_fila, puerta_columna):
    # lógica para determinar la habitación de destino
    # diccionario de 'puertas'
    pass

def Mensajear():
    # funcion para los wpp
    print("Intentas enviar un mensaje...")
    pass

def Opciones_Control_de_Personaje(personaje, inventario, habitacion_actual):
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

    
