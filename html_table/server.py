from flask import Flask, render_template
from dict import users

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html', users=users)

if __name__=="__main__":
    app.run(debug=True) 