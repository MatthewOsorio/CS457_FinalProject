from BackEnd.UserModel import UserModel
from BackEnd.MangaModel import MangaModel
from BackEnd.AnimeModel import AnimeModel
from openai import OpenAI

class Controller:
    def __init__(self):
        self.userModel = UserModel()
        self.mangaModel = MangaModel()
        self.animeModel = AnimeModel()
        self.gpt= OpenAI()

    def createUser(self, firstname, lastname, email, password):
        return self.userModel.insertUserInfo(firstname, lastname, email, password)

    def verifyCredentials(self, email, password):
        status = self.userModel.checkCredentials(email, password)
        
        if status:
            self.populateUserMangaList()
            self.populateUserAnimeList()
            return status
        else:
            return status
        
    def addMangaToUserFavorites(self, title):
        manga = self.mangaModel.retrieveManga(title)

        if manga == None:
            return False
        else:
            self.userModel.insertMangaToUser(manga)
            return True
        
    def populateUserMangaList(self):
        user_id = self.userModel.user.getID()
        mangas = self.mangaModel.getUserMangaList(user_id)
        self.userModel.user.setManga(mangas)

    def populateUserAnimeList(self):
        user_id = self.userModel.user.getID()
        animes = self.animeModel.getUserAnimeList(user_id)
        self.userModel.user.setAnime(animes)

    def addAnimeToUserFavorites(self, title):
        anime = self.animeModel.retrieveAnime(title)

        if anime == None:
            return False
        else:
            self.userModel.insertAnimeToUser(anime)
            return True

    def recommendManga(self):
        gpt_input = []

        for m in self.userModel.user.manga:
            temp = {}
            temp['title'] = m.getTitle()
            temp['author'] = m.getAuthor()
            temp['genre'] = m.getGenre()
            temp['demographic'] = m.getDemographic()

            gpt_input.append(temp)

        response= self.gpt.chat.completions.create(
            model= 'gpt-4',
            messages= [{'role': 'system', 'content': '''You are a manga expert and have read over thousands of manga. 
                                                        Your job is to recommend three manga based on the title, author, genre, and demographic of the manga being given to you.
                                                        Please make these recommendation in a friendly way but concise way and do not repeat manga being given to you.
                                                        Please make the output in this format:1. recommendation \n2. recommendation\n3. recommendation'''},
                        {'role': 'user', 'content': str(gpt_input)}]
        )
        
        return response.choices[0].message.content
    
    def recommendAnime(self):
        gpt_input = []

        for m in self.userModel.user.anime:
            temp = {}
            temp['title'] = m.getTitle()
            temp['studio'] = m.getStudio()
            temp['genre'] = m.getGenere()
            temp['demographic'] = m.getDemographic()

            gpt_input.append(temp)

        response= self.gpt.chat.completions.create(
            model= 'gpt-4',
            messages= [{'role': 'system', 'content': '''You are an anime expert and have watched over thousands of anime. 
                                                        Your job is to recommend three anime based on the title, author, genre, and demographic of the manga being given to you.
                                                        Please make these recommendation in a friendly way but concise way and do not repeat anime being given to you.
                                                        Please make the output in this format:1. recommendation \n 2. recommendation\n 3. recommendation'''},
                        {'role': 'user', 'content': str(gpt_input)}]
        )
        
        return response.choices[0].message.content