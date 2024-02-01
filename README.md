# GVW

Ce projet a été réalisé en groupe dans le cadre de la fin de formation en tant que Data Analyst de 400 h proposée par Global Knowledge. Nous étions un groupe de 4 personnes et nous avons disposé de 9 jours pour réaliser ce projet, qui consistait en l'analyse des données de vente du Groupe Volkswagen (GVW).

# Resumé du projet

L'objectif de ce projet était d'effectuer une analyse des données de vente des différentes marques du GVW sur la période de 2017 à 2022 afin d'évaluer :

- Les meilleures ventes du GVW ;
- Les différences entre les marques du GVW ; 
- Les impacts du COVID sur chacune des marques GVW ;
- La quantité de modèles GVW parmi les voitures les plus vendues en France et en Allemagne ;
- La variation de la quantité de modèles GVW commercialisés parmi les modèles les plus vendus entre 2020 et 2022 ;
- Les tendances générales des voitures BEV et si le Groupe Volkswagen suit ces tendances.

## Méthodologie de travail
Dès le début du projet, nous avons établi un diagramme de Gantt pour identifier les risques associés à chaque tâche, désigner les responsables de chaque activité et planifier soigneusement toutes les étapes. La méthodologie suivie est la CRISP-DM (Cross Industry Standard Process for Data Mining), qui comprend 6 étapes : compréhension du business, compréhension des données, préparation des données, modélisation, évaluation et déploiement.

## Sources de données
### GVW
Les données que nous avons extraites du GVW étaient toutes sous forme de tableaux Excel, comme le suivant :

https://annualreport2022.volkswagenag.com/divisions/brands-and-business-fields.html 

Ces données concernent uniquement la performance du Groupe à l'échelle mondiale.

### Sources externes
Les autres données que nous avons extraites provenaient de différentes sources, telles que des tableaux dans des PDF et des tableaux en ligne.

- https://www.abcbourse.com/analyses/chiffres/VOW3f
- https://www.best-selling-cars.com/electric/2022-full-year-germany-best-selling-electric-cars-by-brand-and-model/
- https://www.best-selling-cars.com/france/2022-full-year-france-top-20-best-selling-car-models/ 
- https://www.best-selling-cars.com/europe/2022-full-year-europe-car-sales-per-eu-uk-and-efta-country/

## ETL
Pour l'extraction des données, nous avons employé le web scraping avec Python et avons également utilisé Python pour extraire des tableaux de documents PDF.

*Exemple de feuilles du GVW et de sources externes*

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/36868bd6-6a71-4df1-9061-1465cd1a4f75" height="250">
&nbsp;
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/771a1d62-156b-4832-900a-cc96aaae0404" height="250">



Pour effectuer la transformation et le nettoyage des données, nous avons également utilisé Python. 

Ainsi, nous avons réalisé les étapes suivantes avec Python  :
- Extraction de données de différentes sources (xlsx, site internet, pdf) ;
- Dépivotement des colonnes ; 
- Suppression des colonnes et lignes non nécessaires.

À la fin de ce processus, nous avons obtenu des flat tables pour les données du GVW et pour les données externes.

*Exemple de flat table obtenue pour les sources du groupe VW*

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/42739ff4-7e5e-4ac6-a4c4-e3bd69c8c8cd" height="250">


Entre l'extraction et le dépivotement des données, nous avons effectué une partie du nettoyage des données avec Excel, car nous avions des données en notation anglo-saxonne (avec des virgules pour les milliers) et nous devions les convertir en notation française.

Ensuite, nous avons utilisé Power BI pour une dernière partie du nettoyage des données. Nous avons également modélisé un entrepôt de données (Data Warehouse) en modèle de constellation pour les données internes du GVW ainsi que pour les données extraites d'autres sources, incluant les groupes concurrents et le groupe VW lui-même.

*Modélisation en constelation du Data Warehouse des données du GVW et des données de sources externes*

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/a7bace7b-9b68-42b3-8fc1-a8da246cbe10" height="250">
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/c47e98bb-276d-489a-a3b9-f9d21172b80b" height="250">



## Analyse de données
Pour réaliser l'analyse des données, nous avons principalement utilisé Python et Power BI.

### Groupe Volkswagen
Nous nous sommes d'abord concentrés sur les marques du groupe. La première question à laquelle nous voulions répondre était : "Quelle marque se vend le mieux ?"

C'est pourquoi nous avons créé un premier tableau de bord pour répondre à cette question selon plusieurs paramètres : ventes de véhicules, bénéfices, chiffre d'affaires.

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/0614ad4e-ec58-42d2-b4b5-ce5d541c2991" height="300">


Pour évaluer le profil de chaque marque sur la période 2017-2022, notamment les changements de stratégies en fonction du COVID, nous avons opté pour réaliser des matrices de corrélation pour chaque marque avec Python avant de créer les tableaux de bord, afin d'identifier les variables numériques présentant une dépendance linéaire.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/c2b51598-ea40-492f-8ee7-7eb77878aae9" height="150">
&nbsp;
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/f95ad710-78e3-4cb3-b658-7208ce0449ef" height="150">

