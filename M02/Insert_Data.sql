use choose_your_story;

/* Usuario de prueba */
INSERT INTO USERS (username, password, created_by)
VALUES ('Tester', 'Passw0rd!', CURRENT_USER());

/* Personaje de prueba */
INSERT INTO CHARACTERS (name, created_by)
VALUES ('Makoke', CURRENT_USER());

/* Aventura de moha */
INSERT INTO ADVENTURE (name, description, created_by)
VALUES ('Vampiro me quiere matar', 'Un joven se ve atrapado en un juego mortal cuando un vampiro comienza a perseguirlo, desatando una lucha entre miedo y supervivencia mientras descubre secretos oscuros que amenazan su vida.', CURRENT_USER());

