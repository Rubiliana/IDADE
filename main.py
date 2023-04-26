import datetime

while True:
    try:
        nome = input("Digite o seu nome completo: ")
        ano_nascimento = int(input("Digite o seu ano de nascimento (entre 1922 e 2021): "))
        if ano_nascimento < 1922 or ano_nascimento > 2021:
            raise ValueError("Ano de nascimento inválido. Tente novamente.")
        break
    except ValueError as error:
        print(error)

ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
print("Nome: ", nome)
print("Idade: ", idade, "anos")
