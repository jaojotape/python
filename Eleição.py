c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulo = 0
branco = 0
while True:
    voto = int(input('Digite o código do seu voto: '))
    if voto == 0:
        break
    elif voto == 1:
        c1+=1
    elif voto == 2:
        c2+=1
    elif voto == 3:
        c3+=1
    elif voto == 4:
        c4+=1
    elif voto == 5:
        nulo+=1
    elif voto == 6:
        branco+=1
    else:
        print('Código inválido')
print('Resultado final: O candidato 1 teve ',c1,' votos, o candidato 2 teve',c2,' votos, o candidato 3 teve',c3,' votos, o candidato 4 teve',c4,' votos, e houveram ',nulo,' votos nulos e',branco,' votos em branco')
    