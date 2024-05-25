import random
from collections import namedtuple
from typing import List


class FrenchDeck:
    Card = namedtuple('Card', ['rank', 'suit'])
    Deck = List[Card]

    suits = ['spade', 'heart', 'diamond', 'club']
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")

    def __init__(self):
        self.deck = [self.Card(r, s) for r in self.ranks for s in self.suits]

    def __repr__(self):
        return str(self.deck)

    def __str__(self):
        return str(self.deck)

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        print(self.deck)
        random.shuffle(self.deck)
        print(self.deck)

    def deal(self) -> Card:
        return random.choice(self.deck)


def main():
    f_deck = FrenchDeck()
    print(f_deck)
    print(len(f_deck))
    f_deck.shuffle()
    print(f_deck.deal())


if __name__ == "__main__":
    main()
