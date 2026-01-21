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
> pyuser --> Usuario que queramos usar para conectar el programa a la base de datos

> host --> IP donde se encuentre la base de datos, si está en local puede ponerse localhost o 127.0.0.1

> contraseña --> Cambiala por la contraseña que quieras utilizar

5. Ejecutar los scripts .sql en el siguiente orden (Se pueden encontrar en M02)
   ```bash
   sudo mysql -u root < Create_DB.sql
   sudo mysql -u root choose_your_story < Alter_Table.sql
   sudo mysql -u root choose_your_story < Insert_Data.sql
   ```

---

## Ejecución y uso

> [!IMPORTANT]
> Para que funcione el juego, hay que tener en cuenta los datos que tenemos configurados dentro de db_manager.py

Al principio del archivo, podremos encontrar la siguiente función que se encarga de la conexión a la base de datos:
```python
def connect_to_db():
    host = "127.0.0.1" # IP de la base de datos. Dejar 127.0.0.1 si es local.
    port = 3307 # Puerto de la base de datos. Si se usa en local, reemplazar por 3306. Si se utiliza otro personalizado cambiarlo.
    user = 'pyuser' # Usuario que hemos configurado antes.
    password = '1234567890' # Reemplazar por la contraseña configurada antes.
    database = 'choose_your_story' # Dejar como está
```
Rellenaremos los datos con lo que indican los comentarios.

Para iniciar el juego, deberemos ejecutar el siguiente comando:
```bash
python3 main.py
```
Para utilizar las opciones del programa se tendrán que escribir los números indicados que tengan las opciones para seleccionarlas.

---

## Equipo del proyecto

| Integrante | Roles | Contacto |
|------------|-------|----------|
| Mohamed Adghir | Programador | madghirettaibi.cf@iesesteveterradas.cat |
| Héctor González | Programador & Gestor de la BBDD | hgonzalezgarcia.25cf@iesesteveterradas.cat |
| Ibtissam Ouald Ali | Programadora & Desarrolladora Web | ioualdali.25cf@iesesteveterradas.cat |

## Estado del proyecto
- Estado: Finalizado
- Versión: 1.0.0
- Tipo: Proyecto académico
