import random


class Cards(object):
    @staticmethod
    def generate_cards():
        print("shuffling...")
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        type_of_cards = ["spade", "heart", "diamond", "club"]
        cards = []
        for number in numbers:
            for element in type_of_cards:
                cards.append([number, element])
        random.shuffle(cards)
        return cards

    @staticmethod
    def deal(cards):
        hand = []
        for i in range(2):
            card = cards.pop()
            if card[0] == 11: card[0] = "J"
            if card[0] == 12: card[0] = "Q"
            if card[0] == 13: card[0] = "K"
            if card[0] == 14: card[0] = "A"
            hand.append(card)
        return hand



    @staticmethod
    def hit(hand,cards):
        card = cards.pop()
        if card[0] == 11: card[0] = "J"
        if card[0] == 12: card[0] = "Q"
        if card[0] == 13: card[0] = "K"
        if card[0] == 14: card[0] = "A"
        hand.append(card)
        return hand
