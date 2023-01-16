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

def est_pleine(plateau:dict) -> bool:
    """Fonction qui permet de savoir si la grille est pleine
    Args:
        plateau (dict): Un plateau de jeu
    Returns:
        bool: True si la grille est pleine, False sinon
    """
    
    for cle in plateau:
        for case in plateau[cle]:
            if case == None:
                return False
    return True

plateau = {
    "A" : [None for _ in range(3)],
    "B" : [None for _ in range(3)],
    "C" : [None for _ in range(3)]
}

termine = False
joueur = "X"