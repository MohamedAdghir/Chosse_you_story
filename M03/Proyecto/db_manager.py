import pymysql

def connect_to_db():
    host = "127.0.0.1"
    user = 'mohapyuser'
    port = 3307
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


def get_id_bystep_adventure():
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT as_step.id_adventure_step, 
                    as_step.description, 
                    as_step.final_step, 
                    asw.id_adventure_step_answer
                FROM ADVENTURE_STEP as_step
                LEFT JOIN ADVENTURE_STEP_ANSWER asw 
                ON as_step.id_adventure_step = asw.id_adventure_step
            """
            cursor.execute(sql)
            resultados = cursor.fetchall()

            id_by_steps = {}

            for row in resultados:
                id_step = row['id_adventure_step']

                if id_step not in id_by_steps:
                    id_by_steps[id_step] = {
                        'Description': row['description'],
                        'answers_in_step': [],
                        'Final_Step': row['final_step']
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
       

#print(get_id_bystep_adventure())
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
    
#insertUser("jeffrey","Phreth!1")

def get_first_step_adventure(adventure_id):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            sql = ""
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
        with connection.cursor(pymysql.cursors.DictCursor)as cursor:
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

def GetPlayerAdventureLog():
    connection = connect_to_db()
    try:
        with  connection.cursor() as cursor:
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
            cursor.execute(sql)
            resultado = cursor.fetcall()
            for row in resultado:
                print("hola")
            else:
              return None
    except pymysql.MySQLError as e:
        print("Error:", e)
    finally:
        connection.close()
