def display(n):
    print(n)
    if n<10:
     display(n+4)

display(9)

a = 0
b = 1
print(a)
print(b)
for i in range (100):
    c = a+b
    print(c)
    a = b 
    b = c

fib = [0,1]
for i in range (100):
    c = fib[i]+fib[i+1]
    fib.append(c)