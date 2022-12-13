from Accounts import Accounts
from Cards import Cards
from Results import Results

class Blackjack(object):
    def __init__(self):
        self.player_account=Accounts.login()
        self.cards=Cards.generate_cards()
    @classmethod
    def game(cls,* arr):
        game=Bj
        if len(arr)==0:
            pass



