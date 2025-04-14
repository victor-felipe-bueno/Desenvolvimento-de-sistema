#1
def idade():
    idade=int(input("Digite sua idade: "))

    if idade <= 17:
        print("Menor de idade!")
    else:
        print("Maior de idade!")
#2
def numero_2():
    n1=float(input("Digite o 1º numero: "))
    n2=float(input("Digite o 2º numero: "))
    if n1 < n2:
        print(n1," é menor que ",n2)
    elif n1 > n2:
        print(n1," é maior que ",n2)
    else:
        print("Os números são iguais!")
#3
def letra():
    letra=str(input("Digite uma letra: "))
    letraM=letra.lower
    if letraM == "a"or "e" or 'i' or 'o' or 'u':
        print(f"A letra {letra} é uma vogal!")
    else:
        print(f"A letra {letra} é uma consoante!")
#4
def senha():

    senha=input("Crie sua senha: ")

    senhaDigitada=input("Digite a sua senha: ")
    if senha == senhaDigitada:
        print("Acesso permitido")
    else:
        print("Senhas não coincidem")
#5
def media():
    n1=float(input("Digite a 1ª nota: "))
    n2=float(input("Digite a 2ª nota: "))
    n3=float(input("Digite a 3ª nota: "))

    m=(n1+n2+n3)/3
    if m>=7:
        print(f"O aluno está aprovado!, com a nota: {m}")
    else:
        print(f"O aluno esta reptovado!, com a nota: {m}")
#6
def n_decrescente():
    n1=int(input("Digite o 1º número: "))
    n2=int(input("Digite o 2º número: "))
    n3=int(input("Digite o 3º número: "))
    l=[n1,n2,n3]
    l.sort()
    l.reverse()
    print(l)

def combustivel():
    #carro faz 12 km por litro 
    tempGast=int(input("Digite o tempo do percurso: "))
    velMed=int(input("Digite a velocidade média: "))
    distancia= tempGast * velMed
    gasto=distancia/12
    print(f"O combsutivel que será gasto é de {gasto}")

escolha=input('Escolha 1 exercicio, idade, numero_2, letra, senha, media, n_decrescente ou combustivel: ')  
escolha1=escolha.lower()
match escolha1:
    case "idade"  :
        print(idade())
    case "numero_2":
        print(numero_2())
    case "letra":
        print(letra())
    case "senha":
        print(senha())
    case "media":
        print(media())
    case "n_decrescente":
        print(n_decrescente())
    case _:
        print("Função invalida!")