from psycopg import connect, errors
from BackEnd.Classes.User import User
from uuid import uuid4

class UserModel:
    def __init__(self):
        self.user= None

    def getConncetion(self):
        try:
            conn= connect("dbname= OtakuAI user=postgres password= password host=localhost port=5432")
            return conn
        
        except Exception as e:
            raise("Error conneting to the database: ", e)
        
    def insertUserInfo(self, firstname, lastname, email, password):
        try:
            status = 0
            u_id = uuid4()
            self.user = User(firstname, lastname, email, u_id)
            connection= self.getConncetion()
            with connection.cursor() as cur:
                cur.execute(''' 
                                INSERT INTO user_info (id, f_name, l_name, email, password)
                                VALUES(%s, %s, %s, %s, %s) ''',
                                (u_id ,firstname, lastname, email, password))
                
            connection.commit()
        except errors.UniqueViolation:
            status = 1
        except Exception as e:
            raise("Error inserting user information: ", e)
        finally:
            connection.close()
            return status

    def checkCredentials(self, email, password):
        try:
            connection= self.getConncetion()
            with connection.cursor() as cur:
                cur.execute('''
                                SELECT email, password, f_name, l_name, id FROM user_info WHERE email = %s
                            ''', (email,))

                record = cur.fetchone()
                
        except Exception as e:
            raise("Error checking credentails")
        
        finally:
            connection.close()

            if record:
                if record[1] == password:
                    self.user = User(record[2], record[3], record[0], record[4])
                    return True
                else:
                    return False
            else:
                return False
            
    def insertMangaToUser(self, manga):
        try:
            status = 0
            manga_title= manga.getTitle()
            connection= self.getConncetion()

            with connection.cursor() as cur:
                cur.execute('''
                                SELECT id FROM manga WHERE title = %s
                            ''', (manga_title,))
                
                m_record = cur.fetchone()
                m_id = m_record[0]

                cur.execute('''
                                INSERT INTO user_manga (user_id, manga_id) VALUES (%s, %s);

                            ''', (self.user.getID(), m_id))
                
                connection.commit()
        except errors.UniqueViolation:
            status = 1
        except Exception as e:

            raise("Error inserting the manga: ", e)
        finally:
            connection.close()
            if status != 1:
                self.user.addManga(manga)
            return status
        
    def insertAnimeToUser(self, anime):
        try:
            status = 0
            anime_title= anime.getTitle()
            connection= self.getConncetion()

            with connection.cursor() as cur:
                cur.execute('''
                                SELECT id FROM anime WHERE title = %s
                            ''', (anime_title,))
                
                a_record = cur.fetchone()
                a_id = a_record[0]

                cur.execute('''
                                INSERT INTO user_anime (user_id, anime_id) VALUES (%s, %s);

                            ''', (self.user.getID(), a_id))
                
                connection.commit()
        except errors.UniqueViolation:
            status = 1
        except Exception as e:

            raise("Error inserting the manga: ", e)
        finally:
            connection.close()
            if status != 1:
                self.user.addAnime(anime)
            return status
            