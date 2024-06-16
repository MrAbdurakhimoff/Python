def IsPrime(son):
    tublar=[]
    for x in range(1,son+1):
        tub=True
        if x==1:
            tub=False
        elif x==2:
            tub=True
        else:
            for n in range(2,x):
                if x%n==0:
                    tub=False
        if tub:
            tublar.append(x)
    if son in tublar:
        qiymat=True
    else:
        qiymat=False
    return qiymat



a = [1,2,3,'a','i','b','q','t','@','#','в', '‱']
a1 = a.copy()

son = '0123456789'
unli_ = 'aioeu'
undosh_ = 'bqt'

unli = []
undosh = []
num = []
symbol = []

for x in a1:
    i = str(x)
    if i in unli_:
        unli.append(i)
        a.remove(i)
    elif i in undosh_:
        undosh.append(i)
        a.remove(i)
    elif i in son:
        num.append(int(i))
        a.remove(int(i))
    else:
        symbol.append(i)
        a.remove(i)

print(f'{unli}\n{undosh}\n{num}\n{symbol}')









