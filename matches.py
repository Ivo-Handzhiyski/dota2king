from env import ACCESS_TOKEN
import requests, json



def get_live_league_games(league_id = None, match_id = None, dpc = None):
    '''
    league_id - | not required | Only show matches of the specified league id
    match_id - | not required | Only show matches of the specified match id
    dpc - | not required | Only show matches that are part of the DPC
    '''

    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?access_token={ACCESS_TOKEN}'

def get_match_details(match_id, include_persona_names = None): # string
    '''
    match_id - | required | Match id
    include_persona_names = | not required | Include persona names as part of the response
    '''
    
    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/?access_token={ACCESS_TOKEN}'

def get_match_history(hero_id = None, game_mode = None, skill = None, min_player = None, account_id = None, league_id = None, start_at_match_id = None, matches_requested = None):
    '''
    hero_id - | not required | The ID of the hero that must be in the matches being queried
    game_mode - | not required | Which game mode to return matches for
    skill - | not required | The average skill range of the match, these can be [1-3] with lower numbers being lower skill. Ignored if an account ID is specified
    min_player - | not required | Minimum number of human players that must be in a match for it to be returned
    account_id - | not required | An account ID to get matches from. This will fail if the user has their match history hidden
    league_id - | not required | The league ID to return games from
    start_at_match_id - | not required | The minimum match ID to start from
    matches_requested - | not required | The number of requested matches to return (maximum 100)
    '''

    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?access_token={ACCESS_TOKEN}'
    data = requests.get(api_point)
    print(json.parse(data))



def get_match_history_by_sequence_number(start_at_match_seq_num = None, matches_requested = None):
    '''
    start_at_match_seq_num - | not required |
    matches_requested - | not required |
    '''
    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?access_token={ACCESS_TOKEN}'

def get_team_info_by_team_id(start_at_team_id = None, teams_requested = None):
    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?access_token={ACCESS_TOKEN}'

def get_top_live_event_game(partner): # int
    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?access_token={ACCESS_TOKEN}'

def get_top_live_games(partner): # int
    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1/?access_token={ACCESS_TOKEN}'

def get_top_weekend_tourney_games(partner): # int
    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetTopWeekendTourneyGames/v1/?access_token={ACCESS_TOKEN}'

def get_tournament_player_stats(account_id): # string
    api_point = f'https://api.steampowered.com/IDOTA2Match_570/GetTournamentPlayerStats/v2/?access_token={ACCESS_TOKEN}'
