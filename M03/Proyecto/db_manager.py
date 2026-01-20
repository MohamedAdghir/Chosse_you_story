import pymysql

def connect_to_db():
    host = "127.0.0.1"
    port = 3307
    user = 'ibtipyuser'
    password = '1234567890'
    database = 'choose_your_story'

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as e:
        print("Error al conectar a la base de datos:", e)
        return None

def get_characters():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM CHARACTERS")
            resultados = cursor.fetchall()

        # Formateo personalizado
        characters = {}
        for row in resultados:
            characters[row['id_character']] = row['name']
        return characters
    except pymysql.MySQLError as e:
        print("Error al ejecutar la sentencia:", e)
        return None
    finally:
        connection.close()

#print(get_characters())
def get_users():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM USERS")
            resultados = cursor.fetchall()

        # Formateo personalizado
        users = {}
        for row in resultados:
            users[row["username"]] = {"password": row["password"], "userId": row["id_user"]}
        return users
    except pymysql.MySQLError as e:
        print("Error al ejecutar la sentencia:", e)
        return None
    finally:
        connection.close()

def get_user_ids():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM USERS")
            resultados = cursor.fetchall()

        # Formateo personalizado
        user_ids = [[],[]]
        for row in resultados:
            user_ids[0].append(row["username"])
            user_ids[1].append(row["id_user"])
        return user_ids
    except pymysql.MySQLError as e:
        print("Error al ejecutar la sentencia:", e)
        return None
    finally:
        connection.close()

#print(get_user_ids())


def get_adventures_with_chars():
    connection = connect_to_db()
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT a.id_adventure, a.name, a.description, ca.id_character FROM ADVENTURE a LEFT JOIN CHARACTER_ADVENTURE ca ON a.id_adventure = ca.id_adventure")
            resultados = cursor.fetchall()
            adventures = {}
            for row in resultados:
                adv_id = row["id_adventure"]
                if adv_id not in adventures:
                    adventures[adv_id] = {"Name": row["name"], "Description": row["description"],"Characters": []}
                adventures[adv_id]["Characters"].append(row["id_character"])
            return adventures
    except pymysql.MySQLError as e:
        print("Error al ejecutar la sentencia:",e)
        return None
    finally:
        connection.close()

#print(get_adventures_with_chars())

