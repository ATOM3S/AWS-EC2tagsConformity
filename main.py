import re
import argparse

from variables import * 
from template import *
from fonctions import *

############
### MAIN ###
############

parser = argparse.ArgumentParser()
parser.add_argument("-ht", "--hidetab", action="store_true", help="permet de masquer l'affichage du tableau")
parser.add_argument("-c", "--csv", action="store_true", help="permet de créer un fichier csv")
args = parser.parse_args()

if not args.hidetab:
    displayHeader(tagTemplate)
    displayTab(convertLists(testLists), tagTemplate)

if args.csv:
    displayHeaderCS(tagTemplate)
    displayTabCS(convertLists(testLists), tagTemplate)
