
from bottle import run, route, static_file, request, template
from bitstring import BitArray
'''
    Returns m * r using Booth's algorithm.
    x = len(m) and y = len(r). Note that this is the length in base 2.
    See http://en.wikipedia.org/wiki/Booth%27s_algorithm
'''

def booth(m, r, x, y):
# Initialize
    totalLength = x + y + 1
    # mA = bitarray(int = m, length = totalLength)
    # rA = bitarray(int = r, length = totalLength)
    A = BitArray(int = m, length = totalLength) << (y+1)
    S = BitArray(int = -m, length = totalLength) << (y+1)
    P = BitArray(int = r, length = y)
    P.prepend(BitArray(int = 0, length = x))
    P = P << 1	
    print "Initial values"
    print "A", A.bin
    print "S", S.bin
    print "P", P.bin
    print "Starting calculation"
    for i in range(1, y+1):
        if P[-2:] == '0b01':
            P = BitArray(int = P.int + A.int, length = totalLength)
            print "P + A:", P.bin
        elif P[-2:] == '0b10':
            P = BitArray(int = P.int +S.int, length = totalLength)
            print "P + S:", P.bin
        P = arith_shift_right(P, 1)
        print "P >> 1:", P.bin
    P = arith_shift_right(P, 1)
    print "P >> 1:", P.bin
    return P.int

def arith_shift_right(x, amt):
    l = x.len
    x = BitArray(int = (x.int >> amt), length = l)
    return x

@route('/login')
def login():
    return template('boothgui')


@route('/login', method='POST')
def do_login():
    n1 = request.forms.get('num1')
    n2 = request.forms.get('num2')
    m, r = int(n1), int(n2)
    x, y = 40, 40
    n3 = booth(m, r, x, y)
    #response.forms.put(n3)
    return '''<h1>The result is {ans}</h1>
              <a href="/login">Go Back to Main Page
              </a>'''.format(ans=n3)

run(host='127.0.0.1', port=8080)
