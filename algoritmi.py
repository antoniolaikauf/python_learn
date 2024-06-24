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