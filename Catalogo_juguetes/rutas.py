from flask import Blueprint, render_template, abort

# Definición del Blueprint. El primer argumento es el nombre del Blueprint.
catalogo_bp = Blueprint('catalogo', __name__, template_folder='templates')

# --- Datos (Requisito: 15 elementos) ---
# Usaremos 15 juguetes de ejemplo
juguetes = [
    {"id": 1, "nombre": "Kit de Construcción Estelar", "fabricante": "Bloques Inc.", "edad_min": 8, "descripcion": "Un set de 500 piezas para construir una nave espacial detallada y funcional.", "imagen": "kit_estelar.jpg"},
    {"id": 2, "nombre": "Muñeca Articulada 'Aventurera'", "fabricante": "Sueños Jugueteros", "edad_min": 3, "descripcion": "Muñeca con 12 puntos de articulación y accesorios de exploración para viajes imaginarios."},
    {"id": 3, "nombre": "Robot Programable 'CodeBot'", "fabricante": "TecnoPlay", "edad_min": 10, "descripcion": "Robot educativo que enseña los fundamentos de la programación por bloques."},
    {"id": 4, "nombre": "Pista de Carreras de Lujo", "fabricante": "Velocidad Extrema", "edad_min": 6, "descripcion": "Pista modular con dos coches de alta velocidad y bucles impresionantes."},
    {"id": 5, "nombre": "Set de Magia Principiante", "fabricante": "Ilusión Máxima", "edad_min": 7, "descripcion": "Incluye 15 trucos de magia fáciles de aprender, con varita y capa."},
    {"id": 6, "nombre": "Puzzle 3D 'Torre Eiffel'", "fabricante": "Mundo Puzzles", "edad_min": 12, "descripcion": "Un desafío de 900 piezas para recrear el famoso monumento parisino."},
    {"id": 7, "nombre": "Tabla de Dibujo Luminosa", "fabricante": "ArteCreativo", "edad_min": 4, "descripcion": "Crea dibujos brillantes en la oscuridad con bolígrafos de luz especiales."},
    {"id": 8, "nombre": "Microscopio Científico", "fabricante": "Explora Ciencia", "edad_min": 8, "descripcion": "Microscopio con aumentos de 100x, 400x y 1200x, incluye láminas preparadas."},
    {"id": 9, "nombre": "Cocinita de Madera Premium", "fabricante": "Juego Clásico", "edad_min": 3, "descripcion": "Cocinita de madera maciza con horno, fregadero y accesorios de metal."},
    {"id": 10, "nombre": "Set de Tren Eléctrico", "fabricante": "Vías Rápidas", "edad_min": 6, "descripcion": "Locomotora a escala con luces y sonidos, 12 tramos de vía y un vagón de carbón."},
    {"id": 11, "nombre": "Dron de Iniciación con Cámara", "fabricante": "Aéreo Tech", "edad_min": 14, "descripcion": "Fácil de volar, ideal para principiantes, con cámara HD para grabar tus vuelos."},
    {"id": 12, "nombre": "Juego de Mesa 'Colonizadores'", "fabricante": "Estrategia Diversión", "edad_min": 10, "descripcion": "Juego de estrategia para 3-4 jugadores, comercio y construcción de civilizaciones."},
    {"id": 13, "nombre": "Arcos y Flechas de Seguridad", "fabricante": "Aventura Segura", "edad_min": 6, "descripcion": "Set de tiro con arco con ventosas y diana, totalmente seguro para uso interior y exterior."},
    {"id": 14, "nombre": "Batería Musical Infantil", "fabricante": "Ritmo Pequeño", "edad_min": 3, "descripcion": "Set de batería con 5 tambores, platillo y pedal, ideal para empezar con la música."},
    {"id": 15, "nombre": "Taller de Cerámica y Alfarería", "fabricante": "Manos Hábiles", "edad_min": 8, "descripcion": "Torre de alfarero eléctrico con arcilla y herramientas para modelar vasijas."},
]


# 1. Requisito: Ruta principal (/)
@catalogo_bp.route('/')
def index():
    """
    Ruta de inicio que muestra el listado completo de juguetes.
    Renderiza la plantilla 'index.html'.
    """
    # Pasamos 'juguetes' en lugar de 'peliculas'
    return render_template('index.html', elementos=juguetes, titulo="Revista de Juguetes Navideños")

# 2. Requisito: Ruta de detalle (/item/<int:id>)
@catalogo_bp.route('/item/<int:id>')
def detalle(id):
    """
    Ruta de detalle que busca un juguete por ID.
    Renderiza la plantilla 'detalle.html' o devuelve 404.
    """
    # Buscamos en 'juguetes'
    elemento = next((j for j in juguetes if j['id'] == id), None)
    
    if elemento is None:
        # Si no se encuentra, abortamos con el error 404
        abort(404)
        
    return render_template('detalle.html', elemento=elemento, titulo=f"Detalle: {elemento['nombre']}")