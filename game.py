# Imports
import random
from Baralho import baralho_list
from time import sleep
from functions import soma, repeat, winner_test, player_hand0, dealer_hand, dealer_buy, player_buy, test_21

# Entrada do nome do player
name = input('Seja bem-vindo jogador!\n'
             'Para uma melhor experiência, nos informe seu nome: ')
sleep(0.5)
print(f'\nCerto, {name}.\nA casa te deseja um ótimo jogo!\n')


sleep(2)

# Print das maos do player e do dealer
print('---' * 15, f'\nMão do Dealer:\n')
print(f'{dealer_hand[0]}\n'
      '{CARTA OCULTA}')
print('---' * 15, f'\n\nMão do Jogador:\n')
for carta in player_hand0:
    print(carta)


repeat('.')

while True:
# Entrada da acao do player
    print(f'{name}, o que deseja fazer?')
    jogada = int(input('[1] -> Stand\n'
                       '[2] -> Hit\n'
                       '[3] -> Double\n'
                       '[4] -> Split\n'
                       '[5] -> Seguro\n'
                       '[6] -> Surrender\n'
                        'Digite o número correspondente a sua ação: '))

    repeat('.')

# Caso o player escolha [1]
    if jogada == 1:
        sleep(1)
        print(' '*5,f'{name} pulou a vez.')

        # DEALER TURN
        repeat('.')
        print(' '*10, '<- TURNO DO DEALER ->')
        print('---' * 15, f'\nMão do Dealer:\n')
        for carta in dealer_hand:
            print(carta)
        print('---' * 15, f'\n\nMão do Jogador:\n')
        for carta in player_hand0:
            print(carta)
        print('---' * 15)
        sleep(2.5)

        if soma(dealer_hand) > soma(player_hand0):
            if soma(dealer_hand) < 17:
                while soma(dealer_hand) < 17:
                    dealer_buy()
                    print(' ' * 5, '<- O Dealer comprou uma carta ->')
                    repeat('.')
                    sleep(1)
                print('---' * 15, f'\nMão do Dealer:\n')
                for carta in dealer_hand:
                    print(carta)
                print('---' * 15, f'\n\nMão do Jogador:\n')
                for carta in player_hand0:
                    print(carta)
                if test_21(dealer_hand):
                    repeat('.')
                    print('A mão do Dealer estourou.')
                    test = winner_test(soma(player_hand0), soma(dealer_hand))
                    break
            else:
                repeat('.')
                print('O Dealer pulou a vez.')
        else:
            while (soma(dealer_hand) < 17) or (soma(dealer_hand) < soma(player_hand0)):
                dealer_buy()
                print(' ' * 5, '<- O Dealer comprou uma carta ->')
                repeat('.')
                sleep(1)
            print('---' * 15, f'\nMão do Dealer:\n')
            for carta in dealer_hand:
                print(carta)
            print('---' * 15, f'\n\nMão do Jogador:\n')
            for carta in player_hand0:
                print(carta)
            if test_21(dealer_hand):
                repeat('.')
                print('A mão do Dealer estourou.')
                test = winner_test(soma(player_hand0), soma(dealer_hand))
                break

        repeat('.')
        continuar = input(f'\nDeseja fazer outra jogada, {name}? [Y/N]').upper()
        if continuar != 'Y':
            test = winner_test(soma(player_hand0), soma(dealer_hand))
            if test != '':
                break
        else:
            continue

