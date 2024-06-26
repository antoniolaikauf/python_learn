from abc import ABC # utilizzato per abstract delle classi https://docs.python.org/3/library/abc.html 

class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print("Instantiating A..")
# a = A(1)
# print(a.alpha())

'''
si nota che l'output sarà Print inside A. anche se non si è inizializzata la classe A 
Perché le dichiarazioni all'interno del corpo di una classe vengono eseguite
indipendentemente dalla creazione dell'istanza. 
'''