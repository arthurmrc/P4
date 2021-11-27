class Match:
    def __init__(self, pair_of_players, score=[0,0]):
        self.pair_of_players=pair_of_players
        self.score=score
    
    def get_pair_of_players(self):
        return self.pair_of_players

    def get_score(self):
        return self.score

class Player:
    def __init__(self, family_name, surname, date_of_birth, sex, init_ranking, total_score = 0):
        self.family_name=family_name
        self.surname=surname
        self.date_of_birth=date_of_birth
        self.sex=sex
        self.init_ranking = init_ranking
        self.total_score=total_score
    
    def get_family_name(self):
        return self.family_name

    def get_surname(self):
        return self.surname

    def get_score(self):
        return float(self.total_score)
    
    def calculate_score(self, new_score): 
        self.total_score=new_score

class Round:
    def __init__(self, name, matches):
        self.name=name
        self.matches=matches

    def get_round_name(self):
        return self.name

    def get_list_of_matches(self):
        return self.matches

class Tournament:
    def __init__(self, name, place, date, number_of_rounds, list_of_pairs_of_players, players):
        self.name=name
        self.place=place
        self.date=date
        self.number_of_rounds=number_of_rounds
        self.list_of_pairs_of_players=list_of_pairs_of_players
        self.players=players
    
    def set_list_of_pairs_of_players(self, pair_of_players):
        self.list_of_pairs_of_players.append(pair_of_players)