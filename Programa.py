# De princípio não é necessário declarar bibliotecas pois várias funções vem embutidas por padrão;
# De início também algumas constantes vem embutidas;
# Da mesma forma inicialmente não é necessária declarar escopo ou função global;
# Trata - se de linguagem interpretada, ou seja, um programa interpretador executa seu código fonte;
# A instrução não passa diretamente pelo SO ou processador;
# Semântica/ tipagem é dinâmica em python, ou seja, não é necessário declarar o tipo da variável;
# O próprio interpretador aloca a variável no tipo que for necessário, sem precisar de declaração;
# Mesmo assim, ainda é possível declarar o tipo da variável nas versões mais recentes;
# Para realizar comentários há duas possibilidades: sharp para comentar apenas uma linha...
# Ou três aspas simples ou duplas em um intervalos para múltiplas linhas (É preferível aspas duplas). Ex:

import math
# Neste caso, declarei a biblioteca math porque ela não veio de forma prévia declarada implicitamente...
# Será necessária para executar função de raiz quadrada, portanto é feita essa declaração explicitamente...
# A biblioteca só toma cor quando uma função ao longo do código faz seu uso.

"""
Comentário em múltiplas linhas
Ideal para isolar trechos grandes do código
É preverível o uso de aspas duplas para comentário de múltiplas linhas
Pois é possível utilizar aspas simples, porém o interpretador emite avisos que outra sintaxe é recomendada
"""

# Aula 229 - Variáveis e tipos de dados
idade: int
# Nesse caso eu mesmo apontei que o tipo dessa variável é inteiro
salario: float
# Novamente, apontei previamente que o tipo dessa variável é float
altura: float
# É possível também colocar ambas as variáveis na mesma linha usando ponto e vírgula
# Ex: salario: float; altura: float = Não é comum o uso dessa sintaxe, porém é possível
genero: str
# Nesse caso o gênero é um caractere (char) mas é usada a mesma variável str
nome: str
# str aqui alocará um texto

idade = 20
# Se previamente eu não declarasse que essa variável seria um inteiro, nesse momento o próprio interpretador atribuiria
salario = 5800.5
altura = 1.63
genero = 'F'
# Pode usar aspas simples ou duplas para declaração de char ou string
nome = "Maria Silva"
cpf = 12345678901
# Nesse caso já criei a variável e atribuí o valor, sem antes indicar o tipo
# Sendo assim, o próprio interpretador já aloca o tipo de acordo com a necessidade, nesse caso um int

print(f"IDADE = {idade}")
# Interpolação de valores acima
# Esta interpolação permite que uma variável seja declarada dentro da área de string
# Sintaxe = print(f"TEXTO {variável}")

print(f"SALARIO = {salario:.2f}")
# Parâmetro : .2f garante que esta variável seja formatada com duas casas decimais
print(f"ALTURA = {altura:.2f}")
print(f"GENERO = {genero}")
# print é comando para impressão de dados
print(f"NOME = {nome}")
print(f"CPF = {cpf} \n")
# \n executa quebra de linha

# Aula 230 - Operadores

# Operador mod - Resto da divisão
x = 5
y = 2

z = 5 % 2
# Resto da divisão de 5 por 2, portanto 1

print(z)

# Potenciação
x1 = 5
y1 = 2

z1 = 5 ** 2
# Comando de potenciação, ou seja 5 elevado ao quadrado (5 X 5 = 25)

print(z1)

# Divisão geral
x2 = 5
y2 = 2

z2 = 5/2
# Divisão geral, nesse caso 2.5

print(z2)

# Divisão inteira
x3 = 5
y3 = 2

z3 = 5 // 2
# // garante que só será exibido a parte inteira dessa divisão, nesse caso 2

print(z3)

# Operadores lógicos (and, or, not)
# Operadores comparativos:
# < Menor
# > Maior
# <= Menor ou igual
# >= Maior ou igual
# == Igual
# != ou <> Diferente

# Aula 231 - Saída de dados

print("\nBom dia/ ", end='')
# Não quebra a linha automaticamente quando se usa end='', ou seja, nesse caso Bom dia e Boa noite são impressos juntos
print("Boa noite")

# Placeholder - Não é usual e nem recomendado, porém segue exemplo:
x4 = "Maria"
y4 = 19

print("%s tem %d anos" % (x4, y4))
# Dentro do print você indica quais variáveis serão alocados dentro dessas aspas, nesse caso string (%s) e inteiro (%d)
# Logo apos usando % (variável1, variável2, etc) você vai apontando as variáveis na ordem que serão alocadas no texto
# É possível essa utilização para %d(Int), %f(Float) e %s(String)

x5: int
y5: int
# Nesse caso, previamente estou indicando que x5 e y5 são inteiros

