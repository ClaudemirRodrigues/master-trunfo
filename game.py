from random import shuffle
from time import sleep
from random import randint

card_001 = ('Bofors Modelo 29', 75, 4000, 90, 6.3, 840, 8565, 1)
card_002 = ('Anticarro M3 37mm', 37, 413.7, 25, .870, 884, 457, 2)
card_003 = ('Ballonkanone 1914 77mm', 77, 2500, 75, 7.85, 485, 3050, 3)
card_004 = ('BL Mk2 5,5pol', 140, 6190, 50, 45.36, 510, 14813, 4)
card_005 = ('Canhão de Montanha 2,75pol', 70, 586, 37, 5.67, 393, 5400, 5)
card_006 = ('BL Mark7 8pol', 203, 8890, 45, 90.72, 457, 11250, 6)
card_007 = ('BLC de 15lb', 76, 1158, 30, 6.35, 484, 5260, 7)
card_008 = ('Anticarro Modelo 01 47mm', 47, 753, 30, 1.4, 823, 1000, 8)
card_009 = ('BL Mk1 60lb', 127, 4470, 27, 27.22, 634, 11245, 9)
card_010 = ('Canhão 75/27', 75, 1067, 80, 6.5, 510, 7600, 10)
card_011 = ('BL Mk1 26cwt 6pol', 152, 3693, 45, 39, 427, 10425, 11)
card_012 = ('Big Bertha', 420, 43285, 35, 820, 425, 9375, 12)
card_013 = ('Bofors L/60', 40, 1981, 95, .907, 823, 1525, 13)
card_014 = ('Anticarro 1918 37mm', 37, 175, 15, .460, 435, 300, 14)
card_015 = ('Brixia Modelo 35', 45, 15.5, 80, .465, 83, 530, 15)
card_016 = ('BL 6pol 30cwt', 152, 3507, 45, 53.75, 237, 4755, 16)
card_017 = ('BL Mk1 5pol', 127, 1212, 50, 22.68, 240, 4390, 17)
card_018 = ('Bofors Modelo 34', 75, 928, 60, 6.58, 455, 9300, 18)
card_019 = ('Breda Modelo 35', 20, 307, 90, .135, 840, 2500, 19)
card_020 = ('Canhão Antiaéreo 13lb 9cwt', 76, 7620, 80, 5.89, 655, 5790, 20)
cards = list()
cards_pc = list()
cards_player = list()
buffer = list()
buffer_pc = list()

choice_player = 0
choice_pc = 0


def new_game():
    global flag
    flag = 99

    cards = []
    cards = [card_001, card_002, card_003, card_004, card_005, card_006, card_007, card_008, card_009, card_010,
             card_011, card_012, card_013, card_014, card_015, card_016, card_017, card_018, card_019, card_020]
    # embaralhar e distribuir as cartas
    shuffle(cards)
    cards_player[:] = cards[:10]
    cards_pc[:] = cards[10:]

    print(f'\033[33m-*' * 20)
    print('-*' * 3, '\033[m\033[32mJOGO DE CARTAS MEGA TRUNFO\033[33m', '-*' * 3)
    print('-*' * 5, '\033[m\033[32mARTILHARIA ANTIGA\033[33m', '*-' * 5 + '*')
    print(f'-*' * 20, '\033[m')
    print(f'\033[7;32;49m[1] Novo Jogo\033[m')
    print(f'\033[7;33;49m[2]   Sair   \033[m')
    choice = int(input(''))
    if choice != 1 and choice != 2:
        while choice != 1 and choice != 2:
            choice = int(input('\033[31mOpção inválida\033[m'))
    if choice == 2:
        game_over()
    elif choice == 1:
        sleep(.5)
        print('\033[32mEmbaralhando\033[m', end='')
        w = randint(2, 9)
        while w > 0:
            wait()
            w -= 1
        sleep(.7)
        print('\033[33m\nDistribuindo\033[m', end='')
        w = randint(2, 9)
        while w > 0:
            wait_2()
            w -= 1
        sleep(.7)

        print('\nEscolha:')
        print('\033[35m[P] Par ou')
        print('[I] Ímpar\033[m')
        choice_2 = input('Para decidir quem começa: ').upper()

        if choice_2 != 'P' and choice_2 != 'I':
            while choice_2 != 'P' and choice_2 != 'I':
                choice_2 = input('\033[31mTente novamente: \033[m').upper()

        play_number = randint(1, 10)
        print('\033[33mVALOR SORTEADO: ')
        sleep(.7)
        print(f'{play_number}\033[m')
        sleep(.6)
        if choice_2 == 'P':
            if (play_number % 2) == 0:
                flag = 1
                game()
            else:
                flag = 0
                game()

        elif choice_2 == 'I':
            if (play_number % 2) != 0:
                flag = 1
                game()
            else:
                flag = 0
                game()


