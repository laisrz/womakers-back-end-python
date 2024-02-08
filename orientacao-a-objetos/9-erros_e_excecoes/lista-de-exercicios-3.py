## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    soma = 0.0
    
    for i, valor in enumerate(valores):
        soma += valor
        i += 1
    tamanho = len(valores)
    return soma / tamanho

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor != "ok":
        valores.append(float(valor))
    elif valor.lower() == 'ok':
        continuar = False

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))