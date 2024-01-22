create table T_auth(email varchar(50),
password varchar(50));

DELIMITER //
CREATE FUNCTION VerifierUtilisateur(email_param VARCHAR(50), password_param VARCHAR(50))
     RETURNS INT
     NO SQL
     BEGIN
         DECLARE utilisateur_existe INT;
     
         -- Vérifier si l'utilisateur existe
         SELECT COUNT(*) INTO utilisateur_existe
         FROM T_auth
         WHERE email = email_param AND password = password_param;
    
        RETURN utilisateur_existe;
    END //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE InscriptionUtilisateur(email_param VARCHAR(50), password_param VARCHAR(50))
    BEGIN
        INSERT INTO T_auth(email, password) VALUES (email_param, password_param);
    END //