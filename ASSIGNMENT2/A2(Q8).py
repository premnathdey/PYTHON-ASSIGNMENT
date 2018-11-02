#python program for nwc
N,M=map(int,raw_input("enter rows and columns").split())
A=[]
for i in range (N):
    A.append([])
    for j in range (M):
        s=int(raw_input())
        A[i].append(s)
print("Supply")
S=[]
for i in range (N):
    k=int(raw_input())
    S.append(k)
print("Demand")
D=[]
for i in range (M):
    k=int(raw_input())
    D.append(k)
T=0
for i in range (N):
    for j in range (M):
         t=min(S[i],D[j])
         T=T+A[i][j]*t
         S[i]=S[i]-t
         D[j]=D[j]-t
print(T)
