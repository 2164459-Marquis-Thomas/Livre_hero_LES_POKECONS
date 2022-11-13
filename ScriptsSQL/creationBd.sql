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
no_chapitre_destination int,
foreign key (no_chapitre_origine) references chapitre(no_chapitre)
);

create table joueur_sauvegarde(
id int auto_increment primary key,
nom blob not null,
chapitre_pogression int,
point_de_vie int,
combat int,
endurance int,
FOREIGN KEY (chapitre_pogression) REFERENCES chapitre(no_chapitre)
);

select no_chapitre_destination from lien_chapitre lc 
inner join chapitre on no_chapitre_origine = no_chapitre 
where no_chapitre_origine = 1;