
alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso!")


def listar_alunos():
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado.")
    else:
        print("\n===== LISTA DE ALUNOS =====")

        for aluno in alunos:
            print("-------------------------")
            print("Nome:", aluno["nome"])
            print("Matrícula:", aluno["matricula"])
            print("Média:", round(aluno["media"], 2))
            print("Situação:", aluno["situacao"])


def consultar_aluno():
    matricula = input("Digite a matrícula do aluno: ")

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("\n===== DADOS DO ALUNO =====")
            print("Nome:", aluno["nome"])
            print("Nota 1:", aluno["nota1"])
            print("Nota 2:", aluno["nota2"])
            print("Nota 3:", aluno["nota3"])
            print("Média:", round(aluno["media"], 2))
            print("Situação:", aluno["situacao"])
            return

    print("\nAluno não encontrado.")


def excluir_aluno():
    matricula = input("Digite a matrícula do aluno: ")

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print("\nAluno excluído com sucesso!")
            return

    print("\nAluno não encontrado.")


while True:
    print("\n===== SISTEMA DE NOTAS DA FACULDADE =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Consultar aluno")
    print("4 - Excluir aluno")
    print("5 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        consultar_aluno()

    elif opcao == "4":
        excluir_aluno()

    elif opcao == "5":
        print("\nEncerrando o sistema...")
        break

    else:
        print("\nOpção inválida! Tente novamente.")
