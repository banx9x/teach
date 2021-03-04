from random import shuffle


class Deck:
    class Suit:
        def __init__(self, symbol, point) -> None:
            self.symbol = symbol
            self.point = point

        def __eq__(self, o: object) -> bool:
            return self.point == o.point

        def __lt__(self, o: object) -> bool:
            return self.point < o.point

        def __gt__(self, o: object) -> bool:
            return self.point > o.point

        def __str__(self):
            return self.symbol

    class Rank:
        def __init__(self, symbol, point) -> None:
            self.symbol = symbol
            self.point = point

        def __eq__(self, o: object) -> bool:
            return self.point == o.point

        def __lt__(self, o: object) -> bool:
            return self.point < o.point

        def __gt__(self, o: object) -> bool:
            return self.point > o.point

        def __str__(self):
            return self.symbol

        def __int__(self):
            return self.point

    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __lt__(self, o):
            if self.suit < o.suit:
                return True
            elif self.suit > o.suit:
                return False
            else:
                return self.rank < o.rank

        def __str__(self):
            return f"{str(self.rank)}{str(self.suit)}"

        def __int__(self):
            return int(self.rank)

        def __eq__(self, o: object) -> bool:
            return self.suit == o.suit and self.rank == o.rank

    def __init__(self):
        suit = [Deck.Suit(s, i + 1) for i, s in enumerate("♠♣♥♦")]
        rank = [Deck.Rank(s, i + 1) for i, s in enumerate("A23456789")]

        self.cards = [Deck.Card(s, r) for s in suit for r in rank]

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, num_of_players):
        sets = [[] for i in range(num_of_players)]

        for i in range(3):
            for j in range(num_of_players):
                sets[j].append(self.cards.pop())

        return sets

    def __str__(self):
        return " ".join([str(c) for c in self.cards])


def total(_list):
    result = 0
    for i in _list:
        result += int(i)
    return result


num_of_players = int(input("🧑 Số người chơi: "))

deck = Deck()
deck.shuffle()

sets = deck.deal(num_of_players)
sets_str = [[str(i) for i in a] for a in sets]
print(sets_str)

points = [(total(s) % 10 if total(s) % 10 != 0 else 10, max(*s)) for s in sets]
points_str = [(total(s) % 10 if total(s) % 10 != 0 else 10, str(max(*s))) for s in sets]
print(points_str)

max_point = max(*[i[0] for i in points])
players_max_point = [i for i in points if i[0] == max_point]

if len(players_max_point) == 1:
    for i, v in enumerate(points):
        if v[0] == players_max_point[0][0] and v[1] == players_max_point[0][1]:
            print("Người chơi thứ ", i + 1, "chiến thắng")
            print(sets_str[i])
else:
    greatest_card = max(*[i[1] for i in players_max_point])
    for i, v in enumerate(points):
        if v[0] == players_max_point[0][0] and v[1] == greatest_card:
            print("Người chơi thứ ", i + 1, "chiến thắng")
            print(sets_str[i])
