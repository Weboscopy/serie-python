# Classes 

class User:

    def __init__(self, username, email):
        self.username = username 
        self.email = email 
        self.permissions = ["view"]
        self.status = "actif"

    def login(self):
        print(f"{self.username} est maintenant connecté")
        return self 

    def has_permission(self, permission):
        return permission in self.permissions

    def show(self):
        print(f"Nom d'utilisateur : {self.username}")
        print(f"Email : {self.email}")
        print(f"Permissions : {', '.join(self.permissions)}")
        return self 

    def logout(self):
        print(f"{self.username} est maintenant déconnecté")
        return self 

    def deactivate(self):
        self.status = "inactif"


user1 = User("tom", "tom@mail.com")
user2 = User("zoé", "zoé@mail.com")

user1.login()
user2.login()
print(user1.has_permission("view"))
print(user2.has_permission("view"))

# Héritage 

class AdminUser(User):

    def __init__(self, username, email):
        super().__init__(username, email)
        self.permissions = ["view", "edit", "delete", "add"]

    def add_permission(self, user, permission):
        if permission not in user.permissions:
            user.permissions.append(permission)
            print(f"Permission '{permission}' donnée à {user.username}")

    # redéfinition des méthodes
    def login(self):
        super().login()
        print("En tant qu'admin")
        return self


user3 = AdminUser("paul", "paul@mail.com")

user3.login()

user3.has_permission("edit")

user3.add_permission(user1, "delete")
print(user1.has_permission("delete"))

user3.login()

# Type intégré

message = "Hello World"
message = str("Hello World")

print(message.upper().replace("WORLD", "PYTHON"))

user4 = User("yanis", "yanis@mail.com")
user4.login().show().logout()

print(user4.email)
user4.email = "test@mail.com"
print(user4.email)

setattr(user4, "email", "alice@mail.com")
user4.show()
print(getattr(user4, "username"))

print(isinstance(user1, AdminUser))
print(isinstance(user1, User))

# Héritage multiples 
from datetime import datetime
class Logger:

    def __init__(self):
        self.log = []
        self.status = "INFO"

    def write_log(self, message):
        self.log.append(message)
        print(f"{datetime.now()} : {self.status} : {message}")

    def show(self):
        print(f"{';'.join(self.log[-3:])}")


class LoggableUser(Logger, User):
    def __init__(self, username, email):
        User.__init__(self, username, email)
        Logger.__init__(self)

    def deactivate_and_log(self):
        self.write_log(f"{self.username} n'est plus actif")
        self.deactivate()


user5 = LoggableUser("noa", "noa@mail.com")
user5.write_log("Tentative de connexion")
user5.write_log("Message 1")
user5.write_log("Message 2")
user5.write_log("Message 3")
user5.login()
user5.show()

print(user5.status)
user5.deactivate_and_log()
print(user5.status)

# Classes abstraites
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, email):
        self.username = username 
        self.email = email 
        self.permissions = []
        self.status = "actif"

    def login(self):
        print(f"{self.username} est maintenant connecté")
        return self 

    def has_permission(self, permission):
        return permission in self.permissions

    def show(self):
        print(f"Nom d'utilisateur : {self.username}")
        print(f"Email : {self.email}")
        print(f"Permissions : {', '.join(self.permissions)}")
        return self 

    def logout(self):
        print(f"{self.username} est maintenant déconnecté")
        return self 

    def deactivate(self):
        self.status = "inactif"

    @abstractmethod
    def access_dashboard(self):
        pass 

# user6 = User("leo", "leo@mail.com")

class AdminUser(User):

    def __init__(self, username, email):
        super().__init__(username, email)
        self.permissions = ["view", "edit", "delete", "add"]

    def add_permission(self, user, permission):
        if permission not in user.permissions:
            user.permissions.append(permission)
            print(f"Permission '{permission}' donnée à {user.username}")

    # redéfinition des méthodes
    def login(self):
        super().login()
        print("En tant qu'admin")
        return self

    def access_dashboard(self):
        print("Accès complet au tableau de bord")

user7 = AdminUser("lia", "lia@mail.com")

user7.access_dashboard()


class GuestUser(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.permissions = ["view"]

    def access_dashboard(self):
        print("Accès limité au tableau de bord")


# Polymorphisme 
import time
def show_dashboard(user : User):
    print("accès au tableau de bord")
    time.sleep(3)
    user.access_dashboard()

admin = AdminUser("admin1", "admin1@mail.com")
guest = GuestUser("guest1", "guest@mail.com")

show_dashboard(admin)
show_dashboard(guest)