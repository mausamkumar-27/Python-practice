class UserAccount:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    @staticmethod
    def is_strong_password(pwd):
        if len(pwd) >=8:
            return True
        else:
            return False
    def check_security(self):
        if UserAccount.is_strong_password(self.__password):
            print(f"User:{self.username} | Strong Password")
        else:
            print(f"User:{self.username} | Weak Password")
a=UserAccount.is_strong_password("abc23")
print(a)
b=UserAccount("Mausam Kumar","Python2026")
b.check_security()