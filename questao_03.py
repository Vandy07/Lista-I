## Lista de exercicio
#3
d = int (input('Digite a quantidade de dias:'))
cd = d * 86400
h = int (input('Digite a quantidade de horas:'))
ch = h *3600
m = int (input('Digite a quantidade de minutos:'))
cm = m * 60
s = int (input ('Digite a quantidade de segundos:'))
conta = (cd + ch + cm+ s)
print ('O total do seus valores somados em segundo eh de: %d' %conta)
