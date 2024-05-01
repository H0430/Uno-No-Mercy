class Card:
    def __init__(self, color="white", number=0, special_ability=None):
        self.color = color
        self.number = number
        self.special_ability = special_ability
   
    def __str__(self):
        return f"{self.get_card_text()} - {self.color}"
   
    def __repr__(self):
        return f"{self.get_card_text()} - {self.color}"
   
    def get_card_text(self):
        if self.number == 0:
            return self.special_ability
        else:
            return str(self.number)

from network import Network # type: ignore

def main():
    run = True
    n = Network()
    p = n.getP()

    while run:
        p2 = n.send(p)

if __name__ == "__main__":
    main()

class Game:
    def __init__(self, player1, player2, player3, player4):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.previous_player = None
        self.turn = "clockwise"
        self.previous_player = 4
        self.previous_card = None

    def play(self):
        while not self.check_winning():
            next_player = self.get_next_player()
            if next_player == 1:
                self.player1_play()
            elif next_player == 2:
                self.player2_play()
            elif next_player == 3:
                self.player3_play()
            elif next_player == 4:
                self.player4_play()

from card import Card # type: ignore
from subprocess import call
import os

def create_all_cards():
    deck = []
    for color in ["red", "blue", "green", "yellow"]:
        for number in range(1, 10):
            deck.append(Card(color, number, None))
        for special_ability in ["reverse", "skip"]:  # "+2", "wild", "wild+4","swaphands","rotate","skipall","wild+6","wild+10","wild+4reverse","discardall"
            deck.append(Card(color, 0, special_ability))

    deck.extend([Card("black", 0, special_ability) for special_ability in ["swaphands", "rotate", "discardall", "wild+4reverse"]])
    deck.extend([Card("black", 0, "wild") for _ in range(4)])

    return deck

def clear():
    _ = call('clear' if os.name == 'posix' else 'cls')

import random

class Card:
    def __init__(self, color, number, special_ability=None):
        self.color = color
        self.number = number
        self.special_ability = special_ability

    def __str__(self):
        return f"{self.number} {self.special_ability}"

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

def create_all_cards():
    deck = []
    for _ in range(4):
        for color in ["red", "green", "blue", "yellow"]:
            for number in range(1, 10):
                deck.append(Card(color, number, None))
            for special_ability in ["skip", "reverse", "+2", "+4", "+6", "+10", "swaphands", "rotate", "discardall"]:
                deck.append(Card(color, 0, special_ability))
            print(color(str(Card), Card.color))
       
    def prompt_card(self, previous_card, game):
        if previous_card is not None:
            print("The previous card is: " + color(str(previous_card), previous_card.color))
        card = input("Type a card you want to play (format: number/name - color). If there's not a usable card, please type 'draw' to get a new card: ")
        res = self.check_card_valid(card, previous_card, game)
        while not res:
            clear()
            print("The previous card is: " + color(str(previous_card), previous_card.color))
            self.print_cards()
            if card == "draw":
                self.draw_card()
            else:  
                print("Card not found or not valid!")
            card = input("Type a card you want to play (format: number/name - color): ")
            res = self.check_card_valid(card, previous_card, game)
        return self.remove_card(card)

    def check_card_valid(self, card, previous_card, game):
        for c in self.cards:
            if str(c) == card:
                if c.number == previous_card.number or c.color == previous_card.color or c.special_ability == "wild":
                    if c.special_ability == "reverse":
                        game.reverse()
                    if c.special_ability == "skip":
                        game.skip()
                    if c.special_ability == "swaphands":
                        game.swaphands()
                    if c.special_ability == "rotate":
                        game.rotate()
                    if c.special_ability == "discardall":
                        game.discardall()
                    if c.special_ability == "wild":
                        color = input("Type a color: ")
                        c.color = color    
                    return True
        return False

    def remove_card(self, card):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                return c

    def draw_card(self):
        self.cards.append(self.deck.pop(random.randint(0, len(self.deck) - 1)))

class Game:
    def __init__(self, player1, player2, player3, player4):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
   
    def play(self):
        print("Game is starting!")
        # Add game logic here
        print("Game over!")