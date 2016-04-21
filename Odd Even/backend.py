# to learn more about bottle visit their site -> bottlepy.org
# to run the code you must have the bottle library installed
# install bottle by using 'pip install bottle'
# run the code as python backend.py
# then open your browser and go to the url -> '127.0.0.1:8080/sort'
from bottle import route, run, request, template
from odd_even_sort import oddevensort
# @route is a decorator in python which is like a function which we use
# to tell what the server should do when a user comes to the /sort page,
# which in this case is display the gui.html page
@route('/sort')
# specify any random function name here
def sorter():
    # return the html page gui.html
    # template is a function that helps display the html page
    return template('gui')

# define what the server should do when a user comes to the /sort page after
# pressing the submit button on the form i.e. method='POST', which in this
# case is to show the result
@route('/sort', method='POST')
# specify any random function name here
def sorter():
    # get the contents of the element of the name 'num_input' in the 'html'
    num_to_sort = request.forms.get('num_input')
    try:
        # convert string of numbers to integers
        num_to_sort = [int(i) for i in num_to_sort.split()]
        num_to_sort = oddevensort(num_to_sort)
        # convert sorted numbers to a string
        num_to_sort = ' '.join([str(i) for i in num_to_sort])
        print 'Numbers have been sorted'
        # format replaces the num_list variable with the value which is
        # in num_to_sort; the curly brackets represent the variable to
        # be replaced
        return '''<h1>The sorted list is {num_list}</h1>
                  <a href="/sort">Go Back to Sort
                  </a>'''.format(num_list=num_to_sort)
    except:
        print 'Error in input :', num_to_sort
        # the if and else print statements get displayed in the command-line
        if ',' in num_to_sort:
            print 'User entered comma as the delimiter.'
        else:
            print 'User entered other characters in the input!'
        return '''<h1>The input wasn't given correctly.
                  Please enter space seperated numeric values!</h1>
                  <a href="/sort">Go Back to Sort</a>'''
# run web app at ip address 127.0.0.1 which is localhost, and at port 8080
# if you want to change anything in the app then stop it by pressing
# command+c at terminal, make changes and run the program again
if __name__=="__main__":
    run(host="localhost", port=8080)
# if you want to style the html, you can add css to the gui.html file
# using the style tag and also style the html written inside the return
# calls by using the style attribute
