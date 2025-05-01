from random import sample
a1=input('digite o nome do primeiro aluno: ')
a2=input('digite o nome do segundo aluno: ')
a3=input('digite o nome do terceiro aluno: ')
a4=input('digite o nome do quarto aluno: ')
s=[a1, a2, a3, a4]
print('a ordem de apresentação sorteada é: \n {}'.format(sample(s, k=len(s))))