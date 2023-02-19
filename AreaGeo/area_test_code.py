from area import *

print("Name in area.py:", __name__)

if __name__ == "__main__":
    print("Prüfung von Oberflächenberechnung Formeln !")

    testsData= \
        [
            (areaTriangle, (3, 4, 5), 6),
            (areaTriangle2, (2, 4), 4),
            (areaRectangle, (2, 3), 6),
            (areaCircle, (10,), 314.1592653589793),
            (areaSemicircle, (10,), 157.07963267948966)
        ]
    for codeTest in testsData:
        if codeTest[0](*codeTest[1]) != codeTest[2]:
            print(f"Es gibt Fehler im {codeTest[0].__name__}")
        else:
            print(f"Es gibt keine Fehler im {codeTest[0].__name__}.")

    assert areaTriangle(3, 4, 5) == 6, 'Fläche falsch berechnet'
    assert areaTriangle(-1, 2, 2) is None, 'negative Flächen müssen None liefern'
    assert areaTriangle(1, -2, 2) is None, 'negative Flächen müssen None liefern'
    assert areaTriangle(1, 2, -2) is None, 'negative Längen sind nicht zulässig'
    assert areaTriangle(-1, -2, 2) is None, 'negative Längen sind nicht zulässig'
    assert areaTriangle(1, -2, -2) is None, 'negative Längen sind nicht zulässig'
    assert areaTriangle(-1, 2, -2) is None, 'negative Längen sind nicht zulässig'
    assert areaTriangle('Text', 2, 2) is None, 'string Längen sind nicht zulässig'
    assert areaTriangle(1,'Text', 2) is None, 'string Längen sind nicht zulässig'
    assert areaTriangle(1, 2,'Text') is None, 'string Längen sind nicht zulässig'
    
    assert areaTriangle2(2, 4) == 4, 'Fläche falsch berechnet'
    assert areaTriangle2(-1, 2) is None, 'negative Flächen müssen None liefern'
    assert areaTriangle2(2, -1) is None, 'negative Flächen müssen None liefern'
    assert areaTriangle2(-1, -2) is None, 'negative Längen sind nicht zulässig'
    assert areaTriangle2('Text', 2) is None, 'string Längen sind nicht zulässig'
    
    assert areaRectangle(2, 4) == 8, 'Fläche falsch berechnet'
    assert areaRectangle(-2, 4) is None, 'negative Flächen müssen None liefern'
    assert areaRectangle(2, -4) is None, 'negative Flächen müssen None liefern'
    assert areaRectangle(-2, -4) is None, 'negative Längen sind nicht zulässig'
    assert areaRectangle('Text', 4) is None, 'string Längen sind nicht zulässig'
    
    assert areaCircle(3) == 28.274333882308138, 'Fläche falsch berechnet'
    assert areaCircle(-3) is None, 'negative Flächen müssen None liefern'
    assert areaCircle('Text') is None, 'string Radius ist nicht zulässig'
    
    assert areaSemicircle(3) == 14.137166941154069, 'Fläche falsch berechnet'
    assert areaSemicircle(-3) is None, 'negative Flächen müssen None liefern'
    assert areaSemicircle('Text') is None, 'string Radius ist nicht zulässig'
    