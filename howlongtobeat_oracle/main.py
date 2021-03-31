from howlongtobeat_oracle.parser import HowLongToBeatParser
from howlongtobeat_oracle.website import HowLongToBeatWebsite


class HowLongToBeatOracle:
    @staticmethod
    def get():
        html = HowLongToBeatWebsite.search_results()
        return HowLongToBeatParser.parse_game_list(html)
