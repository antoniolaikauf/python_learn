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
