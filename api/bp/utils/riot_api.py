from riotwatcher import LolWatcher, ApiError
from flask import Blueprint, current_app


riot_api_bp = Blueprint('riot_api', __name__)


class RiotAPI():

    def __init__(self, region="na1"):
        self.region = region
        self.lol_watcher = LolWatcher(current_app.config["RIOT_API_KEY"])

    def get_matches_by_summoner_name(self, summoner_name, page=0):
        pagenated_by = 10;
        summoner = self.lol_watcher.summoner.by_name(self.region, summoner_name)
        matches = self.lol_watcher.match.matchlist_by_account(self.region, summoner["accountId"], begin_index=page, end_index=page + pagenated_by)
        print(matches)
        return matches
