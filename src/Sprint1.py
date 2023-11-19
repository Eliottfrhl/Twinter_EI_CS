import tweepy
from textblob import TextBlob
from Data.Credentials.credentials import *
from textblob import Word
import json


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


api = twitter_setup()
mots_inutiles = ['mais', 'une', 'pour', 'les', 'mon', 'que', 'est', "j'ai",
                 'avec', 'des', 'ont', 'donc', 'car', 'dans', 'par', 'vers', 'sans']


def extract(data):  # sous la forme de liste de dictionnaires
    """
    Entrée:
        - data : DataFrame pandas des tweets récoltés
    Sortie:
        - res : set des mots utilisés
    """
    L = []
    for i in data:
        l = TextBlob(i).tags
        for tuple in l:
            if '@'not in Word(tuple[0]) and "http" not in Word(tuple[0]) and "/" not in Word(tuple[0]) and Word(tuple[0]) not in mots_inutiles:
                if 'VB' in tuple[1]:
                    word_provisoire = Word(tuple[0])
                    word = Word(word_provisoire).lemmatize("v")
                    L.append(word.upper())
                else:
                    if tuple[1] not in ['DT', 'RB', 'IN', 'NP', 'PRP', 'WDT', 'PRP$', 'CC', 'NNS', 'TO']:
                        word_provisoire = Word(tuple[0])
                        word = Word(word_provisoire).lemmatize()
                        L.append(word.upper())
            else:
                pass
    return [mot for mot in L if len(mot) > 2]


# tweet de la personne qui s'appel : nom
def collect_entity_actuality_tweets(nom):
    user_id = api.get_user(screen_name=nom).id
    statuses = api.user_timeline(id=user_id, count=50)
    L = []
    for status in statuses:
        L.append(status.text)
    return L


def base_donnee(liste_noms):  # {user_id:[(mot,f),...]}
    base_donnee = {}
    for nom in liste_noms:
        dico = {}
        dico_nom = []
        liste_tweets = collect_entity_actuality_tweets(nom)
        liste_mots = extract(liste_tweets)
        for mot in liste_mots:
            if mot in dico:
                dico[mot] += 1
            else:
                dico[mot] = 1
        # liste [('mot',nbr),...] croissant
        M = sorted(dico.items(), key=lambda t: t[1])
        n = 0
        for i in range(-1, -50, -1):
            n += M[i][1]
        for i in range(-1, -50, -1):
            dico_nom.append((M[i][0], M[i][1]/n))
        base_donnee[nom] = dico_nom
    return base_donnee


def store_data(data):
    with open('base_données_twitter.json', "w") as write_file:
        json.dump(data, write_file, indent=4)


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
