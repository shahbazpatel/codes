#from bottle import run, route, request, template
from flask import *
import os
import logging

def bina(n,length):
    if n<0:
        temp='0'*(length-len(bin(n)[3:]))+bin(n)[3:]
        temp=compl(temp)
        return temp
    else:
        return '0'*(length-len(bin(n)[2:]))+bin(n)[2:]

def ars(n):
    return(n[0]+n[0:len(n)-1])

def compl(n):
    carry=0
    n=list(n)
    for i in range(len(n)):
            if n[i]=='1':n[i]='0'
            else: n[i]='1'
    if n[-1]=='1':
            n[-1]='0'
            carry=1
    else: n[-1]='1'
    for i in range(len(n)-2,-1,-1):
            if n[i]=='1' and carry==1:
                    n[i]='0'
                    carry=1
            elif n[i]=='0' and carry==1:
                    n[i]='1'
                    carry=0
            elif n[i]=='1' and carry==0:
                    pass
            elif n[i]=='0' and carry==0:
                    pass
    return ''.join(i for i in n)

def booth(x,y,length=20):
    negx=-x
    x=bina(x,length)
    y=bina(y,length)
    negx=bina(negx,length)
    n=len(x)
    l='0'
    A=x+'0'*length+l
    S=negx+'0'*length+l
    P='0'*length+y+l
    print(" A\t: {}\n S\t: {}\n P\t: {}\n\n".format(A,S,P))
    while(n):
        #print(n,P[-2:])
        if P[-2:]=='00':
            P=ars(P)
            print(" P >> 1 :",P[:20],P[20:-1],P[-1])
            n-=1
        elif P[-2:]=='11':
            P=ars(P)
            print(" P >> 1 :",P[:20],P[20:-1],P[-1])
            n-=1
        elif P[-2:]=='01':
            P=bina(int(A,2)+int(P,2),2*length)
            if len(P)>(2*length+1):
                P=P[1:]
            print(" P + A  :",P[:20],P[20:-1],P[-1])
            P=ars(P)
            print(" P >> 1 :",P[:20],P[20:-1],P[-1])
            n-=1
        elif P[-2:]=='10':
            P=bina(int(S,2)+int(P,2),2*length)
            if len(P)>(2*length+1):
                P=P[1:]
            print(" P + S  :",P[:20],P[20:-1],P[-1])
            P=ars(P)
            print(" P >> 1 :",P[:20],P[20:-1],P[-1])
            n-=1
    if P[0]=='1':        
        #print(" Final value:",-int(compl(P[:len(P)-1]),2))
        return -int(compl(P[:len(P)-1]),2)
    else:
        #print(" Final value:",int(P[:len(P)-1],2))
        return int(P[:len(P)-1],2)

app=Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/index')
def f():
    return render_template('index.html')

port = os.getenv('VCAP_APP_PORT', '5000')

@app.route('/index', methods=['POST'])
def g():
    # num1 and num2 are the names of the input fields in my index.html
    x = int(request.form['num1'])
    y = int(request.form['num2'])
    # to get the address of client trying to connect with me
    #client_ip = request.environ.get('REMOTE_ADDR')
    #print('Received connection from', client_ip)
    #x, y = int(n1), int(n2)
    n3 = booth(x, y)
    return "<p>The result is : "+str(n3)+' </p><a href="/index">Back to index</a>'

if __name__=="__main__":
    app.run(host='0.0.0.0',port=int(port))
