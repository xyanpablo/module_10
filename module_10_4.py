import threading
from queue import Queue
from random import randint
from time import sleep


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for g in guests:
            menu = False
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    print(f'{g.name} сел(-а) за стол номер {t.number}')
                    t.guest.start()
                    menu = True
                    break
            if not menu:
                self.queue.put(g)
                print(f'{g.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(t.guest is not None for t in self.tables):
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f'{t.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {t.number} свободен')
                    t.guest = None
                    if not self.queue.empty():
                        t.guest = self.queue.get()
                        print(f"{t.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {t.number}")
                        t.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
