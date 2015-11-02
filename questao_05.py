#Lista de Exercicios 1
#5

p = float (input('Digite o valor da mercadoria: '))
d = float (input('Digite o valor do desconto: '))
pd = (p * d) / 100
pt = p - pd
print ('O valor do desconto foi de R$%.2f' %pd)
print ('O valor final da mercadoria com desconto foi de R$%.2f' %pt)
