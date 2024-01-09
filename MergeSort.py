def TwoWaySort(a,b):
    i,j=0,0
    c=[]
    
    while(i<=len(a)-1 and j<=len(b)-1):
        if(a[i]<b[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    
    for i in range(i, len(a)):
        c.append(a[i])
    for j in range(j, len(b)):
        c.append(b[j])
    print(c)
    return c

def mergesort(a,l,h):
    if(l<h):
        mid=(l+h)//2
        print(a[l],a[mid],a[h])
        mergesort(a,l,mid)
        mergesort(a,mid+1,h)
        a[l:h+1] = TwoWaySort(a[l:mid+1],a[mid+1:h+1])
        return a[l:h+1]
        
    
a = [9,3,7,5,6,4,8,2]
l=0
h=len(a)-1
print(mergesort(a,l,h))
