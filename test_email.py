#!/usr/bin/env python3
"""
Script de prueba para diagnosticar el sistema de notificaciones por Gmail
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_gmail_connection():
    """Prueba la conexión y configuración de Gmail"""
    
    print("🔧 DIAGNÓSTICO DEL SISTEMA DE NOTIFICACIONES GMAIL")
    print("=" * 60)
    
    # Verificar variables de entorno
    print("\n1. 📋 VERIFICANDO VARIABLES DE ENTORNO:")
    
    gmail_password = os.environ.get('GMAIL_APP_PASSWORD')
    admin_email = os.environ.get('ADMIN_EMAIL')
    
    print(f"   ADMIN_EMAIL: {admin_email}")
    print(f"   GMAIL_APP_PASSWORD: {'✅ Configurada' if gmail_password else '❌ NO CONFIGURADA'}")
    
    if not gmail_password:
        print("\n❌ PROBLEMA IDENTIFICADO:")
        print("   La variable GMAIL_APP_PASSWORD no está configurada.")
        print("\n🔧 SOLUCIÓN:")
        print("   1. Ve a tu cuenta de Google: https://myaccount.google.com/")
        print("   2. Ir a 'Seguridad' → 'Verificación en 2 pasos' (debe estar activada)")
        print("   3. Ir a 'Contraseñas de aplicaciones'")
        print("   4. Seleccionar 'Correo' y 'Otro (nombre personalizado)'")
        print("   5. Escribir 'Inefablestore' como nombre")
        print("   6. Copiar la contraseña de 16 caracteres generada")
        print("   7. Actualizar el archivo .env:")
        print("      GMAIL_APP_PASSWORD=tu_contraseña_de_16_caracteres")
        return False
    
    if gmail_password == 'tu_password_de_aplicacion_gmail':
        print("\n❌ PROBLEMA IDENTIFICADO:")
        print("   La variable GMAIL_APP_PASSWORD tiene el valor por defecto.")
        print("   Necesitas reemplazarla con una contraseña real de aplicación de Gmail.")
        return False
    
    print(f"   Longitud de contraseña: {len(gmail_password)} caracteres")
    
    # Configuración de email
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    email_usuario = "1yorbi1@gmail.com"
    
    print(f"\n2. 🌐 CONFIGURACIÓN DE CONEXIÓN:")
    print(f"   Servidor SMTP: {smtp_server}:{smtp_port}")
    print(f"   Email de envío: {email_usuario}")
    
    # Probar conexión SMTP
    print(f"\n3. 🔌 PROBANDO CONEXIÓN SMTP...")
    
    try:
        print("   Conectando al servidor SMTP...")
        server = smtplib.SMTP(smtp_server, smtp_port)
        
        print("   Iniciando TLS...")
        server.starttls()
        
        print("   Intentando autenticación...")
        server.login(email_usuario, gmail_password)
        
        print("   ✅ Conexión SMTP exitosa!")
        
        # Crear mensaje de prueba
        print(f"\n4. 📧 ENVIANDO EMAIL DE PRUEBA...")
        
        mensaje = MIMEMultipart()
        mensaje['From'] = email_usuario
        mensaje['To'] = email_usuario
        mensaje['Subject'] = "🧪 Prueba de Sistema de Notificaciones - Inefable Store"
        
        cuerpo = f"""
        ¡Prueba exitosa del sistema de notificaciones!
        
        📋 Detalles de la prueba:
        • Fecha: {os.popen('date').read().strip()}
        • Sistema: Inefable Store - SQLite
        • Estado: ✅ FUNCIONANDO CORRECTAMENTE
        
        Si recibes este correo, el sistema de notificaciones está configurado correctamente.
        
        ---
        Sistema de Notificaciones Inefable Store
        """
        
        mensaje.attach(MIMEText(cuerpo, 'plain'))
        
        texto = mensaje.as_string()
        server.sendmail(email_usuario, email_usuario, texto)
        server.quit()
        
        print("   ✅ Email de prueba enviado exitosamente!")
        print(f"   📬 Revisa tu bandeja de entrada en: {email_usuario}")
        
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"   ❌ ERROR DE AUTENTICACIÓN: {str(e)}")
        print("   💡 Verifica que tengas una contraseña de aplicación válida")
        print("   💡 Asegúrate de tener habilitada la verificación en 2 pasos")
        return False
        
    except smtplib.SMTPException as e:
        print(f"   ❌ ERROR SMTP: {str(e)}")
        return False
        
    except Exception as e:
        print(f"   ❌ ERROR GENERAL: {str(e)}")
        print(f"   🔍 Tipo de error: {type(e).__name__}")
        return False

def test_order_notification():
    """Simula el envío de notificación de orden"""
    
    print(f"\n5. 🛒 SIMULANDO NOTIFICACIÓN DE ORDEN...")
    
    # Datos de orden de prueba
    orden_data = {
        'id': 999,
        'juego_nombre': 'Free Fire (PRUEBA)',
        'paquete': '100 Diamantes',
        'monto': 0.99,
        'usuario_email': 'admin@inefablestore.com',
        'usuario_telefono': '+58-412-1234567',
        'usuario_id': '123456789',
        'metodo_pago': 'Pago Móvil',
        'referencia_pago': '123456789',
        'estado': 'procesando',
        'fecha': '2025-09-05 12:00:00'
    }
    
    # Importar función de notificación
    try:
        import sys
        sys.path.append('.')
        from main_sqlite import enviar_notificacion_orden
        
        print("   Enviando notificación de orden de prueba...")
        resultado = enviar_notificacion_orden(orden_data)
        
        if resultado:
            print("   ✅ Notificación de orden enviada exitosamente!")
        else:
            print("   ❌ Error al enviar notificación de orden")
            
        return resultado
        
    except Exception as e:
        print(f"   ❌ Error al importar función: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando diagnóstico del sistema de email...")
    
    # Probar conexión básica
    conexion_ok = test_gmail_connection()
    
    if conexion_ok:
        print("\n" + "=" * 60)
        print("✅ DIAGNÓSTICO COMPLETADO - SISTEMA FUNCIONANDO")
        print("=" * 60)
        print("El sistema de notificaciones por Gmail está configurado correctamente.")
        print("Las notificaciones deberían llegar automáticamente cuando se creen nuevas órdenes.")
        
        # Probar notificación de orden
        test_order_notification()
        
    else:
        print("\n" + "=" * 60)
        print("❌ DIAGNÓSTICO COMPLETADO - PROBLEMA IDENTIFICADO")
        print("=" * 60)
        print("Sigue las instrucciones anteriores para configurar Gmail correctamente.")
