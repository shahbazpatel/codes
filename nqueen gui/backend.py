from bottle import route, run, request, template
import os

@route('/solve')

def sorter():
    return template('gui')


@route('/solve', method='POST')
def sorter():
	size = request.forms.get('size')
	print type(size)
	os.system("echo '%s' | python3 nqueen.py > output.txt"%str(size))
	g=''
	for i in open('output.txt','r').readlines():
		g+=i.rstrip('\n')+'<br>'
	#print g
	return '''<h1>The solutions is </h1>
		<h2> {put} </h2>
		<a href="/solve">Go Back to Sort
		</a>'''.format(put=g)
run(host="localhost", port=8123)
