from PIL import Image  # https://note.nkmk.me/en/python-pillow-concat-images/
import random
import copy


def mosaique(data, max_row=5, max_column=4, alea=False, escargot=True, name="mosaique"):
    """Affiche la mosaïque composée des images pondérées dans le fichier data

    Parameters
    ----------
    data : list
        Liste des couples des images décrit sous la forme (adresse local de l'image, taille de l'image)

    max_row (optionnal) : int
        Nombre de ligne sur la mosaïque.

    max_column (optionnal) : int
        Nombre de colonnes sur la mosaïque.

    alea (optional) : bool
        Si True les images sont mises dans un ordre aléatoire.

    escargot (optional) : bool
        Si True et que  max_row = 5, max_column = 4, les images sont placées sous la forme d'un escargot.

    name (optional) : str
        Nom du fichier .jpg sous lequel sera sauvegardé la mosaïque

    Returns
    -------
    Ne renvoit rien mais sauvegarde la mosaïque dans un fichier .jpg
    """
    temp = copy.deepcopy(data)
    if escargot and (max_row == 5, max_column == 4):
        data[0] = temp[19]
        data[1] = temp[6]
        data[2] = temp[7]
        data[3] = temp[8]
        data[4] = temp[9]
        data[5] = temp[18]
        data[6] = temp[5]
        data[7] = temp[0]
        data[8] = temp[1]
        data[9] = temp[10]
        data[10] = temp[17]
        data[11] = temp[4]
        data[12] = temp[3]
        data[13] = temp[2]
        data[14] = temp[11]
        data[15] = temp[16]
        data[16] = temp[15]
        data[17] = temp[14]
        data[18] = temp[13]
        data[19] = temp[12]

    if alea:
        random.shuffle(data)

    itp = []
    taille_max = temp[0][1]

    for image, taille in data:
        im = Image.open(image)

        size = int(400 * taille/taille_max)
        im = im.resize((size, size))
        itp.append([im, size])

    res = Image.new('RGB', (400*max_row, 400*max_column), (29, 161, 243))

    i = 0
    j = 0

    while j < max_column:
        while i < max_row:
            demi_size = int(itp[max_row*j + i][1]/2)
            res.paste(itp[max_row*j + i][0], (400*i + 200 -
                                              demi_size, 400*j + 200 - demi_size))

            i += 1

        j += 1
        i = 0

    res.save("Résultat.jpg")


#classement(exemple, 20)

# mosaique(exemple)
