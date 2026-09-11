class Song:
    # ---- Class attributes: shared across ALL Song instances ----
    count = 0            # total number of songs ever created
    genres = []          # list of all unique genres seen so far
    artists = []         # list of all unique artists seen so far
    genre_count = {}     # e.g. {"Rap": 5, "Rock": 1, "Country": 3}
    artist_count = {}    # e.g. {"Beyonce": 17, "Jay-Z": 40}
    # NOTE: named artist_count (singular) to match lib/testing/song_test.py,
    # even though the lab brief calls it "artists_count".

    def __init__(self, name, artist, genre):
        # ---- Instance attributes: unique to THIS song ----
        self.name = name
        self.artist = artist
        self.genre = genre

        # Every new song triggers all the class-level bookkeeping
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # ---- Class methods: operate on shared class attributes, not one instance ----

    @classmethod
    def add_song_to_count(cls):
        """Increments the value of count by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds any new genre to the genres list. No duplicates."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds any new artist to the artists list. No duplicates."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates genre_count.
        If the genre already exists, bump it by 1.
        If it's new, add the key and set it to 1.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Updates artist_count.
        If the artist already exists, bump it by 1.
        If it's new, add the key and set it to 1.
        """
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
