import boto3
import re
import argparse

from variables import * 
from template import *
from classes import *

############
### MAIN ###
############

#Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-ht", "--hidetab", action="store_true", help="permet de masquer l'affichage du tableau")
parser.add_argument("-c", "--csv", action="store_true", help="permet de creer un fichier csv")
args = parser.parse_args()

#Utilisation du module boto3
ec2 = boto3.resource('ec2', region)

#Liste vide où seront stocké les tags
tagsList = []

#Récupération des tags et de l'id des ressources
for instance in ec2.instances.all():
    instanceTagsList = instance.tags
    addId = {'Key': 'ID', 'Value': instance.id}
    instanceTagsList.append(addId)
    tagsList.append(instanceTagsList)

#Si l'argument "-ht" ou "--hidetab" n'est pas présent, affichage du tableau
if not args.hidetab:
    newTab = TabDisplay(convertLists(tagsList), tagTemplate)

#Si l'argument "-c" ou "--csv" est présent, création du fichier csv
if args.csv:
    newCSV = CreateCSVFile(convertLists(tagsList), tagTemplate)
