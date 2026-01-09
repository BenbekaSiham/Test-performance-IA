Génération automatique de cas de tests de performance avec l’intelligence artificielle
1. Contexte et objectifs

Ce projet explore l’utilisation de l’intelligence artificielle (modèles de langage de type GPT) pour la génération automatique de scénarios de tests de performance directement exploitables par les outils Apache JMeter et Gatling.
L’objectif est de réduire l’effort manuel nécessaire à la conception de tests de charge tout en assurant la reproductibilité, la traçabilité et la réutilisabilité des scénarios générés.

Le projet a été réalisé dans le cadre d’un travail de maîtrise en génie des technologies de l’information à l’ÉTS Montréal. Il est conçu pour être repris, étendu ou amélioré par d’autres étudiants.

2. Description générale de la solution

La solution repose sur une chaîne de traitement automatisée :

Génération de scénarios de tests de performance à l’aide d’un modèle d’intelligence artificielle.

Production automatique de scripts de test compatibles avec :

Apache JMeter (.jmx)

Gatling (.scala)

Conversion des scénarios générés en documents structurés au format JSON.

Stockage des scénarios et métadonnées dans une base de données MongoDB afin d’assurer leur réutilisation.

Exécution des tests de performance et analyse des résultats via les outils natifs de JMeter et Gatling.

Cette architecture permet une séparation claire entre la génération, le stockage et l’exécution des tests.

3. Structure du dépôt
Test-performance-IA
├── Gatling/
│ ├── Test.scala → Script Gatling généré automatiquement
│ └── Test_Gatling.py → Génère automatiquement un fichier .json pour le stockage dans MongoDB
│
├── JMeter/
│ ├── Test.jmx → Script JMeter généré automatiquement
│ └── Test_JMeter.py → Génère automatiquement un fichier .json pour le stockage dans MongoDB
│
├── Mongo/
│ ├── inserer.py → Insère les documents JSON dans MongoDB
│ ├── document_Gatling.JSON → Script Gatling encodé en JSON
│ └── document_JMeter.JSON → Script JMeter encodé en JSON
│
├── LICENSE
└── README.md

4. Prérequis techniques

Java JDK 8 ou supérieur

Apache JMeter (version 5.6 ou supérieure)

Gatling (version 3.7.6)

Python 3.8 ou supérieur

MongoDB (local ou distant)

Les tests ont été réalisés dans un environnement local, mais la solution peut être adaptée à d’autres contextes.

5. Exécution des tests
5.1 Tests avec Apache JMeter

Ouvrir Apache JMeter.

Charger le fichier :

jmeter/test.jmx

Adapter au besoin les paramètres (nombre d’utilisateurs, durée, URL cible).

Lancer l’exécution du test depuis l’interface graphique ou en mode non graphique.

5.2 Tests avec Gatling

Copier le fichier :

Test.scala

dans le dossier user-files/simulations de Gatling.

Lancer Gatling depuis la ligne de commande.

Sélectionner la simulation Test.

Consulter le rapport HTML généré à la fin de l’exécution.

6. Génération et stockage des scénarios

Les scripts Python permettent de générer automatiquement des descriptions de tests et de les stocker sous forme de documents JSON.

Test_JMeter.py : génération et structuration de scénarios pour JMeter

Test_Gatling.py : génération et structuration de scénarios pour Gatling

inserer.py : insertion des documents JSON dans MongoDB

Ces scripts constituent une base extensible pour automatiser davantage la génération et la gestion des tests.


7. Réutilisation pédagogique

Le dépôt est volontairement structuré de manière simple afin de faciliter sa réutilisation par des équipes étudiantes.
Il peut servir de point de départ pour :

un projet de cours,

un travail de session,

ou une expérimentation de recherche appliquée sur les tests de performance assistés par l’IA.

8. Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE.
9. Auteure

Siham Benbeka
Étudiante à la maîtrise en Génie des technologies de l'information
ÉTS Montréal – supervisé par le Professeur. Alain April
