#ham range():
#for var in iterable:
    #statement
#cu phap:
# range(start, stop, step)

a = range(1, 11)
x = 1
for i in a :
   # print('cau len thu', i ,'ben trong for')
   x *= i 
else: print('vong lap da ket thuc',x)


#break:
#vd: tu 1 toi 20, nhung in toi so 7 thi dung
for i in range(1, 21):
    print(i, end = ' ')
    if i == 7 : break

# for lặp vĩnh viễn:
# from itertools import count
# for i in count():


# nhap 1 so toi khi nhap so 2026 moi dung
from itertools import count
for i in count():
    i = int(input())
    if i == 2026 : print(i); break

#nested loop
for i in range(3):
    for j in range(2):
        print(i,j)