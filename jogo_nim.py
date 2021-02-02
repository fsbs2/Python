def computador_escolhe_jogada(n,m):
        jogada=1

        while jogada!= m:
                if(n-jogada) % (m+1) == 0:
                        return jogada
                else:
                        jogada += 1
        return jogada


def usuario_escolhe_jogada(n,m):
        while True:
                try:
                        jogada = int(input("Faça sua jogada!"))
                        if((jogada <= m) and (jogada > 0)):
                                return jogada
                except:
                        print("Digite um valor válido!")


def partida():
        n=int(input("Quantas peças?"))
        m=int(input("Limite de peças por jogada?"))
        print()
        
        if n% (m+1) == 0:
                print("Você começa!")
                while(n>0):
                        pecas = usuario_escolhe_jogada(n,m)
                        print("Você tirou ",pecas," peças.")
                        n-=pecas
                        if n==0:
                                print("Você ganhou!")
                                break
                        else:
                                print("Agora restam ", n)
                                print()
                        pecas=computador_escolhe_jogada(n,m)
                        print("O computador tirou ",pecas," peças.")
                        n-=pecas
                        if(n==0):
                                print("O computador ganhou!")
                                break
                        else:
                                print("Agora restam ", n)
                                print()
        else:
                print("Computador começa")
                while(n>0):
                        pecas = computador_escolhe_jogada(n,m)
                        print("O computador tirou ",pecas," peças.")
                        n-=pecas
                        if(n==0):
                                print("O computador ganhou!")
                                break
                        else:
                                print("Agora restam ", n)
                                print()
                        pecas = usuario_escolhe_jogada(n,m)
                        print("Você tirou ",pecas," peças.")
                        n-=pecas
                        if(n==0):
                                print("Você ganhou!")
                                break
                        else:
                                print("Agora restam ", n)

def campeonato():
        nRodada=1
        while nRodada <=3:
                print()
                print("**** Rodada ",nRodada,"****")
                print()
                partida()
                nRodada +=1
        print()
        print("Placar: Você 0 x 3 Computador")
        
def main():
        print("Bem vindo ao jogo do NIM")
        print("Escolha:")
        EscolhaValida= True
        while EscolhaValida:
                op = int(input(" 1 - para jogar uma partida isolada\n 2 - para jogar um campeonato"))
                if(op == 1):
                        print()
                        partida()
                        EscolhaValida = False
                        return EscolhaValida
                if(op==2):
                        print()
                        campeonato()
                        EscolhaValida = False
                        return EscolhaValida




main()
