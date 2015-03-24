import collections
import copy
import operator
import Card

class Hand():
    hand_renking = [ 'high_card', 'pair', 'two_pairs', 'three _of_a_kind', 'straight',
                     'flush', 'full_house', 'four_of_a_kind', 'straight_flush']
    def __init__(self, hand_cards):
        # cards_list = list()
        # for card in args:
        #     cards_list.append(Card(card))
        self.value_list = []
        self.shap_list = []
        self.cards_list = dict()
        for card in hand_cards:
            val = self.get_card_value(card.cardvalue)
            valshap = self.shap_and_val(val,card.shap)
            self.value_list.append(val)
            self.shap_list.append(card.shap)
            self.cards_list[valshap] = val

        self.sort_card()

    def sort_card(self):
        self.shap_list = [y for (x,y) in sorted(zip(self.value_list, self.shap_list))]
        self.value_list.sort()

    def add_card(self, card):
        self.value_list = list.append(card.cardvalue)
        self.shap_list = list.append(card.shap)

    def make_val_shap(self, card):
        val = self.get_card_value(card.cardvalue)
        val_shap = str(self.get_card_value(card.cardvalue)) + card.shap
        return {val_shap,val}

    def shap_and_val(self, value, shap):
        shapval = str(self.get_card_value(value)) + shap
        return shapval


    @staticmethod
    def get_card_value(value):
        if value in ['J', 'Q', 'K', 'A']:
            if value == 'J':
                return 11
            if value == 'Q':
                return 12
            if value == 'K':
                return 13
            if value == 'A':
                return 14
        else:
            return int(value)

    def check_pair_or_more(self):
        values = dict()
        for i in range(0,4,1):
            for ii in range(i + 1,5,1):
                if i != ii:
                    if self.value_list[i] == self.value_list[ii]:
                        if self.value_list[i] in values:
                            val_shap = self.shap_and_val(self.value_list[i], self.shap_list[i])
                            if val_shap in self.cards_list.keys():
                                self.cards_list.pop(val_shap)
                                values[self.value_list[i]] += 1
                        else:
                            values[self.value_list[i]] = 2
                            val_shap = self.shap_and_val(self.value_list[i], self.shap_list[i])
                            self.cards_list.pop(val_shap)
                            #val_shap2 = self.shap_and_val(self.value_list[ii], self.shap_list[ii])
                            #self.cards_list.pop(val_shap2)

        if len(values):
            if len(self.cards_list) > 0:
                #left_hand = dict(zip(left_values, left_shaps))
                return values
            else:
                return values
        else:
            return False

    def check_straight(self):
        if str(14) in str(self.value_list):
            if str(2) in str(self.value_list):
                self.value_list[-1].pop()
                self.value_list.append('1')
                self.sort_card()
        straigh = True
        for i in range(3):
            if int(self.value_list[i] + 1) == self.value_list[i+1]:
                continue
            else:
                straigh = False
                break
        if straigh:
            return {straigh :  self.value_list[-1]}
        else:
            return False

    def check_flush(self):
        flush = True
        for i in range(1,5,1):
            if self.shap_list[0] == self.shap_list[i]:
                continue
            else:
                flush = False
                break
        if flush:
            return  {flush : self.value_list[-1]}
        else:
            return False


    @property
    def result(self):
        straight = self.check_straight()
        flush = self.check_flush()
        if straight:
            if flush:
                return {'straight flush': flush[True]}
            else:
                return {'straight': straight[True]}
        if flush:
            return {'flush': flush[True]}
        pair_or_more = self.check_pair_or_more()
        if pair_or_more:
            if len(pair_or_more) > 1:
                s_dict = dict(sorted(pair_or_more.iteritems(), key=operator.itemgetter(1), reverse=True)[:2])
                if max(s_dict.values()) == 3:
                    return 'full house {0} over {1}'.format(s_dict.keys()[0], s_dict.keys()[1])
                else:
                    return 'two pairs {0} and {1}'.format(max(s_dict.keys()), min(s_dict.keys()))

            else:
                return 'pair of {0}'.format(pair_or_more.keys())