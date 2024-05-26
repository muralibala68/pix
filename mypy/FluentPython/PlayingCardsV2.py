import random
from typing import List, Tuple, NamedTuple


# using typing.NamedTuple instead of collections.namedtuple for better type hinting
class Card(NamedTuple):
    rank: str
    suit: str


Cards = List[Card]


class FrenchDeck:
    suits = ['spade', 'heart', 'diamond', 'club']
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")

    def __init__(self):
        self.cards: Cards = [Card(r, s) for r in self.ranks
                                        for s in self.suits]

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return str(self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> Tuple[Cards, Cards, Cards, Cards]:
        return self.cards[0::4], self.cards[1::4], self.cards[2::4], self.cards[3::4]


def main():
    print(FrenchDeck)
    f_deck = FrenchDeck()
    print(f_deck)
    print(len(f_deck))
    print(f_deck[0])
    print(f_deck[1::2])

    print("-----------------")
    print("before shuffling:", f_deck)
    f_deck.shuffle()
    print("after shuffling:", f_deck)
    players: (Cards, Cards, Cards, Cards) = f_deck.deal()
    print("Players/Deal", type(players), "of size", len(players))
    for player in players:
        print("Player", type(player), "of size", len(player))
        print(player)
    print("-----------------")


if __name__ == "__main__":
    main()
