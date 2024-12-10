from psycopg import connect
from Manga import Manga

class MangaModel:
    def __init__(self):
        self.manga= None

    def getConncetion(self):
        try:
            conn= connect("dbname= OtakuAI user=postgres password= osorio56 host=localhost port=5432")
            return conn
        
        except Exception as e:
            raise("Error conneting to the database: ", e)
        
    def findManga(self, title):
        try:
            connection= self.getConncetion()
            with connection.cursor() as cur:
                cur.execute(''' SELECT title, demographic, genres, f_name, l_name FROM manga 
                                JOIN authors ON author_id = authors.id
                                WHERE title LIKE '%Mob Psycho 100%''')