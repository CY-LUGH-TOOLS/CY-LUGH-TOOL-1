print(''' 
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░
█████╗░░██╔████╔██║███████║██║██║░░░░░
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░
███████╗██║░╚═╝░██║██║░░██║██║███████╗
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝

██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝''')

print('')
print('antes de tudo, mude as config do script com o nano')
print('nano bombEmail.py')
print('coloque as informações de ataque e aperte enter apos reiniciar o seu terminal.')
escolha = -1

while escolha < 1 or escolha > 8:
    escolha = int(input("""\033[0;30;0mO que você deseja fazer?
[ 1 ] = iniciar terminal:"""))

if escolha == 1:
    exec(open('bombEmail.py', encoding="utf-8").read(), globals())