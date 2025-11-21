from flask import Flask, render_template
from Catalogo_juguetes.rutas import catalogo_bp # Importamos el Blueprint

# --- Configuración de la aplicación ---
def create_app():
    app = Flask(__name__)
    
    # Requisito: Modo debug activado
    app.config['DEBUG'] = True
    
    # Requisito: Registro del Blueprint
    # El 'url_prefix' asegura que todas las rutas del Blueprint comiencen con '/'
    app.register_blueprint(catalogo_bp, url_prefix='/') 
    
    return app

# --- Ejecución del servidor ---
if __name__ == '__main__':
    app = create_app()
    # Ejecutamos con el modo debug (ya configurado en create_app)
    app.run()