DROP SCHEMA IF EXISTS choose_your_story;
CREATE SCHEMA choose_your_story COLLATE = utf8_general_ci;
USE choose_your_story;

/* SCRIPT DE CREACION DE LA BASE DE DATOS Y SUS TABLAS (SIN RESTRICCIONES) */

/* He tenido que poner el nombre de esta tabla en plural porque USER es una palabra reservada */
CREATE TABLE USERS (
    id_user INT,
    username VARCHAR(10),
    password VARCHAR(12),
    created_at TIMESTAMP,
    created_by VARCHAR(20),
    updated_at TIMESTAMP,
    updated_by VARCHAR(20)
);

/* He tenido que poner el nombre de esta tabla en plural porque CHARACTER es una palabra reservada */
CREATE TABLE CHARACTERS (
    id_character INT,
    name VARCHAR(20),
    description TEXT, /* PREGUNTAR QUE PASA CON LA DESCRIPCIÓN <------------------------ */
    created_at TIMESTAMP,
    created_by VARCHAR(20),
    updated_at TIMESTAMP,
    updated_by VARCHAR(20)
);

CREATE TABLE ADVENTURE (
    id_adventure INT,
    name VARCHAR(40),
    description TEXT,
    created_at TIMESTAMP,
    created_by VARCHAR(20),
    updated_at TIMESTAMP,
    updated_by VARCHAR(20)
);

CREATE TABLE CHARACTER_ADVENTURE (
    id_character INT,
    id_adventure INT,
    created_at TIMESTAMP,
    created_by VARCHAR(20),
    updated_at TIMESTAMP,
    updated_by VARCHAR(20)
);

CREATE TABLE ADVENTURE_STEP (
    id_adventure_step INT,
    id_adventure INT,
    description TEXT,
    first_step BOOLEAN,
    final_step BOOLEAN,
    created_at TIMESTAMP,
    created_by VARCHAR(20),
    updated_at TIMESTAMP,
    updated_by VARCHAR(20)
);

CREATE TABLE ADVENTURE_STEP_ANSWER (
    id_adventure_step_answer INT,
    id_adventure_step INT,
    description TEXT,
    resolution TEXT,
    next_step INT,
    created_at TIMESTAMP,
    created_by VARCHAR(20),
    updated_at TIMESTAMP,
    updated_by VARCHAR(20)
);

CREATE TABLE GAME (
    id_game INT,
    id_user INT,
    id_character INT,
    id_adventure INT,
    playing_date TIMESTAMP
);

CREATE TABLE CHOICE (
    id_game INT,
    id_adventure_step INT,
    id_adventure_step_answer INT
);