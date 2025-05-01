n=input('digite algo: ')
print('='*70)
print('esse valor é de que classe? {} \n esse valor é alfanumérico? {} \n esse valor é numérico? {} \n esse valor é um número decimal? {} \n esse valor é alfabético? {} \n esse valor só tem maiúsculas? {} \n esse valor só tem letras minúsculas? {} \n está captalizado? {} \n só tem espaços? {} '.format(type(n), n.isalnum(), n.isnumeric(), n.isdecimal(), n.isalpha(), n.isupper(), n.islower(), n.istitle(), n.isspace()))
print('='*70)