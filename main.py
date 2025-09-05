"""
Punto de entrada principal para la aplicación Inefable Store
Este archivo importa la aplicación Flask desde main_sqlite.py para compatibilidad con Render
"""

from main_sqlite import app

if __name__ == '__main__':
    # Solo para desarrollo local
    import os
    port = int(os.environ.get('PORT', 5000))
    print(f'🚀 Iniciando servidor en puerto {port}')
    app.run(host='0.0.0.0', port=port, debug=False)
