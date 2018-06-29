class Song:
    """
    Class to represent the song.

    Attributes:
    title (str): The title of the song.
    artist (str): Name of song's creator.
    duration (int): Duration of song in seconds. May be zero.

    Challenge: Modify the program so that Artist objects can hold references to Album objects, and Album objects
    can hold references to Song objects. But no circular references.
    """

    def __init__(self, title, artist, duration=0):
        """Initialize attributes."""

        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        """Getter."""
        return self.title

    name = property(get_title)


class Album:
    """
    Class to represent an album using it's tracklist.

    Attrbutes:
    name (str): The name of the album.
    year (int): Release year.
    artist (str): The name of the artist who made the album. Default to "Various Artists"
    tracks (List[song]): A list of the songs on the album

    Methods:
    add_song: Add song to track list.
    """

    def __init__(self, name, year, artist=None):
        """Initialize attributes."""

        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Add song to track list.

        Arguments:
        song (Song): The title of the song to add.
        position (int) [optional]: Position to add track to, default will add to end.
        """

        song_found = find_object(song, self.tracks)

        if song_found is None:
            song_found = Song(self, self.artist)

            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """
    Basic class to store artist details.

    Attributes:
    name (str): Name of the artist.
    albums (List[Album]): List of albums by this artist (in this collection)

    Methods:
    add_album: Add an album to artists album list
    """

    def __init__(self, name):
        """Initialize attributes."""

        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        Add new album to list.

        Arguments:
        album (Album): Album object to list, if already present do not duplicate
        """

        self.albums.append(album)

    def add_song(self, name, year, title):
        """
        Add new song to albums in the collection. Will make new album if doesnt exist

        Arguments:
        name (str): Name of album
        year (int): Year the album was produced
        title( str): Title of song
        """

        album_found = find_object(name, self.albums)

        if album_found is None:
            print(name + " not found.")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album")

        album_found.add_song(title)


def find_object(field, object_list):
    """
    Check "object_list" to see if an object with a name attribute = "field" exists and return it if so.

    :param field:
    :param object_list:
    :return: item
    """

    for item in object_list:
        if item.name == field:
            return item


def load_data():
    """Load data."""

    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)

            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print(tuple(line.strip("\n").split("\t")))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_check(artist_list):
    """Create a check file from the object data for comparison with the original file."""

    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists.".format(len(artists)))
    create_check(artists)