x5 = 10
y5 = 20

print(x5)
print(y5)

x6: float
x6 = 2.3456
print("{:f}".format(x6))
# Esta formatação indica um ponto flutuante através da expressão f dentro do texto
# Sintaxe: print("{:tipo}".format(variável))
# Ou seja, assim a variável indicada no fim substituirá o tipo dentro do texto

# Por padrão são impressas 6 casas decimais, é necessária formatar para exibir menos
print("{:.2f}".format(x6))
# Para imprimir com uma quantidade específica de casas é necessário indicar o .quantidade entre o : e o tipo

# Interpolação
idade1 = 32
salario1 = 4560.9
nome1 = 'Maria Silva'
sexo1 = "F"
# Como exemplo declarei uma string com aspas simples e um char com aspas duplas para mostrar que tanto faz em Python...
# Ambos são textos para a linguagem, independente da quantidade que ocupa na memória.

print(f"A funcionaria {nome1}, sexo {sexo1}, ganha {salario1:.2f} e tem {idade1} anos.")
# Ou seja, usando interpolação através de um f antes do " " é possível alocar as variáveis no decorrer do texto
# Esta interpolação torna mais prático o texto
# :.2f garante a exibição de duas casas decimais no salário

print("A funcionária {:s}, sexo {:s}, ganha {:.2f} e tem {:d} anos.\n".format(nome1, sexo1, salario1, idade1))
# Esta declaração primeiro aloca espaços no texto com os tipos de variáveis a serem ali colocados
# Posteriormente com .format(var1, var2, etc) é que as variáveis são alocadas na ordem de exibição
# É utilizado .2 entre : e f para formatar salário com duas casas decimais

# Aula 232 - Processamento de dados e casting

x7: int; y7: int
x7 = 5
y7 = 2 * x7
print(x7)
print(y7)

x8: int
y8: float
x8 = 5
y8 = 2 * x8
print(x8)
print(y8)

# Cálculo da área do trapézio
b1: float
b2: float
h: float
area: float

b1 = 6.0
b2 = 8.0
h = 5.0
area = (b1 + b2) / 2.0 * h
print(f"AREA DO TRAPÉZIO = {area}")

a3: int
b3: int
resultado: int
a3 = 5
b3 = 2
resultado = a3 / b3
print(resultado)
# Mesmo eu tendo declarado que resultado seria inteiro, o interpretador ignorou esse fato e decidiu atribuir float...
# Pois ele viu que havia a necessidade de mostrar a casa decimal dessa divisão (2.5)
# Ou seja, ele processa o que ele acha que é o correto
# Para forçar que o resultado seja inteiro é necessário usar // conforme exemplo:
resultado = a3 // b3
print(resultado)

a4: float
b4: int

a4 = 5.2
b4 = a4
print(b4)
# Mesmo eu declarando que b4 deveria ser int, devido a b4 receber a atribuição de outra variável do tipo float...
# ele julga necessário que b4 seja exibido como 5.2 (float).
# Para forçar que seja exibido como int é necessário indicar expressamente com o tipo antes da variável, ex:

b4 = int(a4)
print(b4)

# Aula 233 - Entrada de dados

# Input lê texto, para ler int ou float é necessário indicar entre parênteses
salario2: float
salario3: float
nome2: str
nome3: str
idade2: int
sexo2: str

nome2 = input("\nNome da primeira pessoa: ")
# Esta é a sintaxe, ao usar este comando ele espera que eu digite o texto, e o que for digitado é armazenado
salario2 = float(input("Salário da primeira pessoa: "))
# Este comando permite que o input leia dados de números (int ou float)
# Sintaxe: variavel = float(input("Texto a ser digitado: "))

nome3 = input("Nome da segunda pessoa: ")
salario3 = float(input("Salário da segunda pessoa: "))

idade2 = int(input("Digite uma idade: "))
sexo2 = input("Digite um sexo (F/M): ")

print(f"\nNOME 1: {nome2}")
print(f"SALARIO 1: {salario2:.2f}")
print(f"NOME 2: {nome3}")
print(f"SALARIO 2: {salario3:.2f}")
# .2f para formatar com duas casas decimais
print(f"IDADE: {idade2}")
print(f"SEXO: {sexo2}")

# Aula 234 - Debugger

x9 = int(input("\nDigite X: "))
y9 = 2 * x9
# Breakpoint a partir da próxima linha para teste:
print(f"Valor de y = {y9}")
# Acionado através de Run -> Toggle Breakpoint, clique na lateral da linha ou Ctrl + F8.
z = int(input("Digite z: "))
print(f"Valor de z = {z}")
w = 5 + z
print(f"Valor de w = {w}")

# Aula 235 - Estutura condicional

