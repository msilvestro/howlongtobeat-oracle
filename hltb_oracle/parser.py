from bs4 import BeautifulSoup


class HowLongToBeatParser:
    @staticmethod
    def parse_game_list(html: str):
        games = []

        soup = BeautifulSoup(html, "html.parser")
        games_list = soup.select("div.search_list_details")
        for game_item in games_list:
            game_name = game_item.h3.a.text.strip()
            game_id = int(game_item.h3.a.get("href").split("id=")[-1])
            game = {"name": game_name, "id": game_id}

            game["times"] = {}
            details_block = game_item.select("div.search_list_details_block")[0]
            tidbits = details_block.select("div[class^=search_list_tidbit]")
            current_label = None
            for tidbit in tidbits:
                if current_label:
                    content = tidbit.text.strip()
                    accuracy = 0
                    for block_class in tidbit.get("class"):
                        if block_class.startswith("time_"):
                            accuracy = int(block_class.split("_")[-1])
                    game["times"][current_label] = {
                        "content": content,
                        "accuracy": accuracy,
                    }
                    current_label = None
                else:
                    current_label = tidbit.text.strip()
            games.append(game)

        bottom_h2 = soup.find("h2")
        if not bottom_h2:
            return {"data": games, "pages": {}}

        bottom_spans = soup.find("h2").find_all("span")
        page = 1
        for span in bottom_spans:
            if "back_blue" in span.get("class") and span.text != "":
                page = int(span.text)
        total_pages = int(bottom_spans[-1].text)

        return {"data": games, "pages": {"page": page, "total_pages": total_pages}}
