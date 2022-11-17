DROP DATABASE IF EXISTS Livre_hero;
CREATE DATABASE Livre_hero;
USE Livre_hero;

CREATE TABLE livre(
id int auto_increment primary key,
nom varchar(255)
);

create table chapitre(
no_chapitre int not null primary key,
texte text
);

create table lien_chapitre(
id int auto_increment primary key,
no_chapitre_origine int not null,
no_chapitre_destination int
);

create table joueur_sauvegarde(
id int auto_increment primary key,
nom blob not null,
chapitre_pogression int,
FOREIGN KEY (chapitre_pogression) REFERENCES chapitre(no_chapitre)
);

/*
 * Nouvelle table.
 * */

CREATE TABLE fiche_personnage(
id int PRIMARY key auto_increment,
player_id int,
habilite int,
endurance int,
discipline_kai text,
arme text,
sac_a_dos text
);

