import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/digiwalls/api/free-to-play-games-database'

mcp = FastMCP('free-to-play-games-database')

@mcp.tool()
def games_list() -> dict: 
    '''Get all games!'''
    url = 'https://free-to-play-games-database.p.rapidapi.com/api/games'
    headers = {'x-rapidapi-host': 'free-to-play-games-database.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sort_games(sort_by: Annotated[str, Field(description='')]) -> dict: 
    '''Insert sort by, eg: release-date, alphabetical or relevance'''
    url = 'https://free-to-play-games-database.p.rapidapi.com/api/games'
    headers = {'x-rapidapi-host': 'free-to-play-games-database.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'sort-by': sort_by,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def games_by_platform(platform: Annotated[str, Field(description='')]) -> dict: 
    '''Insert platform, eg: pc, browser.'''
    url = 'https://free-to-play-games-database.p.rapidapi.com/api/games'
    headers = {'x-rapidapi-host': 'free-to-play-games-database.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'platform': platform,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def return_details_from_aspecific_game(id: Annotated[str, Field(description='')]) -> dict: 
    '''Insert game id'''
    url = 'https://free-to-play-games-database.p.rapidapi.com/api/game'
    headers = {'x-rapidapi-host': 'free-to-play-games-database.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def filter_games_by_multiple_tags(tag: Annotated[str, Field(description='')],
                                  platform: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Filter Games by multiple tags and platform for personalized results. Optionally you can also use the "platform" and "sort" parameters.'''
    url = 'https://free-to-play-games-database.p.rapidapi.com/api/filter'
    headers = {'x-rapidapi-host': 'free-to-play-games-database.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'tag': tag,
        'platform': platform,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def games_by_category_or_tag(category: Annotated[str, Field(description='')]) -> dict: 
    '''Insert game category or tag, eg: mmorpg, shooter, pvp, mmofps and more.'''
    url = 'https://free-to-play-games-database.p.rapidapi.com/api/games'
    headers = {'x-rapidapi-host': 'free-to-play-games-database.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'category': category,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def games_by_platform_category_sorted(platform: Annotated[Union[str, None], Field(description='')] = None,
                                      category: Annotated[Union[str, None], Field(description='')] = None,
                                      sort_by: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Get games list using multiple parameters'''
    url = 'https://free-to-play-games-database.p.rapidapi.com/api/games'
    headers = {'x-rapidapi-host': 'free-to-play-games-database.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'platform': platform,
        'category': category,
        'sort-by': sort_by,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
