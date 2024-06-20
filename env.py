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

