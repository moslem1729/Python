from Accounts import Accounts
from Cards import Cards
from Results import Results


#
# # class account is responsible for the player name and amount of money
# class Account(object):
#     def __init__(self, name, family, username, email):
#         self.name = name
#         self.family = family
#         self.username = username
#         self.email = email
#         self.credit = 0
#     # charge the account
#     def charge_account(self, amount):
#             self.credit += amount
#
#     def decrease_money(self,bet_amount):
#         self.credit-=bet_amount
#
#
#
# class PlayPlayer(object):
#     def __init__(self,cards,player_hand,dealer_hand):
#         self.cards=cards
#         self.player_hand=player_hand
#         self.dealer_hand=dealer_hand
#
#
#     @staticmethod
#     def player_turn(self):
#         if self.player_hand[0][0] == self.player_hand[1][0] and self.dealer_hand[1][0] == "A":
#             choice = input("Do you want to [H]it, [S]tand, [S]plit or [I]nsurance :").lower()
#         elif self.player_hand[0][0] == self.player_hand[1][0]:
#             choice = input("Do you want to [H]it, [S]tand or [S]plit :").lower()
#         elif self.dealer_hand[1][0] == "A":
#             choice = input("Do you want to [H]it, [S]tand or [I]nsurance :").lower()
#         else:
#             choice = input("Do you want to [H]it or [S]tand :").lower()
#         if choice=="h":
#             self.hit(self.player_hand,self.cards)
#
#     @staticmethod
#     def hit(hand, cards):
#         card = cards.pop()
#         if card[0] == 11: card[0] = "J"
#         if card[0] == 12: card[0] = "Q"
#         if card[0] == 13: card[0] = "K"
#         if card[0] == 14: card[0] = "A"
#         hand.append(card)
#         return hand
#
#
#     @staticmethod
#     def busted(self,bet_amount):
#         print("busts")
#         self.player.credit-=bet_amount
#     @staticmethod
#     def lose(self,bet_amount):
#         print("loses")
#         self.player.credit-=bet_amount
#
#     @staticmethod
#     def win(self,bet_amount):
#         print("wins")
#         self.player.credit+=bet_amount
#
# class Dealer(object):
#     def __init__(self,dealer):
#         self.dealer=dealer
#     @staticmethod
#     def hit(dealer_hand, cards):
#         while Game.total(dealer_hand)<17:
#             Game.hit(dealer_hand,cards)
#         return dealer_hand
#
#
#
#
# # generating Cards
# class Cards(object):
#     def __init__(self):
#         self.cards = self.generate_cards()
#
#     @staticmethod
#     def generate_cards():
#         numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#         type_of_cards = ["spade", "heart", "diamond", "club"]
#         cards = []
#         for number in numbers:
#             for element in type_of_cards:
#                 cards.append([number, element])
#         return cards
#
#
#
#
#
# class Game(object):
#     def __init__(self):
#         self.account = None
#         self.cards = []
#         self.bet_amount = 0
#
#     # calculate hand
#     @staticmethod
#     def total(hand):
#         total = 0
#         for card in hand:
#             if card[0] == "J" or card[0] == "Q" or card[0] == "K":
#                 total += 10
#             elif card[0] == "A":
#                 if total >= 11:
#                     total += 1
#                 else:
#                     total += 11
#             else:
#                 total += card[0]
#         return total
#
#     # # clear the space after each game
#     # def clear(self):
#     #     if os.name == 'nt':
#     #         os.system('CLS')
#     #     if os.name == 'posix':
#     #         os.system('clear')
#
#     # def play_again(self):
#     #     again = input("Do you want to play again? (Y/N) : ").lower()
#     #     if again == "y":
#     #         self.game()
#     #     else:
#     #         print("Bye!")
#     #         exit()
#
#     # print the winner and calculate the credit of player
#     def calculate_score(self, winner):
#         print("winner is :", winner)
#         if winner == "player":
#             self.account.charge_account(self.bet_amount)
#         else:
#             self.account.decrease_credit(self.bet_amount)
#         print("you have :", self.account.credit)
#
#     def game(self):
#         player_money = self.account.credit
#         print("you have: ", player_money)
#         bet_amount = int(input("how much do you bet:"))
#         if bet_amount > player_money:
#             print("Your account balance is insufficient, please charge your account and try again.")
#         else:
#             self.start_game(bet_amount)
#
#     @staticmethod
#
#
#     @staticmethod
#     def deal(cards):
#         hand = []
#         for i in range(2):
#             random.shuffle(cards)
#             card = cards.pop()
#             if card[0] == 11: card[0] = "J"
#             if card[0] == 12: card[0] = "Q"
#             if card[0] == 13: card[0] = "K"
#             if card[0] == 14: card[0] = "A"
#             hand.append(card)
#         return hand
#
#     def preparing_game(self, bet_amount):
#         cards = Cards()
#         game_cards=cards.cards
#         if
#
#         player_hand = self.deal(self.cards)
#         dealer_hand = self.deal(self.cards)
#
#
#
#
# class BlackJackPlay(object):
#     def __init__(self,cards,player_hand,dealer_hand):
#         self.cards=cards
#         self.player_hand=player_hand
#         self.dealer_hand=dealer_hand
#
#     def split(self,cards,player_hand,dealer_hand):
#         player_hand=player_hand.pop()
#         self.hit(player_hand,cards)
#
#
#     @staticmethod
#     def hit(hand, cards):
#         card = cards.pop()
#         if card[0] == 11: card[0] = "J"
#         if card[0] == 12: card[0] = "Q"
#         if card[0] == 13: card[0] = "K"
#         if card[0] == 14: card[0] = "A"
#         hand.append(card)
#         return hand
#
#         # while True:
#         #     print(str(dealer_hand[1]))
#         #     print(str(player_hand))
#         #     if player_hand[0][0] == player_hand[1][0] and dealer_hand[1][0] == "A":
#         #         choice = input("Do you want to [H]it, [S]tand, [S]plit or [I]nsurance :").lower()
#         #     elif player_hand[0][0] == player_hand[1][0]:
#         #         choice = input("Do you want to [H]it, [S]tand or [S]plit :").lower()
#         #     elif dealer_hand[1][0] == "A":
#         #         choice = input("Do you want to [H]it, [S]tand or [I]nsurance :").lower()
#         #     else:
#         #         choice = input("Do you want to [H]it or [S]tand :").lower()
#         #
#         #     if choice == "h":
#         #         self.hit(player_hand, cards)
#         #         while self.total(player_hand) < 21 and choice == "h":
#         #             print(str(dealer_hand[1]))
#         #             print(str(player_hand))
#         #             self.hit(player_hand, cards)
#         #             choice = input("Do you want to [H]it, [S]tand :").lower()
#         #
#         #         if self.total(player_hand) > 21:
#         #             winner = "dealer"
#         #             print(str(dealer_hand))
#         #             print(str(player_hand))
#         #             self.calculate_score(winner, bet_amount)
#         #         else:
#         #             while self.total(dealer_hand) < 17:
#         #                 self.hit(dealer_hand)
#         #             if self.total(dealer_hand) > 21:
#         #                 winner = "player"
#         #                 print(str(dealer_hand))
#         #                 print(str(player_hand))
#         #                 self.calculate_score(winner, bet_amount)
#         #             else:
#         #                 winner = self.score(dealer_hand, player_hand)
#         #                 print(str(dealer_hand))
#         #                 print(str(player_hand))
#         #                 self.calculate_score(winner, bet_amount)
#         #     elif choice == "s":
#         #         while self.total(dealer_hand) < 17:
#         #             self.hit(dealer_hand, cards)
#         #         if self.total(dealer_hand) > 21:
#         #             winner = "player"
#         #             print(str(dealer_hand))
#         #             print(str(player_hand))
#         #             self.calculate_score(winner, bet_amount)
#         #         else:
#         #             winner = self.score(dealer_hand, player_hand)
#         #             print(dealer_hand)
#         #             print(player_hand)
#         #             self.calculate_score(winner, bet_amount)
#
#
# money = Money(1500)
# moslem = Player("moslem", money)
# game = Game(moslem)
# game.game()


