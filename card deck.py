import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'({self.rank} {self.suit})'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank
                # and self.suit != other.suit)

class Deck:
    def __init__(self):
        self.create()

    def create(self):
        rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        suit = ["d", "h", "c", "s"]
        self.deck = [Card(i, j) for i in rank for j in suit]

    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop(0)

    def sort_deck_by_rank(self):
        self.deck.sort(key=lambda x: x.rank)

    def sort_deck_by_suit(self):
        self.deck.sort(key=lambda x: x.suit)

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, item):
        return self.deck[item]

    def split_to_half(self):
        return self.deck[:26], self.deck[26:]

class Player(Deck):
    def __init__(self, name):
        self.name = name
        # self.deck = []

class Game:
    def __init__(self):
        self.player_1 = Player("One")
        self.player_2 = Player("Two")
        self.war_deck = []

        self.deck = Deck()
        self.deck.create()
        self.deck.shuffle()
        print(self.deck)

        self.player_1.deck, self.player_2.deck = self.deck.split_to_half()

    def game_over(self):
        print("Game over!")
        if self.player_1.deck:
            print(f"{self.player_1.name} won the game.")
        else:
            print(f"{self.player_2.name} won the game.")

    def war(self,x):
        print("War starts now!!!!!!!!!!!!!!!!!!!!!!!!")

        self.war_deck.extend(x)
        for _ in range(3):
            self.war_deck.append(self.player_1.draw())
            self.war_deck.append(self.player_2.draw())

        player1_card = self.player_1.draw()
        player2_card = self.player_2.draw()

        self.war_deck.append(player1_card)
        self.war_deck.append(player2_card)

        print(f"{self.player_1.name} played: {player1_card}")
        print(f"{self.player_2.name} played: {player2_card}")

        if player1_card > player2_card:
            print(f"{self.player_1.name} wins the war!")
            self.player_1.deck.extend(self.war_deck)
            self.war_deck = []
        elif player1_card < player2_card:
            print(f"{self.player_2.name} wins the war!")
            self.player_2.deck.extend(self.war_deck)
            self.war_deck = []
        else:
            print("another war")
            self.war([player1_card, player2_card])

    def play_round(self):
        counter = 0
        stop = 1000
        while len(self.player_1.deck) > 0 and len(self.player_2.deck) > 0 and stop > counter:
            print(f'player 1 has: {len(self.player_1.deck)}')
            print(f'player 2 has: {len(self.player_2.deck)}')

            counter +=1
            print(f"round no. {counter}")
            card_1 = self.player_1.draw()
            card_2 = self.player_2.draw()

            print(f"{self.player_1.name} has drawn: {card_1}")
            print(f"{self.player_2.name} has drawn: {card_2}")

            if card_1 > card_2:
                print(f"{self.player_1.name} won!")
                self.player_1.deck.extend([card_1, card_2])
            elif card_1 < card_2:
                print(f"{self.player_2.name} won!")
                print (len(self.player_2.deck))
                self.player_2.deck.extend([card_1, card_2])

            if card_1 == card_2:
                if len(self.player_1.deck) > 4 and len(self.player_2.deck) > 4:
                    self.war([card_1, card_2])
                else:
                    print("nobody won")
                    self.game_over()
            print("\n")

        self.game_over()

# Example usage:
game_instance = Game()
game_instance.play_round()




