import sys

# Intero
i = 1000000
print(f"Intero (10): {sys.getsizeof(i)} bytes")

# Float
f = 10.0
print(f"Float (10.0): {sys.getsizeof(f)} bytes")

# Booleano
b = True
print(f"Booleano (True): {sys.getsizeof(b)} bytes")

# Stringa
s = "o"
print(f"Stringa (Hello): {sys.getsizeof(s)} bytes")

'''
algoritmo approssimato/approximate algorithm le performance di questo algoritmo vanno in base ai due 
parametri: al range rappresentato come epsilon e l'incremento più è grande il range più sarà veloce ma meno accurato, più 
l'incremento sarà piccolo più l'algoritmo sarà accurato 
'''
guess=54321
increment=0.0001
y=0
epsilon=0.01 #range
# condizione per entrare dentro al range 
while abs(y**2 - guess) >= epsilon and y**2 <= guess: # secondo condizione se y**2 supera il guess essendo che potrebbe superarla 
    y+=increment
if abs(y**2) > guess+increment: print('not found')
else:print('{} root of {}'.format(y,guess)) 


# albero
for x in range(1,6):
    for y in range(x):
        print('#' , end=' ')
    print('\n')


def anagramma(str1,str2):
    if len(str2)==len(str1):
        return all(x in str2 for x in str1)
    else: return False

print(anagramma('heart','earth'))
print(anagramma('heart','earph'))

# Definire una funzione che riceva come argomenti due stringhe s1 e s2 contenenti la prima una frase
# e la seconda una sequenza di lettere qualsiasi; la funzione dovrà restituire il numero di occorrenze
# della stringa s2 all’interno della frase s1 (senza usare la funzione predefinita count). Si assuma per
# semplicità che tutte le lettere delle due stringhe siano minuscole. Per esempio, se s1 ="questo è
# un esercizio difficilissimo" e s2 ="ci", la funzione dovrebbe restituire il valore 2, in quanto in s1 sono presenti due occorrenze della sequenza di lettere "ci" ("questo è un esercizio
# difficilissimo")

def string(s1,s2):
    count=0
    for x in  s1.split():
        if s2 in x:count+=1
    return count 
print(string('questo è un esercizio difficilissimo','ci'))

# Definire una funzione che riceva come argomenti due liste che si assumono avere la stessa lunghezza,
# contenenti i voti (numeri interi compresi tra 0 e 30) conseguiti da un certo insieme di studenti nelle
# due prove di un esame. Posizioni corrispondenti nelle due liste si riferiscono allo stesso studente.
# La funzione dovrà restituire il valore True se tutti gli studenti hanno superato entrambe le prove;
# in caso contrario dovrà restituire il valore False.
# Per esempio, se le liste fossero [21, 28, 26] e [23, 27, 28], la funzione dovrebbe restituire True,
# mentre se le liste fossero [21, 28, 26] e [23, 12, 28] la funzione dovrebbe restituire False.

def arr_list(list1,list2):
    for i,x in enumerate(list2):
        if x <18 or list1[i]<18:
            return False
    return True
print(arr_list([21, 28, 26],[23, 12, 28]))


# Definire una funzione che riceva come argomento una lista composta da dizionari, ciascuno dei quali
# contiene le coordinate di un punto in uno spazio a tre dimensioni, associate alle chiavi "x", "y" e
# "z"; per esempio: [{"x":2, "y":-1, "z":3}, {"x":1, "y":9, "z":0}].
# La funzione dovrà restituire un dizionario contenente le coordinate del baricentro di tali punti,
# che dovrà essere calcolato assumendo identiche le loro masse. Si ricorda che il baricentro di un
# insieme di n punti {(x1, y1, z1),(x2, y2, z2), . . . ,(xn, yn, zn)} aventi massa identica è il punto avente
# coordinate:

point= [{"x":2, "y":-1, "z":3}, {"x":1, "y":9, "z":0}]

def balance(br):
    xBalance=0
    yBalance=0
    zBalance=0
    for x in br:
        xBalance+=x['x']
        yBalance+=x['y']
        zBalance+=x['z']
    Cbalance=[{"x":xBalance/len(br), "y":yBalance/len(br), "z":zBalance/len(br)}]
    return Cbalance

print(balance(point))


# algoritmo ricerca binaria passi in log base 2 di n nell'esempio sotto n è 10 quindi 3,33


def create_arry(num):
    array=[x for x in range(1,num)]
    return array

array_num=create_arry(11)
import math
def search(num, args):
    start=0
    high=len(args) -1
    while start<=high:
        middle =math.floor((start + high) / 2)  # formula per calcolare il punto medio di un range  (minimo + massimo) / 2 
        if num == args[middle]: return True
        elif num > args[middle]: start= middle + 1
        elif num < args[middle]: high= middle -1
    return False 

print(search(1, array_num))


# buble sort 

random_array=[3,5,9,8,2,1,10,24,12]
random_array1=[1,2,3,4]

'''
ogni iterazione si fa (n-1) perchè ad ogni iterazione viene sistemata almeno
 un elemento quindi non ha senso fare un loop ancora su tutti gli elementi 
 nella seconda iterazione sarà (n-2) e csi via 
 count per il controllo se l'array è gia ordinato cosi che non si faccia cicli senza senso 
'''
def sort_array(arg):
    length=len(arg)-1
    count=0
    for y in range(length): 
      for i in range(length - y):
        if arg[i] > arg[i + 1]:
            count+=1 
            arg[i], arg[i+1]=arg[i+1], arg[i]
      if count==0:
        return True
    return arg

print(sort_array(random_array))
print(sort_array(random_array1))


# ottenere indirizzo memoria 

import ctypes

variabile='hello word'
address=int(id(variabile))

print(address)

value=ctypes.cast(address, ctypes.py_object).value
print(value)
print(hex(address))


def factorial(n):
    combination=1
    for i in range(1,n+1):
        combination*=i
    return combination

print(factorial(48))



