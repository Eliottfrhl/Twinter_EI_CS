import urllib.request
from Data.Credentials.credentials import *
import tweepy


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api


def pp(pseudo):
    """Télécharge la photo de profil d'un utilisateur donné

    Parameters
    ----------
    pseudo: @ de l'utilisateur twitter dont on souhaite récupérer la photo de profil"""
    connexion = twitter_setup()
    url_image = connexion.get_user(screen_name=pseudo).profile_image_url
    url_image = url_image.replace("_normal", '')
    urllib.request.urlretrieve(
        url_image, './Data/Pictures/'+pseudo+".jpg")


pseudos = ['MLP_officiel',
           'EmmanuelMacron',
           'JeanCASTEX',
           'ZemmourEric',
           'manuelvalls',
           'EPhilippe_LH',
           'BrunoLeMaire',
           'CCastaner',
           'JLMelenchon',
           'Anne_Hidalgo',
           'Gael_Monfils',
           'vpecresse',
           'J_Bardella',
           'f_philippot',
           'bayrou',
           'fhollande',
           'MichaelYoun',
           'PhilippePoutou',
           'FrancoisFillon',
           'jmblanquer',
           'hugoclement',
           'Manaudou',
           'FlorentManaudou',
           'WejdeneOfficiel',
           'alafpolak1',
           'teddyriner',
           'mayer_deca',
           'Gnougnou25',
           'AlexPinturault',
           'lemaitreathle',
           'airlavillenie',
           'AntoGriezmann',
           'ELS_9_FRANCE',
           'martinfkde',
           'NKARABATIC',
           'Benzema',
           'KMbappe',
           'MonsieurDream',
           'Sardoche_Lol',
           'NormanDesVideos',
           'kyank',
           'xSqueeZie',
           'GaelleGD',
           'Domingo',
           'Maghla_',
           'Jeel_TV',
           'superhenrytran',
           'JoycaOff',
           'superkevintran',
           'Gotaga',
           'Lockl34r',
           'Nato_o',
           'VianneyMusique',
           'Orel_san',
           'amel_bent',
           'Sopranopsy4',
           'shymofficiel',
           'MPokora',
           'GIMS',
           'martinsolveig',
           'JeniferOfficiel',
           'KeenvOfficiel',
           'PatSebastien',
           'dlouapre',
           'DrNozman',
           'enjoyphoenix',
           'rebeudeter',
           'Corobizar',
           'Michoucroute_',
           'dubosc_franck',
           'aminematue',
           'inoxtag']

print(len(pseudos))