# Atenção a identificação após o if, ela que define o escopo
x10 = 10

print("\nBom dia")
if x10 < 10:
    print("Boa tarde")
    # Ao usar o comando if em uma linha e passar o parâmetro, ao quebrar a linha ele mesmo gera essa identação que...
    # indica novo escopo, esse escopo é onde serão passadas as condições.
    # Sintaxe: if parâmetro1 sinal parâmetro2 dois pontos
    # Como o parâmetro não foi correspondido ele pula a condição, imprimindo apenas Bom dia e Boa noite.
print("Boa noite")

hora: int

hora = int(input("Digite uma hora do dia: "))

# Se:
if hora < 12:
    print("Bom dia")
# elif (Encadeamento de condições)
# Senão, se:
elif hora < 18:
    print("Boa tarde")
# Senão:
else:
    print("Boa noite")

# Aula 236 - Estrutura repetitiva while

x11: int
soma: int

soma = 0
# Soma acumulada começando com zero
x11 = int(input("Digite o primeiro número: "))

while x11 != 0:
    # != representa diferente
    soma = soma + x11
    x11 = int(input("Digite outro número: "))

print("SOMA = ", soma)
# Impressão de forma concatenada

# Aula 237 - Estrutura repetitiva for

for i in range(0, 5):
    print(i)
    # Este paramêtro diz que a variável i será impressa na faixa de 0 a 5 pulando de um em um número...
    # No caso é impressão 0, 1, 2, 3 e 4. Como não há um terceiro número entre parênteses, significa o seguinte:
    # Implicitamente é declarado que vai pular de um em um número até chegar no limite, que é um antes do último...
    # Caso fosse passado um número como parâmetro, obeceria a ordem que ele empreender
    # O último número não é impresso, é como se fosse essa declaração: while i < 5:
    # Sintaxe: for variável in range (início, fim, de quantos em quanto pula): Ex:
    # for j in range(0, 10, 2): percorre o alcance de 0 a 10 pulando de dois em dois e armezenando em j. Ex:
print("\n")
# Para garantir quebra de linha;
for j in range(0, 10, 2):
    print(j)

N = int(input("Quantos números serão digitados? "))

soma1 = 0
# Soma acumulada
for i1 in range(0, N):
    x12 = int(input("Digite um número: "))
    soma1 = soma1 + x12

print("SOMA = ", soma1)
# Nessa declaração enquanto estiver no alcance de números eles serão somados

# Aula 238 - Vetores

# Propriamente não há vetores, mas em vez disso listas ou tuplas.
N1 = int(input("Quantos números você vai digitar? "))

vet: [float] = [0 for x in range(N1)]
# Sintaxe: meu_vetor: [tipo] = [0 for x in range(numero_de_elementos)]
# Sendo que o nome do vetor pode ser qualquer um, nesse caso chamamos de vet;
# [] indica que trata - se uma lista, ou seja, esta declarando uma lista desse tipo informado, nesse caso float;
# Esta segunda declaração [] propriamente ocupa os endereços na memória a virem a ser referenciadas pela variável;
# De 0 para x no alcance(variável ou número), ou seja o espaço da memória que será alocado;
# No parênteses é delimitado o tamanho, nesse caso N.

for i2 in range(0, N1):
    vet[i2] = float(input("Digite um número: "))
    # Os números digitados são armazenados em i2 até o limite de alcance (N1)
    # i2 recebe valores de ponto flutuante devido a sua declaração como float

print()
# Para garantir quebra de linha
print("NÚMEROS DIGITADOS: ")
for i2 in range(0, N1):
    print(f"{vet[i2]:.1f}")
    # Este novo escopo imprime o que foi previamente digitado usando a mesma estrutura lógica
    # Ou seja, é exibida a lista vet com formatação de uma casa decimal (.1f)
print()

# Aula 239 - Matrizes

# Como propriamente não há matrizes, é necessária a criação de listas dentro de listas;
M2 = int(input("Quantas linhas vai ter a matriz? "))
N2 = int(input("Quantas colunas vai ter a matriz? "))

mat: [[int]] = [[0 for x in range(N2)] for x in range(M2)]
# Sintaxe: minha_matriz: [[tipo]] = [[0 for x in range(numero_de_colunas)] for x in range(numero_de_linhas)]
# Ao se criar colchetes dentro de colchetes você está declarando uma lista dentro de outra lista...
# Essa estrutura gera uma matriz.
# Num primeiro momento passar o tipo dentro de dois colchetes...
# Após o igual para atribuição passar uma primeiro colchetes com o número de COLUNAS...
# E só após o número de LINHAS no outro colchetes que sobrepoem o anterior.
# Essa segunda declaração que propriamente reserva os espaços na memória.
# Ao utilizar dois x o interpretador emite avisos de redeclaração, porém não está incorreto.

