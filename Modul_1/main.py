number = 10 # int незмінюванний тип даних
number_2 = 10.5123 # float незмінюванний тип даних
name = 'Bob' # str незмінюванний тип даних
is_activ = True # bool незмінюванний тип даних
vare = None # NoneType незмінюванний тип даних
cars = [1, 2, 3, 4, 'bmw', True, False, None] # list змінюванний тип данних
books = {1:'math', 2:'history', 'bmw':5, 'active':True, 3:cars} # dict змінюванний тип данних; ключ це завжди незмінюванний тип данних (int, float, str, tuple)
points = (5, 9) #tuple незмінюванний тип даних
colurs = {'black', 'white', 'ellouw', 'black'} # set змінюванний тип данних. Це список, але збергає лише унікальні елементи
print(colurs)
colurs.add('green')
print(colurs)