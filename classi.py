from abc import ABC, abstractmethod # utilizzato per abstract delle classi https://docs.python.org/3/library/abc.html 

class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print("Instantiating A..")
a = A(1)
print(a.alpha())

'''
si nota che l'output sarà Print inside A. anche se non si è inizializzata la classe A 
Perché le dichiarazioni all'interno del corpo di una classe vengono eseguite
indipendentemente dalla creazione dell'istanza. 
'''


class abstract(ABC):
    @abstractmethod
    def method(self):
        pass

'''
un metdo con @abstractmethod e una funzione/metodo come method non può essere chiamato a meno che non si 
usa un istanza di un figlio che sovvrascrive quel metodo 
'''


class child(abstract):
    def method(self):
        return 'funziono con il figlio e se sono sovrascritto'

child1=child()
print(child1.method())

print(child.mro())
print(help(child))


es=abstract()
print(es.method())
