#2
class InvalidPasswordError(Exception):
    def __int__(self, password):
        self.password = password
def validate_password(password):
         if len(password) < 8:
             raise InvalidPasswordError(password)
         else:
             print('пароль задано')
try:
    password = input('введіть пароль')
    validate_password(password)
except InvalidPasswordError as e:
             print(f"пароль введено не коректно {e.password} "
                   f"мінімум 8 символів")
