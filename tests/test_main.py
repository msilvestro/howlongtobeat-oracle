from unittest.mock import Mock

import pytest

from hltb_oracle.main import HowLongToBeatOracle
from hltb_oracle.parser import HowLongToBeatParser
from hltb_oracle.website import HowLongToBeatWebsite, SortBy, SpecialQuery


@pytest.mark.parametrize(
    "search_query, special_query, expected_query_string",
    [
        ("Persona", None, "Persona"),
        (
            "Persona",
            SpecialQuery.recently_added,
            "recently added",
        ),  # priority to special queries
    ],
)
def test_how_long_to_beat_oracle_get(
    monkeypatch, search_query, special_query, expected_query_string
):
    mock_search_results = Mock(return_value="<html></html>")
    monkeypatch.setattr(HowLongToBeatWebsite, "search_results", mock_search_results)
    mock_parse_game_list = Mock(return_value={"data": [], "pages": {"page": 3}})
    monkeypatch.setattr(HowLongToBeatParser, "parse_game_list", mock_parse_game_list)

    HowLongToBeatOracle.get(
        search_query,
        page=3,
        sort_by=SortBy.most_popular,
        special_query=special_query,
    )

    mock_search_results.assert_called_once_with(
        query_string=expected_query_string, page=3, sort_by=SortBy.most_popular
    )
    mock_parse_game_list.assert_called_once_with("<html></html>")
