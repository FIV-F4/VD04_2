from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def ind():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contacts')
def about():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()
