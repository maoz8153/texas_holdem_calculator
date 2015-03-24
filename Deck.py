import random
from Card import *
from Hand import *
from EvalHands import evalhands
import holdem_gen


class Deck():
    def __init__(self):
        self.deck = []
        shaps = ['h', 'd', 'c', 's']
        val_string = "AKQJT98765432"

        for shap in shaps:
            for cardvalue in val_string:
                x = Card(cardvalue + shap )
                self.deck.append(x)

        random.shuffle(self.deck)
        self.deck = tuple(self.deck)

    def deal_cards(self):
        rand_card = self.cards[0]
        self.cards.pop(0)
        return rand_card

    def cards_in_deck(self):
        return len(deck.cards)

    def remove_cards(self,*arg):
        for id in arg:
            self.deck.remove(id)


    def search_shap(self, shap_to_search):
        counter = 0
        for card in deck.cards:
            if card.shap == shap_to_search:
                counter += 1
        return  counter




deck = Deck()
a = Card('Ah')
b = Card('Ac')
c = Card('Ad')
d = Card('As')
e = Card('Th')
y = evalhands(a,b,c,d,e)
y.hand_result()


# y.cardvalue = '10'
# y.shap = 'd'
#
# z = Card()
# z.cardvalue = '11'
# z.shap = 'h'
#
# a = Card().create_card('11','c')
#
# b = Card()
# b.cardvalue = '10'
# b.shap = 'h'
#
# c = Card()
# c.cardvalue = '10'
# c.shap = 'c'
# deck.remove_cards(a.id)
# y = deck.deal_cards()
# z = deck.deal_cards()
# a = deck.deal_cards()
# b = deck.deal_cards()
# c = deck.deal_cards()

# hand = Hand(y,z,a,b,c)
# print hand.value_list
# ev = hand.result
#
# print (ev)
