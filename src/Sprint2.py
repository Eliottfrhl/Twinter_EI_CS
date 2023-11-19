from src.Sprint1 import *
import json
import pandas as pd


def mots_en_commun(l1, l2):
    compte = 0
    for mot1 in l1:
        for mot2 in l2:
            if mot1[0] == mot2[0]:
                compte += 1
    return compte/len(l1)


def ressemblance(liste, dico):
    l = []
    for name in dico:
        l.append((name, mots_en_commun(liste, dico[name])))
    l = sorted(l, key=lambda x: x[1])
    l = l[::-1]
    return l[:20]
