
from flask import Flask
from .catalogo.vistas import catalogo_bp

app = Flask(__name__)


@app.route('/')
def inicio():
    return '¡Hola, Flask! Esta es mi primera aplicación web.'

# Puedes colocar esta lista al comienzo de tu archivo app.py
# o en un nuevo archivo llamado, por ejemplo, 'datos.py'

juguetes = [
    {
        "id": 1, 
        "nombre": "Robot de Cuerda Vintage", 
        "precio": 15.50, 
        "descripcion": "Clásico robot de metal con mecanismo de cuerda. Altura 10cm, ideal para coleccionistas."
    },
    {
        "id": 2, 
        "nombre": "Set de Construcción 'Ciudad'", 
        "precio": 45.99, 
        "descripcion": "Más de 500 piezas de ladrillos compatibles para construir una pequeña ciudad o lo que imagines."
    },
    {
        "id": 3, 
        "nombre": "Muñeca Articulada 'Aventurera'", 
        "precio": 22.75, 
        "descripcion": "Muñeca de 30cm con 15 puntos de articulación y un set de ropa de exploradora."
    },
    {
        "id": 4, 
        "nombre": "Pista de Coches de Carreras", 
        "precio": 65.00, 
        "descripcion": "Divertida pista con dos mandos, dos coches y un circuito de 5 metros con loopings."
    },
    {
        "id": 5, 
        "nombre": "Puzzle 3D 'Torre Eiffel'", 
        "precio": 18.90, 
        "descripcion": "Puzzle de foam de alta densidad para construir una réplica de la Torre Eiffel. 216 piezas."
    },
    {
        "id": 6, 
        "nombre": "Tren Eléctrico Básico", 
        "precio": 99.99, 
        "descripcion": "Set inicial con locomotora, 3 vagones y circuito de vías ovalado. Escala N."
    },
    {
        "id": 7, 
        "nombre": "Mascota Interactiva 'Perrito'", 
        "precio": 35.20, 
        "descripcion": "Perrito robótico que responde a comandos de voz y caricias. Ladra y camina."
    },
    {
        "id": 8, 
        "nombre": "Kit Científico 'Volcán'", 
        "precio": 12.00, 
        "descripcion": "Experimento didáctico para crear una erupción volcánica segura con bicarbonato y vinagre."
    },
    {
        "id": 9, 
        "nombre": "Figuras de Acción (Set de 5)", 
        "precio": 28.50, 
        "descripcion": "Colección de 5 héroes de acción con accesorios intercambiables y gran detalle."
    },
    {
        "id": 10, 
        "nombre": "Juego de Mesa 'Colonizadores'", 
        "precio": 55.00, 
        "descripcion": "Juego de estrategia para 3-4 jugadores. Fomenta el comercio y la construcción."
    },
    {
        "id": 11, 
        "nombre": "Pelota Saltarina XL", 
        "precio": 8.95, 
        "descripcion": "Pelota de goma de 75cm con asa para saltar. Color azul brillante."
    },
    {
        "id": 12, 
        "nombre": "Kit de Pintura Acuarela", 
        "precio": 14.30, 
        "descripcion": "Set con 24 pastillas de acuarelas, un pincel y un block de papel especial."
    },
    {
        "id": 13, 
        "nombre": "Helicóptero Teledirigido", 
        "precio": 39.99, 
        "descripcion": "Mini helicóptero con 3 canales, control remoto y batería recargable. Para uso interior."
    },
    {
        "id": 14, 
        "nombre": "Pizarra Mágica LCD", 
        "precio": 11.90, 
        "descripcion": "Tableta de dibujo reutilizable con pantalla LCD sensible a la presión. 8.5 pulgadas."
    },
    {
        "id": 15, 
        "nombre": "Bloques de Madera (100 pcs)", 
        "precio": 32.00, 
        "descripcion": "Caja de 100 bloques de madera natural de diferentes formas y tamaños para juego libre."
    }
]

app.register_blueprint(catalogo_bp)

if __name__ == '__main__':
    app.run(debug=True)