for i3 in range(0, M2):
    for j3 in range(0, N2):
        mat[i3][j3] = int(input(f"Elemento [{i3},{j3}]: "))
        # Um for dentro do outro é como se houvesse um escopo dentro do outro, a mesma ideia de um if dentro do outro;
        # Esta matriz mat recebe na ordem linhas (i) e colunas (j);
        # Sintaxe: nome_da_matriz[linhas][colunas] = tipo(input(f"Texto [{linhas},{colunas}]: "))

print()
print("MATRIZ DIGITADA: ")
for i3 in range(0, M2):
    for j3 in range(0, N2):
        print(f"{mat[i3][j3]} ", end="")
        # Este end="" garante um espaço entre uma variável e outra nas linhas;
        # Esse parâmetro imprime a matriz na linha i, coluna j com espaço entre os elementos;
    print()
    # Print para quebra de linha de uma coluna para outra

# Aula 240 - Problema retângulo

base: float
altura2: float
# Declaração de tipo opcionais
base = float(input("\nBase do retângulo: "))
altura2 = float(input("Altura do retângulo: "))

area2 = base * altura2
perimetro = 2 * (base + altura2)
diagonal = math.sqrt(base ** 2 + altura2 ** 2)
# Função math.sqrt executa a raiz quadrada
# Sintaxe: math.sqrt(variavel_a_receber_raiz)
# Exponenciação é executada por **
# Sintaxe: variável ** expoente

print(f"AREA = {area2:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
print()

# Aula 241 - Problema idades
print("Dados da primeira pessoa: ")
nome4 = input("Nome: ")
idade4 = int(input("Idade: "))

print("Dados da segunda pessoa: ")
nome5 = input("Nome: ")
idade5 = int(input("Idade: "))

media = (idade4 + idade5) / 2

print(f"A idade média de {nome4} e {nome5} é de {media:.1f} anos")

# Aula 242 - Problema menor de três
a5 = int(input("Primeiro valor: "))
b5 = int(input("Segundo valor: "))
c5 = int(input("Terceiro valor: "))

if a5 < b5 and a5 < c5:
    menor = a5
# Encadeamento de estruturas condicionais:
elif b5 < c5:
    menor = b5
else:
    menor = c5

print(f"MENOR = {menor}")

# Aula 243 - Problema crescente
print("Digite dois números: ")
x13 = int(input())
y10 = int(input())

# Uso de <> para diferente não é suportado na versão 3.9 do Python;
while x13 != y10:
    if x13 < y10:
        print("CRESCENTE!")
    else:
        print("DECRESCENTE!")

    print("Digite outros dois números: ")
    x13 = int(input())
    y10 = int(input())

# Aula 244 - Problema soma impares
print("Digite dois números: ")
x14 = int(input())
y11 = int(input())

if x14 > y11:
    troca = x14
    x14 = y11
    y11 = troca

soma2 = 0
for i4 in range(x14+1, y11):
    # Se o resto (mod %) da divisão por 2 for diferente de zero, logo não é exata, então o número é impar:
    if i4 % 2 != 0:
        soma2 = soma2 + i4

print(f"SOMA DOS IMPARES = {soma2}")

# Aula 245 - Problema soma vetor
N3 = int(input("Quantos números você vai digitar? "))

vet2 = [0 for x in range(N3)]
# Nesse vetor foi emitido o tipo da variável devido a ser opcional

for i5 in range(0, N3):
    vet2[i5] = float(input("Digite um número: "))

print()
print("VALORES = ", end="")
for i5 in range(0, N3):
    print(f"{vet2[i5]:.1f} ", end="")

print()

soma3 = 0
for i5 in range(0, N3):
    soma3 = soma3 + vet2[i5]

print(f"SOMA = {soma3:.2f}")

media2 = soma3 / N3
print(f"MEDIA = {media2:.2f}")

# Aula 246 - Problema diagonal negativos
N4 = int(input("Qual a ordem da matriz? "))

mat2 = [[0 for x in range(N4)] for x in range(N4)]
# Nessa matriz foi emitido o tipo da variável devido a ser opcional

for i6 in range(0, N4):
    for j4 in range(0, N4):
        mat2[i6][j4] = int(input(f"Elemento [{i6},{j4}]: "))

print("DIAGONAL PRINCIPAL = ")
for i6 in range(0, N4):
    print(f"{mat2[i6][i6]} ", end="")
print()
# Print para realizar quebra de linha

cont = 0
for i6 in range(0, N4):
    for j4 in range(0, N4):
        if mat2[i6][j4] < 0:
            cont = cont + 1

print(f"QUANTIDADE DE NEGATIVOS = {cont}")
