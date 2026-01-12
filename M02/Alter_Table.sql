USE choose_your_story;

/* -------------- Restricciones para la tabla USERS -------------- */

/* id_user */
ALTER TABLE USERS
MODIFY id_user INT UNSIGNED NOT NULL AUTO_INCREMENT, /* INT, no negativo, no nulo, autoincremental */
ADD PRIMARY KEY (id_user); /* Añadirlo como PK */

/* username */
ALTER TABLE USERS
MODIFY username VARCHAR(10) NOT NULL, /* VARCHAR(10), no nulo */
ADD UNIQUE (username), /* Debe ser unico */
ADD CONSTRAINT chk_username_length CHECK (CHAR_LENGTH(username) BETWEEN 6 AND 10), /* La longitud debe ser entre 6 y 10 caracteres */
ADD CONSTRAINT chk_username_chars CHECK (username REGEXP '^[A-Za-z0-9]+$'); /* Validar el input utilizando REGEXP */

/* password */
ALTER TABLE USERS
MODIFY password VARCHAR(12) NOT NULL, /* VARCHAR(12), no nulo */
ADD CONSTRAINT chk_password_length CHECK (CHAR_LENGTH(password) BETWEEN 8 AND 12), /* La longitud debe ser entre 6 y 10 caracteres */
ADD CONSTRAINT chk_password_complexity CHECK (password REGEXP '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])[^ ]+$'); /* Validar el input utilizando REGEXP */

/* created_at */
ALTER TABLE USERS
MODIFY created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
/* TIMESTAMP, no nulo, por defecto será la fecha actual (la fecha de insercion del dato) */

/* created_by */
ALTER TABLE USERS
MODIFY created_by VARCHAR(20) NOT NULL DEFAULT CURRENT_USER;
/* VARCHAR(20), no nulo, por defecto será el usuario actual, el que este introduciendo los datos */

/* updated_at */
ALTER TABLE USERS
MODIFY updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP;
/* TIMESTAMP, puede ser nulo, por defecto será nulo, esta columna se actualizará a la fecha actual si se modifica el dato */

/* updated_by */
ALTER TABLE USERS
MODIFY updated_by VARCHAR(20) NULL DEFAULT NULL ON UPDATE CURRENT_USER;
/* VARCHAR(20), puede ser nulo, por defecto será nulo, esta columna se actualizará con el usuario actual si se modifica el dato */

/* --------------------------------------------------------------- */

/* ----------- Restricciones para la tabla CHARACTERS ------------ */

/* id_character */
ALTER TABLE CHARACTERS
MODIFY id_character INT UNSIGNED NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_character);

/* name */
ALTER TABLE CHARACTERS
MODIFY name VARCHAR(20) NOT NULL,
ADD UNIQUE (name);

/* created_at */
ALTER TABLE CHARACTERS
MODIFY created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
/* TIMESTAMP, no nulo, por defecto será la fecha actual (la fecha de insercion del dato) */

/* created_by */
ALTER TABLE CHARACTERS
MODIFY created_by VARCHAR(20) NOT NULL DEFAULT CURRENT_USER;
/* VARCHAR(20), no nulo, por defecto será el usuario actual, el que este introduciendo los datos */

/* updated_at */
ALTER TABLE CHARACTERS
MODIFY updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP;
/* TIMESTAMP, puede ser nulo, por defecto será nulo, esta columna se actualizará a la fecha actual si se modifica el dato */

/* updated_by */
ALTER TABLE CHARACTERS
MODIFY updated_by VARCHAR(20) NULL DEFAULT NULL ON UPDATE CURRENT_USER;
/* VARCHAR(20), puede ser nulo, por defecto será nulo, esta columna se actualizará con el usuario actual si se modifica el dato */

/* --------------------------------------------------------------- */

/* ------------ Restricciones para la tabla ADVENTURE ------------ */

/* id_adventure */
ALTER TABLE ADVENTURE
MODIFY id_character INT UNSIGNED NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_adventure);

/* name */
ALTER TABLE ADVENTURE
MODIFY name VARCHAR(20) NOT NULL,
ADD UNIQUE (name);

/* description */
ALTER TABLE ADVENTURE
MODIFY description TEXT NOT NULL;

/* created_at */
ALTER TABLE ADVENTURE
MODIFY created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
/* TIMESTAMP, no nulo, por defecto será la fecha actual (la fecha de insercion del dato) */

/* created_by */
ALTER TABLE ADVENTURE
MODIFY created_by VARCHAR(20) NOT NULL DEFAULT CURRENT_USER;
/* VARCHAR(20), no nulo, por defecto será el usuario actual, el que este introduciendo los datos */

