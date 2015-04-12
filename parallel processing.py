from multiprocessing import Process, Queue
import multiprocessing
import EvalHands
import holdem_gen
import time


def parallel_process(opponent_cards):
    board = parallel_process.board_cards
    result_list = parallel_process.result_history
    proc_id = int(multiprocessing.current_process().name[-1]) - 1
    proc = multiprocessing.current_process()
    result = holdem_gen.main_process(board, opponent_cards)
    result_list[proc] = result
    print proc_id

def parallel_initializer(board_cards,result_history):
    parallel_process.board_cards = board_cards
    parallel_process.result_history = result_history

def main_hand(player_cards,board=None):
    deck = holdem_gen.gen_deck_without_cards(player_cards)
    if board is None:
        board = holdem_gen.gen_board_cards(deck)
    result = holdem_gen.main_process(board,player_cards)
    worker = result
    print worker

def main():
    x = holdem_gen.Card.Card('Ah')
    y = holdem_gen.Card.Card('Ad')
    player_cards = list()
    player_cards.extend([x,y])
    deck_before = holdem_gen.gen_deck_without_cards(player_cards)
    board = holdem_gen.gen_board_cards(deck_before)
    deck = holdem_gen.gen_deck_without_cards(player_cards, board)
    num_processes = multiprocessing.cpu_count() - 1
    num_players = 9
    result_history = multiprocessing.Array('i', num_processes * (num_players + 1))
    pool = multiprocessing.Pool(processes=num_processes,
                                initializer=parallel_initializer,
                                initargs=(board,result_history))
    pool.map(parallel_process, holdem_gen.gen_opponent_cards(deck))

    print pool

if __name__ == '__main__':
    start = time.time()
    main()
    print "\nTime elapsed(seconds): ", time.time() - start