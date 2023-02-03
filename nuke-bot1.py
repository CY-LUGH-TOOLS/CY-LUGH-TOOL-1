#python -m pip install -r requirements.txt
print('''
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝

██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░''')
escolha = -1
print('calma ae, antes de usar o script, execute o comando a baixo')
print('\033[0;30;32mpython -m pip install -r install.txt')

while escolha < 1 or escolha > 99:
    escolha = int(input("""\033[0;30;0m
[ 1 ] NUKAR!
[ 2 ] voltar ao menu
[ 3 ]sair 
\033[0;30;34m------> """))
    print(''' ''')
    print('')
    print('')
    

if escolha == 1:
    exec(open('nuke-bot.py', encoding="utf-8").read(), globals())
    
if escolha == 2:
    exec(open('LITTLE-FRIEND2.py', encoding="utf-8").read(), globals())

if escolha == 3:
        print('\033[0;30;32m"Um soldado da tiros, um hacker da enter."')
        exit()