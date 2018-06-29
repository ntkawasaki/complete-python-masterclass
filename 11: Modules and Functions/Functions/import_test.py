# import blackjack

# g = sorted(globals())
# for i in g:
#     print(g)

# single _ implies it is protected, not meant to be used outside of module
# blackjack._deal_card(blackjack.dealer_card_frame)
# blackjack.play()

# double __ mean they should never be changed

# stand alone _ means throw away value
# could use this if you have to specify a variable but dont need to use it
personal_details = ("Tim", 24, "Australia")

name, _, country = personal_details
print(name, country)
print(_)
