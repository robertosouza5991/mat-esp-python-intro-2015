#Neste ponto eh necessario uma limpesa e revisao do programa.
#Devido a nao ter entendido desde o inicio como funcionava o "plot" e o "show" as minhas imagens
#ficaram sobrepostas, e para solucionar indroduzi cogigos que agora estao comentados


# bubble-sort.py

#import matplotlib        Estes comandos foram usados para tentar solucionar o bug nas imagens
#matplotlib.use('Agg')
#import pylab as pl

import matplotlib.pyplot as pl
import numpy as np

# declaracao do valor das cartas, e do numero total de cartas
Cartas =  [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]


#declaracao de duas listas vazias para auxilio
Maiores = [None] * 5
Menores = [None] * 5
n = 20

X = np.linspace(0, n-1, n , endpoint=True)
print ("lista original:",Cartas)

pl.plot(X, Cartas, 'ok')
pl.title("Bubble-inicio")
pl.xlabel("Posicao das Cartas")
pl.ylabel("Valor das Cartas")
pl.xlim(-1,20)
pl.ylim(-1,20)
pl.savefig("fig/bubble-inicio.png")		
pl.show()

#contador das imagens em "bubble-troca-{}}"
t=0
# para cada carta, primeira carta, ate a penultima
for i in range(0,n-1,1):
# e para cada uma das cartas seguintes ate a ultima
    for j in range (i+1,n,1):
# comparar cada carta com todas as seguintes ate a ultima 	
        if Cartas[i] > Cartas[j]:
# e caso esta carta seja maior que uma das seguintes,
# trocar as duas de posicao com o auxilio de uma posicao temporaria.

            t = t+1
            pl.plot(X, Cartas, 'ok')			
            pl.title("Bubble-Troca-{}".format(t))
			
          # pl.xlabel("Posicao das Cartas")  # Comentados por terem se mostrados redundantes
          # pl.ylabel("Valor das Cartas")
          # pl.xlim(-1,20)
          # pl.ylim(-1,20)
			
            pl.savefig("fig/bubble-troca-{}".format(t))		
			
   #        pl.show()  # Comentado para nao ter que ficar fechando 100 imagens
   
            # Sem este comando as imagens iam se sobrepondo, e nao ser que fossem mostradas em uma janela
            pl.clf()
			
			
            temp = Cartas[i]
            Cartas[i] = Cartas[j]
            Cartas[j] = temp

			
print("lista final:",Cartas)

#copia os maiores e menores para as listas vazias # Comentados pois pertencem a tarefa anterior
#for k in range (0,5,1):
#    Maiores[k] = Cartas[n-5+k]
#    Menores[k] = Cartas[k]
#impprime os maiores e menores	
#print("cinco maiores",Maiores)
#print("cinco menores",Menores)		
		

pl.plot(X, Cartas, 'ok')
pl.title("Bubble-fim")

#pl.xlabel("Posicao das Cartas") # Comentados pore serem redundantes
#pl.ylabel("Valor das Cartas")
#pl.xlim(-1,20)
#pl.ylim(-1,20)

pl.savefig("fig/bubble-fim.png")		
pl.show()