from src.Sprint1 import base_donnee
from src.Sprint2 import ressemblance
from src.Sprint3 import adresse_image
from src.Sprint4 import mosaique
import pandas as pd
from PIL import Image
if __name__ == '__main__':

    data = pd.read_json('Data/base_données_twitter.json')
    print("Pseudo :")
    nom_user = input()
    mots_user = base_donnee([nom_user])[nom_user]

    test = adresse_image(ressemblance(mots_user, data))

    mosaique(test)

    im = Image.open('Résultat.jpg')
    im.show()
