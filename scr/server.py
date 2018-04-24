from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('view-stream.html')

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
@app.route('/<userinput>')
def interaction(userinput):
    return userinput
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)