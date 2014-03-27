#!/usr/bin/env python
# -⁻- coding: UTF-8 -*-
import sys       # hay que incluirla al principio del programa
import math
PI35DT= 3.1415926535897931159979634685441852

#***************FUNCION PI*******************
def calcular_pi (n):
  valor_pi= 3.1415926535897931159979634685441852
  sumatorio=0.0
  ini=0
  intervalo= 1.0 / float(n)
  for i in range (n):
    x_i= ((i+1) - 1.0 / 2.0) /n     # así lo hacemos ahora
    #x_i=calcular_xi (n,i+1)     # así, si utilizáramos la función definida aal principio.
    fx_i= 4.0/(1.0+ x_i * x_i)
    # print " " ,i+1,". Subintervalo:[", ini,"," ,ini+intervalo,"] x_",i+1,":" ,x_i,"f(x_",i+1,"):",fx_i
    ini += intervalo                   #Incrementamos ini con el valor de intervalo.
    sumatorio += fx_i                  #Incrementamos el sumatorio con cada pasada por fx_i
  pi=sumatorio / n                     #calculamos la aproximación de π (notar que tiene que estar fuera del for¡¡)
  return (pi)
#****************************************                  * Ahora calcularemos la cantidad de valores que son menores o iguales que el umbral dado por teclado
def error (nro_intervalos, nro_test, umbral):
  intervalo=nro_intervalos
  lista=[]
  for i in range (nro_test):
    valor_pi = calcular_pi(intervalo)
    intervalo += nro_intervalos
    lista.append(valor_pi)
  pi35=[]
  for i in range (nro_test):
    pi35.append(PI35DT)
  dif35=[]
  for i in range (nro_test):
    dif35.append(abs(pi35[i] - lista[i]))
  correcto = 0
  for i in range (nro_test):
    if (dif35[i] <= umbral):
      correcto = correcto + 1
  porcentaje = 100.0*(1.0 - (float(correcto)/float(nro_test)))
  return (porcentaje)



if (__name__=="__main__"):             # Muy importante para que puede leer el modulo, para que lo pueda transformar en .pyc
  argumentos =sys.argv[1:]

  print argumentos            #muestra la lista de parámetros
  if (len(argumentos)==3):
    n=int(argumentos[0])
    aproximaciones = int(argumentos[1])
    umbral = float(argumentos[2])
  else:     #2. O que el usuario, introduzca el intervalo por teclado.
    print "Introduzca el intervalo (n>0)"
    n=int(raw_input())
    print "Introduaca el número de aproximaciones:"
    aproximaciones = int( raw_input())
    print "Introduzca el umbral de error:"
    umbral = float(raw_input());
  if (n>0):
    porcentaje=error(n,aproximaciones,umbral)
    print "El porcentaje de fallos es del ", porcentaje
  else:
    print "El valor del numero de intervalos debe ser mayor que 0."
    