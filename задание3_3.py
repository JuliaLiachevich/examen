class Tomato:
    states = {0: 'цветок', 1: 'зеленый', 2: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._state += 1
        return self._state

    def ripe(self):
        if self._state == 2:
            print('Томат созрел')
        else:
            print('Томат еще не созрел')


tomat = Tomato(0)
tomat.ripe()
tomat.grow()
tomat.ripe()
tomat.grow()
tomat.ripe()