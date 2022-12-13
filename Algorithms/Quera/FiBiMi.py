

class Freind:
    def __init__(self,frontend,backend,money):
        self.frontend=frontend
        self.backend=backend
        self.money=money


def is_okey(first_freind,second_freind):
    if (first_freind.backend>second_freind.backend) ^ (first_freind.frontend>second_freind.frontend):
        return True
    return False



