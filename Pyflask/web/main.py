from flask import Flask, request, make_response, redirect, render_template, url_for
import utilidades as helper
# se crea un objeto del tipo app
app = Flask(__name__)
fileNameCredential = 'users.csv'
data = helper.leerArchivo(fileNameCredential)

@app.route('/')
def baseRoute():
    return redirect(url_for('login'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/home')
def home():
    return render_template('homereto.html')

@app.route('/characters')
def characters():
    return render_template('charactersreto.html')

@app.route('/places')
def places():
    return render_template('placesreto.html')

@app.route('/singin', methods = ['POST','GET'])
def singin():
    data = helper.leerArchivo(fileNameCredential)
    if request.method == 'POST':
        helper.saveUser (data,fileNameCredential,request.form['name'],request.form ['pass'] )
        return redirect(url_for('success'))
    else: 
        return render_template('singIn.html')


@app.route('/login', methods = ['POST','GET'])
def login():
    data = helper.leerArchivo(fileNameCredential)
    if request.method == 'POST':
        nameUser = request.form['name']
        passUser = request.form ['pass']
        output = helper.validatePassword (data, nameUser, passUser)
        if (output == True):
            return  redirect(url_for('home'))
        elif (output == 'Usuario no registrado'):
            return  redirect(url_for('singin'))
        else:
            return 'Falló proceso de autenticación'
    else: 
        return render_template('login.html')


if __name__ == '__main__':
    app.run()