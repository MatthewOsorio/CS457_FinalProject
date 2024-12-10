class Anime:
    def __init__(self):
        self.title = None
        self.first_studio = None
        self.second_studio = None
        self.genre = []
        self.demographic= None

    def setTitle(self, title):
        self.title= title

    def setFirstStudio(self, studio):
        self.first_studio = studio
    
    def setSecondStudio(self, studio):
        self.second_studio
    
    def setGenere(self, genre):
        self.genre= genre

    def setDemographic(self, demographic):
        self.demographic= demographic

    def getTitle(self):
        return self.title

    def getFirstStudio(self):
        return self.first_studio
    
    def getSecondStudio(self):
        return self.second_studio
    
    def getGenere(self):
        return self.genre

    def getDemographic(self):
        return self.demographic