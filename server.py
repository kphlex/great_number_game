from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = 'key1'


@app.route('/')
def random_int():
    if 'number' and 'guess' not in session:
        session['number'] = random.randint(1, 100)
        session['guess'] = 0
    print(session['number'])
    return render_template('layout.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    print(session['guess'])
    return redirect('/check')


@app.route('/check')
def check():
    if  session['number'] > session['guess']:
        return render_template('low.html')
    
    elif session['number'] < session['guess']:
        return render_template('high.html')
    else:
        return render_template('correct.html')


@app.route('/reset')
def reset_game():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def invalid_request(e):
    return ("Under construction")

if __name__ == '__main__':
    app.run(debug=True)