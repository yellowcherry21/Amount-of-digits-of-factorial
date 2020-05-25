from flask import Flask
from flask import render_template, redirect, url_for, request


def amount_of_digits(m):
    i = 0
    factorial = 1
    while m > 1:
        factorial *= m
        m -= 1

    while factorial > 0:
        factorial //= 10
        i = i + 1
    return i


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def solution():
    if request.method == 'POST':
        number = amount_of_digits(int(request.form['number']))
        return '<h1>Result is: {}</h1>'.format(number)
    return render_template('fact.html')

