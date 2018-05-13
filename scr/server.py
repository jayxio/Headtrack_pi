'''
Created on May 11, 2018

This is a front end program that call the back end python script to count num of people

@author: sadde
'''

from flask import Flask,render_template, request
app = Flask(__name__, template_folder='static')

@app.route('/<n>', methods=['POST','GET'])
def index(n):
    # I tried multi-process within a flask func but didnt work
    # just render a simple web page and use javascript to call REST api from python server shell
    numofpeople = request.args.get('numofpeople','')
    #return numofpeople
    return render_template('index.html', num_of_people=n)#umofpeople)
'''
@app.route('/<order>')
def order(order):
    if order=='forward':
        return 'forward'
    elif order=='left':
        return 'left'
    elif order=='right':
        return 'right'
    elif order=='back':
        return 'back'
    else:
        return order
'''
@app.route('/tmp')
def display():
    num = request.args.get('numofpeople','')
    return num

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)