def game():
    global choice_2
    choice_2 = 0
    while True:
        if len(cards_pc) == 0 or len(cards_player) == 0 or choice_2 == 2:
            game_over()
            break
        if flag == 1:
            if len(cards_pc) == 0 or len(cards_player) == 0:
                game_over()
                break
            print('\033[36mSua Vez!\033[m')
            print(f'\033[7;33;46m[1] Nova Rodada\033[m')
            print(f'\033[7;32;46m[2]    Sair    \033[m')
            choice_2 = int(input(''))
            sleep(.5)
            if choice_2 == 2:
                new_game()
                break
            elif choice_2 == 1:
                print(f'\033[30m{cards_player[0][0]}\033[m')
                print(f'\033[33m[1] Calibre__________________________{cards_player[0][1]}mm')
                print(f'[2] Peso_____________________________{cards_player[0][2]}Kg')
                print(f'[3] Ângulo de elevação_______________{cards_player[0][3]}º')
                print(f'[4] Peso do projétil_________________{cards_player[0][4]}Kg')
                print(f'[5] Velocidade inicial do projétil___{cards_player[0][5]}m/s')
                print(f'[6] Alcance__________________________{cards_player[0][6]}m\033[m')
                choice_player = int(input('\033[31mPlay now!\033[m\n'))
                if 6 < choice_player < 1:
                    while 6 < choice_player < 1:
                        choice_player = int(input('\033[31mPlay now!\033[m\n'))
                elif choice_player == 1:
                    if cards_player[0][choice_player] > cards_pc[0][1]:
                        win()
                    elif cards_player[0][1] < cards_pc[0][1]:
                        lose()
                    else:
                        draw()
                elif choice_player == 2:
                    if cards_player[0][choice_player] > cards_pc[0][2]:
                        win()
                    elif cards_player[0][2] < cards_pc[0][2]:
                        lose()
                    else:
                        draw()
                elif choice_player == 3:
                    if cards_player[0][choice_player] > cards_pc[0][3]:
                        win()
                    elif cards_player[0][3] < cards_pc[0][3]:
                        lose()
                    else:
                        draw()
                elif choice_player == 4:
                    if cards_player[0][choice_player] > cards_pc[0][4]:
                        win()
                    elif cards_player[0][4] < cards_pc[0][4]:
                        lose()
                    else:
                        draw()
                elif choice_player == 5:
                    if cards_player[0][choice_player] > cards_pc[0][5]:
                        win()
                    elif cards_player[0][5] < cards_pc[0][5]:
                        lose()
                    else:
                        draw()
                elif choice_player == 6:
                    if cards_player[0][choice_player] > cards_pc[0][6]:
                        win()
                    elif cards_player[0][6] < cards_pc[0][6]:
                        lose()
                    else:
                        draw()
        elif flag == 0:
            if len(cards_pc) == 0 or len(cards_player) == 0:
                game_over()
                break
            sleep(1)
            choice_pc = randint(1, 6)
            print('\033[31mVez da Maquina\033[m')
            sleep(.8)
            if choice_pc == 1:
                if cards_pc[0][1] > cards_player[0][1]:
                    lose()
                elif cards_pc[0][1] < cards_player[0][1]:
                    win()
                else:
                    draw()
            if choice_pc == 2:
                if cards_pc[0][2] > cards_player[0][2]:
                    lose()
                elif cards_pc[0][2] < cards_player[0][2]:
                    win()
                else:
                    draw()
            if choice_pc == 3:
                if cards_pc[0][3] > cards_player[0][3]:
                    lose()
                elif cards_pc[0][3] < cards_player[0][3]:
                    win()
                else:
                    draw()
            if choice_pc == 4:
                if cards_pc[0][4] > cards_player[0][4]:
                    lose()
                elif cards_pc[0][4] < cards_player[0][4]:
                    win()
                else:
                    draw()
            if choice_pc == 5:
                if cards_pc[0][5] > cards_player[0][5]:
                    lose()
                elif cards_pc[0][5] < cards_player[0][5]:
                    win()
                else:
                    draw()
            if choice_pc == 6:
                if cards_pc[0][6] > cards_player[0][6]:
                    lose()
                elif cards_pc[0][6] < cards_player[0][6]:
                    win()
                else:
                    draw()


def win():
    global flag
    flag = 1
    print(f'\033[36mVocê Ganhou a Carta!\033[m')
    print(f'{cards_pc[0][0]}')
    print(f'\033[31m[1] Calibre__________________________{cards_pc[0][1]}mm')
    print(f'[2] Peso_____________________________{cards_pc[0][2]}Kg')
    print(f'[3] Ângulo de elevação_______________{cards_pc[0][3]}º')
    print(f'[4] Peso do projétil_________________{cards_pc[0][4]}Kg')
    print(f'[5] Velocidade inicial do projétil___{cards_pc[0][5]}m/s')
    print(f'[6] Alcance__________________________{cards_pc[0][6]}m\033[m\n')
    buffer = cards_player[0]
    cards_player.pop(0)
    cards_player.append(buffer)
    cards_player.append(cards_pc[0])
    cards_pc.pop(0)
    game()


def lose():
    global flag
    flag = 0
    print(f'\033[31mVocê Perdeu sua Carta!\033[m')
    print(cards_pc[0][0])
    print(f'\033[31m{cards_player[0][choice_player]} - {cards_pc[0][choice_pc]}\033[m')
    buffer_pc = cards_pc[0]
    cards_pc.pop(0)
    cards_pc.append(buffer_pc)
    cards_pc.append(cards_player[0])
    cards_player.pop(0)
    game()


def draw():
    print('Vocês empataram!')
    buffer = cards_player[0]
    cards_player.pop(0)
    cards_player.append(buffer)
    buffer_pc = cards_pc[0]
    cards_pc.pop(0)
    cards_pc.append(buffer_pc)
    game()


def wait():
    print('\033[32m*\033[m', end='')
    sleep(.3)


def wait_2():
    print('\033[33m*\033[m', end='')
    sleep(.3)


def game_over():
    if len(cards_pc) == 0:
        print('PARABÉNS! VOCÊ VENCEU!')
    elif len(cards_player) == 0:
        print('VOCÊ FOI DERROTADO!')


new_game()
print('\033[32mObrigado por Jogar!\033[m')