# Caso o player escolha [2]
    elif jogada == 2:
        estourou = False
        hit_again = 'Y'
        while hit_again == 'Y':
            sleep(1)
            print(' '* 5, f'<- {name} comprou uma carta ->')
            player_buy()
            repeat('.')
            print('---' * 15, f'\nMão do Dealer:\n')
            for carta in dealer_hand:
                print(carta)
            print('---' * 15, f'\n\nMão do Jogador:\n')
            for carta in player_hand0:
                print(carta)
            if test_21(player_hand0):
                estourou = True
                break
            else:
                hit_again = input('Deseja comprar outra carta? [Y/N]\n').upper()
                if hit_again != 'Y':
                    break
        if estourou:
            print(f'{name}, sua mão estourou.')
            test = winner_test(soma(player_hand0), soma(dealer_hand))
            break

        # DEALER TURN
        repeat('.')
        print(' ' * 10, '<- TURNO DO DEALER ->')
        print('---' * 15, f'\nMão do Dealer:\n')
        for carta in dealer_hand:
            print(carta)
        print('---' * 15, f'\n\nMão do Jogador:\n')
        for carta in player_hand0:
            print(carta)
        print('---' * 15)
        sleep(2.5)

        if soma(dealer_hand) > soma(player_hand0):
            if soma(dealer_hand) < 17:
                while soma(dealer_hand) < 17:
                    dealer_buy()
                    print(' ' * 5, '<- O Dealer comprou uma carta ->')
                    repeat('.')
                    sleep(1)
                print('---' * 15, f'\nMão do Dealer:\n')
                for carta in dealer_hand:
                    print(carta)
                print('---' * 15, f'\n\nMão do Jogador:\n')
                for carta in player_hand0:
                    print(carta)
                if test_21(dealer_hand):
                    repeat('.')
                    print('A mão do Dealer estourou.')
                    test = winner_test(soma(player_hand0), soma(dealer_hand))
                    break
            else:
                repeat('.')
                print('O Dealer pulou a vez.')
        else:
            while (soma(dealer_hand) < 17) or (soma(dealer_hand) < soma(player_hand0)):
                dealer_buy()
                print(' ' * 5, '<- O Dealer comprou uma carta ->')
                repeat('.')
                sleep(1)
            print('---' * 15, f'\nMão do Dealer:\n')
            for carta in dealer_hand:
                print(carta)
            print('---' * 15, f'\n\nMão do Jogador:\n')
            for carta in player_hand0:
                print(carta)
            if test_21(dealer_hand):
                repeat('.')
                print('A mão do Dealer estourou.')
                test = winner_test(soma(player_hand0), soma(dealer_hand))
                break

        repeat('.')
        continuar = input(f'\nDeseja fazer outra jogada, {name}? [Y/N]').upper()
        if continuar != 'Y':
            test = winner_test(soma(player_hand0), soma(dealer_hand))
            if test != '':
                break
        else:
            continue

# Caso o jogador escolhe [3]
    elif jogada == 3:
        if dealer_hand[0]['Carta'] != 'A':
            sleep(1)
            print('<- Essa jogada só é permitada quando a carta ascendente do Dealer é um Ás ->')

        # DEALER TURN
            repeat('.')
            print(' ' * 10, '<- TURNO DO DEALER ->')
            print('---' * 15, f'\nMão do Dealer:\n')
            for carta in dealer_hand:
                print(carta)
            print('---' * 15, f'\n\nMão do Jogador:\n')
            for carta in player_hand0:
                print(carta)
            print('---' * 15)
            sleep(2.5)

            if soma(dealer_hand) > soma(player_hand0):
                if soma(dealer_hand) < 17:
                    while soma(dealer_hand) < 17:
                        dealer_buy()
                        print(' ' * 5, '<- O Dealer comprou uma carta ->')
                        repeat('.')
                        sleep(1)
                    print('---' * 15, f'\nMão do Dealer:\n')
                    for carta in dealer_hand:
                        print(carta)
                    print('---' * 15, f'\n\nMão do Jogador:\n')
                    for carta in player_hand0:
                        print(carta)
                    if test_21(dealer_hand):
                        repeat('.')
                        print('A mão do Dealer estourou.')
                        test = winner_test(soma(player_hand0), soma(dealer_hand))
                        break
                else:
                    repeat('.')
                    print('O Dealer pulou a vez.')
            else:
                while (soma(dealer_hand) < 17) or (soma(dealer_hand) < soma(player_hand0)):
                    dealer_buy()
                    print(' ' * 5, '<- O Dealer comprou uma carta ->')
                    repeat('.')
                    sleep(1)
                print('---' * 15, f'\nMão do Dealer:\n')
                for carta in dealer_hand:
                    print(carta)
                print('---' * 15, f'\n\nMão do Jogador:\n')
                for carta in player_hand0:
                    print(carta)
                if test_21(dealer_hand):
                    repeat('.')
                    print('A mão do Dealer estourou.')
                    test = winner_test(soma(player_hand0), soma(dealer_hand))
                    break

        else:
            sleep(1)
            print(f'<- {name} DOBROU a aposta e comprou uma ÚNICA carta ->')
            player_buy()
            repeat('.')
            sleep(1)
            print('---' * 15, f'\nMão do Dealer:\n')
            for carta in dealer_hand:
                print(carta)
            print('---' * 15, f'\n\nMão do Jogador:\n')
            for carta in player_hand0:
                print(carta)

                # DEALER TURN
                repeat('.')
                print(' ' * 10, '<- TURNO DO DEALER ->')
                print('---' * 15, f'\nMão do Dealer:\n')
                for carta in dealer_hand:
                    print(carta)
                print('---' * 15, f'\n\nMão do Jogador:\n')
                for carta in player_hand0:
                    print(carta)
                print('---' * 15)
                sleep(2.5)

                if soma(dealer_hand) > soma(player_hand0):
                    if soma(dealer_hand) < 17:
                        while soma(dealer_hand) < 17:
                            dealer_buy()
                            print(' ' * 5, '<- O Dealer comprou uma carta ->')
                            repeat('.')
                            sleep(1)
                        print('---' * 15, f'\nMão do Dealer:\n')
                        for carta in dealer_hand:
                            print(carta)
                        print('---' * 15, f'\n\nMão do Jogador:\n')
                        for carta in player_hand0:
                            print(carta)
                        if test_21(dealer_hand):
                            repeat('.')
                            print('A mão do Dealer estourou.')
                            test = winner_test(soma(player_hand0), soma(dealer_hand))
                            break
                    else:
                        repeat('.')
                        print('O Dealer pulou a vez.')
                else:
                    while (soma(dealer_hand) < 17) or (soma(dealer_hand) < soma(player_hand0)):
                        dealer_buy()
                        print(' ' * 5, '<- O Dealer comprou uma carta ->')
                        repeat('.')
                        sleep(1)
                    print('---' * 15, f'\nMão do Dealer:\n')
                    for carta in dealer_hand:
                        print(carta)
                    print('---' * 15, f'\n\nMão do Jogador:\n')
                    for carta in player_hand0:
                        print(carta)
                    if test_21(dealer_hand):
                        repeat('.')
                        print('A mão do Dealer estourou.')
                        test = winner_test(soma(player_hand0), soma(dealer_hand))
                        break

        repeat('.')
        continuar = input(f'\nDeseja fazer outra jogada, {name}? [Y/N]').upper()
        if continuar != 'Y':
            test = winner_test(soma(player_hand0), soma(dealer_hand))
            if test != '':
                break
        else:
            continue

