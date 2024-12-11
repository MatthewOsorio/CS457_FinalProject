class Manga:
    def __init__(self, title, author, genre, demographic):
        self.tite= title
        self.author= author
        self.genre= genre
        self.demographic= demographic

    def setTitle(self, title):
        self.tite= title

    def setAuthor(self, author):
        self.first_author= author

    def setGenre(self, genre):
        self.genre= genre

    def setDemogrpahic(self, demographic):
        self.demographic= demographic

    def getTitle(self):
        return self.tite
    
    def getAuthor(self):
        return self.author
    
    def getGenre(self):
        return self.genre
    
    def getDemographic(self):
        return self.demographic