def get_id_bystep_adventure(id_adventure):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT as_step.id_adventure_step, 
                       as_step.description, 
                       as_step.final_step, 
                       as_step.next_step,
                       asw.id_adventure_step_answer
                FROM ADVENTURE_STEP as_step
                LEFT JOIN ADVENTURE_STEP_ANSWER asw 
                       ON as_step.id_adventure_step = asw.id_adventure_step
                WHERE as_step.id_adventure = %s
            """
            cursor.execute(sql, (id_adventure,))
            resultados = cursor.fetchall()

            id_by_steps = {}

            for row in resultados:
                id_step = row['id_adventure_step']

                if id_step not in id_by_steps:
                    id_by_steps[id_step] = {
                        'Description': row['description'],
                        'answers_in_step': [],
                        'Final_Step': row['final_step'],
                        'Next_Step': row['next_step']
                    }

                if row['id_adventure_step_answer'] is not None:
                    id_by_steps[id_step]['answers_in_step'].append(row['id_adventure_step_answer'])

            for step in id_by_steps.values():
                step['answers_in_step'] = tuple(step['answers_in_step'])

            return id_by_steps

    except Exception as e:
        print("Error al ejecutar la sentencia:", e)
        return None
    finally:
        connection.close()

def insertUser(user,password):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "insert into USERS (username,password,created_by) values (%s, %s,CURRENT_USER())"
            cursor.execute(sql,(user,password))
            connection.commit()
    except pymysql.MySQLError as e:
        print("Error al insertar el usuario:", e)
    finally:
        connection.close()

def insertGame(userID,characterID,adventureID):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "insert into GAME (id_user,id_character,id_adventure) values (%s, %s, %s)"
            cursor.execute(sql,(userID,characterID,adventureID))
            connection.commit()
    except pymysql.MySQLError as e:
        print("Error al insertar el usuario:", e)
    finally:
        connection.close()

def insertChoice(gameID,stepID,answerID):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "insert into CHOICE (id_game,id_adventure_step,id_adventure_step_answer) values (%s, %s, %s)"
            cursor.execute(sql,(gameID,stepID,answerID))
            connection.commit()
    except pymysql.MySQLError as e:
        print("Error al insertar el usuario:", e)
    finally:
        connection.close()

def getIdGames():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id_game FROM GAME"
            cursor.execute(sql)
            resultado = cursor.fetchall()

            ids = []
            for fila in resultado:
                ids.append(fila["id_game"])
            return tuple(ids)
    except pymysql.MySQLError as e:
        print("Error:", e)
        return ()
    finally:
        connection.close()

#insertUser("jeffrey","Phreth!1")

def get_first_step_adventure(adventure_id):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "select id_adventure_step from ADVENTURE_STEP where id_adventure = %s and first_step = 1"
            cursor.execute(sql,(adventure_id))
            resultado = cursor.fetchone()
            if resultado is None:
                return None
            else:
                return resultado["id_adventure_step"]
    except pymysql.MySQLError as e:
        print("Error:", e)
    finally:
        connection.close()


#print(get_first_step_adventure(1))
        
def get_answers_bystep_adventure(adventure_id_step):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "select id_adventure_step_answer,id_adventure_step,description,resolution,next_step from ADVENTURE_STEP_ANSWER where id_adventure_step =  %s "
            cursor.execute(sql,(adventure_id_step))
            resultado = cursor.fetchall()
            answers = {}
            for fila in resultado:
                clave = (fila["id_adventure_step_answer"],fila["id_adventure_step"])
                answers[clave] = {"Description": fila["description"],"Resolution_Answer": fila["resolution"],"NextStep_Adventure": fila["next_step"]}
            return answers
    except pymysql.MySQLError as e:
        print("Error:", e)
    finally:
        connection.close()

#print(get_answers_bystep_adventure(1))
def checkUserbdd(user,password):
    existingUsers = get_users()
    if user not in existingUsers:
        return 0
    elif existingUsers[user]["password"] != password:
        return -1
    else:
        return 1

def most_played_player():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = """
                     SELECT 
                       u.username AS "NOMBRE USUARIO", 
                       COUNT(g.id_game) AS "PARTIDAS JUGADAS"
                     FROM 
                        USERS u
                     JOIN 
                         GAME g ON u.id_user = g.id_user 
                     GROUP BY 
                         u.id_user, u.username, u.created_at
                     ORDER BY 
                       "PARTIDAS JUGADAS" DESC, 
                       u.created_at ASC
                     LIMIT 1;
                   """
            cursor.execute(sql)
            resultado = cursor.fetcone()
            if resultado:
                return  resultado["NOMBRE USUARIO"], resultado["PARTIDAS JUGADAS"]
            return None
    except pymysql.MySQLError as e:
        print("Error:", e)
    finally:
        connection.close()


def GetPlayerAdventureLog(username):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT 
                    a.id_adventure AS idadventure, 
                    a.name AS Name, 
                    g.playing_date AS date
                FROM 
                    GAME g
                JOIN 
                    USERS u ON g.id_user = u.id_user
                JOIN 
                    ADVENTURE a ON g.id_adventure = a.id_adventure
                WHERE 
                    u.username = %s
                ORDER BY 
                    g.playing_date DESC;
            """
            cursor.execute(sql, (username,))

            resultado = cursor.fetchall()

            if resultado:
                return resultado
            else:
                print("No se encontraron aventuras para el usuario: {}".format(username) )
                return []
    except pymysql.MySQLError as e:
        print("Error en la base de datos:", e)
        return None
    finally:
        connection.close()

