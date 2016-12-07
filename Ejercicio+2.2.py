"Cantidad a pagar paps"
d=float(input("Distancia recorrida"))
def distancia(x):
    x=(x*1000)/250
    return x
def pagar(x):
  b=8.74
  x=b+(distancia(x)*1.84)
  return x
print pagar(d), "pesos"
#Luis Manuel Garcia Valdivia

