from psycopg import connect
from User import User

class UserModel:
    def __init__(self):
        self.user= None

    def getConncetion(self):
        try:
            conn= connect("dbname= OtakuAI user=postgres password= osorio56 host=localhost port=5432")
            return conn
        
        except Exception as e:
            raise("Error conneting to the database: ", e)
        
    def insertUserInfo(self, firstname, lastname, email, password):
        try:
            connection= self.getConncetion()
            with connection.cursor() as cur:
                cur.execute(''' INSERT INTO user_info (id, f_name, l_name, email, password)
                                VALUES(uuid_generate_v4(), %s, %s, %s, %s) ''',
                                (firstname, lastname, email, password))
                
            connection.commit()
        except Exception as e:
            raise("Error inserting user information: ", e)
        finally:
            connection.close()

    def checkCredentials(self, email, password):
        try:
            connection= self.getConncetion()
            with connection.cursor() as cur:
                cur.execute('''
                            SELECT email, password, f_name, l_name password FROM user_info WHERE email = %s''', (email,))

                record = cur.fetchone()

                if record:
                    if record[1] == password:
                        self.user = User(record[2], record[3])
                        return True
                    else:
                        return False
                else:
                    return False
                
        except Exception as e:
            raise("Error checking credentails")
        finally:
            connection.close()
            
        