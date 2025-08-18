from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bienvenido a Servi Cool ZA-SA - Tu solución en aires acondicionados.'

@app.route('/acerca')
def acerca():
    return 'En Servi Cooll ZA-SA nos dedicamos a la venta, instalación y reparación de aires acondicionados.'

@app.route('/contacto')
def contacto():
    return 'Llámanos al 0996173679 o escríbenos a servicoolzasa@gmail.com'

@app.route('/servicios')
def servicios():
    return 'Nuestros servicios: venta de equipos (12, 18 y 24 kBTU), repuestos, instalación y mantenimiento.'

if __name__ == '__main__':
    app.run(debug=True)
