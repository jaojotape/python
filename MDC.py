a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = 0
divisor = 0
dividendo = 0
if b > a:
    divisor = a
    dividendo = b
else:
    divisor = b
    dividendo = a
while dividendo % divisor != 0:
    c = (dividendo % divisor)
    dividendo = divisor
    divisor = c
print('O MDC é ',divisor)
    