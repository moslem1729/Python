import dataclasses
import hashlib
import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json


class Credit(object):
    @staticmethod
    def add_credit(username, bet_amount):
        with open("Accounts.json", "r+") as file:
            accounts = json.load(file)
        if username in accounts:
            accounts[username]["credit"] = accounts[username]["credit"] + bet_amount
        with open("Accounts.json", "w") as file:
            json.dump(accounts, file, indent=4)

    @staticmethod
    def decrease_credit(username, bet_amount):
        with open("Accounts.json", "r+") as file:
            accounts = json.load(file)
        if username in accounts:
            accounts[username]["credit"] = accounts[username]["credit"] - bet_amount

        with open("Accounts.json", "w") as file:
            json.dump(accounts, file, indent=4)

    @staticmethod
    def charge_account(username):
        pass


class Accounts(object):
    @classmethod
    def login(cls):
        choice = input("do you have an account?[Y]es,[N]o :").lower()
        if choice == "y":
            username = input("please enter your username :")
            cls.check_account(username)
            return username
        else:
            choice = input("do you want to create an account?[Y]es,[N]o :").lower()
            if choice == "n":
                exit(0)
            else:
                cls.create_account()
                return cls.login()

    @classmethod
    def check_account(cls, player_username):
        with open("Accounts.json", "r+") as file:
            accounts = json.load(file)
        if player_username in accounts:
            password = input("please enter your password:")
            sha256 = hashlib.sha256
            encoded_password = password.encode()
            hash_password = sha256(encoded_password).hexdigest()
            if accounts[player_username]["hashpass"] == hash_password:
                return player_username
            else:
                print("your password is not correct please try again ")
                cls.login()
        else:
            print("there is no account with this username")
            choice = input("do you want to create an account?[Y]es,[N]o").lower()
            if choice == "n":
                exit(0)
            else:
                cls.create_account()
                cls.login()

    @classmethod
    def create_account(cls):
        name = input("name :")
        family = input("family : ")
        username = input("please enter a username :")
        email_address = input("please enter your email :")
        password = input("please enter a password :").encode()
        sha256 = hashlib.sha256
        hashpass = sha256(password).hexdigest()
        account = Account(name, family, username, email_address, 0, hashpass)
        with open("Accounts.json") as file:
            loaded = json.load(file)
            loaded[account.username] = dataclasses.asdict(account)

        with open("Accounts.json", 'w') as file:
            json.dump(loaded, file, indent=4)


@dataclass_json
@dataclass
class Account:
    name: str
    family: str
    username: str
    email: str
    credit: int
    hashpass: str
