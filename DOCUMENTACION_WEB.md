# Documentación de Inefablestore - Tienda Online de Juegos

## Descripción General

**Inefablestore** es una aplicación web completa para la venta de productos digitales de juegos y gift cards. La aplicación está desarrollada con Flask (Python) y utiliza una interfaz moderna y responsiva.

## Características Principales

### 🎮 Funcionalidades del Usuario
- **Catálogo de productos**: Visualización de juegos y gift cards organizados por categorías
- **Sistema de carrito**: Agregar productos y gestionar compras
- **Autenticación**: Registro e inicio de sesión de usuarios
- **Historial de compras**: Ver órdenes anteriores y su estado
- **Sistema de valoraciones**: Calificar productos comprados
- **Múltiples métodos de pago**: Pago Móvil y Binance
- **Conversión de moneda**: Soporte para VES y USD
- **Interfaz responsiva**: Optimizada para móvil y desktop

### 🛡️ Panel de Administración
- **Gestión de productos**: Crear, editar y eliminar juegos y paquetes
- **Gestión de órdenes**: Ver, procesar y rechazar órdenes
- **Subida de imágenes**: Sistema de gestión de archivos multimedia
- **Configuración del sistema**: Tasas de cambio, métodos de pago, carrusel
- **Notificaciones por email**: Confirmaciones automáticas a usuarios

### 📧 Sistema de Notificaciones
- **Nuevas órdenes**: Notificación al administrador
- **Órdenes completadas**: Confirmación al usuario
- **Gift cards**: Envío de códigos por email
- **Órdenes rechazadas**: Notificación de rechazo con motivos

## Estructura del Proyecto

```
Python12/
├── main.py                 # Aplicación principal Flask
├── sqlite_fallback.py     # Utilidad para SQLite
├── init_db.sql            # Script de inicialización de BD
├── requirements.txt       # Dependencias Python
├── .env.example          # Variables de entorno ejemplo
├── static/               # Archivos estáticos
│   ├── app.js           # JavaScript frontend
│   ├── styles.css       # Estilos CSS
│   └── images/          # Imágenes subidas
├── templates/           # Plantillas HTML
│   ├── index.html      # Página principal
│   ├── admin.html      # Panel administración
│   └── admin_login.html # Login admin
└── attached_assets/     # Archivos adjuntos
```

## Tecnologías Utilizadas

### Backend
- **Flask 3.1.1**: Framework web principal
- **SQLAlchemy 2.0.41**: ORM para base de datos
- **PostgreSQL/SQLite**: Base de datos (adaptable)
- **Werkzeug**: Utilidades web y seguridad
- **python-dotenv**: Gestión de variables de entorno

### Frontend
- **HTML5/CSS3**: Estructura y estilos
- **JavaScript Vanilla**: Interactividad
- **Diseño Responsivo**: Mobile-first approach
- **PWA Ready**: Optimizado para aplicaciones web progresivas

### Funcionalidades Adicionales
- **Pillow**: Procesamiento de imágenes
- **SMTP**: Envío de emails
- **Flask-Cors**: Manejo de CORS
- **Gunicorn**: Servidor WSGI para producción

## Base de Datos

### Tablas Principales

#### `juegos`
- Almacena información de productos (juegos y gift cards)
- Campos: id, nombre, descripción, imagen, categoría, orden, etiquetas

#### `paquetes`
- Paquetes/precios de cada juego
- Campos: id, juego_id, nombre, precio, orden, imagen

#### `ordenes`
- Órdenes de compra de usuarios
- Campos: id, juego_id, paquete, monto, usuario_email, usuario_id, usuario_telefono, metodo_pago, referencia_pago, estado, fecha, codigo_producto

#### `usuarios`
- Información de usuarios registrados
- Campos: id, nombre, email, telefono, password_hash, es_admin, fecha_registro

#### `valoraciones`
- Sistema de calificaciones de productos
- Campos: id, juego_id, usuario_email, calificacion, comentario, fecha

#### `imagenes`
- Gestión de archivos multimedia
- Campos: id, tipo, ruta