Nous avons ensuite élaboré des tableaux de bord sur Power BI pour obtenir une vue d'ensemble des tendances de chaque marque entre 2017 et 2022.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/816821f4-2b01-4eb2-874a-4ceeda9f1a14" height="400">

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/969f2ec4-58cd-446a-a2c6-0a0369d63e7f" height="400">


Après avoir obtenu une vue générale, nous avons développé des tableaux de bord spécifiques pour chaque marque, en sélectionnant les types de graphiques les plus appropriés pour mettre en évidence les informations souhaitées.

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/b60398f0-fd9f-41c7-84a1-64bce0ea6373" height="400">
<br>
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/fce12737-3a64-4f8b-be7c-fca066dfd578" height="400">

### Le marché français et allemand


Après avoir analysé les données fournies par le GVW, nous nous sommes focalisés sur les données obtenues de sources externes. Concernant les sources externes, nous n'avions pas accès à la même plage d'années que celles du GVW ; la plage d'années était plus restreinte, allant de 2018 à 2022 ou de 2019 à 2022.

Avec ces données, nous nous sommes concentrés sur deux sujets principaux : la présence du GVW en France et en Allemagne par rapport aux autres marques et les tendances du marché électrique dans ces deux pays.

*Quantité de modèles GVW parmi les 21 modèles les plus vendus en France et en Allemagne*

<img src="https://github.com/angelicamiotti/GVW/assets/8940755/7e8042a8-ed67-4885-b0f3-ce1135ab2360" height="150">
&nbsp;
<img src="https://github.com/angelicamiotti/GVW/assets/8940755/a40b47f8-c68c-4cb0-a456-28f80424117b" height="150">


Ensuite, pour analyser les tendances du marché éléctrique, nous avons réalisé une normalisation afin de ne pas prendre en compte les fluctuations du marché au cours des années. C'est pourquoi nous avons analisé la vente de BEV (véhicules électriques à batterie) en pourcentage par rapport au total de véhicules vendus dans la période 2019-2022 dans chaque pays concerné. 

Ces données comprennent les enregistrements de tous les véhicules BEV dans ces pays, toutes marques confondues. Nous avons donc réalisé une régression linéaire avec Python et avons calculé le taux de croissance pour chacun des pays afin de les comparer. Nous avons ainsi  obtenu que la part de marché des BEV en Allemagne grimpe 48,6% plus rapidement que celle de la France, ce qui indique que les pays n'ont pas exactement le même profil. 

En utilisant la régression linéaire, nous avons calculé des dates auxquelles chaque pays pourrait atteindre 50 % de voitures BEV si la tendance observée par ces données se poursuit, et nous avons trouvé que l'Allemagne atteindrait cette valeur en 2028 tandis que la France l'atteindrait en 2032. Il doit être pris en considération que, vu la rareté de nos données, il est possible qu'avec plus de données à partir de 2023, la courbe change de profil.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/f2dedcc2-5367-49c7-8f7a-dafe27fe0c6b" height="250">

Ensuite, nous avons fait la même comparaison, mais cette fois entre la vente de tous les véhicules BEV en Allemagne et la vente de véhicules BEV du GVW en Allemagne, ce qui nous a donné le graphique suivant.


<img src="https://github.com/angelicamiotti/GVW/assets/8940755/45ed604a-572f-489c-9d0e-77f09d9d1b11" height="300">


En réalisant la régression linéaire avec la méthode des moindres carrés, nous avons calculé que le rythme de croissance des BEV en Allemagne dépasse de 38 % celui du Groupe VW, révélant un écart entre le constructeur et la tendance nationale. Avec ce graphique, nous pouvons conclure que le GVW a besoin de repenser ses stratégies s'il veut suivre la tendance des voitures électriques dans les années à venir en Allemagne.

### Conclusion
#### Conclusion de l'analyse
D'après nos analyses, il est possible de conclure que : 
- La marque qui possède la plus grande quantité de véhicules vendus n'est pas nécessairement celle qui génère le plus de profit ;
- Chaque marque possède un profil de consommateur différent et a été impactée de manière distincte par le COVID ;
- Le GVW a adopté des stratégies financières variées en fonction de chaque marque ;
- La stratégie du GVW sur le segment électrique pourrait évoluer pour améliorer l'attractivité de la marque.

#### Conclusion du projet
Après avoir réalisé ce projet, le groupe est arrivé à quelques conclusions. 
Tout d'abord, le projet nous a permis de mettre en pratique les apprentissages acquis durant la formation, tels que :
- La création de scripts Python pour la récupération des données ;
- La construction d'un schéma de Data Warehouse ;
- La normalisation d'une table de données ;
- L'utilisation de PowerBI pour créer des rapports de visualisation ;
- L'utilisation de Python pour créer des visualisations des données.

Le travail d'équipe dans le but de réaliser un projet d'analyse de données nous a permis de développer nos compétences en matière d'organisation du travail et de répartition des tâches, ainsi que de suivi de projet, notamment à travers l'utilisation de diagrammes de Gantt.


Nous avons également conclu que la qualité et la pertinence de l'analyse dépendent grandement de la qualité des données disponibles. Les étapes de compréhension du business et de préparation des données  sont des étapes cruciales dans le travail d'un Data Analyst.

