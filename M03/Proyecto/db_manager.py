import pymysql

def connect_to_db():
    host = "192.168.20.166"
    user = 'pyuserremote'
    password = 'Password1!'
    database = 'choose_your_story'

    try:
        connection = pymysql.connect(
            host=host,
            user=user,
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

print(get_id_bystep_adventure())