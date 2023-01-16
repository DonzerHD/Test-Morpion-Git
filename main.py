import os
def afficher_grille(plateau:dict) -> None:
    """Fonction qui affiche la grille du morpion
    Args:
        plateau (dict): Un plateau de jeu
    """
    os.system("clear")
    print(" \t|\t0\t|\t1\t|\t2\t|")
    print("---------------------------------------------------------")
    for cle in plateau:
        print(cle, end="\t|\t")
        for elt in plateau[cle]:
            if elt == None:
                print(" ", end="\t|\t")
            else:
                print(elt, end="\t|\t")
        print("\n---------------------------------------------------------")
        
"commentaire"
print("ghello worfd")