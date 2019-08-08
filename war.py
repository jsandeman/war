from random import shuffle

class Card:
    ranks = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
    suits = ["clubs", "diamonds", "hearts", "spades"]
    def __init__(self, r, s):
        self.rank = self.ranks[r]
        self.suit = self.suits[s]

    def __repr__(self):
        return self.rank + " of " + self.suit

    def __str__(self):
        return self.rank + " of " + self.suit

    def __gt__(self, c2):
        if self.ranks.index(self.rank) > self.ranks.index(c2.rank):
            return True
        else:
            if self.ranks.index(self.rank) == self.ranks.index(c2.rank):
                return self.suits.index(self.suit) > self.suits.index(c2.suit)
            return False

    def __lt__(self, c2):
        return not self > c2

class Deck:

    def __init__(self):
        self.deck = []
        for i in range(2, 15):
            for j in range(0,4):
                self.deck.append(Card(i,j))
        shuffle(self.deck)

    def draw_card(self):
        if len(self.deck) == 0:
            return
        return self.deck.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

deck = Deck()
name1 = input("Player 1 name: ")
name2 = input("Playe 2 name: ")
if name1 == None or name2 == None:
    exit()
player1 = Player(name1)
player2 = Player(name2)

while True:
    if input("c to continue, q to quit: ") == 'q':
        break
    player1.card = deck.draw_card()
    player2.card = deck.draw_card()
    if player1.card == None or player2.card == None:
        break
    print(player1.name + " draws " + str(player1.card))
    print(player2.name + " draws " + str(player2.card))
    if player1.card > player2.card:
        print(player1.name +  " wins!")
        player1.wins += 1
    else:
        print(player2.name + " wins!")
        player2.wins += 1

if player1.wins > player2.wins:
    print(player1.name + " wins the game!")
elif player1.wins < player2.wins:
    print(player2.name + " wins the game!")
else:
    print("The game ends in a tie!")

