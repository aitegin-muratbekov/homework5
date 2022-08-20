import os
from envparse import env
from random import choice
env.read_envfile('settings.env')


class Casino:
    counter = 0

    def __init__(self):
        self.__my_money = int(os.getenv('MY_MONEY'))
        self.__game_finished = False
        self.__list_of_numbers = range(1, 30)

    @property
    def my_money(self):
        return self.__my_money

    @my_money.setter
    def my_money(self, value):
        self.__my_money = value

    @property
    def game_finished(self):
        return self.__my_money

    @game_finished.setter
    def game_finished(self, value):
        self.__game_finished = value

    @property
    def list_of_numbers(self):
        return self.__list_of_numbers

    def play(self):

        while True:
            if self.__game_finished == False:
                money = int(input(f'Выбери сумму которую будешь ставить(число)    '))
                self.__my_money -= money
                your_number = int(input('Выбери число на которое будешь ставить(1, 30)  '))
                won_number = choice(self.__list_of_numbers)
                if your_number == won_number:
                    print(f'You won 2x from {money}!!!')
                    self.__my_money += 2*money
                else:
                    print(f'You lose ')
                if self.__my_money <= 0:
                    self.__game_finished = True
                else:
                    exit = input('Xотите продолжить? Y/N')
                    if exit.title() == 'N':
                        self.__game_finished = True
                    else:
                        pass
            elif self.__game_finished == True:
                print('Игра закончена ! До следующей игры!')
                print(f'Баланс: {self.__my_money}')
                if self.__my_money > 1500:
                    print(f'выиграно {self.__my_money - 1500}')
                else:
                    print(f'проиграно {1500 - self.__my_money}')
                break