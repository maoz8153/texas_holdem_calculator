from Deck import *
from Hand import *

class Prob():
    max_cards = 7
    max_card_in_hand = 5

    def __init__(self, hand, deck, board):
        self.number_of_cards = len(hand.cards)
        self.num_board_cards = len(board.cards)
        self.cards_left = len(deck.cards) - self.number_of_cards - self.num_board_cards
        self.pro_shap_list = hand.shap_list + board.shap_list
        self.pro_value_list = hand.value_list + board.value_list
        self.grop = ''


        # if self.num_board_cards > 0 :
        #     self.shap_list = hand.shap_list + board.shap_list
        #     self.value_list = hand.value_list + board.value_list
        # else:
        #    self.shap_list = hand.shap_list
        #    self.value_list = hand.value_list

    def suit(self):
        if self.shap_list[0] == self.shap_list[1]:
            return True

    def group_prob(self):
        gap = 0
        if self.value_list[0] == self.value_list[1]:
            self.grop = 'pocket_pair'
        else:
            if '1' in self.value_list:
                gap = abs(self.value_list[0] - self.value_list[1])
                if gap > 4:
                    for index, val in enumerate(self.value_list):
                        if val == '1':
                            self.value_list[index] == '14'
                            break
                    gap = abs(self.value_list[0] - self.value_list[1])









