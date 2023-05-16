#1
class  InvalidUsernameError(Exception):
    def __init__(self, username):
        self.username = username
#InvalidLengtheError
#InvalidCharacterError
#DublicateUsernameError
def register_user(username):
    if len(username) < 5 :
        raise InvalidUsernameError(username)
    else:
        print('вас зареєстровано')
#прикла використання
try :
    username = input('введіть ім я користувача')
    register_user(username)
except InvalidUsernameError as e:
    print(f"неправильне ім'я користувача {e.username} "
          f"мінімум 5 символів")
