MEDIA_APROVACAO = 7
QUANTIDADE_NOTAS = 3

alunos = []


def calcular_media(notas):
    """Recebe uma lista de notas e retorna a média aritmética."""
    if not notas:
        return 0
    return sum(notas) / len(notas)


def verificar_situacao(media):
    """Retorna 'Aprovado' ou 'Reprovado' conforme a média."""
    if media >= MEDIA_APROVACAO:
        return "Aprovado"
    return "Reprovado"


def ler_nota(numero):
    """Pede uma nota ao usuário até que seja um valor válido entre 0 e 10."""
    while True:
        entrada = input(f"Digite a {numero}ª nota: ").strip().replace(",", ".")

        try:
            nota = float(entrada)
        except ValueError:
            print("Erro: digite apenas números (ex.: 7.5).")
            continue

        if nota < 0 or nota > 10:
            print("Erro: a nota deve estar entre 0 e 10.")
            continue

        return nota


def cadastrar_aluno():
    print("\n===== CADASTRO DE ALUNO =====")

    nome = input("Digite o nome do aluno: ").strip()

    if not nome:
        print("Erro: o nome não pode ficar vazio.")
        return

    matricula = input("Digite a matrícula: ").strip()

    if not matricula:
        print("Erro: a matrícula não pode ficar vazia.")
        return

    # Verifica se a matrícula já existe
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("Erro: matrícula já cadastrada!")
            return

    # Recebe e valida as notas
    notas = [ler_nota(i + 1) for i in range(QUANTIDADE_NOTAS)]

    # Calcula a média e a situação acadêmica
    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    # Organiza os dados do aluno
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "notas": notas,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)

    print("\nAluno cadastrado com sucesso!")
    print(f"Nome: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")


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
    matricula = input("Digite a matrícula do aluno: ").strip()

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print("\n===== DADOS DO ALUNO =====")
            print("Nome:", aluno["nome"])
            print("Matrícula:", aluno["matricula"])

            # Exibe as notas do aluno
            for i, nota in enumerate(aluno["notas"], start=1):
                print(f"Nota {i}: {nota}")

            print("Média:", round(aluno["media"], 2))
            print("Situação:", aluno["situacao"])
            return

    print("\nAluno não encontrado.")


def excluir_aluno():
  exclusao - alunos
    matricula = input("\nDigite a matrícula do aluno que deseja excluir: ").strip()

    matricula = input("Digite a matrícula do aluno: ").strip()
      main

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

    opcao = input("\nEscolha uma opção: ").strip()

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