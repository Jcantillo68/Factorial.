#CALCULANDO EL FACTORIAL DE UN NÚMERO ("n").

#FUNCIÓN PARA CALCULAR EL FACTORIAL.

def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado

#CALCULAMOS EL FACTORIAL DE 5.
fact5=factorial(5)

#VISUALIZAMOS RESULTADO.
print(fact5)
120
