class Card:
    colors = {
        "Ca": (0, "♦️"),
        "Tr": (1, "♣️"),
        "Co": (2, "❤️"),
        "Pi": (3, "♠️"),
    }
    values = list(str(i) for i in range(2, 11)) + list("JQKA")
    def __init__(self, num, col):
        if num not in self.values:
            raise ValueError(f"{num} n'est pas um nombre de carte.")
        
        if col not in self.colors.keys():
            raise ValueError(f"{col}  n'est pas une couleur valable.")
        
        self.num = num
        self.col = col

    @property
    def value(self):
        ind = self.values.index(self.num) # 0 pour un 2 et 13 pour l'as
        col_value = self.colors.get(self.col)[0]
        return ind * 4 + col_value

    def __repr__(self):
        return f"Card : ({self.num}, {self.col})"
    
    def __str__(self):
        return f"{self.num} {self.colors[self.col][1]}"
    
    def __eq__(self, other_card):
        return (self.num == other_card.num) & (self.col == other_card.col)
    
    def __lt__(self, other_card):
        return self.value < other_card.value
    
card = Card("A", "Co")
card_2 = Card("10", "Tr")
card_3 = Card("10", "Tr")
print(card)
print([card, card_2])