# Caso o player escolha [4]
    if jogada == 4:
        if player_hand0[0]['Valor'] != player_hand0[1]['Valor']:
            sleep(1)
            print('<- Essa jogada só é permitada quando as suas duas cartas têm o mesmo valor ->')

            # DEALER TURN
            repeat('.')
            print(' ' * 10, '<- TURNO DO DEALER ->')
            print('---' * 15, f'\nMão do Dealer:\n')
            for carta in dealer_hand:
                print(carta)
            print('---' * 15, f'\n\nMão do Jogador:\n')
            for carta in player_hand0:
                print(carta)
            print('---' * 15)
            sleep(2.5)

            if soma(dealer_hand) > soma(player_hand0):
                if soma(dealer_hand) < 17:
                    while soma(dealer_hand) < 17:
                        dealer_buy()
                        print(' ' * 5, '<- O Dealer comprou uma carta ->')
                        repeat('.')
                        sleep(1)
                    print('---' * 15, f'\nMão do Dealer:\n')
                    for carta in dealer_hand:
                        print(carta)
                    print('---' * 15, f'\n\nMão do Jogador:\n')
                    for carta in player_hand0:
                        print(carta)
                    if test_21(dealer_hand):
                        repeat('.')
                        print('A mão do Dealer estourou.')
                        test = winner_test(soma(player_hand0), soma(dealer_hand))
                        break
                else:
                    repeat('.')
                    print('O Dealer pulou a vez.')
            else:
                while (soma(dealer_hand) < 17) or (soma(dealer_hand) < soma(player_hand0)):
                    dealer_buy()
                    print(' ' * 5, '<- O Dealer comprou uma carta ->')
                    repeat('.')
                    sleep(1)
                print('---' * 15, f'\nMão do Dealer:\n')
                for carta in dealer_hand:
                    print(carta)
                print('---' * 15, f'\n\nMão do Jogador:\n')
                for carta in player_hand0:
                    print(carta)
                if test_21(dealer_hand):
                    repeat('.')
                    print('A mão do Dealer estourou.')
                    test = winner_test(soma(player_hand0), soma(dealer_hand))
                    break

        else:
            sleep(1)
            print('<- Seu jogo foi dividido em duas mãos ->')
            repeat('.')
            player_hand1 = [player_hand0[1]]
            player_hand0.remove(player_hand0[1])
            jogada_4_0 = 'Y'
            jogada_4_1 = 'Y'
            while jogada_4_0 == 'Y':
                jogada_4_0 = input(f'{name}, deseja comprar uma carta para a primeira mão? [Y/N]\n').upper()
                if jogada_4_0 != 'Y':
                    break
                else:
                    new_card_hand0 = baralho_list[(random.randint(0, len(baralho_list)))]
                    baralho_list.remove(new_card_hand0)
                    player_hand0.append(new_card_hand0)
                    print('Essa é a sua Mão 1:\n')
                    for c in player_hand0:
                        print(c)
                    j401 = input(f'{name}, deseja comprar outra carta para a segunda mão? [Y/N]\n')
                    if j401 == 'Y':
                        continue
                    else:
                        jogada_4_0 = 'N'
            if test_21(player_hand0):
                print(f'{name}, sua Mão 1 ESTOUROU!')

            while jogada_4_1 == 'Y':
                jogada_4_1 = input(f'{name}, deseja comprar uma carta para a segunda mão? [Y/N]\n').upper()
                if jogada_4_1 != 'Y':
                    break
                else:
                    new_card_hand1 = baralho_list[(random.randint(0, len(baralho_list)))]
                    baralho_list.remove(new_card_hand1)
                    player_hand1.append(new_card_hand1)
                    print('Essa é a sua Mão 2:\n')
                    for c in player_hand0:
                        print(c)
                    j411 = input(f'{name}, deseja comprar outra carta para a segunda mão? [Y/N]\n')
                    if j411 == 'Y':
                        continue
                    else:
                        jogada_4_1 = 'N'
            if test_21(player_hand1):
                print(f'{name}, sua Mão 2 ESTOUROU!')

            if test_21(player_hand0) and test_21(player_hand1):
                print(f'{name}, ambas suas mãos estouraram.\nVocê PERDEU!')
                break

            # DEALER TURN
            repeat('.')
            print(' ' * 10, '<- TURNO DO DEALER ->')
            print('---' * 15, f'\nMão do Dealer:\n')
            for carta in dealer_hand:
                print(carta)
            print('---' * 15, f'\n\nMão do Jogador:\n')
            for carta in player_hand0:
                print(carta)
            print('---' * 15)
            sleep(2.5)

            if soma(dealer_hand) > soma(player_hand0):
                if soma(dealer_hand) < 17:
                    while soma(dealer_hand) < 17:
                        dealer_buy()
                        print(' ' * 5, '<- O Dealer comprou uma carta ->')
                        repeat('.')
                        sleep(1)
                    print('---' * 15, f'\nMão do Dealer:\n')
                    for carta in dealer_hand:
                        print(carta)
                    print('---' * 15, f'\n\nMão do Jogador:\n')
                    for carta in player_hand0:
                        print(carta)
                    if test_21(dealer_hand):
                        repeat('.')
                        print('A mão do Dealer estourou.')
                        test = winner_test(soma(player_hand0), soma(dealer_hand))
                        break
                else:
                    repeat('.')
                    print('O Dealer pulou a vez.')
            else:
                while (soma(dealer_hand) < 17) or (soma(dealer_hand) < soma(player_hand0)):
                    dealer_buy()
                    print(' ' * 5, '<- O Dealer comprou uma carta ->')
                    repeat('.')
                    sleep(1)
                print('---' * 15, f'\nMão do Dealer:\n')
                for carta in dealer_hand:
                    print(carta)
                print('---' * 15, f'\n\nMão do Jogador:\n')
                for carta in player_hand0:
                    print(carta)
                if test_21(dealer_hand):
                    repeat('.')
                    print('A mão do Dealer estourou.')
                    test = winner_test(soma(player_hand0), soma(dealer_hand))
                    break

        repeat('.')
        continuar = input(f'\nDeseja fazer outra jogada, {name}? [Y/N]').upper()
        if continuar != 'Y':
            test = winner_test(soma(player_hand0), soma(dealer_hand))
            if test != '':
                break
        else:
            continue


# Caso o player escolha [5]
    if jogada == 5:
        print('Esse método ainda não está disponível.')

        repeat('.')
        continuar = input(f'\nDeseja fazer outra jogada, {name}? [Y/N]').upper()
        if continuar != 'Y':
            test = winner_test(soma(player_hand0), soma(dealer_hand))
            if test != '':
                break
        else:
            continue


# Caso o player escolha [6]
    elif jogada == 6:
        print(f'{name} desistiu!\nA partida foi encerrada e a casa venceu!')
        sleep(3)
        break

