from time import sleep
import random
from Baralho import baralho_list


player_hand0 = []
dealer_hand = []

while len(player_hand0) != 2:
    card_player = baralho_list[random.randint(0, (len(baralho_list)))]
    player_hand0.append(card_player)
    baralho_list.remove(card_player)

while len(dealer_hand) != 2:
    card_player = baralho_list[random.randint(0, (len(baralho_list)))]
    dealer_hand.append(card_player)
    baralho_list.remove(card_player)


def dealer_buy():
    new_card_dealer = baralho_list[random.randint(0, len(baralho_list))]
    baralho_list.remove(new_card_dealer)
    dealer_hand.append(new_card_dealer)


def player_buy():
    new_card_player = baralho_list[random.randint(0, len(baralho_list))]
    baralho_list.remove(new_card_player)
    player_hand0.append(new_card_player)


def soma(p):
    s = 0
    if f_blackjack(p):
        s = 21
    else:
        for c in p:
            s += c['Valor']
    return s


def f_blackjack(x):
    if (x[0]['Valor'] == 10 and x[1]['Carta'] == 'A') or (x[0]['Carta'] == 'A' and x[1]['Valor'] == 10):
        blackjack = True
    else:
        blackjack = False
    return blackjack


soma(dealer_hand)
soma(player_hand0)


def repeat(x):
    x_count = 0
    while x_count != 3:
        print(x)
        x_count += 1
        sleep(0.25)
    sleep(1)


def winner_test(p, d):
    winner = ''
    if (p > d) and p <= 21:
        winner = p

    elif (p < d) and d <= 21:
        winner = d

    elif p > 21:
        winner = d

    elif d > 21:
        winner = p

    elif p == d:
        if f_blackjack(p):
            if f_blackjack(d):
                winner = 'empate'
            else:
                winner = p
        if f_blackjack(d):
            if f_blackjack(p):
                winner = 'empate'
            else:
                winner = d

    if winner == 'empate':
        print('EMPATE!')
        sleep(5)

    if winner == p:
        print(f'O Jogador venceu!')
        sleep(5)

    if winner == d:
        print('A Casa venceu!')
        sleep(5)


def test_21(x):
    if soma(x) > 21:
        return True
    else:
        return False

