import json
import time

f=open("inp.json",'r')
s=f.read()
print ("Positions: ",s)
x = json.loads(s).get('x')
y = json.loads(s).get('y')
c=0
n=int(input())
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
			print(a,'\n')
			print('. '+'__ '*n)
			for i in range(n):
				print('|',end=' ')
				for j in range(n):
					if j==a[i]-1:
						print('Q',end=' ')
					else:
						print('__',end=' ')
					if j==n-1:
						print('|')
			c+=1                                                   
		return
	for it in range(1,n+1):
		if c==1:break
		a[i]=it
		if check(a,i):
			solve(a,i+1,n)
	  
start=time.time()
solve([0 for i in range(n)],0,n)
print("\nTotal time:",time.time()-start,end='\n\n')
