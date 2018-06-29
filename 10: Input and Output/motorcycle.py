import shelve

# the "bike" is the name of the file to be made
# persisted in files
with shelve.open("bike") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 Dream"
    # bike["color"] = "blue"
    # bike["engine_size"] = 250

    # del bike["engin_size"]  # remove incorrectly spelled one

    for key in bike:
        print(str(key) + ": " + str(bike[key]))

    print("=" * 40)

    print(bike["engine_size"])
    # print(bike["engin_size"])  # this will also return bc of the database wrote both in
    print(bike["color"])  # the typo
