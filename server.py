from ast import Num
from crypt import methods
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key ='cualquier cosa que sea secreta' #Codigo de seguridad, se usa con session/si se cambia y reinicia el servidor los usuarios desloguean



@app.route('/') 
def count():
    if 'counter' in session:
        session['counter']+=1 # Para sumar de +1
    else:
        session['counter'] = 1 # Para regresa a 1
    return render_template('index.html')

@app.route('/destroy_session', methods=['GET'])
def destroy():
    session.clear()
    return redirect('/') #Permite regresar al index con el conteo a 1 (eliminado la sesion)

if __name__=="__main__":
    app.run(debug=True)