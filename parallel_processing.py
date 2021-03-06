import multiprocessing
import EvalHands
import holdem_gen
import time


def parallel_process(opponent_cards):
    test = 0
    player_hand = parallel_process.player_hand
    board = parallel_process.board_cards
    result_list = parallel_process.result_history
    proc_id = int(multiprocessing.current_process().name[-1]) - 1
    proc = multiprocessing.current_process()
    result = holdem_gen.main_process(board, opponent_cards)
    f_result = holdem_gen.compair_hands(player_hand, result)
    if f_result == result:
        test = test + 1
    return result ,test
    #result_list[proc_id + 1] = result


def parallel_initializer(board_cards,result_history, player_hand):
    parallel_process.board_cards = board_cards
    parallel_process.result_history = result_history
    parallel_process.player_hand = player_hand

def main_hand(player_cards,board=None):
    deck = holdem_gen.gen_deck_without_cards(player_cards)
    if board is None:
        board = holdem_gen.gen_board_cards(deck)
    result = holdem_gen.main_process(board,player_cards)
    worker = result
    print worker

def main(card1,card2):
    card1_r =  holdem_gen.Card.Card(card1)
    card2_r =  holdem_gen.Card.Card(card2)
    player_cards = list()
    player_cards.extend([card1_r,card2_r])
    deck_before = holdem_gen.gen_deck_without_cards(player_cards)
    board = holdem_gen.gen_board_cards(deck_before)
    p_hand = holdem_gen.main_process(board, player_cards)
    deck = holdem_gen.gen_deck_without_cards(player_cards, board)
    num_processes = multiprocessing.cpu_count() - 1
    num_players = 9
    result_history = multiprocessing.Array('i', num_processes * (num_players + 1))
    pool = multiprocessing.Pool(processes=num_processes,
                                initializer=parallel_initializer,
                                initargs=(board,result_history,p_hand))
    r = pool.map(parallel_process, holdem_gen.gen_opponent_cards(deck, 100))
    reslt, s = zip(*r)
    print p_hand
    print "---------------"
    print reslt
    print "---------------"
    print sum(s)

# if __name__ == '__main__':
#     start = time.time()
#     main(card1='',card2='')
#     print "\nTime elapsed(seconds): ", time.time() - start