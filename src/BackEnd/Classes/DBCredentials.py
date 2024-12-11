class DBCredetials:
    def __init__(self):
        self.dbname = 'your_db_name'
        self.user = 'your_username'
        self.password = 'your_password'
        self.host= 'your_host'
        self.port = 'your_port'

    def getDBName(self):
        return self.dbname
    
    def getUser(self):
        return self.user
    
    def getPassword(self):
        return self.password
    
    def getHost(self):
        return self.host
    
    def getPort(self):
        return self.port