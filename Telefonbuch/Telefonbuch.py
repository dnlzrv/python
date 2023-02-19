# Problemstellung:
#
# Es soll ein Telefonbuch erstellt werden, in dem sowohl nach Personen als auch nach Telefonnummern gesucht werden kann
# 1) Schreibe eine Funktion, mit der nach einer Telefonnummer gesucht werden kann und der zugehörige Name ermittelt wird
# 2) Schreibe eine Funktion, mit der nach einem Namen gesucht werden kann und die zugehörige Telefonnummer ermittelt
#   wird
# 3) Ermögliche das Eintragen neuer Kontakte in das Telefonbuch
#

contacts = []

def addContact():
	name = input("Geben Sie den Namen ein:\n")
	phone = input("Geben Sie die Telefonnummer ein:\n")
	newContact = (name, phone)
	contacts.append(newContact)

def getPhoneByName():
    name = input("Geben Sie den Namen ein:\n")
    for contact in contacts:
        if name in contact[0]:
            return contact[1]
    return None

def getNameByPhone():
    phone = input("Geben Sie die Telefonnummer ein:\n")
    for contact in contacts:
        if phone in contact[1]:
            return contact[0]
    return None

print("Willkommen im Telefonbuch! ")

while(input("Möchten Sie einen Kontakt hinzufügen? (ja ored nein)\n").upper() == "JA"):
    addContact()

while(input("Möchten Sie nach einem Kontakt suchen? (ja oder nein)\n").upper() == "JA"):
  
    searchBy = (input("Möchten Sie nach Name oder Telefonnummer suchen? (name/nummer)\n")).upper()
    if searchBy == "NAME":
        phone = getPhoneByName()
        if phone == None:
            print("Es gibt keine Telefonnummern für diesen Namen.")
        else:
            print("Die gesuchte Telefonnummer ist: ", phone)

    elif searchBy == "NUMMER":
        name = getNameByPhone()
        if name == None:
            print("Es gibt keine Personen mit dieser Telefonnummer")
        else:
            print("Der gesuchte Name ist :", name)
    else:
        print("SIE haben einen Fehler eingegeben, bitte geben Sie entweder 'Name' oder 'Nummer' ein'")

print("Auf Wiedersehen!")
