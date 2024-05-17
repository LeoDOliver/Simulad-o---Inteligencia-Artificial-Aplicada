nota = 0

print("Questão 1 \n Relacione os criterios com as proposições sobre os ambientes de tarefa a seguir e depois marque a alternativa correta \n\n 1.Completamente X Parcialmente Observável \n 2.Deterministico X Estocástico \n 3.Episodico X Sequencial \n 4.Estático X Dinamico \n 5.Discreto X Contínuo \n\n (     ) Se há dependência dos estados atuais com os estados anteriores ou não. \n (     ) Se o ambiente se modifica ou não enquanto o agente executa a tarefa \n (     ) Se o agente acessa de forma completa ou não os estados do ambiente a cada instante \n (     ) Se há uma mudança brusca ou suave na sequência de estados que o agente experimenta. \n (     ) Se o próximo estado é completamente conhecido pelo estado atual ou não por parte do agente. \n\n A - 3-5-4-1-2 \n B - 4-3-1-2-5 \n C - 5-4-1-3-2 \n D - 3-4-1-5-2 \n E - 1-2-3-4-5 \n")

r1 = input("Digite a opção correta: \n")

if r1 == "D" or r1 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 2 \n Assinale as afirmativas a seguir com os cientistas respectivos e depois marque a alternativa correta: \n\n (     ) Propôs um teste no qual uma pessoa precisa descobrir se está falando com outro humano ou com uma máquina. \n (     ) Cria o software ELIZA para simular diálogos, o programa ancestral dos chatterbots atuais. \n (     ) Em 1962, publica sobre a evolução e recombinação para resolver problemas de otimização \n (     ) Criador da rede neural NETtalk para a pronúncia de palavras em inglês \n (     ) Cria a linguagem LISP, uma linguagem para manipular listas encadeadas como forma de representação de conhecimento. \n\n Cientistas: \n I. Joseph Weizenbaum \n II. Jans-Joachim Bremermann \n III. Alan Turing \n IV. John McCarthy \n V. Terence Sejnowski \n\n A - III – I – II – IV - V \n B - II – I – III – IV - V \n C - III – I – II – V - IV \n D - I – III – IV – V – II \n E - V – III – IV – I – II")

r2 = input("Digite a opção correta: \n")
if r2 == "C" or r2 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 3 \n No caso de um agente com aprendizagem, assinale o elemento que é responsável para sugestão de novas regras e ações que podem levar a novas experiências: \n\n A - Gerador de Problemas \n B - Elemento de Desempenhp \n C - Elemento de aprendizado \n D - Critico \n")

r3 = input("Digite a opção correta: \n")

if r3 == "A" or r3 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 4 \n Fábricas de automóveis ou eletrodomésticos utilizam em larga escala robôs para automatizar as linhas de produção, padronizando as atividades e minimizando o nível operacional de erros. Como exemplo, robôs de soldagem podem ser programados para executar soldas em pontos programados no espaço com altíssima precisão. Tais robôs são construídos na forma de braços robóticos, tais como o ilustrado na figura abaixo. \n\n Podemos classificar o robô de soldagem quanto às definições de IA como: \n\n Escolha, entre as alternativas a seguir, a alternativa correta. \n\n A - Pensar como ser humano \n B - Pensar racionalmente \n C - Agir como ser humando \n D - Agir racionalmente \n E - Pensar e agir como um ser humano \n")

r4 = input("Digite a opção correta: \n")
if r4 == "D" or r4 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Respota Incorreta")

print("\n\n Questão 5 \n Classifique as técnicas descritas a seguir, conforme as linhas de pesquisa de IA e depois marque a alternativa correta: \n\n (    ) Redes neurais artificiais \n (    ) Algoritmos genéticos \n (    ) Sistemas imunológicos artificiais \n (    ) Ontologias \n (    ) Sistemas especialistas \n (    ) Programação genética \n\n Linhas de Pesquisa em Inteligência Artificial.  \n\n I.Conexionista \n II.Simbólica \n III.Evolucionária \n\n Não se esqueça de marcar, entre as alternativas a seguir, aquela que contém a ordem certa de classificação \n\n A - I – II – I – III – III - II \n B - I – III – I – II – II - III \n C - II – III – II –I – I - III \n D - I – II – I – III – III - I \n E - I – II – I – III – I - I")

r5 = input("Digite a opção correta: \n")
if r5 == "B" or r5 == "b":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 6 \n Relacione as estruturas de agentes com as afirmações e depois marque a alternativa correta: \n\n 1.Agentes reativos simples \n 2.Agentes reativos baseados em modelos \n 3.Agentes baseados em objetivos \n 4.Agentes baseados em utilidade \n 5.Agentes com aprendizagem \n\n (  ) agentes que tem o conhecimento de como o mundo funciona \n (  ) dotados de mecanismos que possibilitam aprender na experiência com o ambiente. \n (  ) usam uma função que permite quantificar o mapeamento de um estado ou uma sequência de estados em um número que descreve o grau de “felicidade” alcançado. \n (  ) selecionam as ações a serem executadas com base na percepção atual, desconsiderando o histórico de percepções. \n (  ) além de saberem uma descrição do estado atual, é necessário ainda alguma informação que se relacione a situações ou cenários desejáveis. \n\n A - 3-5-4-1-2 \n B - 2-5-4-1-3 \n C - 3-4-1-2-5 \n D - 5-4-1-3-2 \n E - 1-2-3-4-5")

