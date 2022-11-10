CREATE USER IF NOT EXISTS 'Gab' IDENTIFIED BY 'jouet';
CREATE ROLE IF NOT EXISTS 'esclave';
GRANT 'esclave' TO 'Gab';
GRANT all ON Livre_hero.* TO 'esclave';