class Results(object):
    results = []

    @classmethod
    def send_result(cls):
        for item in cls.results:
            if item["player"] == "win":
                print("you win")
                item["player_account"].increase_bet_amount_to_credit(item["bet_amount"])
            else:
                print("you lose")
                print(item)
                item["player_account"].decrease_bet_amount_from_credit(item["bet_amount"])



    @classmethod
    def check_hands(cls, player_hand, dealer_hand, bet_amount, player_account):
        if cls.total(player_hand) == cls.total(dealer_hand):
            cls.push(player_hand, dealer_hand, bet_amount, player_account)
        else:
            if cls.total(dealer_hand) > 21:
                cls.busted(False, player_hand, dealer_hand, bet_amount, player_account)
            else:
                if cls.total(player_hand) > cls.total(dealer_hand):
                    result = {"player": "win", "bet_amount": bet_amount, "player_hand": player_hand,
                              "dealer_hand": dealer_hand, "player_account": player_account}
                    cls.results.append(result)
                else:
                    result = {"player": "lose", "bet_amount": bet_amount, "player_hand": player_hand,
                              "dealer_hand": dealer_hand, "player_account": player_account}
                    cls.results.append(result)

    @classmethod
    def push(cls, player_hand, dealer_hand, bet_amount,player_account):
        result = {"player": "draw", "bet_amount": bet_amount, "player_hand": player_hand,
                  "dealer_hand": dealer_hand,"player_account":player_account}
        cls.results.append(result)

    @classmethod
    def busted(cls, is_player_busted, player_hand, dealer_hand, bet_amount,player_account):
        if is_player_busted:
            result = {"player": "lose", "bet_amount": bet_amount, "player_hand": player_hand,
                      "dealer_hand": dealer_hand,"player_account":player_account}
            cls.results.append(result)
        else:
            result = {"player": "win", "bet_amount": bet_amount, "player_hand": player_hand,
                      "dealer_hand": dealer_hand,"player_account":player_account}
            cls.results.append(result)

    @classmethod
    def is_busted(cls, hand):
        if cls.total(hand) > 21:
            return True
        else:
            return False

    @staticmethod
    def total(hand):
        total = 0
        for card in hand:
            if card[0] == "J" or card[0] == "Q" or card[0] == "K":
                total += 10
            elif card[0] == "A":
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += card[0]
        return total
