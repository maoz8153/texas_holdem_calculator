suit_index_dict = {"s": 0, "c": 1, "h": 2, "d": 3}
reverse_suit_index = ("s", "c", "h", "d")
val_string = "AKQJT98765432"
hand_rankings = ("High Card", "Pair", "Two Pair", "Three of a Kind",
             "Straight", "Flush", "Full House", "Four of a Kind",
             "Straight Flush", "Royal Flush")
suit_value_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
for num in xrange(2, 10):
    suit_value_dict[str(num)] = num

class Card:


    def __init__(self, card_string):
        value, self.suit = card_string[0], card_string[1]
        self.value = suit_value_dict[value]
        self.suit_index = suit_index_dict[self.suit]

    def __str__(self):
        return val_string[14 - self.value] + self.suit

    def __repr__(self):
        return val_string[14 - self.value] + self.suit

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    # def __init__(self):
    #     self.shap = ''
    #     self.cardvalue = ''
    #     self.id = {self.cardvalue + self.shap : [self.cardvalue , self.shap ] }
    #
    # @property
    # def shap(self):
    #     return self.shap
    #
    # @shap.setter
    # def shap(self, value):
    #     self.shap = value
    #
    # @property
    # def cardvalue(self):
    #     return self.cardvalue
    #
    # @cardvalue.setter
    # def cardvalue(self, value):
    #     self.cardvalue = value
    #
    # def create_card(self, shap, value):
    #     self.cardvalue = value
    #     self.shap = shap
    #     self.id = {self.cardvalue + self.shap : [self.cardvalue , self.shap ] }
    #     return {self.cardvalue + self.shap : [self.cardvalue , self.shap ] }

