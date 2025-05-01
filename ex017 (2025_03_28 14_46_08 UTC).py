from math import hypot
co=float(input('digite o cateto oposto de seu triângulo: '))
ca=float(input('digite o cateto adjacente do seu triângulo: '))
print('se o cateto oposto for {} e o adjacente for {}, logo a sua hipotenusa será igual a {:.1f}'.format(co, ca, hypot(co, ca)))