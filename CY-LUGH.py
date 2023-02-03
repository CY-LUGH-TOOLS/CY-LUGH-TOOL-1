#nome
print('''\033[0;30;32m

░█████╗░██╗░░░██╗░░░██╗░░░░░██╗░░░██╗░██████╗░██╗░░██╗
██╔══██╗╚██╗░██╔╝░░░██║░░░░░██║░░░██║██╔════╝░██║░░██║
██║░░╚═╝░╚████╔╝░░░░██║░░░░░██║░░░██║██║░░██╗░███████║
██║░░██╗░░╚██╔╝░░░░░██║░░░░░██║░░░██║██║░░╚██╗██╔══██║
╚█████╔╝░░░██║░░░██╗███████╗╚██████╔╝╚██████╔╝██║░░██║
░╚════╝░░░░╚═╝░░░╚═╝╚══════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝

████████╗░█████╗░░█████╗░██╗░░░░░
╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░██║░░██║██║░░██║██║░░░░░
░░░██║░░░╚█████╔╝╚█████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝''')
print('')
#aviso
print('''\033[0;30;31m
░█████╗░██╗░░░██╗██╗░██████╗░█████╗░██╗
██╔══██╗██║░░░██║██║██╔════╝██╔══██╗██║
███████║╚██╗░██╔╝██║╚█████╗░██║░░██║██║
██╔══██║░╚████╔╝░██║░╚═══██╗██║░░██║╚═╝
██║░░██║░░╚██╔╝░░██║██████╔╝╚█████╔╝██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░░╚════╝░╚═╝\033[0;30;40m''')
print('')
print('''\033[0;30;31mos comandos 1,2 & 3 estao em desenvolvimento, os outros sao execuatos pelo menu, voce pode usar todos, mas nao dentro do menu.''')
print('')
print('')
escolha = -1

#escolhas

while escolha < 1 or escolha > 99:
    escolha = int(input("""\033[0;30;0mO que você deseja fazer?
[ 1 ] = DoS (by: palahsu)                       [ 9 ] bot nuker discord
[ 2 ] = sqlmap                                  [ 10 ] puxa ip
[ 3 ] = brutalforce                             [ 11 ] dowloader YT (linux debian)
[ 4 ] = rapidscan                               [ 12 ] gerador de nitro
[ 5 ] = banir numero (whatsapp)                 [ 99 ] sair
[ 6 ] = desbanir numero (whatsapp) 
[ 7 ] = email spammer
[ 8 ] = gerador de cpf
Sua escolha: """))
    print(''' ''')
    print('')
    print('')
    
# escolha

if escolha == 1:
    exec(open('DDOS2.py', encoding="utf-8").read(), globals())
    

elif escolha == 2:
    exec(open('SQLI.py', encoding="utf-8").read(), globals())

elif escolha == 3:
    exec(open('brute.py', encoding="utf-8").read(), globals())

elif escolha == 4:
    exec(open('RPD1.py', encoding="utf-8").read(), globals())

if escolha == 5:
    exec(open('ban.py', encoding="utf-8").read(), globals())

if escolha == 6:
    exec(open('desban.py', encoding="utf-8").read(), globals())

if escolha == 7:
    exec(open('menu-bomb.py', encoding="utf-8").read(), globals())

if escolha == 8:
    exec(open('menuCpf.py', encoding="utf-8").read(), globals())
    
if escolha == 9:
    exec(open('nuke-bot1.py', encoding="utf-8").read(), globals())

if escolha == 10:
    exec(open('menuIP.py', encoding="utf-8").read(), globals())

if escolha == 11:
    exec(open('YTDOW.py', encoding="utf-8").read(), globals())

if escolha == 12:
    exec(open('GEN-NITRO.py', encoding="utf-8").read(), globals())


if escolha == 99:
        print('\033[0;30;32m"Um soldado da tiros, um hacker da enter."')
        exit()
else:
    print('''
█▀▀█ ▀▀█▀▀ █▀▀ 　 █▀▄▀█ █▀▀█ ░▀░ █▀▀ 　 ▄ ▀▄ 
█▄▄█ ░░█░░ █▀▀ 　 █░▀░█ █▄▄█ ▀█▀ ▀▀█ 　 ░ ░█ 
▀░░▀ ░░▀░░ ▀▀▀ 　 ▀░░░▀ ▀░░▀ ▀▀▀ ▀▀▀ 　 ▀ ▄▀''')

#opa dev q ta usando o meu script, me da uma nota la pelo insta: @slayerkkk_
#sou iniciante ainda, me fale oq posso melhorar! :)