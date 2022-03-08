a = int(input())
b = int(input())
n = 1
z=1
c=0

list1=[]
list2=[]
while (n <=b) :
    n=n+n
    a=a+a
    list1.append(n//2)
    list2.append(a//2)
list1=list1[::-1]
list2=list2[::-1]
for i in range(len(list1)) :
    if list1[i]<=b:
        b-=list1[i]        
        c+=list2[i]
print(c)