r6 = input("Digite a opção correta: \n")
if r6 == "B" or r6 == "b":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 7 \n Na análise do miniproblema do Jogo da Velha (em inglês, Tic-Tac-Toe), os estados representam qualquer combinação disposta sobre o tabuleiro de nove posições dos oponentes “X” e “O”, enquanto que o estado inicial seria o próprio tabuleiro vazio. Para a função sucessor, poderíamos definir da seguinte forma: \n\n A - Gera os estados válidos conforme a definição de uma função heurística. \n B - Gera os estados válidos a partir das jogadas de um único oponente, ou “X ou “O”. \n C - Gera os estados válidos a partir da colocação de um “X” ou um “O” de forma alternada e incremental. \n D - Gera todos os estados considerando jogadas em sequência de “X” ou “O”. \n E - Não gera qualquer estado e desconsidera todas as jogadas.")

r7 = input("Digite a opção correta: \n")
if r7 == "C" or r7 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 8 \n Considere o sistema especialista descrito abaixo para o comportamento de um robô, com um sensor de distância equipado na frente e movido com rodas, monitorando o nível de tensão da bateria e o movimento (se está movendo-se à frente ou está parado). Uma variável guarda a velocidade do robô, que pode ser 5 cm/s ou 10 cm/s. O robô pode se movimentar em um ambiente retangular com paredes. Este sistema é composto das seguintes regras: \n\n I.SE distância < 10cm E estado = movendo à frente ENTÃO pare o movimento \n II.SE distância < 10cm E estado = parado ENTÃO dê gire aleatoriamente \n III.SE distância >= 10cm E estado = parado ENTÃO mova-se para frente \n IV.SE nível da bateria < 2 Volts ENTÃO velocidade = 5 cm/s \n V.SE nível da bateria >= 2 Volts ENTÃO velocidade = 10 cm/s \n\n Supondo que o monitoramento dos sensores alimente os seguintes fatos ao sistema especialista: \n\n Distância = 12cm.\n\n Estado parado. \n\n Nível da bateria = 2,5 Volts. \n\n Velocidade = 10 cm/s. \n\n Assinale a alternativa que contém quais as regras que serão executadas: \n\n A- I, II e III \n B - II e IV \n C - III e IV \n D - III e V \n E - I e V")

r8 = input("Digite a opção correta: \n")
if r8 == "D" or r8 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 9 \n\n Com relação ao mapa rodoviário definido a seguir, responda ao que é solicitado.\n\n")

print("                                 98 \n")
print("                    Maringa --------------- Londrina\n")
print("                      /                        /     \\ \n")
print("                     /                        /       \\ \n")
print("                 91 /                        /         \\ 274\n")
print("                   /                        /           \\ \n")
print("            Campo Mourão                   /             \\ \n")
print("                /       \\           318  /               Ponta Grossa")
print("               /         \\              /               /          \\ \n")
print("              /           \\ 206        /               /            \\ 114\n")
print("             /             \\          /      163      /              \\ \n")
print("        195 /               Guarapuava ----------------                \\ \n")
print("           /               /     |    \\                                Curitiba \n")
print("          /               /      |     \\                              /        /\n")
print("         /               /       |      \\ 104                    154 /        /\n")
print("        /           332 /        |       \\                          /        / \n")
print("        \\             /         |        \\                        /        /  \n")
print("         \\           /          |         \\                      /        /  \n")
print("          --Cascavel------------ | ----\\     -----Irati-----------        /\n")
print("           /                 188 |      ------       |                    / \n")
print("          /                      |        414 \\     |                   / \n")
print("    140  /                       |             \\    | 123         241  / \n")
print("        /                        |              \\   |                 /  \n")
print("   Foz do Iguaçu-------------Pato Branco         \\  |                / \n")
print("                    337                           \\ |               / \n")
print("                                                     União da Vitoria\n\n")

print("Se considerarmos a origem do percurso a cidade de Maringá e o destino final a cidade de Curitiba, assinale “V” para verdadeiro ou “F” para falso nas afirmativas a seguir sobre a definição formal do problema: \n\n (     ) O estado inicial é descrito como Origem(Maringá). \n (     ) Um par da função sucessor do estado de origem seria <Destino(Guarapuava), Origem(Maringá)>. \n (     ) A função custo para ir da origem para a cidade de Maringá até Foz do Iguaçu pode retornar o custo mínimo de 426. \n (     ) O teste de objetivo compararia o estado atual ocupado pelo agente com Origem(Curitiba). \n (     ) O custo de passo relativo ao par <Destino(Irati), Origem(Guarapuava)> é de 154. \n\n A - V-F-V-V-F \n B - V-F-V-F-V \n C - V-V-F-V-V \n D - F-V-V-V-F \n E - V-F-F-F-V")

