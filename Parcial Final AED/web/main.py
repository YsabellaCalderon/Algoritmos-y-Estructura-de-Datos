from flask import Flask, request, make_response, redirect, render_template, url_for
# se crea un objeto del tipo app
app = Flask(__name__)


@app.route('/')
def baseRoute():
    return render_template('homeparcial.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404parcial.html')

@app.route('/pacientes')
def pacientes():
    return render_template('pacientesparcial.html')


@app.route('/doctores')
def doctores():
    return render_template('doctoresparcial.html')

@app.route('/conocenos')
def conocenos():
    return render_template('conocenosparcial.html')

@app.route('/contactanos')
def contactanos():
    return render_template('contactanosparcial.html')

@app.route('/curioso')
def curioso():
    return render_template('curiosoparcial.html')  

if __name__ == '__main__':
    app.run()