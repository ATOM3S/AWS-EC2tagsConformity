import re
from variables import * 
from template import *
from fonctions import *

############
### MAIN ###
############
        
displayHeader(tagTemplate)
displayTab(convertLists(testLists), tagTemplate)

displayHeaderCS(tagTemplate)
displayTabCS(convertLists(testLists), tagTemplate)
