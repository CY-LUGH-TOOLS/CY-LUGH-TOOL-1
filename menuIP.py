#banner
print('''
░██████╗░███████╗░█████╗░  ██╗██████╗░
██╔════╝░██╔════╝██╔══██╗  ██║██╔══██╗
██║░░██╗░█████╗░░██║░░██║  ██║██████╔╝
██║░░╚██╗██╔══╝░░██║░░██║  ██║██╔═══╝░
╚██████╔╝███████╗╚█████╔╝  ██║██║░░░░░
░╚═════╝░╚══════╝░╚════╝░  ╚═╝╚═╝░░░░░''')
#by
print('''
█▀▀▄ █──█ 　 █▀▀ █── █▀▀█ █──█ █▀▀ █▀▀█ 
█▀▀▄ █▄▄█ 　 ▀▀█ █── █▄▄█ █▄▄█ █▀▀ █▄▄▀ 
▀▀▀─ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀──▀ ▄▄▄█ ▀▀▀ ▀─▀▀''')

escolha = -1

#escolhas

while escolha < 1 or escolha > 99:
    escolha = int(input("""\033[0;30;0mDigite: nano IPadd.py e coloque o seu email no to, entre em contato cmg para que eu faça um script .exe ou apk pra vc. (copie tudo do IPadd.py), para contato me chame via instagram. @slayerkkk_              
[ 1 ] = sair
Sua escolha: """))
    print(''' ''')
    print('')
    print('')
    
# escolha

if escolha == 1:
        print('\033[0;30;32m"Um soldado da tiros, um hacker da enter."')
        exit()