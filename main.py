import os
import time

import panels
import banners

import engineGoogle
import engineBing


while True:
    banners.blurred_black_banner()
    panels.menu_panel()
    menu_panel_option = int(input('Escolha uma opcao: '))
    if menu_panel_option == 1:
        while True:
            banners.blurred_black_banner()
            panels.dork_panel()
            dork_panel_option = int(input('Escolha uma opcao: '))
            if dork_panel_option == 1:
                banners.blurred_black_banner()
                dork = str(input('DorkL: '))
                resultados = int(input('Quantidade de resultados: '))
                for result in engineGoogle.search(dork, resultados):
                    print(f'>> {result}')
                input('Pressione qualquer tecla')
            
            if dork_panel_option == 2:
                banners.blurred_black_banner()
                dork = str(input('DorkL: '))
                resultados = int(input('Quantidade de resultados: '))
                for result in engineBing.search(dork, resultados):
                    print(f'>> {result}')
                input('Pressione qualquer tecla')

            if dork_panel_option == 0:
                banners.blurred_black_banner()
                time.sleep(1)
                break
            else:
                banners.blurred_black_banner()
                print('Escolha uma opcao valida')
    if menu_panel_option == 2:
        print('Ainda em desevolvimento')
        input('Pressione qualquer tecla')
    if menu_panel_option == 3:
        banners.blurred_black_banner()
        panels.about_me()
    if menu_panel_option == 0:
        banners.blurred_black_banner()
        print('Saindo..')
        time.sleep(2.5)
        break
    else:
        banners.blurred_black_banner()
        print('Escolha uma opcao valida')