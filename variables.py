#################
### VARIABLES ###
#################

#liste permettant de tester le script sans le lancer depuis une instance EC2
testLists = [
    [{'Key': 'ID', 'Value': 'i-0d65c8ece8816e4f1'}, {'Key': 'Name', 'Value': 'Instance validation réseau dns'}, {'Key': 'Owner', 'Value': 'nquantin'}],
    [{'Key': 'ID', 'Value': 'i-026dd75ccfb08e0ab'}, {'Key': 'Owner', 'Value': 'dsery.externe'}, {'Key': 'Name', 'Value': 'mongo-client'}, {'Key': 'Departement', 'Value': 'infra'}, {'Key': 'Application', 'Value': 'mongoclient'}, {'Key': 'Auteur', 'Value': 'teamcloud'}],
    [{'Key': 'ID', 'Value': 'i-03fa4593d4a29d66d'}, {'Key': 'Owner', 'Value': 'nquantin'}, {'Key': 'Name', 'Value': 'Instance validation reseau priv'}],
    [{'Key': 'ID', 'Value': 'i-03b3b625540161ca2'}, {'Key': 'Owner', 'Value': 'sleonhenri@macif.fr'}, {'Key': 'Name', 'Value': 'KHSC-KAspersky'}],
    [{'Key': 'ID', 'Value': 'i-0e6699af3e6b7d092'}, {'Key': 'Departement', 'Value': 'cloud'}, {'Key': 'Owner', 'Value': 'jdelaunay'}, {'Key': 'Name', 'Value': 'terraform-test'}],
    [{'Key': 'ID', 'Value': 'i-0bb47f81982bc12ff'}, {'Key': 'CloudManager', 'Value': '{"CloudONTAP.serialnumber":"90120130000000001065","CloudONTAP.version":"9.6P2"}'}, {'Key': 'aws:cloudformation:logical-id', 'Value': 'DotInstance'}, {'Key': 'aws:cloudformation:stack-id','Value':'arn:aws:cloudformation:eu-west3:722996696380:stack/CvoMacif/5e32ee70-e120-11e9-adbe-0a6c618353f8'}, {'Key': 'Application', 'Value': 'Test CVO'}, {'Key': 'Environnement', 'Value': 'Test'}, {'Key': 'Ligne', 'Value': 'LSI Systeme Open'}, {'Key': 'Owner', 'Value': 'i-0fcb1611ca8ac2133'}, {'Key': 'Name','Value': 'CvoMacif'},{'Key':'WorkingEnvironmentId', 'Value': 'VsaWorkingEnvironment-HNb2buqs'}, {'Key': 'ProductOwner', 'Value': 'Arnaud DUBOIS'}, {'Key': 'WorkingEnvironment', 'Value': 'CvoMacif'}, {'Key': 'aws:cloudformation:stack-name', 'Value': 'CvoMacif'}],
    [{'Key': 'ID', 'Value': 'i-07363b66272e25831'}, {'Key': 'Name', 'Value': 'Instance validation reseau pub'},{'Key': 'Owner', 'Value': 'nquantin'}],
    [{'Key': 'ID', 'Value': 'i-0002a7651b67502a5'}, {'Key': 'PO', 'Value': 'Philippe Passarini'}, {'Key': 'Ligne', 'Value': 'LSI Systèmes Open'}, {'Key': 'Projet-description', 'Value': 'Mise en containers des applis et middleware - Lot 2'}, {'Key': 'Projet-code', 'Value': 'N39572'}, {'Key': 'Name', 'Value': 'openshift-controller'}, {'Key': 'Owner','Value': 'tdufaure'}, {'Key': 'Produit', 'Value': 'OpenShift'}, {'Key': 'Utilisateur', 'Value': 'Thomas Dufaure'}],
    [{'Key': 'ID', 'Value': 'i-004e54fe0f376f2ca'}, {'Key': 'application', 'Value': 'gitlab-runner'}, {'Key': 'Name', 'Value': 'GitLab-Runner'}, {'Key': 'Owner', 'Value': 'tkovatchitch'}, {'Key': 'departement', 'Value': 'operations'}],
    [{'Key': 'ID', 'Value': 'i-035632bd773340163'}, {'Key': 'Application', 'Value': 'Nextcloud'}, {'Key': 'Name', 'Value': 'nextcloud-temp'}, {'Key': 'Departement', 'Value': 'Engagements Clients et Collaborateurs'}, {'Key': 'Owner', 'Value': 'terraform'}, {'Key': 'EC2','Value': 'Nextcloud EC2 TEMP'}],
    [{'Key': 'ID', 'Value': 'i-0fcb1611ca8ac2133'}, {'Key': 'Environnement', 'Value': 'Test'}, {'Key': 'Name','Value': 'NetApp Cloud Manager'}, {'Key': 'ProductOwner', 'Value': 'Arnaud DUBOIS'}, {'Key': 'Owner', 'Value': '1569573457257571925'}, {'Key': 'Application', 'Value': 'Test CVO'},{'Key': 'Ligne', 'Value': 'LSI Systeme Open'}],
    [{'Key': 'ID', 'Value': 'i-06af2b8d3e05677cc'}, {'Key': 'Actif', 'Value': 'instance'}, {'Key': 'Owner', 'Value': 'dsery.externe'}, {'Key': 'Name', 'Value': 'bastion-vpc-private'}, {'Key':'Auteur', 'Value': 'teamcloud'}, {'Key': 'Departement', 'Value': 'infra'}],
    [{'Key': 'ID', 'Value': 'i-0b26da14ef38ec8a6'}, {'Key': 'Departement', 'Value': 'Engagements Clients et Collaborateurs'}, {'Key': 'Ligne', 'Value': 'BtoC Sites'}, {'Key': 'Owner', 'Value': 'dsery'}, {'Key': 'Name', 'Value': 'proxy es waflogs'}]
]

#taille des colonnes (en nombre de caractères)
columnLength = 25
