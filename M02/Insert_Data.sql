use choose_your_story;

/* Usuario de prueba */
INSERT INTO USERS (username, password, created_by)
VALUES ('Tester', 'Passw0rd!', CURRENT_USER());

/* Personaje de prueba */
INSERT INTO CHARACTERS (name, created_by)
VALUES ('Makoke', CURRENT_USER()),
       ('Susana', CURRENT_USER());

/* Aventura de testeo */
INSERT INTO ADVENTURE (name, description, created_by)
VALUES ('Aventura de testeo', 'Una descripción lo suficientemente larga como para comprobar que el efecto de los formateos de texto queden efectivamente bien cuando las apliquemos realmente.', CURRENT_USER());

/* Personajes de la aventura de prueba */
INSERT INTO CHARACTER_ADVENTURE (id_character, id_adventure, created_by)
VALUES (1,1,CURRENT_USER()), (2,1,CURRENT_USER());

/* Pasos y respuestas de la aventura */
INSERT INTO ADVENTURE_STEP (id_adventure, description, first_step, final_step, created_by)
VALUES (1, 'Este es el tutorial para aprender a jugar al juego, $NAME.', TRUE, FALSE, CURRENT_USER()),
       (1, 'Te dijimos que si la pulsas ibas a morir.', FALSE, TRUE, CURRENT_USER()),
       (1, 'Pero las cosas no seran tan faciles como esto.', FALSE, FALSE, CURRENT_USER()),
       (1, 'Terminas sin hacer nada y mueres de aburrimiento.', FALSE, TRUE, CURRENT_USER()),
       (1, 'Bueno ya estoy cansado.', FALSE, FALSE, CURRENT_USER()),
       (1, '¿Por qué lo pulsaste si antes no lo hiciste? Estas muerto, por si no te ha quedado claro.', FALSE, TRUE, CURRENT_USER()),
       (1, 'Felicidades ya has pasado el tutorial', FALSE, TRUE, CURRENT_USER());

INSERT INTO ADVENTURE_STEP_ANSWER (id_adventure_step, description, resolution, next_step, created_by)
VALUES (1, 'Pulsa esta opción para continuar', 'Parece que vas entendiendo como funciona esto.', 3, CURRENT_USER()),
       (1, 'Si pulsas esta opción mueres', 'Sin hacer caso a la advertencia, pulsas el botón sin miedo a las amenazas.', 2, CURRENT_USER()),
       (1, 'No pulsar ninguna opción de las anteriores', 'No tienes ganas de jugar así que pulsas la opción mas aburrida que has visto.', 4, CURRENT_USER()),
       (3, 'No haces nada más', 'Piensas que esto es una perdida de tiempo y te rehusas a seguir jugando.', 4, CURRENT_USER()),
       (3, 'Si pulsas este botón ganas', 'Te dije que no iba a ser tan fácil ganar.', 5, CURRENT_USER()),
       (3, 'Como antes no has muerto pulsas esta opción para morir', 'Te pica la curiosidad sobre que hubiese pasado si pulsabas la otra opción y lo haces.', 6, CURRENT_USER()),
       (5, 'Pulsar para finalizar', 'La historia se acaba aquí, pero antes pondré un mensaje super largo para comprobar que el formateo de los textos funciona realmente bien en caso de que en nuestras historias reales pongamos textos así de largos o más.', 7, CURRENT_USER());

