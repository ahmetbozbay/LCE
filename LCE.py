file1 = open('A.txt',"r")
file2 = open('B.txt',"r")

A = file1.read()
B = file2.read()


def LCE(A,B,i,j):
    t = 0
    i = i-1
    j = j-1
    length_A = len(A)
    length_B = len(B)
    if(i>=length_A or j>=length_B):
        return 0
    while((i+t<length_A) and (j+t<length_B) and (A[i+t]==B[j+t])):
        t=t+1
    return t


print(LCE(A,B,1,6))


def lcp(a,b):
    length = 0
    la = len(a)
    lb = len(b)
    while(length<la and length<lb and a[length]==b[length]):
        length+=1
    return length


# In[118]:


# find suffix array
SA1 = dict()
SA2 = dict()
SA = dict()
for p in range(len(A)):
    SA1[str(p+1)+'a'] = A[p:]
for p in range(len(B)):
    SA2[str(p+1)+'b'] = B[p:]

SA = SA1
SA.update(SA2)
SA = dict(sorted(SA.items(), key=lambda x:x[1]))
idx = list(SA.keys())

# find longest common prefix array
LCP = [0 for p in range(len(SA))]
for p in range(1,len(SA)):
    LCP[p] = lcp(SA[idx[p-1]],SA[idx[p]])


def LCE2(A,B,i,j):
    # find RMQ indices
    if(i>len(A) or j>len(B)):
        return 0
    global LCP
    x = idx.index(str(i)+'a')+1
    y = idx.index(str(j)+'b')+1
    if(x<y):
        return min(LCP[x:y])
    elif(x>y):
        return min(LCP[y:x])
    else:
        return LCP[x]


print(LCE2(A,B,1,6))
