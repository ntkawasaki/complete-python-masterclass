# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# metallica = "Ride the Lightening", "Metallica", 1984
# # songs in the album
# # must use brackets for each song to make each into its own tuple
# # otherwise would be one list tuple
# imelda = "More Mayhem", "Emilda Way", 2011, (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), \
#          (4, "Kentish Town Waltz")
#
# print(imelda)
#
# title, artist, year, track_1, track_2, track_3, track_4 = imelda
# print("Title: {}".format(title))
# print("Album: {}".format(artist))
# print("Year: {}".format(year))
# print()
# print(track_1)
# print(track_2)
# print(track_3)
# print(track_4)

# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"),
#     (2, "Psycho"),
#     (3, "Mayhem"),
#     (4, "Kentish Town Waltz")
# )
#
# print(imelda)
# print()
#
# album, artist, year, tracks = imelda
# print("Album Title: {}".format(album))
# print("Artist: {}".format(artist))
# print("Year: {}".format(year))
#
# for track in tracks:
#     print("\t", "Track {}: {}".format(track[0], track[1]))

# list inside a tuple
imelda = "More Mayhem", "Imelda May", 2011, ([(1, "Pulling the Rug"), (2, "Psycho"),
                                              (3, "Mayhem"), (4, "Kentish Town Waltz")])
print(imelda)

# since a list inside a tuple, tuple can technically be changed
imelda[3].append((5, "All For You"))
album, artist, year, tracks = imelda
tracks.append((6, "Eternity"))
print("Album Title: {}".format(album))
print("Artist: {}".format(artist))
print("Year: {}".format(year))

for track in tracks:
    num, name = track
    print("\tTrack {}: {}".format(num, name))


