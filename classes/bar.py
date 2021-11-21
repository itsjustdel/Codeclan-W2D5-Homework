class Bar:
    def __init__(self):
        self.drinks = { "Pina Colada" : 6.95, 
                        "Beer" : 3.50, 
                        "Wine" : 5.00
                        }

    def add_drink_to_tab(self, drink_name, room):
        # check if bar has requested drink before adding to bar tab
        if drink_name in self.drinks:
            room.bar_tab.append(drink_name)