from flask import Flask, request, make_response, redirect, render_template
# se crea un objeto del tipo app
app = Flask(__name__)

@app.route ('/')
def home():
    user_ip = request.remote_addr
    response = make_response(redirect('hello'))
    response.set_cookie('ip',user_ip)
    response.set_cookie('dog','cooper')
    return response


@app.route('/hello')
def helloRoute():
    dog = request.cookies.get('dog')
    ip = request.cookies.get('ip')
    return render_template('hello.html',mascota = dog, userIp = ip)

@app.route('/favorites')
def favoritesRoute():
    return render_template('favorites.html')

if __name__ == '__main__':
    app.run()
