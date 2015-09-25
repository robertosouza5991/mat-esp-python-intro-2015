# bubble-sort.py

# declaracao do valor das cartas, e do numero total de caartas
Cartas =  [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
n = 20
print ("lista original:",Cartas)
# para cada carta, primeira carta, ate a penultima
for i in range(0,n-1,1):
# e para cada uma das cartas seguintes ate a ultima
    for j in range (i+1,n,1):
# comparar cada carta com todas as seguintes ate a ultima 	
        if Cartas[i] > Cartas[j]:
# e caso esta carta seja maior que uma das seguintes,
# trocar as duas de posicao com o auxilio de uma posicao temporaria.
            temp = Cartas[i]
            Cartas[i] = Cartas[j]
            Cartas[j] = temp
print("lista final:",Cartas)		
		
