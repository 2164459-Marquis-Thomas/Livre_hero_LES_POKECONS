/**
 * Crypte un texte clair en utilisant la clé de cryptage définie ci-dessus. 
 * Elle retourne le texte crypté.
 * @param: chaîne de caractère à crypter
 * @return: un blob contenant les données cryptées
 */
DELIMITER $$
CREATE FUNCTION crypter(_donnee TEXT) RETURNS BLOB DETERMINISTIC
 BEGIN RETURN aes_encrypt(_donnee, 'GabinNouchette');
END $$
DELIMITER ;

/*
 * Décrypte un contenu crypté en utilisant la clé de cryptage définie ci-dessus. Elle 
 * retourne le texte clair prêt à être lu par un être humain.
 * @Param: un blob contenant des données cryptées
 * @return: une chaîne de caractère affichant le texte clair
 */
DELIMITER $$
 CREATE FUNCTION decrypter(_donnee BLOB) RETURNS TEXT DETERMINISTIC 
 BEGIN RETURN aes_decrypt(_donnee, 'GabinNouchette');
END $$
DELIMITER ;