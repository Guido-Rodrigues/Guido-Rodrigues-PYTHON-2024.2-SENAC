#faça um programa que imprima os 10 primeiros números da sequência de fibonacci
#Formula > Fn = Fn-1 + Fn-2
n = int(input("Por favor insira quantos numeros da sequencia de fibonacci quer: "))
n1 = 1
n2 = 1
print(n1)
print(n2)
for i in range(2, n):
    n3 = n1 + n2
    print (n3)
    n1 = n2
    n2 = n3