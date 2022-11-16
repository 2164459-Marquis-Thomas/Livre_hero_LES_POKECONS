CREATE USER IF NOT EXISTS 'Gab'@'localhost' IDENTIFIED BY 'jouet';
CREATE ROLE IF NOT EXISTS 'esclave';
GRANT 'esclave' TO 'Gab'@'localhost';
GRANT ALL PRIVILEGES ON Livre_hero.* TO 'Gab'@'localhost';