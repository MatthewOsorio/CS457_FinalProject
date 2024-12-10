from BackEnd.Controller import Controller

class View():
    def __init__(self):
        self.controller = Controller()
        self.manager()

    def manager(self):
        status= 0
        while status == 0:
            status =self.startMenu()

        if status == 1:
            self.displayFavMenu()
        elif status == 2:
            self.addMangaAnimeMenu()
            self.displayFavMenu()

    def startMenu(self):
        print("Welcome to OtakuAI!\n1. Login\n2. New user\n3. Exit")
        user_input = int(input("> "))
        status= 0

        if user_input == 1:
            successful_login = self.loginMenu()
            if successful_login:
                status= 1
            else:
                status= 0
        elif user_input == 2:
            user_creation_successful = self.createUserMenu()
            if user_creation_successful:
                status = 2
            else:
                status = 0 
        elif user_input == 3:
            status = 3
        else:
            print("Invalid input, please try again")
            status = 0

        return status
    
    def loginMenu(self):
        print("Please login")
        email = input("Email: ")
        password = input("Password: ")

        valid_credentials = self.controller.verifyCredentials(email, password)
        if valid_credentials == True:
            print("Login successful, welcome back\n")
            return True
        else:
            print("Email/Password is incorrect\n")
            return False

    def createUserMenu(self):
        print("Please enter your credential below")
        firstname = input("First Name: ")
        lastname = input("Last Name: ")
        email = input("Email: ")
        password = input("Password: ")

        valid_info = self.controller.createUser(firstname, lastname, email, password)

        if valid_info == 0:
            print(f"Your account has been created, welcome {firstname} to OkatuAI\n")
            return True
        else:
            print("Email is already in use")
            return False

    
    def addFavMangaMenu(self):
        finished= False
        print("Enter the title of the manga you would like to add below")

        while not finished:
            title = input("Title: ")
            manga_found= self.controller.addMangaToUserFavorites(title)

            if manga_found:
                print("Manga has been added!")
            else:
                print("Cannot add manga, please try again")

            print("1. Add more manga\n2. Finished")
            user_input = int(input("> "))

            match user_input:
                case 1:
                    continue
                case 2:
                    finished = True
                case _:
                    print("Not an option, returning to previous menu")
                    finished = True

    def addFavAnimeMenu(self):
        finished= False
        print("Enter the title of the anime you would like to add below")

        while not finished:
            title = input("Title: ")
            manga_found= self.controller.addAnimeToUserFavorites(title)

            if manga_found:
                print("Anime has been added!")
            else:
                print("Cannot add anime, please try again")

            print("1. Add more anime\n2. Finished")
            user_input = int(input("> "))

            match user_input:
                case 1:
                    continue
                case 2:
                    finished = True
                case _:
                    print("Not an option, returning to previous menu")
                    finished = True

    def addMangaAnimeMenu(self):
        finished= False
        while not finished:
            print("Would you like to add manga or anime to your list?\n1. Manga\n2. Anime\n3. Neither")
            user_input= int(input("> "))

            match user_input:
                case 1:
                    self.addFavMangaMenu()
                case 2:
                    self.addFavAnimeMenu()
                case 3:
                    print("Returning to your favorites")
                    finished = True
                case _:
                    print("Invalid input")
                    continue

    def displayFavMenu(self):
        finished = False

        while not finished:
            print(f"{self.controller.userModel.user.getFirstName()} Favorites:")

            print("Favorite Manga")
            print('----------------')
            for m in self.controller.userModel.user.getManga():
                print(f"Title: {m.getTitle()}, Author: {m.getAuthor()}, Demographic: {m.getDemographic()}")

            print("\nFavorite Anime")
            print('----------------')
            for a in self.controller.userModel.user.getAnime():
                print(f"Title: {a.getTitle()}, Studio: {a.getStudio()}, Demographic: {a.getDemographic()}")

            print("\n1. Add Manga, 2. Add Anime, 3. Recommend Manga, 4. Recommend Anime, 5. Logout")
            user_input= int(input('> '))

            match user_input:
                case 1:
                    self.addFavMangaMenu()
                case 2:
                    self.addFavAnimeMenu()
                case 3:
                    self.recommendMangaMenu()
                case 4:
                    self.recommendAnimeMenu()
                case 5:
                    print("Goodbye!")
                    return

    def recommendMangaMenu(self):
        recommendations= self.controller.recommendManga()
        print('\n', recommendations, '\n')

    def recommendAnimeMenu(self):
        recommendations= self.controller.recommendAnime()
        print('\n', recommendations, '\n')