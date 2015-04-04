import EvalHands
import holdem_gen
import time
import threading
import Queue


def main():


    def run_hand(q_hand):
        x = holdem_gen.Card.Card('Ah')
        y = holdem_gen.Card.Card('Ad')
        player_cards = list()
        player_cards.extend([x,y])
        deck = holdem_gen.gen_deck_without_cards(player_cards)
        board = holdem_gen.gen_board_cards(deck)
        q_hand = holdem_gen.main_process(board,player_cards)
        return q_hand

    def threader():
        while True:
            hand = q.get()
            run_hand(hand)
            q.task_done()

    def handle():
        global q
        q = Queue.Queue()
        for x in range(10):
            t = threading.Thread(target= threader)
            #t.daemon = True
            t.start()

        start = time.time()

        for hand in range(10):
            q.put(hand)

        q.join()
        duraction = time.time() - start
        #print duraction

    handle()


if __name__ == '__main__':
    main()