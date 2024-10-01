import numpy as np
import matplotlib.pyplot as plt

"""
Este programa simula el experimento de la doble rendija modelando la luz como ondas.
Genera un patrón de interferencia sobre una pantalla, mostrando la superposición de ondas
provenientes de dos rendijas. La visualización final será un patrón de interferencia representado
con líneas verticales que varían en altura de acuerdo a la intensidad de la luz en cada punto de la pantalla.
"""

# Función para calcular la amplitud de una onda desde una rendija
def amplitud_onda(x, pos_rendija, long_onda, dist_pantalla):
    distancia = np.sqrt(dist_pantalla**2 + (x - pos_rendija)**2)
    fase = 2 * np.pi * distancia / long_onda
    return np.cos(fase)

# Función para simular el experimento de la doble rendija
def doble_rendija_simulacion(long_onda, dist_rendijas, dist_pantalla, num_puntos, ancho_pantalla):
    posiciones_x = np.linspace(-ancho_pantalla / 2, ancho_pantalla / 2, num_puntos)

    rendija1_pos = -dist_rendijas / 2
    rendija2_pos = dist_rendijas / 2

    amplitud1 = amplitud_onda(posiciones_x, rendija1_pos, long_onda, dist_pantalla)
    amplitud2 = amplitud_onda(posiciones_x, rendija2_pos, long_onda, dist_pantalla)

    intensidad = (amplitud1 + amplitud2) ** 2

    plt.figure(figsize=(8, 6))
    for i in range(num_puntos):
        plt.vlines(posiciones_x[i], ymin=0, ymax=intensidad[i], color='black')

    plt.title("Patrón de interferencia - Líneas verticales")
    plt.xlabel("Posición en la pantalla (m)")
    plt.ylabel("Intensidad (proporcional)")
    plt.show()

def main():
    long_onda = float(input("Ingrese la longitud de onda: "))
    dist_rendijas = float(input("Ingrese la distancia entre rendijas: "))
    dist_pantalla = float(input("Ingrese la distancia a la pantalla: "))
    num_puntos = int(input("Ingrese el número de puntos en la pantalla: "))
    ancho_pantalla = float(input("Ingrese el ancho de la pantalla "))

    doble_rendija_simulacion(long_onda, dist_rendijas, dist_pantalla, num_puntos, ancho_pantalla)

main()
