print('''\033[0;32m___________________________________________$$s
_________________________$____$$s___________s$$s
_________________________s$$$$s$$$$$$s________$$$___s$
_______________s$$$$$$$$s___s$$$$ss$$$$s________$$$__$$
________________________s$$$s__$$$$$s_$$$s___s$__s$$s_$$
__________s$$$$$$$$$$$$$$$$$$$$sss$$$$s_$$$s__$$$__s$$s$
_____s$$$$$$$$$s_____s$$$$$$$$$$$$$$h$$$__$$$s__$$___$$$s
___s$$$$$s_____________________ss$$$$$$$$s_s$$$s$$$__s$$$
__________________________s$$$s____s$$$$$$$$s$$$$$$$__$$$
_________s$$$$$$$$$$$$$$$s$$$$$$$$$$s$$$$$$$$$ss$$$$s_$$$
_____________________s$$$$$$$$$$s$$$s____s$$$$$$__$$$__$$
________________s$$$$$$$$$$$$$$$$$$$$$$s_____s$$$s_$$__$$
________s$$$$$$$$$$$$$$$$$$$$$$$s$s__s$$$$$$s___$$s_$s$$$
_____s$$$$$s$$$$$$$$$$$$$$s____$$s$$$$$$$$$$$$$s____$$$$s
___s$$$$__s$$$$$$$$$s_____s$$$$$s$$$$$$$$$$$$$$$$$s__$$$
___s$___$$$$$$______s$$$$$$$s_s$$$$$$$$$$$$$$$$$$$$$____$$$
______s$$$s___s$$$$$$$$$$$___$$$$$$$$$$$$$$$$$$$$$$$$s$$$$$$$s
_____$$$__s$$$$$$$$$$$$$$__$$$$$$$$$$$$$$$$$$$$s$s$_$$$$$$$$$$$
____$$$_$$$$$$i$$$$$s_$$__$$$$$$$$$$$$$$$$$$$ss$$$s$$$$$$$$s$$s
___$$__$$$__s$$$$ss__$$_$$$$$$$$$$$$$$$$$$$$s$$$$$_$$$$e$$s$
__$$_s$$___$$$$s_$$_$$s$$$$$$$$$$$$$$$$$$$$s$$$$$s_$$$$$$s$
_s$s$$$___$$$$_s$$__$$__$$$$$$$$$$$$$$$$$$_$$$$$$$_s_$$$
_$$s$s__s$$$__$$____s$$__$$$$$$$$$$$$$$$$$_$$$$$$$$__$$$
$$_$___$$$$_s$$__$$__$$$s__s$$$$$$$$$$$$$$_$$$$$$$$$$$$s
$$____$$$s_$$$__$$$_$_s$$$$s___s$s$$$$$$$$_$$$$$$$$s$$$
$____$$$__$$sss$$$$__$_s$$$$$$$$$$s$s$$$$$___s$$$$s$$$s
____$$$_s$$$_$s$$$$s_s$__$$$$$$___s$$s_$$$s___s$$$_$$$
____$$_s$$$_$$_s$$$$$_s$$___$$$$$________$_____$$$s$$s
___s$$_$$$__$$__$$$$$$$$$$s____s$$$$$_________s$$$$$$
___$$$s$$$__$$___$$ss$$$$$$$$s____s$$$$$s______$$$$$$
___$s$$$$$_s$$__s_$$$_s$$$$$$$$$$s___s$$$$$$$s___sss
___$$$$$$$_$$$__$s_$$$$s__s$$$$$$$$$s___$$$$$$$s
__s$$$$$$$_$$$s_s$__$$$$$$s__s$$$$$$$$$s__$__$$$$s
__$_$$$$s$_s$$$__$$__$$$$$$$$s__$$s$$$$$$$_____$$$$
____s$$$_$$_$$$___$$__$s$$$$$$$$_s__s$$$s$$$____$$$$
_____$$$__$_$$$$___$$_ss_$$$$$$$$$____$$$$_s$____$$$s
_____$$$s_$_s$$$s__$$$____s$$$$$$$$$___s$$$______$$$$
_____s$$$_ss_$$$$___$$s____$$$$$$$$$$___$$$$_____s$$$
______$k$__$__$$$$__s$$____$$$$$$$h$$____$$$$_____$$s
______$$$______$$$s__$$$___$$_$$$$$$$$___s$$$$____$$
_______$$s______$$$__s$$$___$_s$$$$$s____s$$$$____$s
_______$$$_______$$$_s$$_$__$__$$$$$s____s$$$$___$$
________$$_______s$$__$$_______$$$$$s____$$$$$___$s
________$$________s$$_$$______s$$$$$_____$$_$$___$
___________________$$_$$s_____$$$$$_____$$s_$s
____________________$$s$$_____$$$$_____s$$__$
____________________s$_$$____$$$s_____s$$
_____________________$_$$___$$$______s$$
_______________________$$__s$$______$$$
________________________$__$$______$$$
________________________$_$$s____$$$s
__________________________$$___s$$s
__________________________$$__$$s
''')
#by
print('''\033[1;31m
█▀▀ █── █▀▀█ █──█ █▀▀ █▀▀█ 
▀▀█ █── █▄▄█ █▄▄█ █▀▀ █▄▄▀ 
▀▀▀ ▀▀▀ ▀──▀ ▄▄▄█ ▀▀▀ ▀─▀▀''')

escolha = -1

#escolhas

while escolha < 1 or escolha > 2:
    escolha = int(input("""\033[1;0mo email sera enviado infinitamente, para parar o script, use control + C

[ 1 ] BOMB
    
NÃO ME RESPONSABILIZO PELOS SEUS ATOS!!
ESTE METODO PODERA CAUSAR O BANIMENTO DE SEU EMAIL!    
\033[1;34m---> """))
    print(''' ''')
    print('')
    print('')
    
# escolha
while True:
     if escolha == 1:
        exec(open('bombEmail.py', encoding="utf-8").read(), globals())