# coding: utf-8

from collections import OrderedDict

################
### TEMPLATE ###
################

#Clé : nom du tag
#Valeur : norme ou liste de tag
tagTemplate = OrderedDict()

tagTemplate['ID'] = "/"
tagTemplate['Name'] = "/"
tagTemplate['Application'] = r"^[a-z0-9](-?[a-z0-9])*"
tagTemplate['Departement'] = ["cloud", "ia", "dev"]
tagTemplate['Projet'] = r"[A-Z][0-9]{5}"
