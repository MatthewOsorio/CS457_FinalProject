class User:
    def __init__(self, f_name, l_name, email, id):
        self.f_name =  f_name
        self.l_name = l_name
        self.email = email
        self.id = id
        self.manga = []
        self.anime = []

    def setFirstName(self, name):
        self.f_name = name

    def setLastName(self, name):
        self.l_name = name

    def setEmail(self, email):
        self.email =  email
    
    def setID(self, id):
        self.id = id

    def setManga(self, manga):
        self.manga= manga

    def setAnime(self, anime):
        self.anime = anime
    
    def getFirstName(self):
        return self.f_name
    
    def getLastName(self):
        return self.l_name
    
    def getEmail(self):
        return self.email
    
    def getID(self):
        return self.id
    
    def addManga(self, manga):
        self.manga.append(manga)

    def addAnime(self, anime):
        self.anime.append(anime)

    def getManga(self):
        return self.manga
    
    def getAnime(self):
        return self.anime