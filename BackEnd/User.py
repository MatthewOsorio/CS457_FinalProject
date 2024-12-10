class User:
    def __init__(self, f_name, l_name):
        self.f_name =  f_name
        self.l_name = l_name
        self.manga = []
        self.anime = []

    def setFirstName(self, name):
        self.f_name = name

    def setLastName(self, name):
        self.l_name = name

    def getFirstName(self):
        return self.f_name
    
    def getLastName(self):
        return self.l_name
    
    def addManga(self, manga):
        self.manga.append(manga)

    def addAnime(self, anime):
        self.anime.append(anime)

    def getManga(self):
        return self.manga
    
    def getAnime(self):
        return self.anime