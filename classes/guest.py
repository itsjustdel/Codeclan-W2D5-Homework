class Guest:
    def __init__(self, name, fav_song, money):
        self.name = name
        self.fav_song = fav_song
        self.money = money

    def has_enough_money(self, amount):
        if self.money >= amount:
            return True
        else:
            return False

    def reduce_money(self, amount):
        self.money -= amount

    def pay_in(self, entry_fee):
        if(self.has_enough_money(entry_fee)):
            # if guest has enough money, reduce guest's money
            self.reduce_money(entry_fee)
            # return True for a successful payment
            return True
        else:
            # customer doesn't have enough money, return False
            # for an unsuccessful transaction
            return False

    def cheer_loudly(self):
        return "Woohoo!"

    def add_drink_to_tab(self,bar, drink_name, room):

        #customer requests drink, bar puts it on tab for room