/* updated_at */
ALTER TABLE ADVENTURE
MODIFY updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP;
/* TIMESTAMP, puede ser nulo, por defecto será nulo, esta columna se actualizará a la fecha actual si se modifica el dato */

/* updated_by */
ALTER TABLE ADVENTURE
MODIFY updated_by VARCHAR(20) NULL DEFAULT NULL ON UPDATE CURRENT_USER;
/* VARCHAR(20), puede ser nulo, por defecto será nulo, esta columna se actualizará con el usuario actual si se modifica el dato */

/* --------------------------------------------------------------- */

/* ------- Restricciones para la tabla CHARACTER_ADVENTURE ------- */

/* id_character & id_adventure (restricciones) */
ALTER TABLE CHARACTER_ADVENTURE
MODIFY id_character INT UNSIGNED NOT NULL,
MODIFY id_adventure INT UNSIGNED NOT NULL;

/* PK compuesta por ambos campos */
ALTER TABLE CHARACTER_ADVENTURE
ADD PRIMARY KEY (id_character, id_adventure);

/* Creamos la FK de id_character */
ALTER TABLE CHARACTER_ADVENTURE
ADD CONSTRAINT fk_character_adventure_character
FOREIGN KEY (id_character) REFERENCES CHARACTERS(id_character)
ON DELETE CASCADE
ON UPDATE CASCADE;

/* Creamos la FK de id_adventure */
ALTER TABLE CHARACTER_ADVENTURE
ADD CONSTRAINT fk_character_adventure_adventure
FOREIGN KEY (id_adventure) REFERENCES ADVENTURE(id_adventure)
ON DELETE CASCADE
ON UPDATE CASCADE;

/* ON DELETE CASCADE & ON UPDATE CASCADE: Si se elimina/actualiza un personaje/aventura se eliminaran/modificaran los registros en esta tabla */

/* created_at */
ALTER TABLE CHARACTER_ADVENTURE
MODIFY created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
/* TIMESTAMP, no nulo, por defecto será la fecha actual (la fecha de insercion del dato) */

/* created_by */
ALTER TABLE CHARACTER_ADVENTURE
MODIFY created_by VARCHAR(20) NOT NULL DEFAULT CURRENT_USER;
/* VARCHAR(20), no nulo, por defecto será el usuario actual, el que este introduciendo los datos */

/* updated_at */
ALTER TABLE CHARACTER_ADVENTURE
MODIFY updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP;
/* TIMESTAMP, puede ser nulo, por defecto será nulo, esta columna se actualizará a la fecha actual si se modifica el dato */

/* updated_by */
ALTER TABLE CHARACTER_ADVENTURE
MODIFY updated_by VARCHAR(20) NULL DEFAULT NULL ON UPDATE CURRENT_USER;
/* VARCHAR(20), puede ser nulo, por defecto será nulo, esta columna se actualizará con el usuario actual si se modifica el dato */

/* --------------------------------------------------------------- */

/* ---------- Restricciones para la tabla ADVENTURE_STEP --------- */

/* id_adventure_step */
ALTER TABLE ADVENTURE_STEP
MODIFY id_adventure_step INT UNSIGNED NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_adventure_step);

/* id_adventure */
ALTER TABLE ADVENTURE_STEP
MODIFY id_adventure INT UNSIGNED NOT NULL;

/* Creamos la FK de id_adventure */
ALTER TABLE ADVENTURE_STEP
ADD CONSTRAINT fk_adventure_step_adventure
FOREIGN KEY (id_adventure) REFERENCES ADVENTURE(id_adventure)
ON DELETE CASCADE
ON UPDATE CASCADE;

/* description */
ALTER TABLE ADVENTURE_STEP
MODIFY description TEXT NOT NULL;

/* first_step */
ALTER TABLE ADVENTURE_STEP
MODIFY first_step BOOLEAN NOT NULL;

/* final_step */
ALTER TABLE ADVENTURE_STEP
MODIFY final_step BOOLEAN NOT NULL;

/* created_at */
ALTER TABLE ADVENTURE_STEP
MODIFY created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
/* TIMESTAMP, no nulo, por defecto será la fecha actual (la fecha de insercion del dato) */

/* created_by */
ALTER TABLE ADVENTURE_STEP
MODIFY created_by VARCHAR(20) NOT NULL DEFAULT CURRENT_USER;
/* VARCHAR(20), no nulo, por defecto será el usuario actual, el que este introduciendo los datos */

/* updated_at */
ALTER TABLE ADVENTURE_STEP
MODIFY updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP;
/* TIMESTAMP, puede ser nulo, por defecto será nulo, esta columna se actualizará a la fecha actual si se modifica el dato */

