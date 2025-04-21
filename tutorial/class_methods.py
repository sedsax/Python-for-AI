class User:
    users = []
    next_id = 1

    def __init__(self, name):
        self.name = name
        self.id = User.next_id
        User.next_id += 1
        User.users.append(self)

    @classmethod
    def user_count(cls):
        return len(cls.users)

    @classmethod
    def list_user_names(cls):
        return [user.name for user in cls.users]

    @classmethod
    def remove_user_by_name(cls, name):
        for user in cls.users:
            if user.name == name:
                cls.users.remove(user)
                return True
        return False

    @staticmethod
    def greet():
        print("Merhaba, kullanıcılar!")

    def __str__(self):
        return f"User(id={self.id}, name={self.name})"

u1 = User("Ali")
u2 = User("Nino")
print(User.user_count())           
print(User.list_user_names())      
User.greet()                     
print(u1)                         
User.remove_user_by_name("Ali")
print(User.list_user_names())  