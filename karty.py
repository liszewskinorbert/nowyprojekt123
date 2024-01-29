# To jest mój pierwszy program
#print("Hello World")

import random

# stale przedstawiajace karty
SUT_TUPLE = ('pik', 'kier', 'trefl', 'karo')
RANK_TUPLE = ('as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'walet', 'dama', 'krol')
NCARDS = 8

#przekazanie talii. Wartoscia zwrotna jest losowo wybrana karta z talii
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

#przekazanie talii. Wartoscia zwrotna funkcji jest talia, w ktorej karty sa ulozone losowo
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

#Kod glowny programu
print("""
Witaj w grze wieksza czy mniejsza
Musisz odgadnać, czy następna wyświetlona karta będzie miała 
wartość większą czy mniejszą, od aktualnej karty.
Jeżeli zgadniesz, zdobywasz 20 punktów. W przeciwnym razie
tracisz 15 punktów. Na początek masz 50 punktów.
""")

startingDeckList = []
for suit in SUT_TUPLE:
    for thisValue,rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print("Pierwsza widoczna karta to:", currentCardRank+ " of "+ currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS): #Jedna gra z tych wielu kard
        answer = input("Jaka będzie następna karta: większa czy mniejsza niż " + currentCardRank+currentCardSuit+ "?(wpisz w lub m):")
        answer = answer.casefold() #małe litery
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print("Następna karta to :", nextCardRank, nextCardSuit)

        if answer == "w":
            if nextCardValue > currentCardValue:
                print("Masz rację, karta miała większą wartość.")
                score = score + 20
            else:
                print("Niestety, karta nie miała większe wartości.")
                score = score - 15

        elif answer == "m":
            if nextCardValue < currentCardValue:
                print("Masz rację, karta miała niższą wartość.")
                score = score + 20
            else:
                print("Niestety, karta nie miała mniejszej wartości")
                score = score - 15

        print("Twoj wynik to: ", score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input("Nacisnij Enter, aby zagrać ponownie. 'q' kończy grę:")
    if goAgain == "q":
        break

print("Żegnaj !!!")

