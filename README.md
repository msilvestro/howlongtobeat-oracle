# How Long To Beat Oracle

Extract information from How Long To Beat.

Unlike other libraries, it allows to browse all of the results (even when not searching for a specific game).

## How to use

To begin with, import the main class:

```python
from hltb_oracle import HowLongToBeatOracle
```

### Get sorted results page by page

This code will get page 3 of the games ordered by release date:

```python
from hltb_oracle import HowLongToBeatOracle, SortBy

games = HowLongToBeatOracle.get(page=3, sort_by=SortBy.release_date).data
```

All How Long To Beat orderings are supported:

- `name`
- `main_story`
- `main_extra`
- `completionist`
- `average_time`
- `top_rated`
- `most_popular` (default one)
- `most_backlogs`
- `most_submissions`
- `most_played`
- `most_speedruns`
- `release_date`

### Get recently updated games

This code will get the first page of the recently updated games ordered by most submissions:

```python
from hltb_oracle import HowLongToBeatOracle, SortBy

games = HowLongToBeatOracle.get(page=3, sort_by=SortBy.release_date, only_recently_updated=True).data
```

### Search for a game

You can still search by game name:

```python
from hltb_oracle import HowLongToBeatOracle, SortBy

games = HowLongToBeatOracle.get("Persona", sort_by=SortBy.top_rated).data
```
