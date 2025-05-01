from random import choice
a1=input('digite o nome do primeiro aluno: ')
a2=input('digite o nome do segundo aluno: ')
a3=input('digite o nome do terceiro aluno: ')
a4=input('digite o nome do quarto aluno: ')
print('dentre os aluno {}, {}, {}, {} \n o escolhido para apagar o quadro foi: \n {}'.format(a1, a2, a3, a4, choice([a1, a2,a3,a4])))