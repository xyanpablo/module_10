import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run(self, enemies=100, counter=0):
        print(f'{self.name}, на нас напали!')
        while enemies:
            counter += 1
            print(f'{self.name} сражается {counter} дней, осталось {enemies - self.power} воинов.')
            enemies -= self.power
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {counter} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