r9 = input("Digite a opção correta: \n")
if r9 == "A" or r9 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 10 \n Os sistemas especialistas podem ser classificados quanto às definições da IA no quadrante “agir como humanos”. Consiste assim numa ferramenta que possui a capacidade de entender o conhecimento sobre um problema específico e usar este conhecimento de maneira inteligente para sugerir alternativas de ação. Podemos enumerar assim os componentes de um SE: \n\n A - Base de conhecimento, quadro negro e neurônios.\n B - Base de conhecimento, mecanismo de inferência e o domínio. \n C - Base de conhecimento, quadro negro e mecanismo de inferência. \n D - Base de conhecimento, mecanismo de inferência e antecedentes. \n E - Base de conhecimento, antecedentes e mecanismo de inferência")

r10 = input("Digite a opção correta: \n")
if r10 == "C" or r10 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 11 \n Suponha o sistema abaixo em PROLOG para a descoberta de conhecimento sobre árvore genealógica. Existe a cláusula “progenitor” indicando que o indivíduo no primeiro argumento é progenitor do indivíduo no segundo argumento. Duas regras são criadas para inferir “irmão” e “primo”, a partir de “progenitor”. \n\n progenitor(José, Luiz). \n progenitor(José, Carlos). \n progenitor(Carlos, Maria). \n progenitor(Luiz,Sandro).\n\n irmão(X,Y) :- progenitor(Z,X),progenitor(Z,Y). \n primo(X,Y) :- progenitor(Z,X),progenitor(W,Y), irmão(Z,W). \n\n Após a execução deste programa no PROLOG, assinale as consultas a seguir com “V” para verdadeira ou “F” para falsa: \n\n (     ) irmão(Maria,Sandro). \n (     ) primo(Maria, Sandro). \n (     ) progenitor(José, Y), com Y = Luiz, Y = Carlos. \n (     ) primo(Carlos, Luiz). \n (     ) progenitor(Maria,Y). \n\n A - V-V-V-F-F \n B - F-V-V-F-F \n C - F-V-V-V-F \n  D - F-V-V-F-V \n E - F-F-F-V-V")

r11 = input("Digite a opção correta: \n")
if r11 == "B" or r11 == "b":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 12 \n No caso de um AG utilizar como alfabeto a numeração hexadecimal com 10 genes, qual o cromossomo abaixo seria um exemplo de representação de um indivíduo: \n\n A - 11AF09921B \n B - 11ABFH4550 \n C - FE0033LH99 \n D - A218FF3AAG \n E - AA012345KJ")

r12 = input("Digite a opção correta: \n")
if r12 == "A" or r12 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 13 \n Relacione as afirmações com as estratégias de busca a seguir e depois marque a alternativa com a sequência correta:\n I. Busca em amplitude \n II. Busca de custo uniforme \n III. Busca em profundidade \n IV. Busca em profundidade limitada \n V. Busca em aprofundamento iterativo \n\n (     ) Caso se tenha algum conhecimento sobre o problema, pode-se restringir a busca a um nível limite de expansão dos nós. \n (     ) Combina os benefícios da busca em profundidade e da busca em extensão. \n (     ) O nó raiz é expandido, depois os nós sucessores do nó raiz, depois os sucessores dos sucessores e assim por diante. \n (     ) Variante da busca em amplitude por considerar a expansão do nó que possui o custo mais baixo. \n (     ) Pode ser implementada por um algoritmo de busca em árvore com uma estrutura de pilha. \n\n A - III-IV-V-II-I \n B - V-IV-I-III-II \n C - IV-V-I-II-III \n D - IV-V-III-II-I \n E - I-II-III-V-IV")

r13 = input("Digite a opção correta: \n")
if r13 == "C" or r13 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 14 \n Considere o problema do puzzle de 8 peças, com os estados descritos abaixo: \n")

print("  Estado Atual: \n")
print("-------------------\n")
print("|  3  |  6  |  2  |\n")
print("|  4  |  5  |  7  |\n")
print("|  8  |  1  |     |\n")
print("-------------------\n")

print("  Estado Final: \n")
print("-------------------\n")
print("|  1  |  2  |  3  |\n")
print("|  8  |     |  4  |\n")
print("|  7  |  6  |  5  |\n")
print("-------------------\n")

print("Se utilizarmos a função heuristica da distância de Manhattan considerando o estado atual em relação ao estado final, temos que a distância será de: \n\n A - 14 \n B - 15 \n C - 16 \n D - 17 \n E - 18")

