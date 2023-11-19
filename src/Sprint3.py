def adresse_image(personnes):
    """Affiche une liste de couples constiués de l'adresse de l'image associée à un nom et la ressemblance avec l'utilisateur

    Parameters
    ----------
    personnes: liste de couples (pseudo twitter, ressemblance avec l'utilisateur)

    Returns
    -------
    liste: liste de couples (adresse de l'image associée au pseudo twitter, ressemblance avec l'utilisateur)"""

    liste = []
    for personne in personnes:
        liste.append(
            ("./Data/Pictures/"+personne[0]+".jpg", personne[1]))
    return liste