/* updated_by */
ALTER TABLE ADVENTURE_STEP
MODIFY updated_by VARCHAR(20) NULL DEFAULT NULL ON UPDATE CURRENT_USER;
/* VARCHAR(20), puede ser nulo, por defecto será nulo, esta columna se actualizará con el usuario actual si se modifica el dato */

/* --------------------------------------------------------------- */

/* ------ Restricciones para la tabla ADVENTURE_STEP_ANSWER ------ */

/* id_adventure_step_answer */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY id_adventure_step_answer INT UNSIGNED NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_adventure_step_answer);

/* id_adventure_step */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY id_adventure_step INT UNSIGNED NOT NULL;

/* Creamos la FK de id_adventure_step */
ALTER TABLE ADVENTURE_STEP_ANSWER
ADD CONSTRAINT fk_adventure_step_answer_adventure_step
FOREIGN KEY (id_adventure_step) REFERENCES ADVENTURE_STEP(id_adventure_step)
ON DELETE CASCADE
ON UPDATE CASCADE;

/* description */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY description TEXT NOT NULL;

/* resolution */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY resolution TEXT NOT NULL;

/* next_step */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY next_step INT UNSIGNED NULL;

/* Creamos la FK de id_adventure_step */
ALTER TABLE ADVENTURE_STEP_ANSWER
ADD CONSTRAINT fk_adventure_step_answer_next_step_adventure_step
FOREIGN KEY (next_step) REFERENCES ADVENTURE_STEP(id_adventure_step);

/* created_at */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
/* TIMESTAMP, no nulo, por defecto será la fecha actual (la fecha de insercion del dato) */

/* created_by */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY created_by VARCHAR(20) NOT NULL DEFAULT CURRENT_USER;
/* VARCHAR(20), no nulo, por defecto será el usuario actual, el que este introduciendo los datos */

/* updated_at */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP;
/* TIMESTAMP, puede ser nulo, por defecto será nulo, esta columna se actualizará a la fecha actual si se modifica el dato */

/* updated_by */
ALTER TABLE ADVENTURE_STEP_ANSWER
MODIFY updated_by VARCHAR(20) NULL DEFAULT NULL ON UPDATE CURRENT_USER;
/* VARCHAR(20), puede ser nulo, por defecto será nulo, esta columna se actualizará con el usuario actual si se modifica el dato */

/* --------------------------------------------------------------- */

/* -------------- Restricciones para la tabla GAME --------------- */

/* id_game */
ALTER TABLE GAME
MODIFY id_game INT UNSIGNED NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (id_game);

/* id_user */
ALTER TABLE GAME
MODIFY id_user INT UNSIGNED NOT NULL;

/* Creamos la FK de id_user */
ALTER TABLE GAME
ADD CONSTRAINT fk_game_user
FOREIGN KEY (id_user) REFERENCES USERS(id_user);

/* id_character */
ALTER TABLE GAME
MODIFY id_character INT UNSIGNED NOT NULL;

/* Creamos la FK de id_character */
ALTER TABLE GAME
ADD CONSTRAINT fk_game_characters
FOREIGN KEY (id_character) REFERENCES CHARACTERS(id_character);

/* id_adventure */
ALTER TABLE GAME
MODIFY id_adventure INT UNSIGNED NOT NULL;

/* Creamos la FK de id_adventure */
ALTER TABLE GAME
ADD CONSTRAINT fk_game_adventure
FOREIGN KEY (id_adventure) REFERENCES ADVENTURE(id_adventure);

/* playing_date */
ALTER TABLE GAME
MODIFY playing_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;

/* --------------------------------------------------------------- */

/* -------------- Restricciones para la tabla CHOICE ------------- */

/* Reestricciones para las PKFK */
ALTER TABLE CHOICE
MODIFY id_game INT UNSIGNED NOT NULL,
MODIFY id_adventure_step INT UNSIGNED NOT NULL,
MODIFY id_adventure_step_answer INT UNSIGNED NOT NULL;

/* PK compuesta */
ALTER TABLE CHOICE
ADD PRIMARY KEY (id_game, id_adventure_step, id_adventure_step_answer);

/* FK adventure_step */
ALTER TABLE CHOICE
ADD CONSTRAINT fk_choice_game
FOREIGN KEY (id_game) REFERENCES GAME(id_game);

/* FK adventure_step */
ALTER TABLE CHOICE
ADD CONSTRAINT fk_choice_adventure_step
FOREIGN KEY (id_adventure_step) REFERENCES ADVENTURE_STEP(id_adventure_step);

/* FK adventure_step_answer */
ALTER TABLE CHOICE
ADD CONSTRAINT fk_choice_adventure_step_answer
FOREIGN KEY (id_adventure_step_answer) REFERENCES ADVENTURE_STEP_ANSWER(id_adventure_step_answer);
