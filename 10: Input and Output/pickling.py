# pickling is serializing objects, converting to a byte stream
import pickle

# tuple with a tuple or tuples (tracks)
# imelda = ("More Mayhem",
#           "Imelda May",
#           "2011",
#           ((1, "Pulling the Rug"),
#            (2, "Psycho"),
#            (3, "Mayhem"),
#            (4, "Kentish Town Waltz")))

# with open("imelda.pickle", "wb") as pickle_file:  # stores
#     pickle.dump(imelda, pickle_file)

# with open("imelda.pickle", "rb") as imelda_pickled:  # retrieves
#     imelda_2 = pickle.load(imelda_pickled)
#
# print(imelda_2)
#
# album, artist, year, track_list = imelda_2
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_no, track_title = track
#     print(track_no, track_title)

# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)  # dumping imelda into pickle_file
#     pickle.dump(even, pickle_file, protocol=0)
#     pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#     pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#
#
# with open("imelda.pickle", "rb") as imelda_pickled:  # named here
#     imelda_2 = pickle.load(imelda_pickled)  # unpickling and retrieving imelda_2
#     even_list = pickle.load(imelda_pickled)
#     odd_list = pickle.load(imelda_pickled)
#     x = pickle.load(imelda_pickled)
#
# print(imelda_2)
# album, artist, year, track_list = imelda_2
# print(album)
# print(artist)
# print(year)
# for track in track_list:
#     track_no, track_title = track
#     print(track_no, track_title)
#
# print("=" * 40)
#
# for i in even_list:
#     print(i)
#
# print("=" * 40)
#
# for i in odd_list:
#     print(i)
#
# print("=" * 40)
#
# print(x)
#
# print("=" * 40)

# rm = removes file, deleted the file
pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR")      # Mac
