# Solucionador de Restricciones

Un algoritmo de retroceso para resolver un problema de programación de torneos de 3 jugadores.

## Descripción del problema

Hay **3 jugadores**: **A**, **B** y **C**.

- Juegan un total de **21 partidas**.

- Objetivos de participación final:

- **A**: 17 partidas

- **B**: 15 partidas

- **C**: 10 partidas

### Reglas
- Solo **2 jugadores** juegan cada partida (uno descansa).

- El **ganador** permanece en la mesa.

- El **perdedor** es reemplazado por el jugador que estaba descansando.

## Cómo funciona

Este programa utiliza una **búsqueda en profundidad (retroceso)** con poda para explorar todas las secuencias posibles de victorias y derrotas, comenzando con `A vs B` (C descansando), hasta encontrar historiales de torneos válidos que coincidan exactamente con el número de participaciones objetivo.

## Características

- Poda eficiente cuando un jugador supera su límite de partidas
- Encuentra todo tipo de "universos" (válidos y no validos)
- No puede superar los 21 partidos (sumatoria de los 3 jugadores)
- Imprime las primeras partidas de cada solución válida
- Demuestra la resolución de problemas de satisfacción de restricciones

## Primeros pasos
<details>
<summary>Uso</summary>

```bash
# Usar Replit
https://replit.com/

# Ejecutar la simulación
pega el archivo "sc.py" y ejecutalo
````
## Origen del Problema

Este problema matemático fue creado por **Adrián Paenza**.  
[Ver en Wikipedia](https://es.wikipedia.org/wiki/Adri%C3%A1n_Paenza)
