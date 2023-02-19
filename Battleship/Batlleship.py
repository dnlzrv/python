# 11.11.2022
#
# Es soll das Spiel "Schiffe-Versenken" programmiert werden. Dabei soll zunächst lediglich ein Spieler gegen sich
# selbst spielen können, indem er selbst die Schiffe platziert und im Anschluss darauf schießt. Später soll das Programm
# so erweitert werden, dass zwei Personen bzw. eine Person und der PC gegeneinander spielen können.
#
# Gehen Sie dabei wie folgt vor:
# 1) Erstellen Sie einen PAP/Struktogramm. Informieren Sie sich über die Regeln im Internet (falls notwendig).
# 2) Welcher Datentyp ist für das Spielfeld geeignet? Welche sonstigen Datenstrukturen werden benötigt?
#    Welche Teile des Codes können in Funktionen ausgelagert werden?
#
# 3) Initialisiere das Spielfeld / die Spielfelder. Dazu gehört:
#       - Eingabe der Spielfeldgröße durch den Nutzer
#       - Initialisierung des Spielfeldes
# 4) Ermöglichen Sie eine Darstellung des Spielfeldes. Berücksichtigen Sie dabei, dass der Spieler beim
#       Setzen der Schiffe sehen muss, an welcher Position er schon Schiffe platziert hat. Im Spiel sollte der Spieler
#       die Positionen der Schiffe nicht mehr erkennen können.
# 5) Ermöglichen Sie das Platzieren der Schiffe. Geben Sie dabei dem Nutzer
#       folgende Schiffstypen zur Auswahl:
#           Fregatte (2 Felder), Zerstörer (3 Felder), Kreuzer (4 Felder), Schlachtschiff (5 Felder)
#       Die Anzahl der Schiffe des jeweiligen Schiffstyps soll der Nutzer selbst wählen können.
#       Der Nutzer soll auswählen können, ob er die Schiffe horizontal oder vertikal platziert.
#       Zur Positionierung soll der Nutzer die Start-Koordinaten (x und y) des Schiffes eingeben.
# 6) Berücksichtigen Sie in 5), dass Schiffe nicht direkt nebeneinander liegen dürfen.
# 7) Stellen Sie die Funktionsweise des Spieles bis zur abgeschlossenen Eingabe aller Schiffe sicher.
#       Testen Sie das Teilprogramm ausführlich.
# 8) Schreiben Sie eine Funktion, welche es dem Nutzer ermöglicht, einen einzelnen Schuss abzugeben. Sollte er auf ein
#       Feld schießen, welches er schon einmal beschossen hatte, soll ihm eine Fehlermeldung ausgegeben werden.
# 9) Ermöglichen Sie dem Nutzer, mehrmals hintereinander einen Schuss abzugeben. Stellen Sie sicher, dass das
#       Programm beendet wird, sobald der Nutzer alle Schiffsteile auf dem Spielfeld getroffen hat
# 10) Kommentieren Sie den gesamten Code ausführlich. Stellen Sie sicher, dass ein nicht-involvierter Kollege den Code
#       lesen und verstehen kann. Räumen Sie den Code auf, sodass keine nutzlosen Code-Schnipsel mehr vorhanden sind.
#
# mögliche Erweiterungen für schnelle Programmierer:
# a) Ermöglichen Sie ein Spiel Mensch gegen Mensch
# b) Ermöglichen Sie ein Spiel Mensch gegen PC (random)
# c) Ermöglichen Sie ein Spiel Mensch gegen PC (random, mit intelligenten Folgeschüsse bei Treffern)

import csv
import os, pathlib

def readMap(mapName):
    pwd = pathlib.Path().resolve()
    mapsPath = pwd.joinpath("maps")
    fileName = mapName + ".csv"
    filePath = os.path.join(mapsPath, fileName)

    with open(filePath, newline='') as file:
        reader = csv.reader(file)
        return list(reader)

def containsShips(playerMap):
    for line in playerMap:
        if 'x' in line:
            return True
    return False

mapComp = readMap("computer")
mapPlayer = readMap("player")

columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

def getValidInput(message, list):
    playerInput = input(message).upper()
    while playerInput not in list:
        print("Sie haben einen falschen Wert eingegeben.")
        playerInput = getValidInput(message, list)
    return playerInput

def getPlayerInput(player:str):
    message = f"{player}, Geben Sie bite die Spalte (A...J) ein:\n"
    column = getValidInput(message, columns)
    columnIndex = columns.index(column)

    message = f"{player}, Geben Sie bite die Reihe (1...10) ein:\n "
    rowIndex = int(getValidInput(message, rows)) - 1

    return (columnIndex, rowIndex)

while containsShips(mapComp):
    playerInput = getPlayerInput("Spieler 1")
    columnIndex = playerInput[0]
    rowIndex = playerInput[1]

    if mapComp[rowIndex][columnIndex] == "x":
        print("Gut gemacht Spieler 1, Ziel getroffen!\n")
        mapComp[rowIndex][columnIndex] = "_"
        
        if not containsShips(mapComp):
            print("Spiel ist aus!")
    else:
        print("Verpasst, Spieler 1 \n")
        while containsShips(mapPlayer):
            playerInput = getPlayerInput("Spieler 2")
            columnIndex = playerInput[0]
            rowIndex = playerInput[1]

            if mapPlayer[rowIndex][columnIndex] == "x":
                print("Gut gemacht Spieler 2, Ziel getroffen!\n")
                mapPlayer[rowIndex][columnIndex] = "_"

                if not containsShips(mapPlayer):
                    print("Spiel ist aus!")
            else:
                print("Verpasst, Spieler 1 \n")
                break
