# GVW

Ce projet a été réalisé en groupe dans le cadre de la fin de formation en tant que Data Analyst de 400 h proposée par Global Knowledge. Nous avons disposé de 9 jours pour réaliser ce projet, qui consistait en l'analyse des données de vente du Groupe Volkswagen (GVW).

# Resumé du projet

L'objectif de ce projet était d'effectuer une analyse des données de vente des différentes marques du GVW sur la période de 2017 à 2022 afin d'évaluer :

- Les différences entre les marques du GVW ; 
- Les impacts du COVID sur chacune des marques GVW ; 
- La présence du GVW dans différents pays ;
- Les tendances générales des voitures BEV et si le Groupe Volkswagen suit ces tendances.

## Méthodologie de travail
Dès le début du projet, nous avons établi un diagramme de Gantt pour identifier les risques associés à chaque tâche, désigner les responsables de chaque activité et planifier soigneusement toutes les étapes. La méthodologie suivie est la CRISP-DM (Cross Industry Standard Process for Data Mining), qui comprend 5 étapes : compréhension du business, compréhension des données, préparation des données, modélisation, évaluation et déploiement.

## Sources de données
### GVW
Les données que nous avons extraites du GVW étaient toutes sous forme de tableaux Excel, comme le suivant :

https://annualreport2022.volkswagenag.com/divisions/brands-and-business-fields.html 

Ces données concernent uniquement la performance du Groupe à l'échelle mondiale.

### Sources externes
Les autres données que nous avons extraites provenaient de différentes sources, telles que des tableaux dans des PDF et des tableaux en ligne.

- https://www.abcbourse.com/analyses/chiffres/VOW3f
- https://www.best-selling-cars.com/electric/2022-full-year-germany-best-selling-electric-cars-by-brand-and-model/
- https://www.best-selling-cars.com/germany/2022-full-year-germany-best-selling-car-brands/ 
- https://www.best-selling-cars.com/france/2022-full-year-france-top-20-best-selling-car-models/ 

https://www.best-selling-cars.com/europe/2022-full-year-europe-car-sales-per-eu-uk-and-efta-country/

## ETL
Pour l'extraction des données, nous avons employé le web scraping avec Python et avons également utilisé Python pour extraire des tableaux de documents PDF.

*Exemple de feuilles du GVW et de sources externes*

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/36868bd6-6a71-4df1-9061-1465cd1a4f75" height="250">
&nbsp;
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/771a1d62-156b-4832-900a-cc96aaae0404" height="250">



Pour effectuer la transformation et le nettoyage des données, nous avons également utilisé Python. 

Ainsi, nous avons réalisé les étapes suivantes avec Python  :
- Extraction de données de différentes sources (xlsx, site internet, pdf) en utilisant Pandas ;
- Dépivotement des colonnes ; 
- Suppression des colonnes et lignes non nécessaires ;

À la fin de ce processus, nous avons obtenu des flat tables pour les données du GVW et pour les données externes.

*Exemple de flat table obtenue pour les sources du groupe VW*

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/42739ff4-7e5e-4ac6-a4c4-e3bd69c8c8cd" height="250">


Entre l'extraction et le dépivotement des données, nous avons effectué une partie du nettoyage des données avec Excel, car nous avions des données en notation anglo-saxonne (avec des virgules pour les milliers) et nous devions les convertir en notation française.

Ensuite, nous avons utilisé Power BI pour une dernière partie du nettoyage des données. Nous avons également modélisé un entrepôt de données (Data Warehouse) pour les données internes du GVW ainsi qu'un autre pour les données extraites d'autres sources, incluant les groupes concurrents et le propre groupe VW.


## Analyse de données
Pour réaliser l'analyse des données, nous avons principalement utilisé Python et Power BI.

Tout d'abord, nous voulions répondre à la question : "Quelle marque se vend le mieux ?"

C'est pourquoi nous avons créé un premier tableau de bord pour répondre à cette question selon plusieurs paramètres : ventes de véhicules, bénéfices, chiffre d'affaires.

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/0614ad4e-ec58-42d2-b4b5-ce5d541c2991" height="300">


Pour évaluer le profil de chaque marque sur la période 2017-2022, notamment les changements de stratégies en fonction du COVID, nous avons opté pour, avant de faire les tableaux de bord, réaliser des matrices de corrélation pour chaque marque avec Python afin d'avoir des premières pistes sur les variables numériques qui ont une dépendance linéaire.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/c2b51598-ea40-492f-8ee7-7eb77878aae9" height="150">
&nbsp;
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/f95ad710-78e3-4cb3-b658-7208ce0449ef" height="150">

Nous avons ensuite élaboré des tableaux de bord sur Power BI pour obtenir une vue d'ensemble des tendances de chaque marque entre 2017 et 2022.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/68194466-3a42-4a35-a36b-72c60acc4361" height="250">

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/343266cf-9b6f-4a13-8e89-5b547ca35161" height="250">

Après avoir obtenu une vue générale, nous avons développé des tableaux de bord spécifiques pour chaque marque, en sélectionnant les types de graphiques les plus appropriés pour mettre en évidence les informations souhaitées.

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/f53a2f32-5f6d-4aca-bffd-21f364620f32" height="250">

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/ffc06928-a31b-4d9a-99a1-497a0d3beb15" height="300">


