media_turma = 0
aprovados = 0
reprovados = 0
final = 0

for i in range(1, 41):
    nota = float(input('Insira a nota do aluno: '))
    media_turma += nota
    if nota >= 70 and nota <= 100:
        aprovados += 1
    elif nota < 70 and nota >= 40:
        final += 1
    elif nota < 40:
        reprovados += 1

media_final = (media_turma / 40)
print(f'Aprovados: {aprovados}, final: {final}, reprovados: {reprovados} \n Média da turma: {media_final}')        