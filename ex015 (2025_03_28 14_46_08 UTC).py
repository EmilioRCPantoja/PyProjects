d=float(input('digite a quantidade de dias que o carro foi alugado: '))
k=float(input('digite a quantidade de quilometros rodados pelo carro: '))
print('se o carro foi utilizado por {} dias e percorreu {:.2f}Km, será pago R${:.2f} de aluguel pelo carro'.format(d, k, d*60+k*0.15))