This project is detailed in the ETL class.

You are part of a 4-person data engineering team at a startup, tasked with designing and implementing an ELT pipeline. Your assignment is to submit a 2-4 page report detailing the choices made for the ELT pipeline and to provide a demo of an example database.

In your report, you need to clearly explain and justify your decisions for each phase of the pipeline:

Extract (E): Identify and explain where the data is coming from. Discuss the sources and why they were chosen.

Transform (T): Explain how the data is being transformed. Describe the processes, tools, and techniques used to clean, aggregate, or modify the data to make it useful for its intended purpose.

Load (L): Detail how the data is loaded into the system, how it is stored, and how it will be used or queried. Discuss the database or storage options chosen, and explain how the data will be utilized by the organization or application.

Along with the report, you are expected to provide a demo of an example database. You can use PostgreSQL or another database system of your choice. The demo should include:

Documented scripts to load and manipulate example data that demonstrates the choices made for the ETL pipeline.
The data used in the demo does not need to be exhaustive, but it should be sufficient to illustrate the key decisions in the ETL process.
coucou c'est moi 


On est deux types de données : les données statiques (fichier JSON) avec les caractéristiques des stations et les données temps-réel qui prennent en compte le remplissage des stations. 

ELT : car mise à jour des données temps-réel 



données statiques : 
number le numéro de la station. Attention, ce n'est pas un id, ce numéro n'est unique qu'au sein d'un contrat
contractName le nom du contrat de cette station
name le nom de la station
address adresse indicative de la station, les données étant brutes, parfois il s'agit plus d'un commentaire que d'une adresse.
position les coordonnées au format WGS84
banking indique la présence d'un terminal de paiement
bonus indique s'il s'agit d'une station bonus
overflow indique si la station accepte le repose de vélos en overflow
shape non utilisé pour l'instant


Données dynamiques

status indique l'état de la station, peut être CLOSED ou OPEN
connected indique si la station est connectée au système central
totalStands indique la capacité totale de la station
mainStands indique la capacité physique de la station
overflowStands indique la capacité overflow de la station
availabilities indique le nombre de place disponibles et le nombre de vélos accrochés par types de vélos
lastUpdate timestamp indiquant le moment de la dernière mise à jour
