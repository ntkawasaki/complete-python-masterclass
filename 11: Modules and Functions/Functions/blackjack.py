# blackjack!

import random
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def load_images(card_images):
    """ Loads images into program. """

    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    # version test
    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    # for each suit, retrieve the image for the cards
    for suit in suits:

        # numbered cards 1-10
        for card in range(1, 11):
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))  # tuple with card value, card image

        # face cards
        for card in face_cards:
            name = "cards/{}_{}.{}".format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))  # tuple with card value, card image


def _deal_card(frame):
    """ Deal cards. """

    # pop card from top of deck
    next_card = deck.pop(0)

    # add card back to bottom of deck
    deck.append(next_card)

    # add image to label, display label
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")

    # return cards face value
    return next_card


def score_hand(hand):
    """
    Calculate the total score of all cards in the list.
    Only one ace can have value 11, reduce to 1 if hand would bust
    :param hand:
    """

    score = 0
    ace = False

    for next_card in hand:
        card_value = next_card[0]

        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        # check bust for ace
        if score > 21 and ace:
            score -= 10
            ace = False

    return score


def deal_dealer():
    """ Deal cards to dealer after player. """

    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins.")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins.")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins.")
    else:
        result_text.set("Draw.")


def deal_player():
    """ Deal cards to player. """

    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)

    if player_score > 21:
        result_text.set("Dealer Wins!")


# make this function so there isnt duplicated code, can fix here and affect everywhere used
def initial_deal():
    """ Initial deal of the game. """

    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    """ Clears card_frame and re-adds it to simulate restarting a game. """

    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")
    dealer_hand = []
    player_hand = []

    initial_deal()


def shuffle():
    """ Shuffle deck. """

    random.shuffle(deck)


def play():
    """ Method that starts gameplay. """
    initial_deal()
    main_window.mainloop()


main_window = tkinter.Tk()

# screen and frames for dealer and player
main_window.title("Blackjack")
main_window.geometry("640x480")
main_window.configure(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

# dealer
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
# dealer embedded frame to hold card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# player
player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
# player embedded frame to hold card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

# frame for buttons
button_frame = tkinter.Frame(main_window, background="white")
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)  # no parentheses
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New game", command=new_game)
new_game_button.grid(row=1, column=0, columnspan=1)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=1, column=1)

# load cards
cards = []
load_images(cards)
print(cards)

# create a new deck of cards, shuffle
deck = list(cards) + list(cards) + list(cards)
shuffle()

# create lists to store dealer and player hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()