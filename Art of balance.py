# cook your dish here
for _ in range(int(input())):
    st=input().upper()
    lst=len(st)
    s=set(st)
    c=[]
    min_avg=999999
    min_i=0
    min_c=0
    for i in s:
        c.append(st.count(i))
    c.sort()
    c.reverse()
    l=len(c)
    #print(c)
    i=1
    f=[]
    #print(f)
    while i<=26 and i<=l:
       if lst%i==0:
           f.append(i)
       i+=1
    #print(f)
    for i in f:
        #print("for i="+str(i))
        comp=lst//i
        #print("comp="+str(comp))
        diff=0
        avg=0
        for j in range(i):
            #print("for j="+str(j),end=" ")
            diff+=abs(comp-c[j])
            avg+=diff
            #print(diff)
        #avg=diff/i
        #print(avg)
        if avg<min_avg:
            min_avg=avg
            min_i=i
            min_c=comp
    #print("min i="+str(i))
    for i in range(l):
        if i<=min_i-1:
            c[i]=float(min_c-c[i])

    #print(c)
    #c=[abs(x) for x in c]
    #print(int(sum(c)/2))
    nebe = 0
    debe2 = 0
    debe1 = 0
    for i in c:
        if i > 0:
            if type(i) == float:
                nebe += abs(i)
            if type(i) == int:
                debe2 += abs(i)
        elif i < 0:
            debe1 += abs(i)
    if nebe == debe1 + debe2:
        print(int(nebe))
    elif nebe < debe1 + debe2:
        print(int(debe1 + debe2))
