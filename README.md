# Music Library System

A Python `Song` class that models individual songs while tracking library-wide statistics — total song count, unique genres and artists, and per-genre/per-artist song counts. Built as part of a lab on class attributes and class methods.

## Description

This project simulates the core data model behind a music streaming service's song catalog. Each `Song` object represents a single track with its own `name`, `artist`, and `genre`. Beyond that, the `Song` class itself keeps running, shared statistics across every song ever created:

- `count` — total number of songs created
- `genres` — list of all unique genres seen so far
- `artists` — list of all unique artists seen so far
- `genre_count` — dict mapping each genre to how many songs belong to it
- `artist_count` — dict mapping each artist to how many songs they're responsible for

These class-level stats update automatically every time a new `Song` is instantiated, powering features like personalized recommendations and catalog analytics.

## Installation

1. Clone this repository:
   ```bash
   git clone <your-forked-repo-url>
   cd python-music-library-system-lab
   ```
2. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
   ```

## Usage

```python
from song import Song

s1 = Song("Level Up", "Beyonce", "Pop")
s2 = Song("Sorry", "Beyonce", "Pop")
s3 = Song("99 Problems", "Jay-Z", "Rap")

print(Song.count)          # 3
print(Song.genres)         # ["Pop", "Rap"]
print(Song.artists)        # ["Beyonce", "Jay-Z"]
print(Song.genre_count)    # {"Pop": 2, "Rap": 1}
print(Song.artist_count)   # {"Beyonce": 2, "Jay-Z": 1}
```

## Testing

Run the test suite with:

```bash
pytest
```

All tests live in `lib/testing/song_test.py` and cover instance attributes, the running song count, unique genre/artist tracking, and per-genre/per-artist counts.

## Screenshot

<!-- Add a screenshot of your passing test output or CodeGrade result below -->
![Completed work](./screenshot.png)

## Features

- Instance-level song data (`name`, `artist`, `genre`)
- Automatic, class-wide tracking of total songs, unique genres, and unique artists
- Per-genre and per-artist song counts, updated on every song creation
- Full test coverage via `pytest`

## Contributing

This is a lab submission and not open to outside contributions. See `CONTRIBUTING.md` for the original contribution guidelines if you're working from the upstream template repo.

## License

See `LICENSE.md` for details.