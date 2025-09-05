#!/usr/bin/env python3
"""
Script para probar el envío de notificaciones usando órdenes existentes
"""

import sqlite3
import sys
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_notification_with_real_order():
    """Prueba el envío de notificación usando una orden real de la base de datos"""
    
    print("🧪 PROBANDO NOTIFICACIONES CON ORDEN REAL")
    print("=" * 60)
    
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('inefablestore.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # Obtener la orden más reciente
        cursor.execute("""
            SELECT o.*, j.nombre as juego_nombre 
            FROM ordenes o 
            LEFT JOIN juegos j ON o.juego_id = j.id 
            ORDER BY o.fecha DESC 
            LIMIT 1
        """)
        
        orden = cursor.fetchone()
        
        if not orden:
            print("❌ No hay órdenes en la base de datos")
            return False
            
        print(f"📦 USANDO ORDEN #{orden['id']}:")
        print(f"   Email: {orden['usuario_email']}")
        print(f"   Juego: {orden['juego_nombre']}")
        print(f"   Paquete: {orden['paquete']}")
        print(f"   Monto: ${orden['monto']}")
        print(f"   Estado: {orden['estado']}")
        
        # Convertir a diccionario para la función de notificación
        orden_data = {
            'id': orden['id'],
            'juego_id': orden['juego_id'],
            'paquete': orden['paquete'],
            'monto': orden['monto'],
            'usuario_email': orden['usuario_email'],
            'usuario_id': orden['usuario_id'],
            'usuario_telefono': orden['usuario_telefono'],
            'metodo_pago': orden['metodo_pago'],
            'referencia_pago': orden['referencia_pago'],
            'estado': orden['estado'],
            'fecha': orden['fecha'],
            'juego_nombre': orden['juego_nombre']
        }
        
        conn.close()
        
        # Importar y probar función de notificación
        print(f"\n📧 PROBANDO ENVÍO DE NOTIFICACIÓN...")
        
        sys.path.append('.')
        from main_sqlite import enviar_notificacion_orden
        
        print("   Enviando notificación de orden...")
        resultado = enviar_notificacion_orden(orden_data)
        
        if resultado:
            print("   ✅ Notificación enviada exitosamente!")
            print(f"   📬 Revisa tu bandeja de entrada en: 1yorbi1@gmail.com")
            return True
        else:
            print("   ❌ Error al enviar notificación")
            return False
            
    except Exception as e:
        print(f"❌ Error en la prueba: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_order_completion_notification():
    """Prueba notificación de orden completada"""
    
    print(f"\n🎉 PROBANDO NOTIFICACIÓN DE ORDEN COMPLETADA...")
    
    try:
        # Obtener una orden procesada
        conn = sqlite3.connect('inefablestore.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT o.*, j.nombre as juego_nombre, j.categoria
            FROM ordenes o 
            LEFT JOIN juegos j ON o.juego_id = j.id 
            WHERE o.estado = 'procesado'
            ORDER BY o.fecha DESC 
            LIMIT 1
        """)
        
        orden = cursor.fetchone()
        
        if not orden:
            print("   ⚠️ No hay órdenes procesadas para probar")
            return False
            
        print(f"   Usando orden #{orden['id']} (estado: {orden['estado']})")
        
        # Convertir a diccionario
        orden_dict = dict(orden)
        
        conn.close()
        
        # Importar función de confirmación
        from main_sqlite import enviar_correo_recarga_completada
        
        print("   Enviando confirmación de recarga completada...")
        resultado = enviar_correo_recarga_completada(orden_dict)
        
        if resultado:
            print("   ✅ Confirmación enviada exitosamente!")
            return True
        else:
            print("   ❌ Error al enviar confirmación")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return False

def check_gmail_config():
    """Verifica la configuración de Gmail"""
    
    print(f"\n🔧 VERIFICANDO CONFIGURACIÓN DE GMAIL...")
    
    gmail_password = os.environ.get('GMAIL_APP_PASSWORD')
    
    if not gmail_password:
        print("   ❌ GMAIL_APP_PASSWORD no configurada")
        return False
        
    if gmail_password == 'tu_password_de_aplicacion_gmail':
        print("   ❌ GMAIL_APP_PASSWORD tiene valor por defecto")
        return False
        
    print(f"   ✅ GMAIL_APP_PASSWORD configurada ({len(gmail_password)} caracteres)")
    
    # Probar conexión SMTP
    import smtplib
    
    try:
        print("   Probando conexión SMTP...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("1yorbi1@gmail.com", gmail_password)
        server.quit()
        print("   ✅ Conexión SMTP exitosa")
        return True
    except Exception as e:
        print(f"   ❌ Error SMTP: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando prueba de notificaciones...")
    
    # 1. Verificar configuración de Gmail
    gmail_ok = check_gmail_config()
    
    if not gmail_ok:
        print("\n❌ Configuración de Gmail incorrecta")
        exit(1)
    
    # 2. Probar notificación de nueva orden
    print("\n" + "=" * 60)
    notif_ok = test_notification_with_real_order()
    
    # 3. Probar notificación de orden completada
    print("\n" + "=" * 60)
    completion_ok = test_order_completion_notification()
    
    # Resumen
    print("\n" + "=" * 60)
    print("📋 RESUMEN DE PRUEBAS:")
    print(f"   Gmail configurado: {'✅' if gmail_ok else '❌'}")
    print(f"   Notificación nueva orden: {'✅' if notif_ok else '❌'}")
    print(f"   Notificación orden completada: {'✅' if completion_ok else '❌'}")
    
    if gmail_ok and (notif_ok or completion_ok):
        print("\n🎉 ¡SISTEMA DE NOTIFICACIONES FUNCIONANDO!")
        print("   Las notificaciones deberían llegar automáticamente")
    else:
        print("\n⚠️ Hay problemas con el sistema de notificaciones")
