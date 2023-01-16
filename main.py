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

def est_coup_valide(plateau:dict, coup:str) -> bool:
    """Fonction qui vérifie si un coup est valide

    Args:
        plateau (dict): Le plateau de jeu
        coup (str): Un coup de la forme "A1" avec le premier caractere entre A et C et le second entre 0 et 2 

    Returns:
        bool: True si le coup est valide, False sinon
    """
    
    # On vérifie si le coup est une case qui existe
    if coup[0].upper() not in ["A", "B", "C"]:
        return False
    if coup[1] not in ["0", "1", "2"]:
        return False
    
    # On vérifie si la case est vide
    if plateau[coup[0].upper()][int(coup[1])] == None:
        return True
    else:
        return False