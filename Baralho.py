# Criacao da classe Baralho
import random

baralho_list = []

class Baralho:
    def __init__(self, card, naipe, value):
        self.card = card
        self.naipe = naipe
        self.value = value
        self.dic = {'Naipe': self.naipe, 'Carta': self.card, 'Valor': self.value}
        baralho_list.append(self.dic)


cards_list = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
naipes = ['Paus', 'Copas', 'Espadas', 'Ouro']


for c in cards_list:
    for n in naipes:
        if type(c) == int:
            Baralho(c, n, c)
        else:
            if c == 'A':
                Baralho(c, n, 1)

            else:
                Baralho(c, n, 10)

random.shuffle(baralho_list)
