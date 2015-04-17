from collections import Counter
import Hand
import operator
class evalhands():

    hand_renking =  {'high_card': 1, 'pair': 2, 'two_pairs': 3, 'three _of_a_kind': 4, 'straight': 5,
                     'flush': 6, 'full_house': 7, 'four_of_a_kind': 8, 'straight_flush': 9}

    def __init__(self, hand):
        self.result = dict()
        self.value_list = []
        self.shap_list = []
        self.cards_list = {}
        for card in hand:
            self.value_list.append(card.value)
            self.shap_list.append(card.suit)
            self.cards_list[str(card.value) + card.suit] = {card.value: card.suit}

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

    # return array of value hand, hand string, kickers
    def check_pair_or_more(self):
        values = dict()
        for i in range(5):
                if self.value_list[i] in values:
                    values[self.value_list[i]] += 1
                else:
                    values[self.value_list[i]] = 1

        values = sorted(values.items(), key=lambda x: (x[1],x[0]), reverse=True)
        if len(values) == 2:
            if values[0][1] == 4:
                res = 'four of a kind {0}'.format(values[0][0])
                return [8, res, values[0][0], values[1][0]]
            else:
                res = 'full house{0} over {1}'.format(values[0][0],values[1][0])
                return [7 , res, values[0][0],values[1][0]]
        elif len(values) == 3:
            if values[0][1] == 3:
                res = 'three of a kind{0}'.format(values[0][0])
                return [4 ,res,values[0][0],values[1][0],values[2][0]]
            if values[0][1] == 2 and  values[1][1] == 2:
                res = ['two pairs {0} and {1}'.format(values[0][0],values[1][0]), [values[0][0],values[1][0]]]
                return [3 , res,values[0][0],values[1][0],values[2][0]]
        elif len(values) == 4 :
            res = 'pairs {0} '.format(values[0][0])
            return [2, res,values[0][0],values[1][0],values[2][0],values[3][0]]
        elif len(values) > 4:
            res = 'high card {0} '.format(self.value_list[-1])
            return [1,res, self.value_list]



    def check_straight(self):
        values = list(self.value_list)
        if str(14) in str(values):
            if str(2) in str(values):
                for val in self.value_list:
                    if val == 14:
                        values.remove(val)
                        values.append(1)
                values.sort()
        straigh = True
        for i in range(3):
            if int(values[i] + 1) == values[i + 1]:
                continue
            else:
                straigh = False
                break
        if straigh:
            return [5,'straigh',self.value_list[-1]]
        else:
            return False


    def check_flush(self):
        flush = True
        for i in range(1, 5, 1):
            if self.shap_list[0] == self.shap_list[i]:
                continue
            else:
                flush = False
                break
        if flush:
            return [6 , 'flush' ,self.value_list[-1]]
        else:
            return False


    # return reuslt with agrument as 1.result 2.kicker 3.suit
    def hand_result(self):
        straight = self.check_straight()
        flush = self.check_flush()
        if straight:
            if flush:
                #self.result = [flush, self.value_list[-1]]
                return flush
            else:
                #self.result = [straight, self.value_list[-1]]
                return  straight
        if flush:
            #self.result = [flush, self.value_list[-1]]
            return flush
        pair_or_more = self.check_pair_or_more()
        #self.result = pair_or_more
        return pair_or_more

    def quad_kicker(self, val):
        kicker = list()
        if val == self.value_list[0]:
            kicker = self.value_list[-1]
        else:
            kicker = self.value_list[0]
        return kicker

    def triple_kicker(self, val):
        kicker = list()
        for value in self.value_list:
            if val != value:
                kicker.append(value)
        kicker.sort()
        return kicker

    def pair_kicker(self, val):
        kicker = list()
        for value in self.value_list:
            if val != value:
                kicker.append(value)
        kicker.sort()
        return kicker







