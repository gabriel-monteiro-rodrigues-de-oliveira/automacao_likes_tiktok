import webbr
import tt
import conn
import valid
from time import sleep


tt_url = 'https://www.tiktok.com/'

while True:
    sleep(0.75)
    print(' ' * 3, end='')
    print('=' * 24)
    print(' ' * 3, end='')
    print('LIKES AUTOMÁTICOS TIKTOK')
    print(' ' * 3, end='')
    print('=' * 24)
    sleep(0.75)
    print('(1) - Verificar conexão com TikTok.')
    print('(2) - Entrar no TikTok.')
    print('(3) - Logar o usuário no TikTok (Caso não estiver logado).')
    print('(4) - Curtir vídeos de um criador TikTok.')
    print('(5) - Deslogar o usuário no TikTok.')
    print('(0) - Encerrar o programa.')
    sleep(0.75)
    opt = input('Digite o número de uma das opções: ')[0]

    if opt == '1':
        conn.test_conn(tt_url)

    elif opt == '2':
        while True:
            usr_webbr = input('Digite o nome do navegador: ')
            if not valid.is_empty(usr_webbr):
                break
            else:
                print('Valor inválido... Valor vazio')
        webbr.open_webbr(usr_webbr)
        webbr.open_tt(tt_url)

    elif opt == '3':
        while True:
            usr_phone = input('Digite o número do usuário TikTok para login: ')
            if not valid.is_empty(usr_phone):
                break
            else:
                print('Valor inválido... Valor vazio...')
        while True:
            usr_passwd = input('Digite a senha TikTok para login: ')
            if not valid.is_empty(usr_passwd):
                break
            else:
                print('Valor inválido... Valor vazio...')
        tt.login_tt(usr_phone, usr_passwd)

    elif opt == '4':
        # while True:
        tt_creator = input('Digite o criador TikTok para curtir: ') # X
            # empty = valid.is_empty(tt_creator)
            # has_at_char = valid.frst_char_at_sign(tt_creator)
            # if not empty and has_at_char:
                # break
            # else:
                # print('Valor inválido... Valor vazio/Falta "@"...')

        # while True:
            # max = 10
        likes = input('Digite a quantidade de vídeos: (Até 10) ')
            # likes_is_int = valid.is_int(likes)
            # likes_is_less_than = valid.is_less_than(likes, max, likes_is_int)

            # if likes_is_int and likes_is_less_than:
                # break
            # else:
                # print('Valor inválido. Digite um número inteiro no intervalo.')

        tt.srch_creator(tt_url, tt_creator)

        tt.srch_frst_video()

        tt.like_videos(likes)

    elif opt == '5':
        ...

    elif opt == '0':
        sleep(0.75)
        print('Finalizando o programa...')
        sleep(0.75)
        break

    else:
        sleep(0.75)
        print('Valor inválido. Digite um número inteiro no intervalo.')


# usr_name = input('Digite o usuário TikTok para login: ')
# usr_passwd = input('Digite a senha TikTok para login: ')

# while True:
#     tt_creator = input('Digite o criador TikTok para curtir: ')

#     if tt_creator[0] == '@':
#         print('@')

# while True:
#     likes = input('Digite a quantidade de vídeos para curtir: ')

#     if likes.isdigit():
#         break
#     else:
#         print('Valor inválido... Digite um número inteiro no intervalo...')

# webbr.open_webbr(usr_webbr)

# webbr.open_tt(tt_url)

# tt.login_tt(usr_name, usr_passwd)

# tiktok.search_creator(tt_url, tt_creator)

# tiktok.search_first_video()

# tiktok.like_videos(likes)
