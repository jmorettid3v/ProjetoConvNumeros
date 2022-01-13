# Nome do Projeto: Conversor de números Reais para Binário
print('\t\t***** Nome do Projeto: Conversor de números Reais para Binário *****')

# Função para processamento e saída dos Dados
def processamento(n):
    print('Resultados\n')
    # Declaração de variáveis e listas
    L = []
    bit = []
    copy = []
    coef = 0.5
    coef2 = 0.5
    add = 0
    add1 = 0
    vai = 0
    x = n
    # Processamento
    for i in range(0, 8):
        n *= 2
        L.append(n)
        bit.append(int(L[i]))  # sequência de bits A Menor
        copy = bit[:]  # sequência dinâmica de bits A Maior
        add += (bit[i] * coef)
        coef = coef/2  # coeficientes para A Menor
        if(i >= 4 and i < 16):
            # complemento de 2 (soma 1 ao bit menos signficativo)
            if(copy[-1] == 1):
                copy[i] = 0
                vai = 1
            else:
                copy[i] = 1
            for j in range(len(copy)-2, -1, -1):
                if(vai == 1 and copy[j] == 1):
                    copy[j] = 0
                    vai = 1
                elif(vai == 0 and copy[j] == 0):
                    vai = 0
                else:
                    copy[j] = 1
                    vai = 0
            for k in range(len(copy)):
                add1 += (copy[k] * coef2)
                coef2 = coef2/2  # coeficientes para A Maior
            error1, error2 = calc(add, add1, x)  # chamada da função calc()
            # Saídas
            print('Com %d bits' % (i+1))
            print(f'Aproximação a menor: 0.%s -> {add} com erro = %.3f%%' % (
                (''.join(str(x) for x in bit)), error1))
            print(f'Aproximação a maior: 0.%s -> {add1} com erro = %.3f%%\n' % (
                (''.join(str(x) for x in copy)), error2))
            add1 = 0
            coef2 = 0.5
        if(n >= 1):
            n -= 1

# Função para cálculo dos erros
def calc(a, b, x):
    error = 0
    for i in range(2):
        # cálculo do erro
        err_menor = error
        sub = (x - a)
        if sub < 0:
            sub *= -1
        error = (sub / x) * 100
        a = b
    return(err_menor, error)


# main() - Entrada de Dados pelo usuário
n = float(input('Dado de Entrada: '))
while(n <= 0 or n >= 1):
    print('Número inválido. Informe um número real no intervalo aberto de (0, 1)!!!\n')
    n = float(input('Dado de Entrada: '))
processamento(n)  # chamada da função processamento()
