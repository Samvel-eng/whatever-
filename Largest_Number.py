num = int(input('num = '))
if num // 10 == 0:
    print('no')
    #sdjbjgfk,dklnldkncklnd
else:
    d1 = num % 10
    d2 = num // 10 % 10
    result = False
    while num // 10 != 0:
        if d2 - d1 < 0:
            result = True
            break
        num //= 10
        d1 = num % 10
        d2 = num // 10 % 10
    if result:
        print('yes')
    else:
        print('no')
'''dshvjksdbjksbjk'''
