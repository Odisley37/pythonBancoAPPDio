import random
import string
import pandas as pd
import os

# Lista de clientes
clientes = []

# Nome do arquivo CSV
csv_filename = "clientes.csv"

# Lista de frases aleatórias de otimismo
frases_aleatorias = [
    "Acredite em si mesmo, você é capaz de conquistar grandes coisas.",
    "Cada dia é uma nova oportunidade para ser feliz e alcançar seus sonhos.",
    "O sucesso vem para aqueles que trabalham duro e nunca desistem.",
    "Seja positivo e coisas incríveis acontecerão em sua vida."
]

# Função para gerar um número de cartão aleatório
def gerar_numero_cartao():
    numeros = ''.join(random.choices(string.digits, k=16))
    return f"{' '.join([numeros[i:i+4] for i in range(0, len(numeros), 4)])}"

# Função para cadastrar um cliente
def cadastrar_cliente():
    nome = input("Nome completo: ")
    endereco = input("Endereço: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")
    salario = float(input("Salário: "))

    if salario <= 1200:
        limite = 3000
        bandeira = "Visa"
    elif salario < 10000:
        limite = 12000
        bandeira = "Master"
    else:
        limite = 25000
        bandeira = "Diners"

    numero_cartao = gerar_numero_cartao()

    cliente = {
        "Nome": nome,
        "Endereço": endereco,
        "Telefone": telefone,
        "CPF": cpf,
        "Salário": salario,
        "Limite": limite,
        "Bandeira": bandeira,
        "Número do Cartão": numero_cartao
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

    # Atualiza o arquivo CSV com os dados do cliente
    atualizar_csv()

# Função para atualizar o arquivo CSV com os dados dos clientes
def atualizar_csv():
    df = pd.DataFrame(clientes)
    df.to_csv(csv_filename, index=False, mode="w", header=False)

# Função para listar todos os clientes
def listar_clientes():
    if clientes:
        for i, cliente in enumerate(clientes, 1):
            print(f"Cliente {i}:")
            for key, value in cliente.items():
                print(f"{key}: {value}")
            print("\n")
    else:
        print("Nenhum cliente cadastrado.")

# Função para o cliente consultar saldo, cartão, limite e frase aleatória
def consultar_cliente(cpf):
    for cliente in clientes:
        if 'CPF' in cliente and cliente['CPF'] == cpf:
            print(f"Olá, {cliente['Nome']}!")
            print(f"Seu saldo atual é: R${cliente['Salário']:.2f}")
            print(f"Seu cartão {cliente['Bandeira']} com número {cliente['Número do Cartão']} possui um limite de R${cliente['Limite']:.2f}")
            frase_aleatoria = random.choice(frases_aleatorias)
            print(f"Frase de otimismo para você: {frase_aleatoria}")
            return

    print("Cliente não encontrado.")

# Função principal
def main():
    # Verifica se o arquivo CSV existe
    if not os.path.exists(csv_filename):
        # Cria o arquivo CSV com as colunas especificadas
        with open(csv_filename, "w") as file:
            file.write("Nome,Endereço,Telefone,CPF,Salário,Limite,Bandeira,Número do Cartão\n")

    # Carrega os dados dos clientes do arquivo CSV, se existir
    try:
        df = pd.read_csv(csv_filename)
        global clientes
        clientes = df.to_dict(orient="records")
    except pd.errors.EmptyDataError:
        pass

    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar Cliente")
        print("2. Consultar Cliente")
        print("3. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
            if clientes:
                cpf = input("Digite o CPF do cliente para consulta: ")
                consultar_cliente(cpf)
            else:
                print("Nenhum cliente cadastrado.")
        elif opcao == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