r14 = input("Digite a opção correta: \n")
if r14 == "C" or r14 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 15 \n Examine o quadro a seguir, contendo a representação do cromossomo e o resultado da avaliação pela função objetivo durante uma geração qualquer, em um processo de maximização por AG, e responda às questões: \n Cromossomo              Função Objetivo\n 001011            5\n 111001            -3\n 011011            0\n 001010            2\n 111110            -4\n 011111            -1\n Assinale a alternativa que conterá, após a reordenação, 33% da população a qual será considerada para a próxima geração: \n\n A - 001011 (5) e 001010 (2) \n B - 111110 (-4) e 111001 (-3) \n C - 001011 (5) e 111110 (-4) \n D - 011011 (2) e 001010 (0) \n E - 011011 (3) e 001000 (4)")

r15 = input("Digite a opção correta: \n")
if r15 == "A" or r15 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 16 \n Assinale as afirmações abaixo com “V” para verdadeiro ou “F” para falso e depois marque a alternativa correta: \n\n (     ) Sistema Especialista consiste numa técnica da IA desenvolvida para resolver problemas em um determinado domínio, cujo conhecimento utilizado é obtido de pessoas que são especialistas naquele domínio \n (     ) DENDRAL foi um sistema desenvolvido em 1965 contendo redes neurais artificiais para resolver problemas relacionados à química orgânica. \n (     ) MYCIN foi um sistema especialista desenvolvido para resolver o problema do diagnóstico e tratamento de doenças infecciosas do sangue através de um conjunto de 450 regras. \n (     ) A fase da implementação do Sistema Especialista é considerada a parte mais sensível no desenvolvimento de um SE, muitas vezes o gargalo do processo \n (     ) Nas regras determinísticas, quando a premissa for verdadeira, sempre acontecerá a ação da conclusão da regra. \n\n A - V-F-V-F-V \n B - V-F-V-F-F \n C - F-F-V-F-V \n D - V-V-F-F-V")

r16 = input("Digite a opção correta")
if r16 == "A" or r16 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 17 \n Considerando uma busca em extensão para  um problema que tenha expansão b=6 nós com a solução no nível d=4, podemos afirmar que o número de nós gerados será de: \n\n A - 9325 \n B - 9331 \n C - 1561 \n D - 1555 \n E - 8766")

r17 = input("Digite a opção correta: \n")
if r17 == "A" or r17 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 18 \n Na execução de um AG, considere os seguintes cromossomos: \n\n Cromossomo 1: 110001001\n Cromossomo 2: 101111101\n\n Considerando o ponto de corte após o gene de número 5, como seriam os descendentes destes cromossomos em caso de crossover? \n\n A - 110111101 e 101001001 \n B - 110001101 e 101111001 \n C - 110000101 e 101110001 \n D - 110011101 e 101101001 \n E - 101101001 e 110011101")

r18 = input("Digite a opção correta: \n")
if r18 == "B" or r18 == "b":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 19 \n A arquitetura com camadas ocultas requer algoritmos de aprendizagem que contemplem a atualização dos pesos relacionados às camadas internas. O processo de ativação acontece primeiramente nas camadas ocultas para depois chegar até a camada de saída. A retroalimentação do erro também é feita nos pesos que conectam a(s) camada(s) oculta(s). O algoritmo mais comum utilizado para o treinamento de um perceptron multicamada é: \n\n A - Algoritmo de campo local induzido. \n B - Algoritmo de sinal funcional. \n C - Algoritmo de erro contínuo. \n D - Algoritmo de retropropagação \n E - Algoritmo de biopropagação induzida.")

r19 = input("Digite a opção correta: \n")
if r19 == "D" or r19 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 20 \n A aplicação de uma RNA a um problema qualquer com uma grande quantidade de sinais de entrada exige que seja feita a normalização para padronizar o cálculo internamente à RNA. Considerando a normalização de um sinal de entrada para um neurônio relativo à que tenha o valor mínimo de 100 (zero), o sinal máximo de 10000 e um valor qualquer de entrada de 3450, o valor normalizado para esta entrada específica (com duas casas decimais) será de: \n\n A - 0,56 \n B - 0,38 \n C - 0,34 \n D - 3,45 \n E - 1,00")

r20 = input("Digite a opção correta: \n")
if r20 == "C" or r20 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print(" \n\n Questão 21 \n Seja uma rede neural artificial com camada de entrada com dimensão dois que recebe dados (x1, x2). Essa rede aplica pesos w1 em x1, w2 em x2 e adiciona um viés w0. A função de ativação é dada pela função sinal s(z) = +1, se z = 0, e s(z) = -1, se z < 0. Essa rede não tem nenhuma camada oculta e será utilizada para classificar observações em y = +1 ou y = -1 \n\n Para pesos w1 = 2, w2 = 3 e viés w0 = 1, a região de classificação é uma reta que passa nos pontos: \n\n A - (x1 = -1/2, x2 = 0) e (x1 = 0, x2 = -1/3) e classifica como -1 os pontos acima da reta; \n B - (x1 = 1/2, x2 = 0) e (x1 = 0, x2 = 1/3) e classifica como +1 os pontos acima da reta; \n C - (x1 = -1/2, x2 = 0) e (x1 = 0, x2 = -1/3) e classifica como +1 os pontos acima da reta; \n D - (x1 = -1/2, x2 = 0) e (x1 = 0, x2 = 1/3) e classifica como +1 os pontos acima da reta; \n E - (x1 = 1/2, x2 = 0) e (x1 = 0, x2 = -1/3) e classifica como -1 os pontos acima da reta.")

