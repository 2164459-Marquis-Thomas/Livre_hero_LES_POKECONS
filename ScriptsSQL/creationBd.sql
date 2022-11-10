DROP DATABASE IF EXISTS Livre_hero;
CREATE DATABASE Livre_hero;
USE Livre_hero;

CREATE TABLE livre(
id int auto_increment primary key,
nom varchar(255)
);

create table chapitre(
id int auto_increment primary key,
no_chapitre varchar(255) not null,
texte text
);

create table lien_chapitre(
id int auto_increment primary key,
no_chapitre_origine varchar(255) not null,
no_chapitre_destination varchar(255)
);

create table joueur_sauvegarde(
id int auto_increment primary key,
nom blob not null,
chapitre_pogression varchar(255),
point_de_vie int,
combat int,
endurance int
);