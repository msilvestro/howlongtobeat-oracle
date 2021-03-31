from typing import Optional

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class HowLongToBeatWebsite:
    base_url = "https://howlongtobeat.com/"

    @classmethod
    def search_results(cls, query_string: str = "", page: Optional[int] = None):
        ua = UserAgent()
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "accept": "*/*",
            "User-Agent": ua.random,
        }
        data = {
            "queryString": query_string,
            "t": "games",
            "sorthead": "popular",
            "sortd": "Normal Order",
            "plat": "",
            "length_type": "main",
            "length_min": "",
            "length_max": "",
            "detail": "",
        }
        page_param = f"?page={page}" if page else ""
        res = requests.post(
            f"{cls.base_url}search_results.php{page_param}",
            data=data,
            headers=headers,
        )
        return res.text


class HowLongToBeatOracle:
    @staticmethod
    def get_list():
        html = HowLongToBeatWebsite.search_results()
        games = []

        soup = BeautifulSoup(html, "html.parser")
        details = soup.find_all("div", class_="search_list_details")
        for detail in details:
            game_name = detail.h3.a.text.strip()
            game_id = int(detail.h3.a.get("href").split("id=")[-1])
            game = {"name": game_name, "id": game_id}

            detail_block = (
                detail.find("div", class_="search_list_details_block")
                .find("div")
                .find_all("div")
            )
            current_label = None
            for block in detail_block:
                if current_label:
                    value = block.text.strip()
                    accuracy = 0
                    for block_class in block.get("class"):
                        if block_class.startswith("time_"):
                            accuracy = int(block_class.split("_")[-1])
                    game[current_label] = {"value": value, "accuracy": accuracy}
                    current_label = None
                else:
                    current_label = block.text.strip()
            games.append(game)

        return games
