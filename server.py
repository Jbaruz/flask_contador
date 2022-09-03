from crypt import methods
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key ='cualquier cosa que sea secreta' #Codigo de seguridad, se usa con session/si se cambia y reinicia el servidor los usuarios desloguean


@app.route('/', methods=['GET'])
def count():
    if 'counter' in session and 'visits' in session:
        session['visits']+=1
        session['counter']+=1 # Para sumar de +1
    else:
        session['visits']=1
        session['counter'] = 1 # Para regresa a 1
    return render_template('index.html')

@app.route('/destroy_session', methods=['GET'])
def destroy():
    session.clear()
    return redirect('/') #Permite regresar al index con el conteo a 1 (eliminado la sesion)

@app.route('/count_by_two', methods=['GET'])
def count_x_two():
    session['counter']+=2 # Para sumar de +2
    return render_template('/index.html')

@app.route('/add_by', methods=['POST'])
def count_by_num():
    num=request.form['counter'] #Agrego counter porque necesito info de la session inicial('/')
    session['counter']+=int(num)
    return render_template('/index.html')

if __name__=="__main__":
    app.run(debug=True)