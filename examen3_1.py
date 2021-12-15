def karta(nomer):
    a=nomer[-4:]
    b=len(nomer)-4
    print('*'*b+a)
nomer=input('Введите номер карты: ')
karta(nomer)