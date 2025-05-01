from math import sin,cos, tan, radians
n=float(input('digite um ângulo em graus: '))
r=radians(n)
si=sin(r)
co=cos(r)
ta=tan(r)
print(' se o seu ângulo for equivalente a {} graus: \no seu seno será igual a {:.1f} \n o seu cosseno será {:.1f}\n e sua tangente será {:.1}'.format(n, si, co, ta))
