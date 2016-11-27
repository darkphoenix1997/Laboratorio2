

#4
print "Coordenadas del poligono"
n=int(input("Dime el numero de lados papu"))
l=int(input("¿Que longitud tienen sus lados?"))
x=[]
y=[]
angulo=0
import math
def completar(a,x,y):
  for i in range (0,a):
    x.append(0)
    y.append(0)
  return x,y
completar(n,x,y)
def inclinacion(x):
  global inclinacion
  inclinacion=((math.pi*2)/x)
inclinacion(n)
def coordenadas(a,b,c,d,e):
  cx=0
  cy=0
  ti=0
  for i in range (0,a):
    cx=b*math.cos(ti)
    if cx<0.00000000001 and cx>-0.00000000001:
      cx=0.0
    cy=b*math.sin(ti)
    if cy<0.00000000001 and cy>-0.00000000001:
      cy=0.0
    ti=ti+c
    if i==0:
      d[i]=cx
      e[i]=cy
    elif i==-1:
      d[i]=0
      e[i]=0
    else:
      d[i]=cx+d[i-1]
      e[i]=cy+e[i-1]
  return d,e
def imprime(x,y):
    for i in range(0,len(x)):
      print x[i],",",y[i]
coordenadas(n,l,inclinacion,x,y)
imprime(x,y)