r21 = input("Digite a opção correta: \n")
if r21 == "C" or r21 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 22 \n Considere o texto abaixo sobre o agente com aprendizagem representado na figura: \n\n Um carro autônomo pode dirigir numa estrada de acordo com o elemente de desempenho embutido em sua programação, numa velocidade definida e em uma faixa á esquerda.\n 1. O crítico recebe informações do mundo e vai repassando-as ao elemente de aprendizado. \n 2.Caso algum carro que está posicionado logo atrás esteja buzinando, o elemento de crítico pode formular uma regra definindo que este cenário de direção em uma faixa central ou á esquerda seja uma situação ruim. \n 3.O elemente de desempenho é modificado, graças ao elemento crítico, para fazer com que o carro autônomo siga na faixa da direita. \n\n Assinale a alternativa correta:\n\n A - O texto está correto porque o elemento de aprendizagem depende do elemento de desempenho para que as modificações sejam definitivas. \n B - O texto está correto porque apesar de o elemento de aprendizagem depender do elemento de desempenho para que as modificações sejam definitivas é possível se fazer estimativas estocásticas. \n C - O texto está correto porque o elemento de aprendizagem depende do elemento de desempenho o qual recebe informações dos sensores.\n D - O texto está correto porque o elemento de aprendizagem e não o elemento crítico formula regras que alteram o elemento de desempenho. \n E - O texto está incorreto porque o elemento de aprendizagem e não o elemento crítico formula regras que alteram o elemento de desempenho.")

r22 = input("Digite a opção correta: \n")
if r22 == "E" or r22 == "e":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 23 \n Quais as principais vantagens e desvantagens de RNA deste modelo se comparado a outros modelos de aprendizado de máquina (como sistemas simbolicos, por exemplo)? \n\n A - RNAs podem aprender com os erros dos sistemas simbolicos, uma vez que nem todo problema é simbolicamente distinto de um neurônio. \n B - Sistemas simbolicos exigem o entendimento ou modelagem do problema ao passo que técnicas conexionistas necessitam apenas de um conjunto de dados válidos para permitir o treinamento. \n C - Sistemas simbolicos não exigem o entendimento nem a modelagem do problema, mas tecnicas conexionistas necessitam de um conjunto de conhecimento, normalmente obtido de um especialista para permitir o treinamento. \n D - RNAs podem aprender com os erros mas dependem de sistemas simbolicos, uma vez que todo problema é simbolicamente distinto. \n E - Nenhuma resposta é verdadeira.")

r23 = input("Digite a opção correta: \n")
if r23 == "B" or r23 == "b":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 24 \n O que se entende por aprendizado em Redes Neurais Artificais? \n\n A - Aprendizado é o processo pelo qual o erro de saída é reinserido na entrada por uma realimentação entre estes neurônios. \n B - Aprendizado é o processo pelo qual busca-se treinar um RNA para que ganhe a capacidade de predição. O que define a capacidade de predição é o treinamento da RNA e não sua arquitetura, embora exista uma arquitetura mínima necessária para que a rede possa operar. \n C - Aprendizado é o processo pelo qual busca-se treinar uma RNA para que ganhe a capacidade de corrigir erros. O que define a capacidade de correção é o treinamento da RNA e não sua arquitetura, embora exista uma arquitetura mínima necessária para que a rede possa operar. \n  D - Aprendizado é o processo pelo qual busca-se treinar uma RNA para que ganhe a capacidade de generalização, mas o que define esta capacidade é a sua arquitetura, embora exista um treinamento mínimo necessário para que a rede possa operar.")

r24 = input("Digite a opção correta: \n")
if r24 == "B" or r24 == "b":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 25 \n Um neurônio recebe 4 entradas cujos valores são iguais a 10, -20, 4 e -2. Os respectivos pesos sinápticos são 0.8, 0.2, -1.0 e -0.9. Calcule a saída do neurônio supondo que o neurônio é baseado na função de ativação limiar (degrau) com níveis de saída +1 ou -1. \n\n A - Para bias = 0 a saída será -1.8 \n B - Para bias = 0 a saída será nula pois qualquer número multiplicado por zero é zero. \n C - Para bias = -1 a saída será 1. \n D - Para bias = 0 a saída será -1 \n E - Para bias = -1 a saída será 17,8")

