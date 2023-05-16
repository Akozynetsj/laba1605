try:
    print('start code')
    print(error)
    print('end')
except:
    print('no problems')
print('any code////')

def checker(var):
   if type(var)!= str:
       raise TypeError(f'Ssoorryyy,we cant work with{type(var)}, nam treba str')
   else:
    return var
a = 1234
checker(a)

class BuldingError(Exception):
    def __str__(self):
        return 'щось не те дуже багато'

def chek_material_build(amount, limit):
    if amount > limit:
        return 'достатньо матеріалів'
    else:
       raise  BuldingError()
chek_material_build(10, 300)

