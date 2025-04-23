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

