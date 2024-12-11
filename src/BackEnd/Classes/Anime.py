class Anime:
    def __init__(self, title, studio, genre, demographic):
        self.title = title
        self.studio = studio
        self.genre = genre
        self.demographic= demographic

    def setTitle(self, title):
        self.title= title

    def setStudio(self, studio):
        self.studio = studio
    
    def setGenere(self, genre):
        self.genre= genre

    def setDemographic(self, demographic):
        self.demographic= demographic

    def getTitle(self):
        return self.title

    def getStudio(self):
        return self.studio
    
    def getGenere(self):
        return self.genre

    def getDemographic(self):
        return self.demographic