def GetMostUsedAnswersReport():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT 
                    CONCAT(a.id_adventure, ' - ', a.name) AS "ID AVENTURA - NOMBRE",
                    CONCAT(s.id_adventure_step, ' - ', s.description) AS "ID PASO - DESCRIPCION",
                    CONCAT(ans.id_adventure_step_answer, ' - ', ans.description) AS "ID RESPUESTA - DESCRIPCION",
                    COUNT(c.id_adventure_step_answer) AS "NUMERO VECES SELECCIONADA"
                FROM 
                    ADVENTURE a
                JOIN 
                    ADVENTURE_STEP s ON a.id_adventure = s.id_adventure
                JOIN 
                    ADVENTURE_STEP_ANSWER ans ON s.id_adventure_step = ans.id_adventure_step
                LEFT JOIN 
                    CHOICE c ON ans.id_adventure_step_answer = c.id_adventure_step_answer
                GROUP BY 
                    a.id_adventure, a.name, 
                    s.id_adventure_step, s.description, 
                    ans.id_adventure_step_answer, ans.description
                ORDER BY 
                    a.id_adventure ASC, 
                    s.id_adventure_step ASC, 
                    COUNT(c.id_adventure_step_answer) DESC;
            """
            cursor.execute(sql)

            resultado = cursor.fetchall()

            if resultado:
                return resultado
            else:
                print("No se encontraron datos para el informe de respuestas.")
                return []
    except pymysql.MySQLError as e:
        print("Error en la base de datos:", e)
        return None
    finally:
        connection.close()

def getIdGames():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id_game FROM GAME"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            ids = []
            for fila in resultado:
                ids.append(fila["id_game"])
            n=len(ids)
            for i in range(n):
                cambios = False
                for j in range (0,n - i - 1):
                    if ids[j] > ids[j+1]:
                        ids[j],ids[j+1] = ids[j+1],ids[j]
                        cambios = True
                if not cambios:
                    break
            return tuple(ids)
    except pymysql.MySQLError as e:
        print("Error:", e)
        return ()
    finally:
        connection.close()

#print(getIdGames())

def getReplayAdventures():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT 
                    g.id_game,
                    u.id_user,
                    u.username,
                    a.id_adventure,
                    a.name AS adventure_name,
                    g.playing_date,
                    c.id_character,
                    c.name AS character_name
                FROM GAME g
                JOIN USERS u ON g.id_user = u.id_user
                JOIN ADVENTURE a ON g.id_adventure = a.id_adventure
                JOIN CHARACTERS c ON g.id_character = c.id_character
                ORDER BY g.playing_date DESC
            """
            cursor.execute(sql)
            resultado = cursor.fetchall()

            replayAdventures = {}
            for fila in resultado:
                replayAdventures[fila["id_game"]] = {
                    "idUser": fila["id_user"],
                    "Username": fila["username"],
                    "idAdventure": fila["id_adventure"],
                    "Name": fila["adventure_name"],
                    "date": fila["playing_date"],
                    "idCharacter": fila["id_character"],
                    "CharacterName": fila["character_name"]
                }
            return replayAdventures
    except pymysql.MySQLError as e:
        print("Error:", e)
        return {}
    finally:
        connection.close()

#print(getReplayAdventures())



def getChoices(idGame):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT 
                    id_adventure_step,
                    id_adventure_step_answer
                FROM CHOICE
                WHERE id_game = %s
                ORDER BY id_adventure_step ASC
            """
            cursor.execute(sql, (idGame,))
            resultado = cursor.fetchall()

            choices = []
            for fila in resultado:
                choices.append(
                    (fila["id_adventure_step"], fila["id_adventure_step_answer"])
                )

            return tuple(choices)
    except pymysql.MySQLError as e:
        print("Error:", e)
        return ()
    finally:
        connection.close()

#print(getChoices(1))
