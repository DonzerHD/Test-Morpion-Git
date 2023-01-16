
def jouer_coup(plateau:dict, joueur:str, coup:str) -> None:
    """Fonction qui joue un coup (Ne vérifie pas si le coup est valide)
    Args:
        plateau (dict): Le plateau de jeu
        joueur (str): "O" ou "X"
        coup (str): Coordonnées de la forme "A1"
    """
    plateau[coup[0].upper()][int(coup[1])] = joueur