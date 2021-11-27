from models import *
from vues import *
from datetime import datetime


class Controller:

    def __init__(self):
        pass    

    def menu(self):
        answer=int(input("Pour ajouter des joueurs tapez 1,  \n\rPour ajouter le résultat de matchs tapez 2 "))

        if answer==1:
            return 1

        if answer==2:
            return 2

    def create_players(self):
        players=[]
        rankings_players=[]
        nb_players = 4
        for i in range(1,nb_players+1):
            surname=input("Entrez le prénom du joueur {}: ".format(i))
            family_name=input("Entrez le nom du joueur {}: ".format(i))
            while True :
                    try:
                        date = input('Entrez la date de naissance du joueur {} au format dd/mm/yyyy:'.format(i))
                        dte = datetime.strptime(date,"%d/%m/%Y")
                        date_of_birth = dte
                        break
                    except ValueError as e:
                        print(e)
                        print("Format invalide")
            sex=input("Entrez le sexe du joueur {} sous le format f ou m : ".format(i))
            while sex!="m" and sex!="f":
                sex=input('Format invalide, veuillez rééssayer') 
            ranking=int(input("Entrez le rang du joueur {} en choisissant un chiffre entre 1 et 8: ".format(i)))
            while ranking in rankings_players:
                ranking=int(input("Veuillez entrer un nombre différent de ceux déja entrés pour les autres joueurs {}:".format(rankings_players)))

            
            rankings_players.append(ranking)

            player=Player(family_name=family_name, surname=surname, date_of_birth=date_of_birth, sex=sex, ranking=ranking)

            players.append(player)
        
        #print(sorted(players, key=lambda player:player.ranking)[0].surname)

        return sorted(players, key=lambda player:player.ranking)
    
    def create_matches(self, list_of_players, list_of_matches, round):

        if round==1:
            
            for i in range(0,int(len(list_of_players)/2)):
                match = Match((list_of_players[i],list_of_players[i+int(len(list_of_players)/2)]))
                list_of_matches.append(match)
            return list_of_matches

        #if round>1:
            #for i in range(0,len(list_of_players)):
                #match=Match
            
    
    def create_rounds(self, list_of_matches):
        round_1=Round(name="Round_1", matches=list_of_matches)
        return round_1

    def create_list_of_pairs_of_players(self, list_of_matches, list_of_pairs_of_players):
        for elem in list_of_matches:
            list_of_pairs_of_players.append((elem.pair_of_players[0].surname,elem.pair_of_players[1].surname))
        return list_of_pairs_of_players

    def set_score(self, round):
        for elem in round.matches:
            j1 = elem.pair_of_players[0].surname
            j2 = elem.pair_of_players[1].surname
            while True:
                score_1 = float(input("Entrez le score de {} : ".format(j1)))
                score_2 = float(input("Entrez le score de {} : ".format(j2)))
                if score_1 + score_2 != 1.0:
                    print("Veuillez entrer les bons scores (0, 1, 0.5)")
                else:
                    break
            elem.score = [score_1, score_2]
            elem.pair_of_players[0].calculate_score(elem.pair_of_players[0].get_score()+score_1)
            elem.pair_of_players[1].calculate_score(elem.pair_of_players[1].get_score()+score_2)
            print("score de {} = {}".format(j1,elem.pair_of_players[0].get_score()+score_1))
            print("score de {} = {}".format(j2,elem.pair_of_players[1].get_score()+score_2))


if __name__=="__main__":
    controller=Controller()
    controller.menu()
        