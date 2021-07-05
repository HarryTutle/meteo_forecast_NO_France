# meteo_terre_traitement (traitment meteo pour le Nord Ouest de la France).
 
 ce module (meteo_terre_traitement) permet de traiter les trois gros fichiers csv de MeteoNet pour accoucher de 2 array l'un le dataset et l'autre les cibles, prêt pour sklearn  !
 
 Il comprend des fonctions et surtout une classe (Meteo_Data_View) avec les paramètres suivants:
 
 - heures: par défaut 1. Indique si on veut des données toutes les heures (1) ou alors toutes les 2, 3 heures... Du coup on diminue les dimensions du dataset mais au risque de perdre de l'efficacité da,s nos prévisions.
 
 - jours: par défaut 1. Indique si on veut un échantillon intégrant 1 jour, 2 jours, 3 jours... Plus on met de jours dans nos échantillons, plus les dimensions du dataset grimpent par contre avec moins d'échantillons.

 - var_corbeille: c'est une liste où on peut mettre les variables que l'on veut enlever dans notre dataset. Les variables qu'on peut enlever sont: latitude, longitude, altitude, temps, pression, pluie, point_rosée, direction, température, humidité, force.

 - vue: indique l'heure de la prévision que l'on souhaite; une heure, deux heures, trois heures...Evidemment on est limité par la taille de nos échantillons. Par exemple si l'échantillon comprend une journée, on ne peut pas aller à plus de 23 heures; si c'est 2 jours alors c'est 47 heures etc ...

 -cible: indique quel type de variable on veut prédire: la force du vent ('force'), la direction du vent ('direction'), la température ('température').
 
 
 Avec ce module vous trouverez un fichier 'voir un peu' qui donne un exemple sur la façon d'utiliser le module.
 
 Amusez-vous bien ! Si il y a des améliorations hésitez pas !
 
 
