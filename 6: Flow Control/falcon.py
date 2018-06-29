falcon = "Peregrine Falcon"
letter = input("Please enter a character: ")

if letter.lower() in falcon.lower():
    print("Give me an {}, brobeans!".format(letter.lower()))
else:
    print("I dont need that letter.")