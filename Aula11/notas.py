#Criar função para calculo da tabela PRICE
# VP = P * [(1+I)^n -1] / [(1+I)^n]*i
# VP = P * [(1+I)^-n -1] / I
# P = VP * [(1+i)^n *1] / [(1+i)^n -1]
# P = VP * [I / (1+I)^-n -1]

def PriceVP(parcela,taxa,tempo):
    return parcela * (pow(1+taxa,tempo)-1)/(pow(1+taxa,tempo)*taxa)

def PricePGTO(valorPresente,taxa,tempo):
    return valorPresente * (pow(1+taxa,tempo)*taxa)/(pow(1+taxa,tempo)-1)

#def PriceJuros(valorPresente, parcela, taxa):



vp = float(input("VP = "))
i = float(input("i = "))
n = float(input("n = "))
resultado = PricePGTO(vp,i,n)
print(resultado)