class Blackjack(object):
    def __init__(self):
        self.player_account = Accounts.login()
        self.cards = Cards.generate_cards()

    def game(self):
        game = BjGame(self.cards, self.player_account)
        game.play()


class BjGame(object):
    def __init__(self, cards, player_account):
        self.cards = cards
        self.player_account = player_account
        self.bet_amount = 10

    def play(self,* arr):
        player_hand = Cards.deal(self.cards)
        dealer_hand = Cards.deal(self.cards)
        self.player_turn(player_hand, dealer_hand)

    def player_turn(self, player_hand, dealer_hand):
        print(str(dealer_hand[1]))
        print(str(player_hand))
        if player_hand[0][0] == player_hand[1][0] and dealer_hand[1][0] == "A":
            choice = input("Do you want to [H]it, [S]tand, [S]plit or [I]nsurance :").lower()
        elif player_hand[0][0] == player_hand[1][0]:
            choice = input("Do you want to [H]it, [S]tand or [S]plit :").lower()
        elif dealer_hand[1][0] == "A":
            choice = input("Do you want to [H]it, [S]tand or [I]nsurance :").lower()
        else:
            choice = input("Do you want to [H]it or [S]tand :").lower()

        if choice == "h":
            self.player_hit(player_hand, dealer_hand)

    def player_hit(self, player_hand, dealer_hand):
        choice = "h"
        while True:
            if choice == "h":
                player_hand = Cards.hit(player_hand, self.cards)
                if Results.total(player_hand) < 21:
                    print(str(dealer_hand[1]))
                    print(str(player_hand))
                    choice = input("Do you want to [H]it or [S]tand :").lower()
                elif Results.total(player_hand) > 21:
                    Results.busted(True, player_hand, dealer_hand, self.bet_amount, self.player_account)
                    break
                else:
                    break
            else:
                break
        self.dealer_turn(player_hand, dealer_hand)

    def dealer_turn(self, player_hand, dealer_hand):
        while Results.total(dealer_hand) < 17:
            dealer_hand = Cards.hit(dealer_hand,self.cards)
        Results.check_hands(player_hand, dealer_hand, self.bet_amount, self.player_account)
        Results.send_result()

    def play_again(self):
        again = input("Do you want to play again? (Y/N) : ").lower()
        if again == "y":
            if len(self.cards) > 0:
                self.play()
            else:
                self.cards = Cards.generate_cards()
                self.play()
        else:
            print("Bye!")
            exit()


blackjack = Blackjack()
blackjack.game()
