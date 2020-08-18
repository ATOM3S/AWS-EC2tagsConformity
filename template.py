# -*- coding: ISO-8859-1 -*-

from collections import OrderedDict

################
### TEMPLATE ###
################

#Clé : nom du tag
#Valeur : norme ou liste de tag
tagTemplate = OrderedDict()

tagTemplate['ID'] = "/"
tagTemplate['Name'] = r"^[a-z0-9]+"
tagTemplate['Departement'] = ["cloud", "secc"]
tagTemplate['Application'] = r"^[a-z0-9]+"
