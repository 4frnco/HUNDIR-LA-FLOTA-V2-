Hundir la flota - Diagramas en Mermaid
Este documento contiene los diagramas en formato Mermaid para poder subirlos a GitHub y visualizarlos correctamente.
---
1. Clase `Nave`
Método `recibir_disparo()`
```mermaid
flowchart TD
    A([Inicio]) --> B{¿La nave ya está hundida?}
    B -- Sí --> C[Devolver HUNDIDO 2]
    C --> Z([Fin])

    B -- No --> D[Restar 1 a la vida]
    D --> E{¿La vida es menor o igual a 0?}

    E -- Sí --> F[Marcar hundido = True]
    F --> G[Mostrar nombre hundido]
    G --> H[Devolver HUNDIDO 2]
    H --> Z

    E -- No --> I[Mostrar nombre tocado y vida restante]
    I --> J[Devolver TOCADO 1]
    J --> Z
```
---
2. Clase `Casilla`
Método `recibir_disparo()`
```mermaid
flowchart TD
    A([Inicio]) --> B{¿La casilla ya fue disparada?}

    B -- Sí --> C{¿La casilla tiene nave?}
    C -- Sí --> D[Mostrar casilla ya disparada con datos de la nave]
    D --> E[Devolver None]
    E --> Z([Fin])

    C -- No --> F[Mostrar casilla ya disparada de agua]
    F --> G[Devolver None]
    G --> Z

    B -- No --> H{¿La casilla es agua?}
    H -- Sí --> I[Marcar disparada = True]
    I --> J[Devolver 0]
    J --> Z

    H -- No --> K[Llamar a nave.recibir_disparo]
    K --> L[Guardar resultado]
    L --> M[Marcar disparada = True]
    M --> N[Devolver resultado]
    N --> Z
```
---
3. Clase `Tablero`
Constructor `__init__()`
```mermaid
flowchart TD
    A([Inicio]) --> B[Definir constantes AGUA TOCADO HUNDIDO]
    B --> C[Crear portaaviones Manuel]
    C --> D[Crear fragata Damian]
    D --> E[Crear fragata Elena]
    E --> F[Crear fragata Noelia]
    F --> G[Crear submarinos U-47 U-96 U-505 U-534]
    G --> H[Construir matriz casillero de 10x10]
    H --> I[Asignar agua o naves a cada Casilla]
    I --> Z([Fin])
```
---
4. Clase `Jugador`
Constructor `__init__()`
```mermaid
flowchart TD
    A([Inicio]) --> B[Recibir nombre]
    B --> C[Guardar self.nombre]
    C --> D[Crear self.tablero = Tablero]
    D --> E[Llamar a self._obtener_flota]
    E --> F[Guardar resultado en self.flota]
    F --> Z([Fin])
```
Método `_obtener_flota()`
```mermaid
flowchart TD
    A([Inicio]) --> B[Crear conjunto vacío naves]
    B --> C[Recorrer filas del tablero]
    C --> D[Recorrer casillas de la fila]
    D --> E{¿La casilla es distinta de agua?}

    E -- Sí --> F[Añadir nave al conjunto]
    F --> G{¿Quedan más casillas o filas?}
    E -- No --> G

    G -- Sí --> D
    G -- No --> H[Convertir conjunto en lista]
    H --> I[Devolver lista]
    I --> Z([Fin])
```
Método `ha_perdido()`
```mermaid
flowchart TD
    A([Inicio]) --> B{¿Todas las naves están hundidas?}
    B -- Sí --> C[Devolver True]
    B -- No --> D[Devolver False]
    C --> Z([Fin])
    D --> Z
```
Método `mostrar_flota()`
```mermaid
flowchart TD
    A([Inicio]) --> B[Recorrer cada nave de la flota]
    B --> C[Mostrar nombre tipo vida y hundido]
    C --> D{¿Quedan naves?}
    D -- Sí --> B
    D -- No --> Z([Fin])
```
---
5. Clase `Flota`
Constructor `__init__()`
```mermaid
flowchart TD
    A([Inicio]) --> B{¿Se recibió lista de naves?}
    B -- Sí --> C[Guardar lista en self.naves]
    B -- No --> D[Crear lista vacía]
    C --> Z([Fin])
    D --> Z
```
Método `agregar_nave()`
```mermaid
flowchart TD
    A([Inicio]) --> B{¿La nave ya está en self.naves?}
    B -- Sí --> C[No hacer nada]
    B -- No --> D[Añadir nave a self.naves]
    C --> Z([Fin])
    D --> Z
```
Método `todas_hundidas()`
```mermaid
flowchart TD
    A([Inicio]) --> B{¿Todas las naves están hundidas?}
    B -- Sí --> C[Devolver True]
    B -- No --> D[Devolver False]
    C --> Z([Fin])
    D --> Z
```
Método `mostrar_estado()`
```mermaid
flowchart TD
    A([Inicio]) --> B[Recorrer cada nave]
    B --> C{¿La nave está hundida?}
    C -- Sí --> D[Estado = Hundido]
    C -- No --> E{¿La vida es menor que vida_max?}
    E -- Sí --> F[Estado = Tocado]
    E -- No --> G[Estado = Intacto]
    D --> H[Mostrar nombre tipo estado y vida]
    F --> H
    G --> H
    H --> I{¿Quedan naves?}
    I -- Sí --> B
    I -- No --> Z([Fin])
```
> Nota: en el código actual de `Nave` no existe `vida_max`, así que este flujo representa la lógica escrita en `Flota`, aunque ese método fallaría al ejecutarse si no se añade ese atributo.
---
6. Clase `Ataque`
Constructor `__init__()`
```mermaid
flowchart TD
    A([Inicio]) --> B[Recibir x y resultado]
    B --> C[Guardar self.x]
    C --> D[Guardar self.y]
    D --> E[Guardar self.resultado]
    E --> Z([Fin])
```
Método `__str__()`
```mermaid
flowchart TD
    A([Inicio]) --> B[Crear diccionario de resultados]
    B --> C[Buscar texto según self.resultado]
    C --> D[Construir cadena Ataque a x y]
    D --> E[Devolver cadena]
    E --> Z([Fin])
```
---
7. Clase `Juego`
Secuencia general de ataque
```mermaid
sequenceDiagram
    autonumber
    actor Usuario
    participant Juego as :Juego
    participant Tablero as :Tablero
    participant Casilla as :Casilla
    participant Nave as :Nave

    Usuario->>Juego: lanzar_ataque(x, y)
    activate Juego

    Juego->>Tablero: acceder a casillero[x][y]
    activate Tablero
    Tablero-->>Juego: devolver casilla
    deactivate Tablero

    Juego->>Casilla: recibir_disparo()
    activate Casilla

    alt Casilla ya disparada
        Casilla-->>Juego: None
    else Casilla con agua
        Casilla-->>Juego: 0
    else Casilla con nave
        Casilla->>Nave: recibir_disparo()
        activate Nave
        Nave-->>Casilla: 1 o 2
        deactivate Nave
        Casilla-->>Juego: 1 o 2
    end

    Juego->>Juego: mostrar_resultado(resultado)
    Juego-->>Usuario: Agua / Tocado / Hundido
    deactivate Juego
```
Método `mostrar_resultado(resultado)`
```mermaid
flowchart TD
    A([Inicio]) --> B{¿resultado == 0?}
    B -- Sí --> C[Mostrar Agua]
    B -- No --> D{¿resultado == 1?}
    D -- Sí --> E[Mostrar Tocado]
    D -- No --> F{¿resultado == 2?}
    F -- Sí --> G[Mostrar Hundido]
    F -- No --> Z([Fin])
    C --> Z
    E --> Z
    G --> Z
```
Método `lanzar_ataque(x, y)`
```mermaid
flowchart TD
    A([Inicio]) --> B[Mostrar Ataque a x y]
    B --> C[Obtener casilla del tablero en x y]
    C --> D[Llamar resultado = casilla.recibir_disparo]
    D --> E{¿resultado es distinto de None?}
    E -- Sí --> F[Llamar a mostrar_resultado]
    E -- No --> Z([Fin])
    F --> Z
```
Constructor `__init__()`
```mermaid
flowchart TD
    A([Inicio]) --> B[Crear self.tablero = Tablero]
    B --> C[Lanzar ataque 1 0]
    C --> D[Lanzar ataque 1 0]
    D --> E[Lanzar ataque 1 1]
    E --> F[Lanzar ataque 1 2]
    F --> G[Lanzar ataque 2 1]
    G --> H[Lanzar ataque 1 4]
    H --> Z([Fin])
