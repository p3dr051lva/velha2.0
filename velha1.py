#casas do tabuleiro
c1 = '1'
c2 = '2'
c3 = '3'
c4 = '4'
c5 = '5'
c6 = '6'
c7 = '7'
c8 = '8'
c9 = '9'

VEZ = 'X'

def init():
    global c1, c2, c4, c4, c5, c6, c7, c8, c9, VEZ
    c1 = '1'
    c2 = '2'
    c3 = '3'
    c4 = '4'
    c5 = '5'
    c6 = '6'
    c7 = '7'
    c8 = '8'
    c9 = '9'
    VEZ = 'X'

#introducao do jogo.
print("Ola, seja muito bem vindo ao nosso jogo da velha, caso voce nao saiba\n \
o jogo da velha consiste em dois joagadore, X e O, que tem o objetivo de\n \
preencher tres casas em coluna, fileira ou diagonal, com o seu simbolo\n \
agora que voce ja sabe, bom jogo!! \n \
    ")
#tabuleiro 2.0
def print_tabuleiro (c1, c2, c3, c4, c5, c6, c7, c8, c9):
    print(      "| |--------------------------------------------| |")
    print(      "| |--------------------------------------------| |")
    print(      "| |              |               |             | |")
    print(      "| |      %s       |      %s        |     %s       | |") % (c1, c2, c3)
    print(      "| |              |               |             | |")
    print(      "| |____________________________________________| |")
    print(      "| |              |               |             | |")
    print(      "| |      %s       |      %s        |     %s       | |") % (c4, c5, c6)
    print(      "| |              |               |             | |")
    print(      "| |____________________________________________| |")
    print(      "| |              |               |             | |")
    print(      "| |      %s       |      %s        |     %s       | |") % (c7, c8, c9)
    print(      "| |              |               |             | |")
    print(      "| |--------------------------------------------| |")
    print(      "| |--------------------------------------------| |")
#define se tem perdedor, pois se c1 eh igual a c2 e c3, e c1 eh X por exemplo, X ganhou, e O perdeu.
def tem_perdedor (c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 == c2 == c3 or c4 == c5 == c6 or c7 == c8 == c9 or \
       c1 == c4 == c7 or c2 == c5 == c8 or c3 == c6 == c9 or \
       c1 == c5 == c9 or c3 == c5 == c7:
        (print_tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9))
        print("O jogador %s perdeu. " % VEZ,)
        return True
    else:
        return False
#define se deu velha pois se todas as casas foram preenchidas, deu velha.
def deu_velha (c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if c1 != '1' and c2 != '2' and c3 != '3' and \
       c4 != '4' and c5 != '5' and c6 != '6' and \
       c7 != '7' and c8 != '8' and c9 != '9':
        print("Parece que deu velha meu parceirinho")
        return True
    return False 

JOGANDO = True

#valida a jogada, pois se a casa nao eh igual ao seu numero original, ela esta ocupada pelo outro jogador, logo a jogada nao pode ser validada.
def valida_jogada (c, c1, c2, c3, c4, c5, c6, c7, c8, c9):
    if (c == '1' and c1 != '1') or \
       (c == '2' and c2 != '2') or \
       (c == '3' and c3 != '3') or \
       (c == '4' and c4 != '4') or \
       (c == '5' and c5 != '5') or \
       (c == '6' and c6 != '6') or \
       (c == '7' and c7 != '7') or \
       (c == '8' and c8 != '8') or \
       (c == '9' and c9 != '9'):
        return False
    return True
print_tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
while JOGANDO:
    while not tem_perdedor( c1, c2, c3, c4, c5, c6, c7, c8, c9) and \
          not deu_velha(c1, c2, c3, c4, c5, c6, c7, c8, c9):
       
        c =str( input ("Jogador %s escolha sua jogada: " %VEZ))
        if valida_jogada (c, c1, c2, c3, c4, c5, c6, c7, c8, c9):
           
            if (c == '1'):c1 = VEZ
            elif (c == '2'): c2 = VEZ
            elif (c == '3'): c3 = VEZ
            elif (c == '4'): c4 = VEZ
            elif (c == '5'): c5 = VEZ
            elif (c == '6'): c6 = VEZ
            elif (c == '7'): c7 = VEZ
            elif (c == '8'): c8 = VEZ
            elif (c == '9'): c9 = VEZ
            if VEZ == 'X':
                VEZ = 'O'
            else:
                VEZ = 'X'
        else:
           print ("Jogada invalida!!")
        print_tabuleiro(c1, c2, c3, c4, c5, c6, c7, c8, c9)
    else:
        JOGANDO = raw_input("Gostaria de jogar mais uma vez? (sim/nao) ") == "sim"
        if JOGANDO:
            init()



