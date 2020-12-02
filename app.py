from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
# import os
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.tpl")


@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')
    if username and room:
        return render_template('chat.tpl')
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
