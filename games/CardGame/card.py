#  Python Card GAme 

#  TRIDIB BAG GSSOC'22

import random
import sys

class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660'] 
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, rank=0):
        """Default constructor """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation """
        return '%s %s' % (Card.suits[self.suit], Card.ranks[self.rank])
     

   


class Deck:
    def __init__(self):
        """Initializes the Deck with 52 cards."""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        """Returns a string representation of the deck."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def __len__(self):
        """Overriding len operator"""
        return len(self.cards)


    def wincard(self, cards):
        """Get the highest winner card from list"""
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.wincount = 0



def play(argv):
    deck = Deck()  
    hands = []
    for i in range(1, 5):
        player = 'Player %d' % i  
        if len(argv) > i:
            player = argv[i]  
        hands.append(Hand(player))  

    while len(deck) > 0:
        for hand in hands: 

    print(hands[0])  
    input("Lets start playing. Press any key to continue : ") 

    for i in range(1, 14):
        cards = [] 
        floors = [] 
        for hand in hands:
            card = hand.pop_card()
            cards.append(card) 
            floors.append(hand.getlabel() + " : " + str(card)) 

        winner_card = deck.wincard(cards)  
        winner_hand = hands[cards.index(winner_card)] 
        print("Round", i, ":-", ", ".join(floors), ", Winner :- ", winner_hand.getlabel(), ":", winner_card)
        input() 
    for hand in hands:  
        print("Score for", hand.getlabel(), "is", hand.getwincount())


def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        play(argv)
        answer = input("Play Again (Y/N)? : ")
    print("Bye Bye")


if __name__ == '__main__':
    main(sys.argv)