# Choose Your Story

Hemos creado un minijuego desarrollado en Python como proyecto para el curso primero de DAW (Desarrollo de Aplicaciones Web).

---

## Descripción del proyecto

El juego consiste en una **versión reducida del género de juego aventura conversacional**.

Características principales:
- Sistema de registro de usuarios
- Visualización de las partidas de otros jugadores
- Estadísticas
- 2 historias para jugar

Una de las historias está basada en el reconocido juego Stanley Parable, pero una versión más reducida a modo de demo.

---

## Tecnologías utilizadas

- Lenguaje: Python
- Librerías: PyMySQL y os (Para limpiar el terminal)
- Desarrollado en: VSCode y PyCharm

---

## Requisitos del sistema

Para ejecutar el proyecto es necesario contar con:

- Se conoce que funciona bien con Python 3.12.3
- Debería funcionar con cualquier sistema operativo (Windows, Linux o macOS), pero está testeado en Windows 11 y Ubuntu
- Instalar la librería PyMySQL.

---

## Instalación (Programa Python)

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/MohamedAdghir/Choose_your_story.git
   ```

2. Accedir al directori del projecte:
   ```bash
   cd Choose_your_story
   ```

3. Instalar el paquete PyMySQL:
   ```bash
   pip3 install pymysql
   ```

## Instalación (Base de datos)

*Nosotros hemos utilizado Ubuntu para hostear nuestra base de datos, así que el tutorial a continuación serán los pasos para Ubuntu o distribuciones parecidas.*

1. Instalar MySQL Server:
   ```bash
   sudo apt install mysql-server
   ```

2. Activar el servicio:
   ```bash
   sudo service mysql start
   ```

3. Accedemos a la base de datos:
   ```bash
   sudo mysql -u root
   ```

4. Dentro de la base de datos creamos el usuario que utilizará el programa python para acceder a la base de datos:
   ```sql
   CREATE USER 'pyuser'@'host' IDENTIFIED BY 'contraseña';
   ```
> [!NOTE]
> pyuser puede ser cambiado por el nombre que quieras darle al usuario, pero luego deberá editarse en el código.
> host deberá ser sustituido por la IP donde se encuentre hosteada la base de datos, si tienes la base de datos en tu ordenador, deberás poner localhost o 127.0.0.1
> contraseña cambiala por la contraseña que quieras utilizar