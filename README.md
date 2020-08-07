# Script : Conformité des tags des intances EC2 AWS

## Description
Ce script permet de récupérer les tags des instances EC2 sur AWS. Il les affiche dans un tableau en précisant si le tag est conforme, non-conforme, ou inexistant.

>Sortie du tableau :  
>+++ : Le tag existe et est conforme  
>--- : Le tag n'existe pas  
>Nom du tag : Le tag existe mais n'est pas conforme  

Ce projet est un projet Open Source. Vous pouvez l'utiliser, le modifier ou contribuer librement. 

## Mise en place

Pour fonctionner, ce script doit être lancé depuis une instance EC2 sous AWS.

Python et Boto3 doivent être installé sur l'instance. (Le script a été testé avec python3 et boto3. Il n'est pas sûr que le script puisse fonctionner avec des versions entérieur).

Installation de boto3 : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

L'instance EC2 doit disposer des droits nécessaires à l'aide d'IAM. Plus d'information sur IAM et les droits : https://docs.aws.amazon.com/iam/index.html

Pour lancer le script, appelez simplement "main.py" suivit si besoin des commandes.

## Commandes

-ht --hidetab
Permet de cacher l'affichage du tableau dans le terminal. Utile si l'on souhaite uniquement lancer le script sans afficher le résultat dans le terminal. 

-c --csv
Permet de créer un fichier .csv (coma separated value). Ce fichier porte comme nom la date et l'heure à laquelle il été généré. Il est sauvegardé dans le même dossier que le script. Ce fichier peut être facilement converti en tableur microsoft excel, openoffice classeur, google sheets etc...

## Fonctionnement

### main.py

Fichier principale. Il va lancer la ou les classes en fonction des paramètres sont mis ou non en argument (voir Commandes).

### classe.py

C'est ici que sont

### variables.py

### template.py

