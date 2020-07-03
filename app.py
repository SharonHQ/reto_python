from flask import Flask 
import requests
from flask import render_template

app = Flask(__name__)

#Añadimos la ruta /math/numero 
@app.route('/math/<numero>', methods=['GET'])
#Pasamos el parametro numero
def math(numero):
	#Llamando al api de curiosidades numericas
	r=requests.get('http://numbersapi.com/'+numero)
	#Pasamos el texto que devuelve el api a una variable result
	result=r.text
	#Enviamos el valor result al documento math.html
	return render_template('math.html', result=result)