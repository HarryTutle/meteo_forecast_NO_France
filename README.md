# meteo_terre_traitement (traitment meteo pour le Nord Ouest de la France).
 
 ce module permet de traiter les trois gros fichiers csv de MeteoNet pour accoucher de 2 array l'un le dataset et l'autre les cibles, prêt pour sklearn  !
 
 Il comprend des fonctions et surtout une classe avec les paramètres suivants:
 
 - heures: par défaut 1. Indique si on veut des données toutes les heures (1) ou alors toutes les 2, 3 heures... Du coup on diminue les dimensions du dataset mais au risque de perdre de l'efficacité da,s nos prévisions.
 
 - jours: par défaut 1. Indique si on veut un échantillon intégrant 1 jour, 2 jours, 3 jours... Plus on met de jours dans nos échantillons, plus les dimensions du dataset grimpent par contre avec moins d'échantillons.

 - 
 
