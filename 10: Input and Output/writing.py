# cities = ["Adelaide", "Darwin", "Alice Springs", "Melbourne", "Sydney"]
#
# with open("cities.txt", "w") as city_file:  # w means write mode
#     for city in cities:
#         # when using params don't put spaces around operators
#         print(city, file=city_file)  # writes into folder on computer

# # cities.txt already saved
# cities = []
#
# with open("cities.txt", "r") as city_file:
#     for city in city_file:
#         cities.append(city.strip("\n"))  # strip()
#
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda Way", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
# )
#
# with open("imelda.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)