
from bottle import route, run, request, template
from odd_even_sort import oddevensort


@route('/sort')

def sorter():
    return template('gui')

@route('/sort', method='POST')

def sorter():
    
    num_to_sort = request.forms.get('num_input')
    try:
        
        num_to_sort = [int(i) for i in num_to_sort.split()]
        num_to_sort = oddevensort(num_to_sort)
        
        num_to_sort = ' '.join([str(i) for i in num_to_sort])
        print 'Numbers have been sorted'

        return '''<h1>The sorted list is {num_list}</h1>
                  <a href="/sort">Go Back to Sort
                  </a>'''.format(num_list=num_to_sort)
    except:
        print 'Error in input :', num_to_sort
        
        if ',' in num_to_sort:
            print 'User entered comma as the delimiter.'
        else:
            print 'User entered other characters in the input!'
        return '''<h1>The input wasn't given correctly.
                  Please enter space seperated numeric values!</h1>
                  <a href="/sort">Go Back to Sort</a>'''

run(host="localhost", port=8080)



