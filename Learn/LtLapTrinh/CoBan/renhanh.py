#if dk:
    #code
#else: 
 #   code
#ket hop voi and or not:
'''
n = float(input())
t = int(input())

if n < 0:
    print('am')
elif n % 2 == 0:
    print('chan')
else:
    print('le')

if t==1 or t==3 or t == 5 or t == 7 or t == 8 or t == 10 or t== 12:
    print(31)
elif t == 4 or t==6 or t== 9 or t == 11:
    print(30)
elif t == 2 :
    print(28)
else:
    print('du lieu khong hop le')


#variable = statement if condition else statement
#vd:
a, b = map(float, input().split())
res = 'bang' if a < b else 5
print(res)
'''
# nested if
#kiem tra n la so lon hon hoac bang 50 va chia het 1 trong 3 so 3 5 7
n = int(input())
if n >= 50 :
    if (n % 3 == 0 or n % 5 == 0 or n % 7 == 0 ):
        print('yes')
    else: print('no')
else: print('no')