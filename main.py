import re
import argparse

from variables import * 
from template import *
from classes import *

############
### MAIN ### test
############

parser = argparse.ArgumentParser()
parser.add_argument("-ht", "--hidetab", action="store_true", help="permet de masquer l'affichage du tableau")
parser.add_argument("-c", "--csv", action="store_true", help="permet de créer un fichier csv")
args = parser.parse_args()

if not args.hidetab:
    newTab = TabDisplay(convertLists(testLists), tagTemplate)

if args.csv:
    newCSV = CreateCSVFile(convertLists(testLists), tagTemplate)
