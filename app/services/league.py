# coding=utf-8

from app.models.base import Session, engine, Base
from app.models.game import Game
from app.models.league import League
from app.models.user import User

Base.metadata.create_all(engine)

def extract_winner(game):
    if (game.winner):
        return game.winner
    else:
        return None

def extract_league_info(league_data):
    return {league.id : {'id': league.id, 'name': league.league_name, 'members': [member.id for member in league.members]} for league in league_data}

def extract_league_games(league_data):
    return {league.id : [{'time': game.date.isoformat(), 'gameId': game.id, 'winner': extract_winner(game)} for game in league.games] for league in league_data}

def extract_user_data(users):
    return {user.id : {'userId': user.id, 'username': user.username} for user in users}

def league_data(user_id):
    res = {
        'success': False,
        'data': {}
    }

    session = Session()
    users = session.query(User).filter(User.id == user_id).all()

    if len(users) != 0:
        league_data = users[0].leagues;

        league_ids = [league.id for league in league_data]
        league_info = extract_league_info(league_data)
        league_games = extract_league_games(league_data)
        user_ids = {member.id for league in league_data for member in league.members}
        all_relevant_users = session.query(User).filter(User.id.in_(user_ids)).all()
        user_data = extract_user_data(all_relevant_users)

        data = {
            'myLeagues': league_ids,
            'leagueInfo': league_info,
            'leagueGames': league_games,
            'userData': user_data
        }

        res['success'] = True
        res['data'] = data

    session.close()
    return res
