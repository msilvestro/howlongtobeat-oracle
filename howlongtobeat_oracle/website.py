from typing import Optional

import requests
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
