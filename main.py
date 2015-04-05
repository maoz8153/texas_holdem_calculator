import EvalHands
import holdem_gen
from multiprocessing import Process, Queue
import multiprocessing


x = holdem_gen.Card.Card('Ah')
y = holdem_gen.Card.Card('Ad')
player_cards = list()
player_cards.extend([x,y])


def run_hand():
    deck = holdem_gen.gen_deck_without_cards(player_cards)
    board = holdem_gen.gen_board_cards(deck)
    result = holdem_gen.main_process(board,player_cards)
    worker = result
    print worker

num_processes = multiprocessing.cpu_count() - 1



def mp_handler():
    p = multiprocessing.Process(target=run_hand, args=())
    p.start()
    #p = multiprocessing.Pool(3)
    #p.map(run_hand, player_card)

if __name__ == '__main__':
    mp_handler()