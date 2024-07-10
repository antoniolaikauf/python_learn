def pair(Li1,Li2):
    try:
        len(Li1) == len(Li2)
        return [round(y / Li2[x],2)  for x,y in enumerate(Li1)]
    except ZeroDivisionError: raise ZeroDivisionError('divisione per 0 infinita')
    except: raise ValueError('liste di diversa lunghezza')

num1=[1,2,3,4]
num2=[3,2,5,6]
print(pair(num1,num2))
exit(0)

def num_list(n):
    return [x for x in range(n+1)]

print(num_list(10))

def removed_ele(L,n):
    return [x for x in L if x != n]

L=[1,2,2,3,4]
print(removed_ele(L,2))

def count_word(sen):
    words=sen.split(' ')
    return len(words)

print(count_word('hello word'))

def eliminate_element(ListN,n):
    li = ListN.copy()
    ListN.clear()
    for x in li: 
        if x != n: ListN.append(x)

Li=[1,2,3,4,5,6]
eliminate_element(Li,2)
print(Li)
'''
sum and prod
'''

def sum_and_prod(*L):
    sum=0
    prod=1
    for x in L:
        sum+=x
        prod*=x
    return (sum,prod)

print(sum_and_prod(1,2,3,5,2,4,6))

'''
dividi stringa in consonanti e vocali
'''

def divide(s):
    vocali='aeiou'
    v=0
    c=0
    s= s.replace(' ', '')
    if type(s) != str: return False
    for x in s:
        if x in vocali: v+=1
        else:c+=1
    return(v,c)

print(divide('ciao come'))

def apply(criteria,n):
    countE=0
    for x in range(n+1):
        if criteria(x) == True: countE+=1 
    return countE

def is_even(x):
    return x % 2 == 0

how_many=apply(is_even,10)
print(how_many)
'''
trovare tutte le radice quadrate di un range 
'''

def square_root(i, e):
    low=0
    high=i
    middle=(low + high) / 2
    while abs(middle**2 - i) > e:
        if middle**2 < i: low = middle
        else: high= middle
        middle=(low + high) /2
    return middle
    
def count_num(root, epsilon):
    count=0
    for x in range(1,root**3):
        SQR=square_root(x,epsilon)
        if abs((SQR - root)) < epsilon:
            count+=1
            print(SQR)
    return count

print(count_num(10,0.1))

'''
valore triangular 
un valore si dice che è triangular se è uguale alla somma dei numeri naturali (in fila)
es. 6 è triangular perché 1+2+3 fa 6, 10 è triangular 1+2+3+4 =10
'''
def triangular(p):
    value=0
    for x in range(p+1):
        value += x 
        if value == p :return True
    return False

print(triangular(10))
print(triangular(1))
print(triangular(30))

def divide(a,b):
    return a % b == 0

print(divide(10,3))
print(divide(195,13))

'''
ricerca binaria cubo
'''

cube=10
start=0
high=cube
epsilon=0.01

middle=(start + high) / 2
while abs((middle**3) - cube) > epsilon:
    if middle**3  < cube: start = middle
    else : high= middle
    middle= (start + high) / 2 

print(middle) 

'''
trasformare numero decimale in binario
'''

num=-1057
string=''
flag=False
if num < 0:
     num= abs(num)
     flag= True

while num > 0:
    if num == 0 : string='0'
    string += str(num%2)
    num= num // 2
if flag: string= '-' + string
print(string)

'''
trasformazione numero decimale in binario
nella memoria vengono salvati due numeri in coppia  (125 , -2) prima si trasforma 125 in base 2 
quindi 1111101 e sarebbero le cifre più importanti invece l'altro numero sarebbe in base due 
e dice dove posizionare la virgola 11111.01 
125 * 2**-2 = 31.25 quindi 11111.01 nella memoria è la rappresentazione di 31.25
'''

x = 31.25
p = 0
# trovare p
while ((2**p) * x) % 1 != 0:
    p += 1
#convertire in binario
num = int(x * (2**p))
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
# aggiungere 0
for i in range(p - len(result)):
    result = '0' + result
# Compone la stringa binaria frazionaria
result = result[:-p] + '.' + result[-p:]

print(f'{p} è il numero corretto')
print('{} rappresentazione binario {}'.format(x, result))



'''
floating point error
'''
i=0
for x in range(11):
    i+=0.1
print(i , 0,1*10)
print(i == 1)


questionn=input('put verb: ')
print(f'i can {questionn} better then you')
print((questionn + ' ') * 5)

import math

'''
algoritmo per indovinare la radice quadrata, all'inizio dovrai fornire il numero che pensi sia la radice quadrata di X
se il numero non lo è allora si dovra utilizzare come guess l'output che si ha ottenuto fino a quando non diventa il numero che si avvicina piu possibile 
alla radice quadrata si X
'''

def radice():
    x=int(input('radice quadrata di: '))
    return x

def guess():
    g=input('guess: ')
    return g

X=radice()
R= math.sqrt(X)

def calcolo():
    G=guess()
    G=float(G)
    nextGuess= G - ((G**2) - X) / (2*G**2)
    print(nextGuess)
    if nextGuess != R: calcolo()
    else: return nextGuess

calcolo()

'''
potenza
'''
G=0
x=int(input('Number: '))
while G**2 < x:
    G+=1
if G**2==x: print(f'{G} è il quadrato di {x}')
elif x<0:print(f'intendevi {-x} ?')
else:print(f'{x} non è un quadrato perfetto')