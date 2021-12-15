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
class TomatoBush:
    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num - 1)]
    def grow_all(self):
        self.tomatoes = [Tomato(index +1) for index in range(0, num - 1)]
        return self.tomatoes
    def all_are_ripe(self):
        if 'цветок' in self.tomatoes or 'зеленый'  in self.tomatoes:
            return False
        else:
            return True
    def five_away_all(self):
        self.tomatoes=[]
        return self.tomatoes



tomat = Tomato(0)
tomat.ripe()
tomat.grow()
tomat.ripe()
tomat.grow()
tomat.ripe()