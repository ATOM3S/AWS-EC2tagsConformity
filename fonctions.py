import re
from variables import * 
from template import *

#################
### FONCTIONS ###
#################

def convertLists(lists):
    """permet si besoin de convertir une liste de liste de plusieurs dictionnaires (format boto3) en simple liste de un dictionnaire"""
    newList = []
    for list in lists:
        newDict = dict()
        for elt in list:
            newDict[elt['Key']]=elt['Value']
        newList.append(newDict)
    return newList
    
def tagControler(tags, key, template):
    """Fonction permettant de controler si un tag correspond à une norme donnée"""
    if not(key in tags):
        return "---"
    elif re.search(template[key], tags[key]) is None:
        return tags[key]
    else:
        return "+++"

def displayHeader(template):
    """Fonction qui permet d'afficher l'entête d'un tableau.
    Prend en paramètre un dictionnaire et en affiche les clés dans une ligne"""
    row = ''
    for key in template.keys():
        row = row + key[:columnLength].center(columnLength) + '|'
    print(row)
    print('')

def displayRow(liste):
    """Fonction qui permet l'affichage d'une ligne.
    Prend en paramètre un dictionnaire et en affiche les valeurs dans une ligne"""
    row = ''
    for elt in liste:
        row = row + elt[:columnLength].center(columnLength) + '|'
    print(row)

def displayTab(liste, template):
    """Fonction qui permet d'afficher les lignes d'un tableau. Prend en paramètre une liste de dictionnaire et
    fait appelle à la fonciton displayRow pour en afficher les clés (une ligne par dictionnaire)"""
    for elt in liste:
        tagList = []
        for key in template.keys():
            tagList.append(tagControler(elt, key, template))
        displayRow(tagList)

###############################################################################################################

def displayHeaderCS(template):
    """Fonction qui permet d'afficher l'entête d'un tableau.
    Prend en paramètre un dictionnaire et en affiche les clés dans une ligne"""
    row = ''
    for key in template.keys():
        row = row + key + ','
    print(row)
    print('')

def displayRowCS(liste):
    """Fonction qui permet l'affichage d'une ligne.
    Prend en paramètre un dictionnaire et en affiche les valeurs dans une ligne"""
    row = ''
    for elt in liste:
        row = row + elt + ','
    print(row)

def displayTabCS(liste, template):
    """Fonction qui permet d'afficher les lignes d'un tableau. Prend en paramètre une liste de dictionnaire et
    fait appelle à la fonciton displayRow pour en afficher les clés (une ligne par dictionnaire)"""
    for elt in liste:
        tagList = []
        for key in template.keys():
            tagList.append(tagControler(elt, key, template))
        displayRowCS(tagList)
