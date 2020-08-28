import boto3
import re
import argparse

from variables import * 
from template import *
from classes import *

############
### MAIN ###
############

parser = argparse.ArgumentParser()
parser.add_argument("-ht", "--hidetab", action="store_true", help="permet de masquer l'affichage du tableau")
parser.add_argument("-c", "--csv", action="store_true", help="permet de creer un fichier csv")
args = parser.parse_args()

ec2 = boto3.resource('ec2', region)

tagsList = []

for instance in ec2.instances.all():
    instanceTagsList = instance.tags
    addId = {'Key': 'ID', 'Value': instance.id}
    instanceTagsList.append(addId)
    tagsList.append(instanceTagsList)

if not args.hidetab:
    newTab = TabDisplay(convertLists(tagsList), tagTemplate)

if args.csv:
    newCSV = CreateCSVFile(convertLists(tagsList), tagTemplate)
