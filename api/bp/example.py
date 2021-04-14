from flask import Blueprint, Flask, jsonify, render_template, request
from bp.utils.riot_api import RiotAPI


example_api_bp = Blueprint("example_api", __name__)


@example_api_bp.route('/')
def example_api():
    summoner_name = request.args.get('summonerName')
    riot_api = RiotAPI(region="jp1")
    matches = riot_api.get_matches_by_summoner_name(summoner_name)

    return jsonify(
        matches
    )


@example_api_bp.route('/test')
def test_api():
    summoner_name = request.args.get('summonerName')
    riot_api = RiotAPI(region="jp1")
    data = riot_api.get_matches_by_summoner_name(summoner_name)

    return render_template("example.html", data=data) #変更

