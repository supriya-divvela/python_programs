n,x,y=map(int,input().split())
l=[[0 for i in range(n)]for j in range(n)]
c=1
l[0][0]=1
for i in range(1,n):
    if i%2!=0:
        j=[i,0]
        while 1:
            if l[j[0]][j[1]]==0:
                c+=1
                l[j[0]][j[1]]=c
                if j==[0,i]:
                    break
            j[1]+=1
            j[0]-=1
    else:
        j=[0,i]
        while(1):
            if l[j[0]][j[1]]==0:
                c+=1
                l[j[0]][j[1]]=c
                if j==[i,0]:
                    break
            j[1]-=1
            j[0]+=1
for i in range(1,n):
    if i%2!=0:
        j=[i,n-1]
        while 1:
            if l[j[0]][j[1]]==0:
                c+=1
                l[j[0]][j[1]]=c
                if j==[n-1,i]:
                    break
            j[1]-=1
            j[0]+=1
    else:
        j=[n-1,i]
        while(1):
            if l[j[0]][j[1]]==0:
                c+=1
                l[j[0]][j[1]]=c
                if j==[i,n-1]:
                    break
            j[1]+=1
            j[0]-=1
[print(*i) for i in l]
print(l[x][y])
'''
input :
9 1 2
output:
1 3 4 10 11 21 22 36 37
2 5 9 12 20 23 35 38 46
6 8 13 19 24 34 39 47 60
7 14 18 25 33 40 48 59 61
15 17 26 32 41 49 58 62 71
16 27 31 42 50 57 63 70 72
28 30 43 51 56 64 69 73 78
29 44 52 55 65 68 74 77 79
45 53 54 66 67 75 76 80 81
9



input 2:
8 5 6
output:
1 3 4 10 11 21 22 36
2 5 9 12 20 23 35 37
6 8 13 19 24 34 38 49
7 14 18 25 33 39 48 50
15 17 26 32 40 47 51 58
16 27 31 41 46 52 57 59
28 30 42 45 53 56 60 63
29 43 44 54 55 61 62 64
57
'''
