import area as geoArea

area = geoArea.areaTriangle(3, 4,-5)
print("Die Fläche des Dreiecks (3, 4,-5):", area, "cm^2")

area1 = geoArea.areaTriangle(3, 4, 5)
print("Die Fläche des Dreiecks (3, 4, 5):", area1, "cm^2")

area2 = geoArea.areaTriangle2(3, -2)
print("Die Fläche des Dreiecks (3, -2):", area2, "cm^2")

area3 = geoArea.areaTriangle2(3, 2)
print("Die Fläche des Dreiecks (3, 2):", area3, "cm^2")

area4 = geoArea.areaRectangle(4, -5)
print("Die Fläche des Rechtecks (4, -5):", area4, "cm^2")

area5 = geoArea.areaRectangle(4, 5)
print("Die Fläche des Rechtecks (4, 5):", area5, "cm^2")

area6 = geoArea.areaCircle(-5)
print("Die Fläche des Kreieses (-5):", area6, "cm^2")

area7 = geoArea.areaCircle(5)
print("Die Fläche des Kreieses (5):", area7, "cm^2")

area8 = geoArea.areaCircle(5)
print("Die Fläche des Kreieses (5):", format(area8,'.2f'), "cm^2")

area9 = geoArea.areaSemicircle(-6)
print("Die Fläche des Halbkreieses (-6):", area9,"cm^2")

area10 = geoArea.areaSemicircle(6)
print("Die Fläche des Halbkreieses (6):", area10,"cm^2")

area11 = geoArea.areaSemicircle(6)
print("Die Fläche des Halbkreieses (6):", format(area11,'.2f'), "cm^2")
