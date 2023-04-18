from flask import Flask, render_template, request
import sys

app = Flask(__name__)
frame_r = 0
news_flag = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/about')
def company():
    return render_template('company.html')


@app.route('/reporting')
def reporting():
    return render_template('reporting.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/questions')
def questions():
    return render_template('questions.html')


@app.route('/legislation')
def legislation():
    return render_template('legislation.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
