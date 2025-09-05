# Inefablestore - Versión SQLite

Esta es la versión adaptada de Inefablestore para usar únicamente SQLite como base de datos, eliminando la dependencia de PostgreSQL.

## 🚀 Instalación Rápida

### 1. Instalar Dependencias

```bash
pip install -r requirements_sqlite.txt
```

### 2. Configurar Variables de Entorno

```bash
# Copiar el archivo de configuración
cp .env_sqlite .env

# Editar las variables según tus necesidades
nano .env
```

### 3. Ejecutar la Aplicación

```bash
python main_sqlite.py
```

La aplicación estará disponible en: http://localhost:5000

## 📋 Características

### ✅ Funcionalidades Incluidas
- ✅ **Base de datos SQLite** - Sin necesidad de servidor externo
- ✅ **Tienda online completa** - Catálogo, carrito, pagos
- ✅ **Panel de administración** - Gestión de productos y órdenes
- ✅ **Sistema de usuarios** - Registro, login, historial
- ✅ **Notificaciones por email** - Confirmaciones automáticas
- ✅ **Subida de imágenes** - Gestión de archivos multimedia
- ✅ **Sistema de valoraciones** - Calificaciones de productos
- ✅ **Múltiples categorías** - Juegos y Gift Cards
- ✅ **Conversión de moneda** - VES y USD
- ✅ **Interfaz responsiva** - Móvil y desktop

### 🔧 Ventajas de SQLite
- **Sin configuración** - No requiere servidor de base de datos
- **Portabilidad** - Un solo archivo de base de datos
- **Rendimiento** - Excelente para aplicaciones pequeñas/medianas
- **Simplicidad** - Fácil backup y migración
- **Desarrollo local** - Ideal para desarrollo y testing

## 📁 Estructura del Proyecto

```
Python12/
├── main_sqlite.py          # Aplicación principal (SQLite)
├── requirements_sqlite.txt # Dependencias para SQLite
├── .env_sqlite            # Configuración de ejemplo
├── DOCUMENTACION_WEB.md   # Documentación completa
├── README_SQLITE.md       # Este archivo
├── static/               # Archivos estáticos
│   ├── app.js           # JavaScript frontend
│   ├── styles.css       # Estilos CSS
│   └── images/          # Imágenes subidas
├── templates/           # Plantillas HTML
│   ├── index.html      # Página principal
│   ├── admin.html      # Panel administración
│   └── admin_login.html # Login admin
└── inefablestore.db     # Base de datos SQLite (se crea automáticamente)
```

## ⚙️ Configuración

### Variables de Entorno (.env)

```env
# Aplicación
SECRET_KEY=tu_clave_secreta_muy_segura
PORT=5000

# Email (opcional)
GMAIL_APP_PASSWORD=tu_password_de_aplicacion_gmail

# Usuario administrador
ADMIN_EMAIL=admin@inefablestore.com
ADMIN_PASSWORD=admin123
```

### Base de Datos

La base de datos SQLite se crea automáticamente en `inefablestore.db` con:
- **Productos de ejemplo** - Free Fire, PUBG, Call of Duty
- **Usuario administrador** - Según variables de entorno
- **Configuración básica** - Tasas de cambio, métodos de pago

## 🎮 Uso

### Para Usuarios
1. **Navegar** el catálogo de productos
2. **Registrarse** o iniciar sesión
3. **Agregar productos** al carrito
4. **Realizar pago** con Pago Móvil o Binance
5. **Recibir confirmación** por email

### Para Administradores
1. **Acceder** a `/admin` con credenciales de admin
2. **Gestionar productos** - Crear, editar, eliminar
3. **Procesar órdenes** - Aprobar, rechazar, enviar códigos
4. **Subir imágenes** - Individual o masiva
5. **Configurar sistema** - Tasas, métodos de pago

## 🔄 Migración desde PostgreSQL

Si tienes datos en PostgreSQL y quieres migrar a SQLite:

1. **Exportar datos** de PostgreSQL
2. **Adaptar formato** para SQLite
3. **Importar** usando el script de inicialización
4. **Verificar** integridad de datos

## 🛠️ Desarrollo

### Estructura de la Base de Datos

```sql
-- Tablas principales
juegos          -- Productos (juegos y gift cards)
paquetes        -- Precios y opciones de cada producto
ordenes         -- Compras de usuarios
usuarios        -- Cuentas de usuario
valoraciones    -- Calificaciones de productos
imagenes        -- Archivos multimedia
configuracion   -- Configuración del sistema
```

### API Endpoints

- `GET /productos` - Lista de productos públicos
- `POST /orden` - Crear nueva orden
- `GET /admin/ordenes` - Lista de órdenes (admin)
- `PATCH /admin/orden/<id>` - Actualizar orden (admin)
- Ver documentación completa en `DOCUMENTACION_WEB.md`

## 🔒 Seguridad

- **Autenticación** de sesiones segura
- **Hash de contraseñas** con Werkzeug
- **Validación de archivos** solo imágenes
- **Sanitización** de nombres de archivo
- **Protección CSRF** con headers seguros

## 📧 Notificaciones por Email

Configurar Gmail App Password para:
- **Nuevas órdenes** - Notificación al admin
- **Órdenes completadas** - Confirmación al usuario
- **Gift cards** - Envío de códigos
- **Órdenes rechazadas** - Notificación de rechazo

## 🚀 Despliegue

### Desarrollo Local
```bash
python main_sqlite.py
```

### Producción
```bash
# Usar Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main_sqlite:app

# O configurar con systemd/supervisor
```

## 📊 Rendimiento

SQLite es ideal para:
- **< 100,000 productos**
- **< 1,000 usuarios concurrentes**
- **Aplicaciones de lectura intensiva**
- **Desarrollo y testing**

Para mayor escala, considera migrar a PostgreSQL usando `main.py`.

## 🆘 Solución de Problemas

### Base de datos bloqueada
```bash
# Verificar procesos que usan la BD
lsof inefablestore.db

# Reiniciar aplicación
```

### Permisos de archivos
```bash
# Dar permisos a la carpeta de imágenes
chmod 755 static/images/
```

### Error de email
- Verificar `GMAIL_APP_PASSWORD`
- Habilitar verificación en 2 pasos en Gmail
- Usar contraseña de aplicación, no contraseña normal

## 📞 Soporte

- **Documentación**: `DOCUMENTACION_WEB.md`
- **Issues**: Reportar en el repositorio
- **Email**: Configurar en variables de entorno

---

**Versión SQLite - Enero 2025**
*Adaptación completa para base de datos local*
