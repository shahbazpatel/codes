import json
import time
f=open("inp.json",'r')
s=f.read()
print (s)
x = json.loads(s).get("x")
y = json.loads(s).get("y")
c=0
n=int(input("Enter the chessboard size: "))
#n=8
def check(a,i):
        for j in range(i):
                if a[j]==a[i]:
                        return False
                if abs(a[j]-a[i])==abs(j-i):
                        return False
        return True
def solve(a,i,n):
        global c
        if i==n:
                if a[x-1]==y:
                        print '\n'
                        print a,'\n'
                        print '+'*(2*(n+1)+1)
                        for i in range(n):
                                print '|',
                                for j in range(n):
                                        if j==a[i]-1:
                                                print 'Q',
                                                if j==n-1:
                                                        print '|'
                                        else:
                                                print '.',
                                                if j==n-1:
                                                        print '|'
                        print '+'*(2*(n+1)+1)
                        c+=1                                                   
                return
        for it in range(1,n+1):
                #print a
                if c==1:
                        break
                a[i]=it
                if check(a,i):
                        solve(a,i+1,n)
				  

solve([0 for i in range(n)],0,n)
#print("\nTotal ",count," solutions for N =",n)
