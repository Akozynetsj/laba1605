#3
class InvalidFileFormatError(Exception):
    def __int__(self, f):
        self.f = f
#FileNotError
    def read_file(f):
        try:
            with open(f, 'r') as file:
                content = file.read()
                print('Вміст файлу :', content)
        except IOError:
            raise InvalidFileFormatError(f)

try:
    read_file(input('введіть назіу файлу:'))
except InvalidFileFormatError as e:
    print(f"невірний формат файлу {e.f}"
          f"підтримують онлі текстові файли")