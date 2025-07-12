from time import sleep

"""Criação das funções utilizadas no programa"""

def linha():
    print('-=' * 30)


def contador(i, f, p):
    if p < 0:
        p *= -1

    if p == 0:
        p = 1
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.0)

    if i < f:
        num = i
        while num <= f:
            print(num, end=' ', flush=True)
            sleep(0.3)
            num += p
        print('FIM!')
        sleep(0.5)
    else:
        num = i
        while num >= f:
            print(num, end=' ', flush=True)
            sleep(0.3)
            num -= p
        print('FIM!')
        linha()

"""Definição das contagens fixas para demonstração"""

contador(1, 10, 1)
contador(10, 0, 2)

"""Programa principal, com definição da contagem personalizada pelo usuário"""

print('Agora é sua vez de personalizar a contagem!')
c1 = int(input('Início: '))
c2 = int(input('Fim:    '))
c3 = int(input('Passo:  '))

if c3 == 0:
    c3 = 1
    print('O valor do Passo foi 0, portanto será automaticamente trocado para 1')

contador(c1, c2, c3)
