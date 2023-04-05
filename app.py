from flask import Flask, render_template, request
import sys

app = Flask(__name__)
frame_r = 0

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)