r25 = input("Digite a opção correta: \n ")
if r25 == "C" or r25 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 26 \n Segundo RUSSELL e NORVIG, os agentes podem ser classificados em quatro tipos: Agentes reativos simples; Agentes reativos baseados em modelo; Agentes baseados em objetivos; Agentes baseados na utilidade. \n\n Considerando o texto acima, escolha a alternativa que identifique quais das afirmativas abaixo NÃO estão corretas: \n\n I.Os agentes reativos simples selecionam as ações a serem executadas com base na percepção atual, desconsiderando o historico de percepções. \n II. Um agente que tem o conhecimento de como o mundo funciona, possui o que se denomina de modelo do mundo. Assim, o agente que utiliza este modelo é chamado de agente reativo baseado em modelo. \n III. Uma tomada de decisão baseada em objetivos é diferente da utilização de regras se-então, por envolver uma consideração sobre o futuro \n IV.Uma especificação de uma função de utilidade permite a tomada de decisões racionais em casos em que a decisão por objetivos é inadequada. \n\n A - I e II são afirmações falsas. \n B - III e IV são afirmações falsas. \n C - II e III são afirmações falsas. \n D - I e IV são afirmações falsas. \n E - Não há alternativa falsa. Todas são verdadeiras.")

r26 = input("Digite a opção correta: \n")
if r26 == "E" or r26 == "e":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 27 \n Marque apenas as abordagens conexionistas das tecnicas listadas abaixo \n\n I) Sistema Especialista \n II) Rede Neural \n III) Lógica Difusa (Fuzzy) \n IV) Algoritmos Genéticos \n V) SVM \n VI) RBF \n\n A - São abordagens conexionistas somente II, V e VI \n B - São abordagens conexionistas somente I, II e IV \n C - São abordagens conexionistas somente I,III e V \n D - São abordagens conexionistas somente II e III \n E - Não há abordagens conexionistas nas tecnicas listadas")

r27 = input("Digite a opção correta: \n")
if r27 == "A" or r27 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 28 \n Leia o texto abaixo: \n\n Um algoritmo de busca recebe na sua entrada um problema e apresenta na sua saída uma solução, descrita sob a forma de uma sequência de ações definidas. A partir da obtenção da solução, as ações recomendadas por ela são colocadas em execução. O algoritmo para a resolução de problemas simples pode ser então descrito nos seguintes passos: formulação do objetivo e do problema; busca de uma sequencia de ações que resolvem o problema; execução das ações uma por uma. Quando a sequencia se completa, o agente formula outro objetivo e então recomeça. \n\n Considerando o afirmado pelo texto e o exposto em aula, é correto afirmar: \n\n A - O agente, na execução da sequencia, não leva em contas as percepções, baseia-se na suposição de que a solução que encontrou na busca sempre irá funcionar. \n B - O agente executa a sequencia e recomeça, a interrupção dependerá das percepções do meio. \n C - O agente utiliza sensores e atuadores para seguir ou não a execução da sequencia. \n D - A função sucessor identifica as ações invalidas em determinado estado.")

r28 = input("Digita a opção correta: \n")
if r28 == "A" or r28 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 29 \n Dois são os tipos de estrategia de busca, no que se refere ao uso do conhecimento previo. A busca cega alija-se do uso de informações na consecução da busca. Por outro lado, na busca informada, com uso de heuristicas, podemos aplicar o conhecimento relativo ao problema no algoritmo de busca. \n\n No que se refere a estrategias de busca informada é correto afirmar: \n\n A - A definição de uma função heurística irá depender da natureza do problema de busca. A heuristica nunca deve superestimar o custo para se alcançar o objetivo. \n B - A estrategia informada de busca de custo uniforme difere da busca em extensão por considerar a expansão do no com o custo mais baixo. \n C - A busca informada gulosa é uma estrategia que tenta expandir o no mais proximo a meta, mas não utiliza informações heuristicas para otimizar o algoritmo. \n D - As estrategias de busca com informação dividem-se em: Busca em extensão ou amplitude; Busca de custo uniforme; Busca em profundidade; Busca em profundidade limitada; Busca de aprofundamento iterativo; Busca bidirecional; Busca em Extensão ou Amplitude.")

r29 = input("Digite a opção correta: \n")
if r29 == "A" or r29 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 30 \n O perceptron pode executar as funções logicas AND, OR e NOT, mas não resolve o OU-EXCLUSIVO (XOR) porque: \n\n A - O circuito logico da porta XOR exige mais eletronica e por este motivo mais neuronios deverão ser empregados. \n B - O plano de saída do neuronio é bidimensional e um perceptron é capaz de dividi-lo segundo uma função limear, ou seja, +1 e -1, mas a porta XOR precisa de 0 ou 1. \n C - Um perceptron pode dividir o espaço de saída de formar linear, ou seja, por um plano ou reta. Se plotarmos as saídas desejadas segundo as entradas, respeitadas as tabelas-verdade de cada função logica, veremos que apenas a porta XOR e OR permitem esta execução. \n D - Um perceptron pode dividir o espaço de saída de forma linear, ou seja, por um plano ou reta. Se plotarmos as saídas desejadas segundo as entradas, respeitadas as tabelas-verdade de cada função logica, veremos que apenas na porta XOR não é possível dividir linearmente as saídas.")

