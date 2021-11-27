from controller import *
from vues import *
from models import *



controller=Controller()
vues = Vues()
step=controller.menu()

list_of_pairs_of_players=[]

if step==1:

    list_of_players=controller.create_players()
    list_of_matches=[]
    first_match = controller.create_matches(list_of_players, list_of_matches, 1)
    vues.display_round_and_matches(first_match)

    first_round = controller.create_rounds(first_match)

    list_of_pairs_of_players = controller.create_list_of_pairs_of_players(first_match,list_of_pairs_of_players)

    controller.set_score(first_round)
    

print(list_of_pairs_of_players)
    
    









#créer menu: ajouter joueur, ajouter score match
#controleur
#if 1 alors
#if 2
#methode save pour enregistrer le joueur




#Players={family_name=player.family_name, surname=player.surname, date_of_birth=player.date_of_birth, sex=player.sex, ranking=player.ranking}