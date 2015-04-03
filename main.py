import EvalHands
import holdem_gen


def main():
    x = holdem_gen.Card.Card('Ah')
    y = holdem_gen.Card.Card('Ad')
    player_cards = list()
    player_cards.extend([x,y])
    deck = holdem_gen.gen_deck_without_cards(player_cards)
    board = holdem_gen.gen_board_cards(deck)
    result = holdem_gen.main_process(board,player_cards)
    print result

if __name__ == '__main__':
    main()