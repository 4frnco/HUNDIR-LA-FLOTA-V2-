# Hundir la flota - Diagramas de flujo

Este documento contiene los diagramas de flujo en texto de las clases del proyecto **Hundir la flota**.

## Índice

* [Nave](#1-diagrama-de-flujo-de-nave)
* [Casilla](#2-diagrama-de-flujo-de-casilla)
* [Tablero](#3-diagrama-de-flujo-de-tablero)
* [Jugador](#4-diagrama-de-flujo-de-jugador)
* [Flota](#5-diagrama-de-flujo-de-flota)
* [Ataque](#6-diagrama-de-flujo-de-ataque)
* [Juego](#7-diagrama-de-flujo-de-juego)

---

# 1. Diagrama de flujo de `Nave`

## Método `recibir_disparo()`

```text
[Inicio]
   |
   v
¿La nave ya está hundida?
   |--- Sí ---> [Devolver HUNDIDO (2)] ---> [Fin]
   |
   |--- No --->
               |
               v
        [Restar 1 a la vida]
               |
               v
        ¿La vida <= 0?
               |--- Sí ---> [Marcar hundido = True]
               |            |
               |            v
               |     [Mostrar "<nombre> hundido"]
               |            |
               |            v
               |     [Devolver HUNDIDO (2)]
               |            |
               |            v
               |          [Fin]
               |
               |--- No ---> [Mostrar "<nombre> tocado. Vida restante: X"]
                            |
                            v
                    [Devolver TOCADO (1)]
                            |
                            v
                          [Fin]
```

---

# 2. Diagrama de flujo de `Casilla`

## Método `recibir_disparo()`

```text
[Inicio]
   |
   v
¿La casilla ya fue disparada?
   |--- Sí ---> ¿La casilla tiene nave?
   |              |--- Sí ---> [Mostrar "Casilla ya disparada con ..."]
   |              |            |
   |              |            v
   |              |      [Devolver None]
   |              |            |
   |              |            v
   |              |          [Fin]
   |              |
   |              |--- No ---> [Mostrar "Casilla ya disparada es de agua"]
   |                           |
   |                           v
   |                     [Devolver None]
   |                           |
   |                           v
   |                         [Fin]
   |
   |--- No --->
               |
               v
       ¿La casilla es agua?
               |--- Sí ---> [Marcar disparada = True]
               |            |
               |            v
               |      [Devolver 0]
               |            |
               |            v
               |          [Fin]
               |
               |--- No ---> [Llamar a nave.recibir_disparo()]
                            |
                            v
                    [Guardar resultado]
                            |
                            v
                    [Marcar disparada = True]
                            |
                            v
                    [Devolver resultado]
                            |
                            v
                          [Fin]
```

---

# 3. Diagrama de flujo de `Tablero`

## Constructor `__init__()`

```text
[Inicio]
   |
   v
[Definir constantes AGUA, TOCADO, HUNDIDO]
   |
   v
[Crear nave por1 = Manuel]
   |
   v
[Crear nave fra1 = Damián]
   |
   v
[Crear nave fra2 = Elena]
   |
   v
[Crear nave fra3 = Noelia]
   |
   v
[Crear submarinos sub1, sub2, sub3, sub4]
   |
   v
[Construir matriz self.casillero de 10x10]
   |
   v
[Asignar agua o naves a cada Casilla]
   |
   v
[Fin]
```

### Explicación breve

* `Tablero` crea todas las naves.
* Después crea la matriz 10x10.
* Cada posición se guarda como objeto `Casilla`.
* Cada `Casilla` contiene `'agua'` o una `Nave`.

---

# 4. Diagrama de flujo de `Jugador`

## Constructor `__init__()`

```text
[Inicio]
   |
   v
[Recibir nombre]
   |
   v
[Guardar self.nombre]
   |
   v
[Crear self.tablero = Tablero()]
   |
   v
[Llamar a self._obtener_flota()]
   |
   v
[Guardar resultado en self.flota]
   |
   v
[Fin]
```

## Método `_obtener_flota()`

```text
[Inicio]
   |
   v
[Crear conjunto vacío: naves]
   |
   v
[Recorrer cada fila del tablero]
   |
   v
[Recorrer cada casilla de la fila]
   |
   v
¿La casilla es distinta de 'agua'?
   |--- No ---> [Seguir recorriendo]
   |
   |--- Sí ---> [Añadir la nave al conjunto]
                    |
                    v
             [Seguir recorriendo]
                    |
                    v
      ¿Quedan filas/casillas por recorrer?
                    |--- Sí ---> [Volver al bucle]
                    |
                    |--- No ---> [Convertir conjunto en lista]
                                  |
                                  v
                           [Devolver lista]
                                  |
                                  v
                                [Fin]
```

## Método `ha_perdido()`

```text
[Inicio]
   |
   v
¿Todas las naves de la flota están hundidas?
   |--- Sí ---> [Devolver True] ---> [Fin]
   |
   |--- No ---> [Devolver False] ---> [Fin]
```

## Método `mostrar_flota()`

```text
[Inicio]
   |
   v
[Recorrer cada nave de la flota]
   |
   v
[Mostrar nombre, tipo, vida y hundido]
   |
   v
¿Quedan naves?
   |--- Sí ---> [Seguir recorriendo]
   |
   |--- No ---> [Fin]
```

---

# 5. Diagrama de flujo de `Flota`

## Constructor `__init__()`

```text
[Inicio]
   |
   v
¿Se recibió una lista de naves?
   |--- Sí ---> [Guardar esa lista en self.naves]
   |
   |--- No ---> [Crear lista vacía]
   |
   v
[Fin]
```

## Método `agregar_nave()`

```text
[Inicio]
   |
   v
¿La nave ya está en self.naves?
   |--- Sí ---> [No hacer nada] ---> [Fin]
   |
   |--- No ---> [Añadir nave a self.naves] ---> [Fin]
```

## Método `todas_hundidas()`

```text
[Inicio]
   |
   v
¿Todas las naves están hundidas?
   |--- Sí ---> [Devolver True] ---> [Fin]
   |
   |--- No ---> [Devolver False] ---> [Fin]
```

## Método `mostrar_estado()`

```text
[Inicio]
   |
   v
[Recorrer cada nave]
   |
   v
¿La nave está hundida?
   |--- Sí ---> [Estado = "Hundido"]
   |
   |--- No ---> ¿La vida es menor que vida_max?
                  |--- Sí ---> [Estado = "Tocado"]
                  |
                  |--- No ---> [Estado = "Intacto"]
   |
   v
[Mostrar nombre, tipo, estado y vida]
   |
   v
¿Quedan naves?
   |--- Sí ---> [Seguir]
   |
   |--- No ---> [Fin]
```

> Nota: en el código actual de `Nave` no existe `vida_max`, así que este flujo representa la lógica escrita en `Flota`, aunque ese método fallaría al ejecutarse si no se añade ese atributo.

---

# 6. Diagrama de flujo de `Ataque`

## Constructor `__init__()`

```text
[Inicio]
   |
   v
[Recibir x, y, resultado]
   |
   v
[Guardar self.x]
   |
   v
[Guardar self.y]
   |
   v
[Guardar self.resultado]
   |
   v
[Fin]
```

## Método `__str__()`

```text
[Inicio]
   |
   v
[Crear diccionario resultados]
   |
   v
[Buscar texto correspondiente a self.resultado]
   |
   v
[Construir cadena "Ataque a (x,y): resultado"]
   |
   v
[Devolver cadena]
   |
   v
[Fin]
```

---

# 7. Diagrama de flujo de `Juego`

Estos diagramas corresponden al siguiente código base:

```python
from tablero import Tablero  # Importa la clase Tablero para crear el tablero del juegoo

class Juego:
    def __init__(self):
        # Crea una instancia del tablero
        self.tablero = Tablero()

        # Lanza varios ataques de prueba al iniciar el juego
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(2, 1)
        self.lanzar_ataque(1, 4)

    def mostrar_resultado(self, resultado):
        # Muestra por pantalla el resultado del disparo según el valor recibido
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        # Muestra las coordenadas a las que se dispara
        print(f"Ataque a {x},{y}")

        # Accede a la casilla concreta del tablero usando fila y columna
        casilla = self.tablero.casillero[x][y]

        # Llama al método de la casilla para procesar el disparo
        resultado = casilla.recibir_disparo()

        # Si el resultado no es None, significa que el disparo sí produce un resultado válido
        # None ocurre cuando la casilla ya había sido disparada antes
        if resultado is not None:
            self.mostrar_resultado(resultado)

# Crea y ejecuta el juego
juego = Juego()
```

## Constructor `__init__()`

```text
[Inicio]
   |
   v
[Crear self.tablero = Tablero()]
   |
   v
[Lanzar ataque (1,0)]
   |
   v
[Lanzar ataque (1,0)]
   |
   v
[Lanzar ataque (1,1)]
   |
   v
[Lanzar ataque (1,2)]
   |
   v
[Lanzar ataque (2,1)]
   |
   v
[Lanzar ataque (1,4)]
   |
   v
[Fin]
```

## Método `mostrar_resultado(resultado)`

```text
[Inicio]
   |
   v
¿resultado == 0?
   |--- Sí ---> [Mostrar "Agua"] ---> [Fin]
   |
   |--- No --->
               |
               v
        ¿resultado == 1?
               |--- Sí ---> [Mostrar "Tocado"] ---> [Fin]
               |
               |--- No --->
                           |
                           v
                    ¿resultado == 2?
                           |--- Sí ---> [Mostrar "Hundido"] ---> [Fin]
                           |
                           |--- No ---> [Fin]
```

## Método `lanzar_ataque(x, y)`

```text
[Inicio]
   |
   v
[Mostrar "Ataque a x,y"]
   |
   v
[Obtener casilla = self.tablero.casillero[x][y]]
   |
   v
[Llamar resultado = casilla.recibir_disparo()]
   |
   v
¿resultado es distinto de None?
   |--- Sí ---> [Llamar a mostrar_resultado(resultado)] ---> [Fin]
   |
   |--- No ---> [Fin]
```

## Ejecución final

```text
[Inicio del programa]
   |
   v
[Crear objeto Juego]
   |
   v
[Se ejecuta automáticamente __init__()]
   |
   v
[Fin]
```

---

# Resumen final

Los métodos con más lógica y más importantes para representar en un examen son:

1. `Juego.lanzar_ataque()`
2. `Casilla.recibir_disparo()`
3. `Nave.recibir_disparo()`
4. `Jugador._obtener_flota()`

Son los diagramas que mejor explican cómo se comunican los objetos dentro del programa.

En un diagrama de flujo se usa un óvalo para marcar el inicio y el fin, un rectángulo para las acciones o procesos y un rombo para las decisiones o preguntas que pueden tener varias salidas, como “sí” o “no”.

Las flechas indican el orden en que se ejecuta el programa, conectando cada símbolo desde el inicio hasta el final según la lógica del código.