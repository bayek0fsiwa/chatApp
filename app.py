from flask import Flask
from flask import app

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello There!'


if __name__ == '__main__':
    app.run(debug=True)