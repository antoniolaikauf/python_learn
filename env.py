error= 200

if error== 200 or error == 201:
    print('success')
elif error == 400:
    print('bad request')
else:
    print('not found')

match error:
    case 200 | 201:
        print('success')
    case 400:
        print('bad request')
    case _:
        print('not know')


import time 

satrt_time= time.time()

for i in range(10):
    for y in range(10):
        print(y, end=' ')
    print('\n')

print(round(time.time() - satrt_time))

# variabile globale 
global_vr=5

def num2():
    # encloser variabile 
    encloser_vr=20
    def num():
       # local variabile    
       local_vr=10
       print('variabile globale', global_vr)
       print('variabile encloser', encloser_vr) 
    num()

num2()

# args 
def sum(*args):
    print(type(args))
    for i in args:
        print(i)

sum(1,2,3,4,5,6,7,8)

# elenco 
set =['string', 2 , True, 4.54]
# tuple
tuple=('string', 1 , False, 4.76)
# set 
set={1,2,3,4,5,6}
# dizionaro
dizionario={1:'acqua', 2:'aranciata'}


# gestione errore 
def division(a,b):
    return a/b
try:
  print(division(40,0))
except Exception as e:
    print(e)


import random
name=['Ace', 'Atlas', 'Bailey', 'Bear', 'Blaze', 'Boomer', 'Buddy', 'Coco', 'Cooper', 'Duke', 'Dozer', 'Echo', 'Gizmo', 'Harley', 'Mac', 'Max', 'Milo', 'Oscar', 'Rex', 'Rocky', 'Rocket', 'Wolfie']
try:
# leggere file 
  with open('text.txt', mode='r') as f:
      read_content=f.read().split()
      random_choise=random.choice(read_content)
      print(random_choise)
    # for i in name:
        # f.writelines(i+'\n')
except FileNotFoundError as e:
    print(e)

# algoritmo
import math
def palindome(str):
    index=0
    half=math.floor(len(str)/2)

    for x in range(len(str)-1, half, -1):
        if str[index] != str[x]: return 'parola non palindroma'
        index+=1
    return 'parola palindoma'

print(palindome('racecar'))
print(palindome('racecarhfhfh'))


list_num=[1,2,3,4]
# funzione pure non cambia una variabile globale ma cambia un avariabile nel proprio ambito
def pure_function(lst, num):
    nl=lst.copy()
    nl.append(num)
    return nl

print(pure_function(list_num,5))
print(list_num)

# time O(n!)
def factorial(n):
    factorial=1
    for i in range(1,n+1):
        print(i)
        factorial*=i
    return factorial

print(factorial(5))
#  metodo ricorsione 
def factorial_recursive(n):
    if n > 1:
        return n * factorial_recursive(n -1)
    else:
        return 1
print(factorial_recursive(5))

# comprensione 
# set
comp=[x for x in range(5)]
print(comp)

data = [2,3,5,8,11,13,17,19,23,29,31]

comp1=[x for x in data]
print(comp1)

data=[x for x in data if x % 4==0]
print(data)


# dizionari 
number=[1,2,3,4,5,6,7]

comp2={x:x**2 for x in number}
print(comp2)

# senza le comprensioni 
# without_comp= []
# for x in range(5):
#     without_comp.append(x)
# print(without_comp)

# in python non esesite una funzione per invertire la parola si usa questo metodo 
parola='ciao'
print(parola[::-1])

# stampa i 50 numeri dopo la virgola e f dopo 50 significa trattameli come float
num=1/3
print(f'{num:.50f}')


def main():
    for i in range(altezza()):
        for y in range(i):
             print('*', end='')
        print('\n')


def altezza():
    while True:
      value=int(input('altezza: '))
      if value > 0: return value 

main()


# lambda 

lam=lambda a,b: a*b
print(lam(2,3))