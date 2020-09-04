data = [
    {
        "id": 1,
        "username": "admin",
        "pass": "root",    
        }
]

class User:
    def __init__(self, data):
        self.data = data
        self.currentLogin = False
        self.lastLogin = False
    def login(self,username,password):
        for i, val in enumerate(self.data):
            if val["username"] == username and val["pass"] == password:
                self.lastLogin = val
                self.currentLogin = val
                print("done",self.currentLogin)
                return
        print("rejected")

user = User(data)
user.login("admin","root")
