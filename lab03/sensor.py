porog=float(input())
n=int(input())
error=0
xmax=0
x=0
summa=0.0
maxx=None
for i in range(n):
    a=input()
    if a=='error':
        error+=1
    else:
        a=float(a)
        x+=1
        summa+=a
        if a>porog:
            xmax+=1
        if maxx is None or a>maxx:
            maxx=a
sr=summa/x
print(n)
print(error)
print(xmax)
print(f"{maxx:.1f}")
print(f"{sr:.1f}")
