N,M=map(int,raw_input().split())
ARR=[]
for i in range(N):
     ARR.append([])
     for j in range(M):
           s=int(raw_input())
           ARR[i].append(s)
print(ARR)
J,K=map(int,raw_input().split())
BRR=[]
for i in range (J):
    BRR.append([])
    for j in range (K):
        p=int(raw_input())
        BRR[i].append(p)
print(BRR)
CRR=[]
if(M==J):
      for i in range (N):
                   CRR.append([])
                   for j in range (K):
                                      sum=0
                                      for k in range (J):
                                                     sum+=ARR[i][k]*BRR[k][j]
                                      CRR[i].append(sum)
      print(CRR)
else:
    print("MULTIPLICATION NOT POSSIBLE")