r30 = input("Digite a opção correta: \n")
if r30 == "D" or r30 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 31 \n Um neuronio recebe 4 entradas cujos valores são iguais a 10, -20, 4 e -2. Os respectivos pesos sinapticos são 0.8, 0.2, -1.0 e -0.9. Calcule a saída do neuronio supondo que o neuronio é linear. \n\n A - Para bias = 0 a saída será -1,8. \n B - Para bias = 0 a saída será nula pois qualquer numero multiplicado por zero é zero \n C - Para bias = -1 a saída será 1.8. \n D - Para bias = 0 a saída será 1.8 \n E - Para bias = -1 a saída será 17.8")

r31 = input("Digite a opção correta: \n")
if r31 == "D" or r31 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 32 \n Dada a tabela tutor e as saídas correspondentes da IA (B,A,A,B,A,C) geradas pelo tratamento \n\n")

print(" ______ _______ ________\n")
print("|   X  |   Y   |   Tutor|\n")
print("|   1  |   9   |     B  |\n")
print("|   5  |   7   |     A  |\n")
print("|   1  |   7   |     A  |\n")
print("|   7  |   1   |     A  |\n")
print("|   3  |   2   |     B  |\n")
print("|   2  |   10  |     C  |\n")
print(" ______ _______ ________\n")

print("\n\n Marque as alternativas corretas sobre esse sistema. \n\n A - Classe B é erroneamente classificada na linha 1 da tabela; \n B - Classe A é erroneamente classificada na linha 2 da tabela; \n C - Classe A é erroneamente classificada na linha 3 da tabela; \n D - Classe A é erroneamente classificada na linha 4 da tabela;")

r32 = input("Digite a opção correta: \n")
if r32 == "D" or r32 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 33 \n Um agente inteligente tem definido o seu grau de inteligência a partir da sua racionalidade, que depende de quatro fatores: \n\n A - Sequência de percepções, ações, conhecimento previo e medida de desempenho \n B - Sequencia de percepções, medida de desempenho, função do agente e programa do agente \n C - Sequencia de percepções, ações, programa do agente e função do agente \n D - Sequencia de percepções, ações, ambiente da tarefa e arquitetura \n E - Sequencia de percepções, medida de desempenho, ações, programa do agente")

r33 = input("Digite a opção correta: \n")
if r33 == "A" or r33 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 34 \n Marque as alternativas a seguir com  “V” para verdadeiro e “F” para falso e depois assinale a alte rnativa correta com relação  aos agentes inteligentes: \n\n (     ) Os sensores permitem que o agente  perceba o que  acontece no ambiente onde  ele (o agente) está inserido. \n (     ) Hoje em dia os robôs são constr uídos tendo atuadores tais como câmeras e  dispositivos de captação de infravermelho e som \n (     ) As percepções são processadas pelo agente par a depois se trans formarem em  ações sobre o ambiente por meio de at uadores \n (     ) A sequência de percepções perm ite que se mapeie as ações com a memór ia do agente. \n (     ) Um programa de agente é um a implementação concreta de uma função do  agente enquanto uma função abstrata. \n\n A - V-V-V-F-V \n B - V-F-F-F-V \n C - V-F-V-F-V \n D - F-F-V-F-F \n E - F-F-F-F-V")

r34 = input("Digite a opção correta: \n")
if r34 == "C" or r34 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 35 \n Cientista cognitivo, considerado co-fundador da area de IA, desenvolveu uma teoria da mente como uma sociedade de agentes, inteligencia surge como um produto da interação de partes não-inteligentes. Estamos falando de: \n\n A - Marvin Minsky \n B - Nathaniel Rochester \n C - Claude Shannon \n D - Norbert Wiener \n E - Albert Einstein")

r35 = input("Digite a opção correta")
if r35 == "A" or r35 == "a":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 36 \n Assinale com V ou F as alternativas a seguir e depois marque a alternativa correta: \n\n (  )Nem sempre o metodo da força bruta para calcular todas as rotas no problema de roteirizaçao pode ser uma alternativa de abordagem \n (  )Problemas do mundo real são aqueles problemas abstraidos do mundo real que tendem a ter uma descriçao exata e concisa \n (  )Uma solução otima é aquela que apresenta o menor custo dentre todas as soluções possiveis. \n (  )Uma função sucessor pode gerar arvores de busca a partir do estado inicial de um certo problema. \n (  )Enquanto que o puzzle de 24 peças (5x5) pode ser resolvido com facilidade, o de 8 peças (3x3) ainda é bastante dificil de resolver de forma otima. \n\n A - V-F-V-F-F \n B - V-F-F-V-F \n C - F-F-V-V-F \n D - V-V-V-F-F \n E - V-F-V-V-F")

