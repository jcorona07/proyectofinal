from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import requests

app = Flask(__name__)

'''
db_config = {
    'host': 'localhost',  
    'user': 'root',
    'password': '',
    'database': 'auto', 
}

# Función para realizar la consulta a la base de datos
def obtener_resultados():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    consulta = "SELECT * FROM auto"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

# URL de la API
url = "https://api.escuelajs.co/api/v1/products?limit=5&offset=1"

def get_data():

    # Realizar la solicitud GET
    response = requests.get(url)

# Verificar que la solicitud fue exitosa
    if response.status_code == 200:
    # Convertir la respuesta a JSON
        data = response.json()

    # Ahora puedes trabajar con los datos
        print(data)
        return data
    else:
        print(f"Error: {response.status_code}")

'''

# Creating simple Routes ____________________________________________________________________________________________
@app.route('/test')
def test():
    return "inicio Page"

@app.route('/test/acerca/')
def acerca_test():
    return "acerca Page"

@app.route('/test/contactos/')
def contact_test():
    return "contactos Page"


@app.route('/test/portafolio/')
def portafolio_test():
    return "portafolio Page"

@app.route('/test/servicios/')
def servicios_test():
    return "servicios Page"

@app.route('/test/consulta/')
def consulta_test():
    resultados = obtener_resultados()
    for fila in resultados:
        print(fila)  # Esto imprimirá los resultados en la consola del servidor Flask
    return render_template("consulta.html")

# Routes to Render Something
@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/acerca', strict_slashes=False)
def acerca():
    return render_template("acerca.html")

@app.route('/contactos')
def contactos():
    return render_template("contactos.html")

@app.route('/servicios')
def servicios():
    resultados=get_data()
    return render_template("servicios.html", resultados=resultados)

@app.route('/portafolio')
def portafolio():
    return render_template("portafolio.html")

@app.route('/consulta')
def consulta():
    resultados= obtener_resultados()
    return render_template("consulta.html", resultados=resultados)



# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True) 
