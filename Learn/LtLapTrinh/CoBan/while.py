# while condition:
#     statement
# else:
#     statement

# while n <= 5:
#     print(n, sep= '\n')
#     n += 1

# chu so thu k cua mot so
n = 54565
k = 4
print((n // 10**(len(str(n))-k)) % 10)

#so bi lat
n = int(input())
k = 0
while n // 10 != 0 :
    k = k * 10 + (n % 10)
    n = n // 10
else : k = k * 10 + n
print(k)
