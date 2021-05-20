#PROJETO RPG
#Domingo Neto(32032889) e João Lipert(32088876)
import sys
import random
import time
vida=100
nivel=1
vidagoblin=200
print("BEM VINDO AVENTUREIRO")
print("1 = COMEÇAR A JOGAR")
print("2 = TUTORIAL")
print("3 = SAIR")
inicio=int(input("ESCOLHA SUA OPÇÃO = "))
while inicio == 2:
    if inicio == 2:
        print("O jogo funciona a base de escolhas. A cada escolha, o rumo da historia é alterado. Dependendo do caminho em que o jogador escolher, o jogo pode ficar mais fácil ou difícil. A cada evento o jogo proporcionará várias opções, sendo uma boa, algumas mediana, e outras péssimas. Caso a sua vida chegue a 0 é GAME OVER! Sua vida só será mostrada no final do jogo, e servirá como pontuação para avaliar o seu desempenho. Boa sorte na sua aventura!")
        inicio=int(input("ESCOLHA SUA OPÇÃO = "))
if inicio == 3:
        sys.exit("FIM")
elif inicio == 1:
        print("BEM VINDO AO RPG, AGORA VAMOS CRIAR SEU PERSONAGEM:")
        print("")
        nome=input("Digite o Nome do seu personagem: ")
        print("")
        print("Narrador :",nome,"acorda.")
        time.sleep(1)
        print("")
        print(nome,': "Hoje é dia de ganhar dinheiro."')
        time.sleep(3)
        print(nome,': "Acho que hoje vou na taverna procurar um quest nova."')
        time.sleep(4)
        print("")
        print("Narrador :",nome,"sai de casa em busca de uma quest. Mal sabia ele o que estava se metendo...")
        time.sleep(5)
        print("Narrador : Ao chegar a taverna",nome,"se depara com várias quests:")
        time.sleep(2)
        print("")
        print("LISTA DE QUEST, NIVEL 1 \n 1:SALVE O GATO DE CIMA DA ÁRVORE \n 2:SALVE O CACHORRO DO RIO \n 3:AJUDE A VELHINHA NAS COMPRAS")
        print("")
        Quests=int(input("ESCOLHA SUA MISSÃO DE INICIANTE: "))
        print("")
        xp1 = (random.randrange (1, 4))
        print("SISTEMA : MISSÃO COMPLETADA COM SUCESSO SUBIU",xp1,"NÍVEIS")
        nivel=1+xp1
        print("NIVEL : ",nivel)
        time.sleep(1)
        print("")
        print("LISTA DE QUEST NIVEL",nivel,"\n 1:AJUDA A ESCOLTAR O DONO DA TAVERNA \n 2:AJUDE A TRANSFERIR OS ITENS DO BANCO \n 3:FAÇA A SEGURANÇA DA FILHA DO DONO DA TAVERNA")
        print("")
        Quests=int(input("ESCOLHA SUA MISSÃO DE NÍVEL:"))
        print("")
        xp2 = (random.randrange (1, 4))
        print("SISTEMA : MISSÃO COMPLETADA COM SUCESSO SUBIU",xp2,"NÍVEIS")
        nivel=1+xp1+xp2
        print("NÍVEL : ",nivel)
        time.sleep(1)
        if nivel >= 1:
            print("Recepicionista : Olá",nome,". Vi que já fez bastante missão em nossa taverna, e atingiu o nível",nivel,". Começaremos a te dar missões mais difíceis.")
            time.sleep(3)
            print("")
            print("LISTA DE QUEST, NIVEL",nivel,"\n 1:MATAR MONSTROS NA FLORESTA \n 2:CAÇAR LOBOS DEMÔNIOS \n 3:DERROTAR O REI DEMÔNIO")
            print("")
        quest=int(input("Escolha sua Quest: "))
        if quest == 1 or 2 or 3:
                print("")
                print(nome,': "Essa parece boa pena que sou fraco ainda."')
                time.sleep(2)
                print("")
                print('Estranho : "Ei, você!"')
                time.sleep(2)
                print('Estranho : "Por favor me ajude. Tenho uma quest pra você."')
                time.sleep(2)
                print('Estranho : "Se você aceitar é claro..."')
                time.sleep(4)
                print("")
                print(nome,': "O que seria?"')
                time.sleep(2)
                print("")
                print('Estranho : "Uma quest que paga bem, é isso que importa."')
                time.sleep(3)
                print('Estranho : "Minha filha foi raptada por ladrões e estou desesperado para salvá-la."')
                time.sleep(4)
                print('Estranho : "Infelizmente sou muito velho e não consigo, por isso preciso de um bravo aventureiro."')
                time.sleep(5)
                print('Estranho : "Se aceitar, vá até a dungeon de Mordor, eles a esconderam lá."')
                time.sleep(5)
                print("")
                print('Narrador : Sem pensar duas vezes,',nome, 'aceita e corre até Mordor e assim começa a sua aventura.')
                time.sleep(6)
                print('Narrador : Ao entrar na dungeon,',nome, 'se depara com três caminhos(esquerda, meio ou direita).')
                time.sleep(5)
                print("")
                caminho=input("Qual caminho deseja seguir: ")
                while caminho!="meio":
                    if caminho == "esquerda":
                        print("")
                        print("Narrador : ",nome, "se depara com uma armadilha de espinhos, é ferido e perde vida.")
                        vida=vida-50
                        time.sleep(3)
                        if vida <=0:
                            print("")
                            print('Sua vida chegou a 0')
                            sys.exit("""GAME OVER!
Nem chegar no boss da história você consegue KKKKKKKKKKKKKKKKKK""")
                        else:
                            print("Narrador : ",nome, "volta.")
                            print("")
                            caminho=input("Qual caminho deseja seguir: ")
                    elif caminho == "direita":
                        print("")
                        print("Narrador : ",nome, "encontra uma gangue de goblins.")
                        time.sleep(2)
                        print("Narrador : ",nome, "mata os goblins com sucesso, porém perde bastante vida.")
                        vida =vida-50
                        time.sleep(3)
                        if vida <=0:
                            print("")
                            print('Sua vida chegou a 0')
                            sys.exit("""GAME OVER!
Nem chegar no boss da história você consegue KKKKKKKKKKKKKKKKKK""")
                        else:
                            print("Narrador : ",nome, "volta.")
                            print("")
                            caminho=input("Qual caminho deseja seguir: ")
                    elif vida <=0:
                        sys.exit("""GAME OVER!
Nem chegar no boss da história você consegue KKKKKKKKKKKKKKKKKK""")
                if caminho == "meio":
                    print("")
                    print("Narrador :",nome, "encontra uma poção de escudo no chão, deixada por outro aventureiro e segue em frente.")
                time.sleep(5)
                print("Narrador : Após andar por 30 minutos",nome, "se depara com o chefe dos goblins e logo atrás, o que se parece a filha do velho.")
                time.sleep(6)
                print("Narrador :",nome, "se prepara para atacar")
                time.sleep(5)
                print("")
                print("""Opções de ataque:
1:atacar na cabeça
2:acertar a perna
3:cortar um braço fora
4:usar poção de escudo
5:atacar por trás
6:fugir""")
                print("")
                print("VIDA DO CHEFE GOBLIN : ",vidagoblin)
                print("")
                ataque=int(input("O que deseja fazer: "))
                while vidagoblin>0:
                    if ataque == 1:
                        print("")
                        print("Narrador : ",nome,"tenta atacar a cabeça e tira 75 de vida do chefe goblin.")
                        vidagoblin=vidagoblin-75
                        print("")
                        print("VIDA DO CHEFE GOBLIN : ",vidagoblin)
                        time.sleep(3)
                        if vida>0 and vidagoblin>0:
                            print("")
                            ataque=int(input("O que deseja fazer: "))
                    elif ataque == 2:
                        print("")
                        print("Narrador : ",nome, "tenta atacar a perna do chefe goblin, porém toma um chute e sai voando.",nome, "perde vida.")
                        vida=vida-50
                        print("")
                        print("VIDA DO CHEFE GOBLIN : ",vidagoblin)
                        time.sleep(4)
                        if vida>0 and vidagoblin>0:
                            print("")
                            ataque=int(input("O que deseja fazer: "))
                    elif ataque == 3:
                        print("")
                        print("Narrador : ",nome, "tenta realizar o ataque, acerta o chefe goblin porém não consegue cortar o braço fora e recebe um soco." ,nome,"perde vida e o chefe goblin perde 70 de vida.")
                        vidagoblin=vidagoblin-70
                        vida=vida-20
                        print("")
                        print("VIDA DO CHEFE GOBLIN : ",vidagoblin)
                        if vida>0 and vidagoblin>0:
                            time.sleep(3)
                            print("")
                            ataque=int(input("O que deseja fazer: "))
                    elif ataque ==  4:
                        print("")
                        print("Narrador : Você usa a poção e recebe 30 de escudo. Agora você pode receber mais dano.")
                        vida=vida+30
                        time.sleep(2)
                        if vida>0 and vidagoblin>0:
                            print("")
                            ataque=int(input("O que deseja fazer: "))
                    elif ataque == 5:
                        print("")
                        print("Narrador : ",nome, "tenta atacar por trás, e tira 50 de vida do chefe goblin. Infelizmente não foi rápido o suficiente e recebeu um soco.",nome,"perde vida.")
                        vidagoblin=vidagoblin-50
                        vida=vida-30
                        print("")
                        print("VIDA DO CHEFE GOBLIN : ",vidagoblin)
                        time.sleep(3)
                        if vida>0 and vidagoblin>0:
                            print("")
                            ataque=int(input("O que deseja fazer: "))
                    elif ataque == 6:
                        print("")
                        print("Narrador : ",nome, "percebe que não é páreo para enfrentá-lo e foge igual um covarde.")
                        time.sleep(2)
                        sys.exit("""GAME OVER!
Você é um covarde""")
                    elif vida<=0:
                        print("")
                        print('Sua vida chegou a 0 e você morreu')
                        print("")
                        print("""CLASSIFICAÇÕES:
1:CHEGOU ATÉ O FINAL COM VIDA COMPLETA - MASTER
2:CHEGOU ATÉ O FINAL COM VIDA ABAIXO DE 100 - BOM
3:MORREU PRO CHEFE GOBLIN - MEDIO
4:MORREU ANTES DE CHEGAR NO CHEFE GOBLIN - RUIM""")
                        sys.exit("""GAME OVER!
Pelo menos você conseguiu chegar no boss.""")
                if vidagoblin<=0:
                    print("")
                    print("Narrador : Parabéns! Você conseguiu matar o chefe goblin com sucesso.")
                    time.sleep(4)
                    print("Narrador :",nome, "anda em direção da filha do velho para libertá-la, porém algo inesperado acontece.")
                    time.sleep(5)
                    print("Narrador : A dungeon começa a desmoronar e você tem pouco tempo para sair de lá.")
                    time.sleep(4)
                    print("Narrador : Desesperado,",nome,"precisa tomar uma decisão.")
                    time.sleep(3)
                    print("")
                    print("DECISÃO :\n 1:Fugir da dungeon sozinho e deixá-la lá\n 2:Desamarrar ela e sair da dungeon juntos")
                    time.sleep(3)
                    print("")
                    fuga=int(input("Decisão: "))
                    if fuga==1:
                        print("")
                        print("Narrador :",nome, "desiste de salvá-la pois valoriza mais sua vida do que a de outros.")
                        time.sleep(3)
                        print("Narrador :",nome, "corre desesperadamente igual um covarde para fora da dungeon sem nem olhar para trás e foge com sucesso.")
                        time.sleep(4)
                    if fuga==2:
                        print("")
                        print("Narrador :",nome, "decide desamarrá-la rapidamente e sair da dungeon juntos.")
                        time.sleep(4)
                        print("Narrador : Ao chegar na saída",nome, "percebe que não da tempo dos dois sairem vivos.",nome,"decide empurra a mulher para fora e então é sufocado pelas ruínas da dungeon.")
                        time.sleep(7)
                        print("")
                    print("Sua vida : ",vida)
                    time.sleep(4)
print("")
print("""CLASSIFICAÇÕES:
1:CHEGOU ATÉ O FINAL COM VIDA COMPLETA - MASTER
2:CHEGOU ATÉ O FINAL COM VIDA ABAIXO DE 100 - BOM
3:MORREU PRO CHEFE GOBLIN - MEDIO
4:MORREU ANTES DE CHEGAR NO CHEFE GOBLIN - RUIM""")
sys.exit("FIM")
