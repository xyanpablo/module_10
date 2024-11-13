import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self, balance=100):
        self.balance = int(balance)
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 101):
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            rnd = randint(50, 500)
            self.balance += rnd
            print(f'Пополнение: {rnd}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(1, 101):
            rnd = randint(50, 500)
            print(f'Запрос на {rnd}')
            if self.balance >= rnd:
                self.balance -= rnd
                print(f'Снятие: {rnd}. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                print(f'Запрос отклонён, недостаточно средств')
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
