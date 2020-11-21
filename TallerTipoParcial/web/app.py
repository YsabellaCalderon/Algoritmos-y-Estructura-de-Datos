from flask import Flask, request, make_response, redirect, render_template, url_for
# se crea un objeto del tipo app
app = Flask(__name__)


@app.route('/')
def baseRoute():
    return render_template('hometaller.html')


@app.route('/doctors')
def doctors():
    return render_template('doctortaller.html')


@app.route('/services')
def services():
    return render_template('servicestaller.html')

@app.route('/about')
def about():
    return render_template('abouttaller.html')

@app.route('/contact')
def contact():
    return render_template('contacttaller.html')

if __name__ == '__main__':
    app.run()