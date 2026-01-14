import pymysql

def connect_to_db():
    host = "192.168.20.166"
    user = 'ibtipyuser'
    password = '1234567890'
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