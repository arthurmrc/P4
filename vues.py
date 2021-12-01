class Vues:

    def __init__(self):
        pass    

    def display_round_and_matches(self, first_match):
        print(int(len(first_match)))
        for i in range(0,int(len(first_match))):
            print(f'Match {i+1} : {first_match[i].pair_of_players[0].surname} {first_match[i].pair_of_players[0].family_name} VS {first_match[i].pair_of_players[1].surname} {first_match[i].pair_of_players[1].family_name}') 