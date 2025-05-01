n=float(input('quanto dinheiro você tem? R$ '))
print('='*40)
print('com R${:.2f} você poderá comprar: \n {:.2f} dólares estadunidenses \n {:.2f} libras \n {:.2f} ienes'.format(n, n/6.11, n/7.3, n/0.04))
print('='*40)