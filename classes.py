# -*- coding: ISO-8859-1 -*-

import re

from time import strftime
from datetime import datetime
from collections import OrderedDict

from variables import * 
from template import *

# Delaunay Jonas <contact@jonasdelaunay.com>
# https://github.com/ATOM3S/AWS-EC2tagsConformity
# Licence MIT

###############
### CLASSES ###
###############

#Classe permettant l'affichage du tableau des tags
class TabDisplay:

    def __init__(self, tagsList, tagsTemplate):
        """Constructeur de la classe"""
        self.displayHeader(tagsTemplate)
        self.displayTab(tagsList, tagsTemplate)
    
    @staticmethod  
    def tagControler(tags, key, template):
        """Fonction permettant de controler si un tag correspond à une norme donnée
        ou si il est conforme à une liste"""
        if type(template[key]) == list:
            if not(key in tags):
                return "---"
            elif tags[key] in template[key]:
                return "+++"
            else:
                return tags[key]
        else:
            if not(key in tags):
                return "---"
            elif re.search(template[key], tags[key]) is None:
                return tags[key]
            else:
                return "+++"

    @staticmethod
    def displayHeader(template):
        """Fonction qui permet d'afficher l'entête d'un tableau.
        Prend en paramètre un dictionnaire et en affiche les clés dans une ligne"""
        row = ''
        for key in template.keys():
            row = row + key[:columnLength].center(columnLength) + '|'
        print(row)
        print('')

    @staticmethod
    def displayRow(liste):
        """Fonction qui permet l'affichage d'une ligne.
        Prend en paramètre un dictionnaire et en affiche les valeurs dans une ligne"""
        row = ''
        for elt in liste:
            row = row + elt[:columnLength].center(columnLength) + '|'
        print(row)
    
    def displayTab(self, liste, template):
        """Fonction qui permet d'afficher les lignes d'un tableau. Prend en paramètre une liste de dictionnaire et
        fait appelle à la fonciton displayRow pour en afficher les clés (une ligne par dictionnaire)"""
        for elt in liste:
            tagList = []
            for key in template.keys():
                tagList.append(self.tagControler(elt, key, template))
            self.displayRow(tagList)



#Classe gérant la création d'un fichier CSV (Comma-Separated Values)
class CreateCSVFile(TabDisplay):

    def __init__(self, tagsList, tagsTemplate):
        time = datetime.now().strftime("%m%d%Y%H%M%S")
        fileName = time + '.cvs'
        self.file = open(fileName, "a")
        
        TabDisplay.__init__(self, tagsList, tagsTemplate)

        self.file.close()
    
    def displayHeader(self, template):
        """Fonction qui permet d'afficher l'entête d'un tableau.
        Prend en paramètre un dictionnaire et en affiche les clés dans une ligne"""
        row = ''
        for key in template.keys():
            row = row + key + ','
        self.file.write(row)
        self.file.write('\n')
    
    def displayRow(self, liste):
        """Fonction qui permet l'affichage d'une ligne.
        Prend en paramètre un dictionnaire et en affiche les valeurs dans une ligne"""
        row = ''
        for elt in liste:
            row = row + elt + ','
        self.file.write(row)
        self.file.write('\n')


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
