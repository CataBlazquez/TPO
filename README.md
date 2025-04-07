# TPO

Integrantes:
Solange Laura Limachi Barra
Facundo Ezequiel Arnaudo
Ana María Martínez Pérez
Catalina Micaela Blazquez

Propósito del documento
Este documento tiene como objetivo detallar los aspectos fundamentales del desarrollo de un videojuego tipo escape room o laberinto creado en Python sin entorno gráfico visual. Servirá como guía para el equipo de desarrollo, así como para cualquier persona interesada en entender el propósito, alcance y funcionalidades del proyecto. Se describen los requisitos del sistema, los beneficios del producto, las funcionalidades principales y los entregables a lo largo del proceso de desarrollo.

Alcance del Producto
Este videojuego consiste en una experiencia de escape room en la oscuridad, donde el jugador debe encontrar las hojas dispersas de un trabajo práctico para poder ganar el juego. El entorno está completamente basado en texto y se ejecuta en consola, lo que aumenta la sensación de tensión y misterio.

Beneficios
Permite ejercitar el razonamiento lógico y la paciencia de manera entretenida para el usuario.
Ofrece una experiencia inmersiva con mínimos recursos.
Es fácilmente accesible en sistemas con Python instalado.

Objetivos
Crear una historia atrapante que mantenga al jugador inmerso en la misión.
Desarrollar un sistema de comandos segun opciones predeterminadas para permitir la jugabilidad, utilizando emojis y lenguaje informal para lograr un guion dinamico y comico.
Lograr que el juego cumpla con la etiqueta de “choice-matters” o “ las decisiones importan”.

Metas del producto
Completar el desarrollo del juego base con interacción por comandos.
Implementar una estructura de niveles o habitaciones dentro del juego.
Integrar un sistema de inventario y pistas relacionadas con la ubicación de las hojas.

Requisitos funcionales
El videojuego incluye las siguientes funciones y características:
Sistema de navegación por texto: El jugador podrá moverse por distintas habitaciones oscuras utilizando comandos como “caminar hacia...”, “buscar”, “encender linterna”, “mandar mensaje a...”, “revisar...” ,etc.
Objetos interactivos: El jugador podrá recolectar objetos (como “libro”, “gelatina”, “cuchara”, etc ) que le ayudarán a progresar en el juego.
Inventario: Visualización de los objetos recolectados y sus usos.
Pistas y desafíos: Algunas habitaciones contienen acertijos, obstáculos o trampas que deben resolverse para poder avanzar.
Objetivo final: Encontrar todas las hojas del trabajo práctico y escapar del lugar.

Entregables
40% del desarrollo:
Navegación básica entre habitaciones mediante comandos de texto.
Estructura inicial del mapa del juego (al menos 3 habitaciones conectadas).
Interacción con objetos básicos (recoger, ver inventario).
80% del desarrollo:
Implementación de acertijos o desafíos en algunas habitaciones.
Lógica de progresión del jugador: solo se puede acceder a ciertas áreas con objetos clave.
Primera versión jugable de principio a fin.
100% del desarrollo:
Historia completa integrada con textos atmosféricos y pistas narrativas.
Todos los objetos y hojas del trabajo distribuidos estratégicamente.
Validaciones de errores en los comandos del jugador.
Mejora del flujo de juego y corrección de errores.
Documentación básica de usuario y guía para jugar.

Desarrollo del juego
El juego comienza en el pasillo de un edificio, tratando de lograr entrar al departamento del amigo del protagonista. Una vez logrado, se entra en el living, donde el personaje puede moverse evitando los muebles y buscando como ingresar al resto de las habitaciones mientras explora para conseguir las hojas del trabajo practico. En cada habitacion, el jugador va a encontrarse con diferentes problemas para resolver o para empeorar. Las distintas habitaciones van a estar diagramadas como matrices, segun la posicion en la que el jugador se encuentre, los objetos que haya o los limites de la habitacion en si. A medida que el jugador va encontrando las distintas hojas, puede preguntar por el chat al dueño del departamento donde pudo haber dejado las hojas.
