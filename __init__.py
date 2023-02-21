from ast import main
from flask import Flask

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello World!'

if __file__ == "__main__":
    app.run(dubug=True)