#### `configuracion`
- Configuración global del sistema
- Campos: id, campo, valor

## API Endpoints

### Públicos
- `GET /` - Página principal
- `GET /productos` - Lista de productos
- `GET /config` - Configuración pública
- `POST /orden` - Crear nueva orden
- `POST /registro` - Registrar usuario
- `POST /login` - Iniciar sesión
- `POST /logout` - Cerrar sesión
- `GET /usuario` - Información del usuario
- `GET /usuario/historial` - Historial de compras

### Valoraciones
- `POST /valoracion` - Crear/actualizar valoración
- `GET /valoraciones/<juego_id>` - Valoraciones de un producto
- `GET /valoracion/usuario/<juego_id>` - Valoración del usuario

### Administración (requiere autenticación admin)
- `GET /admin` - Panel de administración
- `GET /admin/ordenes` - Lista de órdenes
- `PATCH /admin/orden/<id>` - Actualizar orden
- `PATCH /admin/orden/<id>/rechazar` - Rechazar orden
- `GET /admin/productos` - Lista de productos
- `POST /admin/producto` - Crear producto
- `PUT /admin/producto/<id>` - Actualizar producto
- `DELETE /admin/producto/<id>` - Eliminar producto
- `GET /admin/imagenes` - Lista de imágenes
- `POST /admin/imagenes` - Subir imagen
- `POST /admin/imagenes/bulk` - Subida masiva
- `DELETE /admin/imagen/<id>` - Eliminar imagen
- `GET /admin/config` - Configuración
- `PUT /config` - Actualizar configuración

## Variables de Entorno

```env
# Base de datos
DATABASE_URL=postgresql://user:pass@host:port/db
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=inefablestore

# Aplicación
SECRET_KEY=tu_clave_secreta_muy_segura
PORT=5000

# Email
GMAIL_APP_PASSWORD=tu_password_de_aplicacion_gmail

# Admin por defecto
ADMIN_EMAIL=admin@inefablestore.com
ADMIN_PASSWORD=admin123
```

## Características de Seguridad

- **Autenticación de sesiones**: Sistema seguro de login
- **Hash de contraseñas**: Usando Werkzeug
- **Validación de archivos**: Solo imágenes permitidas
- **Sanitización de nombres**: Archivos seguros
- **Protección CSRF**: Headers de seguridad
- **Validación de permisos**: Decoradores para admin

## Flujo de Compra

1. **Usuario navega** el catálogo de productos
2. **Selecciona producto** y paquete deseado
3. **Agrega al carrito** y procede al pago
4. **Selecciona método de pago** (Pago Móvil/Binance)
5. **Ingresa referencia** de pago realizado
6. **Administrador procesa** la orden
7. **Usuario recibe confirmación** por email
8. **Para gift cards**: Código enviado por email

## Instalación y Configuración

### Requisitos
- Python 3.8+
- PostgreSQL o SQLite
- Cuenta Gmail con contraseña de aplicación

### Pasos de Instalación
1. Clonar repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Configurar variables de entorno
4. Inicializar base de datos: `python main.py`
5. Ejecutar aplicación: `python main.py`

## Optimizaciones Implementadas

- **Lazy loading** de imágenes
- **Cache busting** para archivos estáticos
- **Compresión de imágenes** automática
- **Consultas optimizadas** con JOINs
- **Limpieza automática** de órdenes antiguas
- **Responsive design** mobile-first
- **PWA ready** con service workers

## Mantenimiento

- **Limpieza automática**: Mantiene solo 40 órdenes por usuario
- **Logs detallados**: Para debugging y monitoreo
- **Backup recomendado**: Base de datos y carpeta de imágenes
- **Monitoreo de emails**: Verificar envío de notificaciones

## Soporte y Contacto

- **Facebook**: https://www.facebook.com/InefablestoreR
- **Instagram**: https://www.instagram.com/inefable_store_12/
- **WhatsApp**: +58 412-571-2917

---

*Documentación actualizada: Enero 2025*
*Versión: 2.0*
