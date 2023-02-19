import random

isPlayer1Cpu = True
isPlayer2Cpu = False
matches = 13

def getValidInput(message):
    playerInput = input(message)
    while type(playerInput) != int:
        try:
            playerInput = int(playerInput)
        except:
            playerInput = input("Geben si e bite eine ganze Zahl:\n")

    while playerInput > 3 or playerInput < 1:
        playerInput = getValidInput(message)

    return playerInput
def remainingMatchesMsg(matches):
    if matches == 1:
        return "noch 1 Streichholz ist geblieben."
    else:
        return f"noch {matches} Streichhölzer sind geblieben."
    
def selectedMatchesMsg(playerInput):
    if playerInput == 1:
        return "nimmt 1 Streichholz,"
    else:
        return f"nimmt {playerInput} Streichhölzer,"

def getPlayer1Input():
    if isPlayer1Cpu == True:
        return random.randint(1,3)
    else:
        return getValidInput("Spieler 1, geben Sie bitte eine ganze Zahl von 1 bis 3 ein\n")

def getPlayer2Input():
    if isPlayer2Cpu == True:
        return random.randint(1,3)
    else:
        return getValidInput("Spieler 2, geben Sie bitte eine ganze Zahl von 1 bis 3 ein\n")

while matches >= 2:
    player1Input = getPlayer1Input()
    matches = matches - player1Input
    print(f"Spieler 1", selectedMatchesMsg(player1Input), remainingMatchesMsg(matches) )
    if matches == 0:
        print(f"Spieler 1 hat gewonnen,", remainingMatchesMsg(matches) )
        break
    elif matches == 1:
        print(f"Spieler 1 hat verloren,", remainingMatchesMsg(matches) )
        break
    else:
        player2Input = getPlayer2Input()
        matches = matches - player2Input
        print(f"Spieler 2,", selectedMatchesMsg(player2Input), remainingMatchesMsg(matches) )
        if matches == 0:
            print(f"Spieler 2 hat gewonnen,", remainingMatchesMsg(matches) )
            break
        elif matches == 1:
            print(f"Spieler 1 hat verloren,", remainingMatchesMsg(matches) )
            break 

