from address import Address #Импортируем класс Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return f"To: {self.to_address},From: {self.from_address},Cost: {self.cost}, Track: {self.track}"

