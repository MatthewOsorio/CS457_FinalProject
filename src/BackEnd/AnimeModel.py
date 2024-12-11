from psycopg import connect
from BackEnd.Classes.Anime import Anime
from BackEnd.Classes.DBCredentials import DBCredetials

class AnimeModel:
    def __init__(self):
        self.db_connection = DBCredetials()

    def getConncetion(self):
        try:
            conn= connect(f"dbname= {self.db_connection.getDBName()} user={self.db_connection.getUser()} password= {self.db_connection.getPassword()} host= {self.db_connection.getHost()} port= {self.db_connection.getPort()}")
            return conn
        
        except Exception as e:
            raise("Error conneting to the database: ", e)
        
    def retrieveAnime(self, title):
        formatted_title = '%' + title + '%'

        try:
            connection= self.getConncetion()
            with connection.cursor() as cur:
                cur.execute('''
                                SELECT title, name, demographic, genres FROM anime
                                JOIN studios ON anime.studio_id = studios.id
                                WHERE title ILIKE %s
                                ORDER BY LENGTH(title)''', (formatted_title, ))
                
                record = cur.fetchone()

        except Exception as e:
            raise("Error retrieving manga: ", e)
        finally:
            connection.close()

            if record:
                a_title= record[0]
                studio = ''
                genres = record[3]
                demographic = record[2]

                if record[1] == None:
                    studio = ''
                else:
                    studio = record[1]

                anime = Anime(a_title, studio, genres, demographic)
                return anime
            else:
                return None

    def getUserAnimeList(self, user_id):
        try:
            anime_list= []
            connection = self.getConncetion()
            with connection.cursor() as cur:
                cur.execute('''
                                SELECT title, name, demographic, genres
                                FROM ( SELECT title, studio_id as s_id, genres, demographic FROM user_anime
                                        JOIN anime ON anime.id = user_anime.anime_id 
                                        WHERE user_id = %s) 
                                JOIN studios ON studios.id = s_id ''',(user_id,))

                
                records= cur.fetchall()

        except Exception as e:
            raise("Error retrieving manga list: ",e)
        
        finally:
            connection.close()

            if records:
                for i in records:
                    a_title= i[0]
                    a_studio= ''
                    a_genre = i[3]
                    a_demo= i[2]

                    if a_studio != None:
                        a_studio = i[1]

                    new_anime= Anime(a_title, a_studio, a_genre, a_demo)
                    anime_list.append(new_anime)

            return anime_list
