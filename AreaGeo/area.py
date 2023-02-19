# 08.11.2022
#
# Schreibe ein eigenes Modul (eine Python-Datei) mit dem Namen: Flaechenberechnung.py
#
# Stelle in dem Modul folgende Funktionen zur Verfügung:
#   - Flächeninhalt vom Dreieck: flaeche_dreieck(...)
#   - Flächeninhalt vom Rechteck: flaeche_rechteck(...)
#   - Flächeninhalt vom Kreis: flaeche_kreis(...)
#   - Flächeninhalt vom Halbkreis: flaeche_halbkreis(...)

import math

def areaTriangle(side_a, side_b, side_c):
    if not isinstance(side_a, int) or isinstance(side_a, float):
        return None
    if not isinstance(side_b, int) or isinstance(side_b, float):
        return None
    if not isinstance(side_c, int) or isinstance(side_c, float):
        return None 
    if side_a + side_b <= side_c or side_a +side_c <= side_b or side_b + side_c <= side_a:
        return None
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return None
    p = (side_a + side_b + side_c) / 2
    return math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))

def areaTriangle2(height, base):
    if not isinstance(height, int) or isinstance(height, float):
        return None
    if not isinstance(base, int) or isinstance(base, float):
        return None
    if height <= 0 or base <= 0:
        return None
    return 0.5 * height * base

def areaRectangle(length_a, width_b):
    if not isinstance(length_a, int) or isinstance(length_a, float):
        return None
    if not isinstance(width_b, int) or isinstance(width_b, float):
        return None
    if length_a <= 0 or width_b <= 0:
        return None
    return length_a * width_b

def areaCircle(radius):
    if not isinstance(radius, int) or isinstance(radius, float):
        return None
    if radius <= 0:
        return None
    return math.pi * radius**2

def areaSemicircle(radius):
    if not isinstance(radius, int) or isinstance(radius, float):
        return None
    if radius <= 0:
        return None
    return (math.pi * radius ** 2) / 2
