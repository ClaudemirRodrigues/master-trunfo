from random import shuffle
import os

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
card_014 = ('Anticarro 918 37mm', 37, 175, 15, .460, 435, 300, 14)
card_015 = ('Brixia Modelo 35', 45, 15.5, 80, .465, 83, 530, 15)
card_016 = ('BL 6pol 30cwt', 152, 3507, 45, 53.75, 237, 4755, 16)
card_017 = ('BL Mk1 5pol', 127, 1212, 50, 22.68, 240, 4390, 17)
card_018 = ('Bofors Modelo 34', 75, 928, 60, 6.58, 455, 9300, 18)
card_019 = ('Breda Modelo 35', 20, 307, 90, .135, 840, 2500, 19)
card_020 = ('Canhão Antiaéreo 13lb 9cwt', 76, 7620, 80, 5.89, 655, 5790, 20)
cards = list()
cards_pc = list()
cards_player = list()


def new_game():
    cards = []
    cards = [card_001, card_002, card_003, card_004, card_005, card_006, card_007, card_008, card_009, card_010,
             card_011, card_012, card_013, card_014, card_015, card_016, card_017, card_018, card_019, card_020]
    print(f'\033[36m{cards[8]}\033[m')

    shuffle(cards)
    cards_player[:] = cards[:10]
    cards_pc[:] = cards[10:]
    for c in range(0, 10):
        print(cards_pc[c])
        print(f'\033[32m{cards_player[c]}\033[m')


new_game()
