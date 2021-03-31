from typing import Optional

from howlongtobeat_oracle.models import HowLongToBeatGame
from howlongtobeat_oracle.parser import HowLongToBeatParser
from howlongtobeat_oracle.website import HowLongToBeatWebsite, SortBy


class HowLongToBeatOracle:
    @staticmethod
    def get(page: Optional[int] = None, sort_by: SortBy = SortBy.most_popular):
        html = HowLongToBeatWebsite.search_results(page=page, sort_by=sort_by)
        return [
            HowLongToBeatGame(game)
            for game in HowLongToBeatParser.parse_game_list(html)
        ]
