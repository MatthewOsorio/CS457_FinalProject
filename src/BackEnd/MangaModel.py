from psycopg import connect
from BackEnd.Classes.Manga import Manga

class MangaModel:
    def __init__(self):
        pass

    def getConncetion(self):
        try:
            conn= connect("dbname= OtakuAI user=postgres password= password host=localhost port=5432")
            return conn
        
        except Exception as e:
            raise("Error conneting to the database: ", e)
        
    def retrieveManga(self, title):
        formatted_title = '%' + title + '%'

        try:
            connection= self.getConncetion()
            with connection.cursor() as cur:
                cur.execute('''
                                SELECT title, demographic, genres, f_name, l_name FROM manga 
                                JOIN authors ON author_id = authors.id
                                WHERE title ILIKE %s''', (formatted_title,))
                
                record = cur.fetchone()

        except Exception as e:
            raise("Error retrieving manga: ", e)
        finally:
            connection.close()

            if record:
                m_title= record[0]
                demographic = record[1]
                genres = record[2]
                m_f_name = ''
                m_l_name = ''

                if record[3] == None:
                    m_f_name = ''
                else:
                    m_f_name = record[3]

                if record[4] == None:
                    m_l_name = ''
                else:
                    m_l_name = record[4]

                m_author = m_f_name +' '+ m_l_name

                manga = Manga(m_title, m_author, genres, demographic)
                return manga
            else:
                return None

    def getUserMangaList(self, user_id):
        try:
            manga_list= []
            connection = self.getConncetion()
            with connection.cursor() as cur:
                cur.execute('''
                                SELECT title, f_name, l_name, demographic, genres
                                FROM ( SELECT title, author_id as a_id, genres, demographic FROM user_manga
                                        JOIN manga ON manga.id = user_manga.manga_id 
                                        WHERE user_id = %s) 
                                JOIN authors ON authors.id = a_id ''',(user_id,) )
                
                records= cur.fetchall()

        except Exception as e:
            raise("Error retrieving manga list: ",e)
        
        finally:
            connection.close()


            if records:
                for i in records:
                    m_title = i[0]
                    m_demographic = i[3]
                    m_genre= i[4]
                    m_author = ''
                    m_f_name= ''
                    m_l_name=''

                    if i[1] == None:
                        m_f_name= ''
                    else:
                        m_f_name = i[1]

                    if i[2] == None:
                        m_l_name= ''
                    else:
                        m_l_name= i[2]          

                    m_author= m_f_name + ' '+ m_l_name      

                    new_manga= Manga(m_title, m_author, m_genre, m_demographic)
                    manga_list.append(new_manga)

            return manga_list
