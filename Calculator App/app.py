from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send',methods=['POST'])
def send(sum = sum):
    if request.method == 'POST':
        firstNumber = request.form['first']
        secondNumber = request.form['second']
        operations = request.form['operation']

        if operations == 'add':
            sum = float(firstNumber) + float(secondNumber)
            return render_template('app.html' , sum = sum)
        elif operations == 'subtract':
            sum = float(firstNumber) - float(secondNumber)
            return render_template('app.html' , sum = sum)
        elif operations == 'multiply':
            sum = float(firstNumber) * float(secondNumber)
            return render_template('app.html' , sum = sum)
        elif operations == 'divide':
            sum = float(firstNumber) / float(secondNumber)
            return render_template('app.html' , sum = sum)
        else:
            return render_template('app.html')
