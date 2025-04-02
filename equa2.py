a, b, c = input('digite os valores a, b e c da equação: ').split()
a = int(a)
b = int(b)
c = int(c)
delta = (b**2)-(4*a*c)
if a == 0:
    print('é uma equação de primeiro grau')
    zero = -b/c
    print("o zero da funçao é: ", zero)
    if b < 0:
        print('é uma função decrescente')
    else:
        print('é uma função crescente')
elif a < 0:
    print('a concavidade será para cima ')
else:
    print('a concavidade será para baixo')

if b == 0:
    print('o resultado é 0 e {:.2f}'.format(c/a))
elif c == 0:
    print('o resultado é 0 e {:.2f}'.format(-b/a))
else:
    if delta < 0:
        print('imaginario')
    else:
        if a == 0:
            print("")
        else:
            raizdelta = delta**0.5
            x1 = (-b+raizdelta)/(2*a)
            x2 = (-b-raizdelta)/(2*a)
            valorx2 = 'o valor da segunda raiz é {:.2f}'.format(x2)
            valorx1 = 'o valor da primeira raiz é {:.2f}'.format(x1)
            yv = (-b)/2*a
            xv = -delta/(4*a)
            print(valorx1, valorx2)
            print('o ponto mais alto do gráfico esta nas coordenadas {:.2f} e {:.2f}'.format(xv, yv))