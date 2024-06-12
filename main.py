# função calcular média
def calcular_media(notas):
    return sum(notas) / len(notas)

# programa principal
alunos = []

for i in range(30):
    nome_aluno = input(f"Digite o nome do {i+1}º aluno: ")
    notas_aluno = []
    for x in range(5):
        nota = float(input(f"Digite a {x+1}ª nota (de 0 a 10) do aluno {nome_aluno}: "))    
        while nota < 0 or nota > 10:
            nota = float(input("Nota inválida! Digite uma nota de 0 a 10: "))
        notas_aluno.append(nota)
       
    
    media = calcular_media(notas_aluno)
    situacao = "aprovado" if media >= 7 else "reprovado"
    
    alunos.append((nome_aluno, media, situacao))

# retorna os alunos aprovados
aprovados = [aluno[0] for aluno in alunos if aluno[1] >= 7]

print("\nLista de alunos aprovados:")
for aluno in alunos:
    print(f"{aluno[0]} - Média: {aluno[1]} - Situação: {aluno[2]}")

# exibe na tela os alunos aprovados
print("\nAlunos aprovados:")
for aluno in aprovados:
    print(aluno)
