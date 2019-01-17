from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')

@app.route('/login', methods = ['GET', 'POST'])
def hello_world():
    if me == 'POST':

    return render_template('login.html')


host = 'localhost'
port = 9999


if __name__ == '__main__':
    app.run(host, port, debug=True)
