#magic square

'''n=int(input())
sq=[[0]*n for i in range(n)]
num=1
i=n//2
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if sq[i][j]:
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
for i in sq:
    print(i)
for i in sq:
    print(*i)
print('magic constant',n*((n*n)+1)//2)
    
    
#magic square recursive

def generate_sq(n):
    sq=[[0]*n for i in range(n)]
    def fill(i,j,num):
        if num>(n*n):
            return sq
        if i<0 and j==n:
            i=0
            j=n-2
        else:
            if i<0:
                i=n-1
            if j==n:
                j=0
        if sq[i][j]:
            i=i+1
            j=j-2
            return fill(i,j,num)
        sq[i][j]=num
        return fill(i-1,j+1,num+1)
    return fill(n//2,n-1,1)
n=int(input())
l=generate_sq(n)
for i in l: 
    print(*i)

#check subsets_target sum
def check_subset(nums,target):
    def backtrack(start,sum):
        if sum==target:
            return True
        if sum>target or start==len(nums):
            return False
        if backtrack(start+1,sum+nums[start]):
            subset.append(nums[start])
            return True
        return backtrack(start+1,sum)
    subset=[]
    if backtrack(0,0):
       return True  , subset
    else:
        return False, []
nums=[1,2,3,4]
target=9
bool, subset=check_subset(nums,target)
if bool:
    print('print subset with sum',target,'exists:',subset)
else:
    print('no subset with sum')

#bubble sort
l=list(map(int,input().split()))
n=int(input())
for i in range(1,n):
    for j in range(n-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]


n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
flag=False
for i in range(1,n):
    for j in range(n-i):
        if l[j]>l[j+1]:
            flag=True
            l[j],l[j+1]=l[j+1],l[j]
    if flag==False:
        break
    flag=False
print(l)


#selection sort
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if l[j]<l[min]:
            min=j
    l[i],l[min]=l[min],l[i]
print(l)'''

#insertion sort
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)