r36 = input("Digite a opção correta: \n")
if r36 == "E" or r36 == "e":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 37 \n Podemos conceituar uma rede neural artificial como um processador maciçamente e paralelamente distribuido constituido de unidades de processamento simples, que tem a propensao natural para armazenar conhecimento experiemental e torna-lo disponivel para o uso. São propiedades de uma rede neural artificial: \n\n A - Não-linearidade, mapeamento entrada-saída, seleção, mutação e resposta a evidências \n B - Não-linearidade, mapeamento entrada-saída, mecanismo de inferencia e adaptabilidade \n C - Não-linearidade, mapeamento entrada-saída, adaptabilidade e resposta a evidencias \n D - Seleção, mutação, crossover, população e fitness")

r37 = input("Digite a opção correta: \n")
if r37 == "C" or r37 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 38 \n Assinale as afirmações a seguir com V para verdadeiro ou F para falso e depois marque a alternativa correta: \n\n (  )Num sistema PROLOG, o componente de controle estabelece como a solução pode ser obtida. \n (  )Num sistema PROLOG, o componente logico estabelece como a solução pode ser obtida. \n (  ) Uma clausula pode ser um fato, regra ou consulta. \n (  ) filho(X,Y) :- pai (Y,X) é um fato \n (  ) A programação procedural é o paradigma fundamental da programação em logica. \n\n A - F-V-V-F-F \n B - V-F-V-F-V \n C - V-F-V-V-F \n D - V-F-V-F-F \n E - V-V-V-V-F")

r38 = input("Digite a opção correta: \n")
if r38 == "D" or r38 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 39 \n Um perceptron simples, com duas entradas e uma saida para classificar +1 ou -1, sem camada oculta, possui os valores de pesos e a tabela com as 4 (quatro) amostras descritos a seguir. Com base no preenchimento da tabela de amostras de acordo com as formulas o perceptron simples, marque as afirmações com V ou F e depois assinale a alternativa correta. \n\n")

print(" w1                 w2                   w0\n")
print("0.45               0.10                  -1\n\n")

print("Amostra              x1      x2      d       f       o       e       e²\n")
print("1                    8       3                       1                 \n")
print("2                    1       3                      -1                 \n")
print("3                    4       2                      -1                 \n")
print("4                    1       1                       1                 \n")

print("\n\n (  )O perceptron classifica erroneamente as amostras 2 e 3. \n (  )O perceptron tem o somatorio do erro quadratico igual a 8. \n (  )As amostras 1 e 2 são classificadas corretamente. \n (  )Para a amostra 2, d = 2,9. \n (  )Para a amostra 3, d = 1. \n\n A - V-V-V-F-F \n B - F-F-F-V-V \n C - F-V-V-F-V \n D - V-V-F-F-V \n E - V-V-V-F-V")

r39 = input("Digite a opção correta: \n")
if r39 == "C" or r39 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 40 \n Relacione os conceitos de AG com as afirmações a seguir e depois marque a alternativa correta: \n\n I.Seleção \n II.Crossover \n III.Mutação \n IV.Gene \n V.Fitness \n\n (  )Compõe um cromossomo, referindo-se geralmente a um bit. \n (  )Altera levemente a caracteristica de um individuo. \n (  )Uma medida de quão boa é a adaptação ou adequação de um individuo. \n (  )Ocorre pela mistura de dois (ou mais) individuos. \n (  )Analogo a sobrevivencia dos mais adaptados no mundo natural. \n\n A - V-III-IV-I-II \n B - IV-V-II-I-III \n C - III-V-II-IV-I \n D - IV-III-V-II-I")

r40 = input("Digite a opção correta: \n")
if r40 == "D" or r40 == "d":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("\n\n Questão 41 \n Assinale as afirmações sobre Algoritmos Geneticos (AG) a seguir com V para verdadeiro ou F para falso e depois marque a alternativa correta: \n\n (  ) Um AG é considerado um algoritmo de busca em feixe estocastica, onde os estados sucessores são criados a partir da combinação de dois (ou mais) estados pais. \n (  )AG usa estruturas de neuronios para executar a sua busca por um estado otimo. \n (  )Um AG contem regras com premissas e consequentes para executar o seu algoritmo. \n (  )Os AG perfazem uma busca cega, sendo a unica exigencia o conhecimento da função objetivo de cada individuo. \n (  )Um AG procura uma solução dentro de um espaço para um problema de otimização. \n\n A - V-V-F-F-V \n B - V-F-V-V-F \n C - V-F-F-V-F \n D - F-F-F-V-F \n E - V-V-V-F-F")

r41 = input("Digite a opção correta: \n")
if r41 == "C" or r41 == "c":
    print("Resposta Correta")
    nota += 1
else:
    print("Resposta Incorreta")

print("Sua nota é", nota)
