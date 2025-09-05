#!/usr/bin/env python3
"""
Script para verificar la estructura de la base de datos SQLite y los datos de órdenes
"""

import sqlite3
import os
from datetime import datetime

def check_database():
    """Verifica la estructura y datos de la base de datos"""
    
    print("🔍 VERIFICANDO BASE DE DATOS SQLITE")
    print("=" * 60)
    
    db_path = 'inefablestore.db'
    
    if not os.path.exists(db_path):
        print(f"❌ Base de datos no encontrada: {db_path}")
        return
    
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # 1. Verificar estructura de la tabla ordenes
        print("\n1. 📋 ESTRUCTURA DE LA TABLA 'ordenes':")
        cursor.execute("PRAGMA table_info(ordenes)")
        columns = cursor.fetchall()
        
        for col in columns:
            print(f"   - {col['name']}: {col['type']} {'(NOT NULL)' if col['notnull'] else ''}")
        
        # 2. Contar órdenes totales
        cursor.execute("SELECT COUNT(*) FROM ordenes")
        total_ordenes = cursor.fetchone()[0]
        print(f"\n2. 📊 TOTAL DE ÓRDENES: {total_ordenes}")
        
        if total_ordenes == 0:
            print("   ⚠️ No hay órdenes en la base de datos")
            print("   💡 Esto explica por qué no se envían notificaciones")
            return
        
        # 3. Verificar últimas órdenes
        print(f"\n3. 📋 ÚLTIMAS {min(5, total_ordenes)} ÓRDENES:")
        cursor.execute("""
            SELECT id, usuario_email, usuario_telefono, juego_id, paquete, monto, 
                   metodo_pago, referencia_pago, estado, fecha
            FROM ordenes 
            ORDER BY fecha DESC 
            LIMIT 5
        """)
        
        ordenes = cursor.fetchall()
        
        for orden in ordenes:
            print(f"\n   📦 ORDEN #{orden['id']}:")
            print(f"      Email: {orden['usuario_email'] or '❌ NO CONFIGURADO'}")
            print(f"      Teléfono: {orden['usuario_telefono'] or '❌ NO CONFIGURADO'}")
            print(f"      Juego ID: {orden['juego_id']}")
            print(f"      Paquete: {orden['paquete']}")
            print(f"      Monto: ${orden['monto']}")
            print(f"      Método: {orden['metodo_pago']}")
            print(f"      Referencia: {orden['referencia_pago']}")
            print(f"      Estado: {orden['estado']}")
            print(f"      Fecha: {orden['fecha']}")
        
        # 4. Verificar usuarios registrados
        print(f"\n4. 👥 USUARIOS REGISTRADOS:")
        cursor.execute("SELECT COUNT(*) FROM usuarios")
        total_usuarios = cursor.fetchone()[0]
        print(f"   Total usuarios: {total_usuarios}")
        
        if total_usuarios > 0:
            cursor.execute("SELECT id, nombre, email, es_admin FROM usuarios ORDER BY id DESC LIMIT 3")
            usuarios = cursor.fetchall()
            
            for usuario in usuarios:
                admin_text = " (ADMIN)" if usuario['es_admin'] else ""
                print(f"   - {usuario['nombre']} ({usuario['email']}){admin_text}")
        
        # 5. Verificar órdenes sin email
        cursor.execute("SELECT COUNT(*) FROM ordenes WHERE usuario_email IS NULL OR usuario_email = ''")
        ordenes_sin_email = cursor.fetchone()[0]
        
        if ordenes_sin_email > 0:
            print(f"\n⚠️ PROBLEMA IDENTIFICADO:")
            print(f"   {ordenes_sin_email} órdenes NO tienen email de usuario configurado")
            print(f"   Esto explica por qué no se envían notificaciones")
        
        # 6. Verificar relación entre usuarios y órdenes
        print(f"\n5. 🔗 RELACIÓN USUARIOS-ÓRDENES:")
        cursor.execute("""
            SELECT 
                o.usuario_email,
                COUNT(*) as total_ordenes,
                u.nombre as nombre_usuario
            FROM ordenes o
            LEFT JOIN usuarios u ON o.usuario_email = u.email
            GROUP BY o.usuario_email
            ORDER BY total_ordenes DESC
        """)
        
        relaciones = cursor.fetchall()
        
        for rel in relaciones:
            usuario_info = rel['nombre_usuario'] if rel['nombre_usuario'] else "❌ Usuario no encontrado"
            print(f"   - {rel['usuario_email']}: {rel['total_ordenes']} órdenes ({usuario_info})")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error al verificar base de datos: {e}")

def test_order_creation():
    """Simula la creación de una orden para verificar el proceso"""
    
    print(f"\n6. 🧪 SIMULANDO CREACIÓN DE ORDEN:")
    print("   Verificando el proceso de creación de órdenes...")
    
    try:
        # Importar función de creación de orden
        import sys
        sys.path.append('.')
        
        # Verificar si hay sesión activa simulada
        print("   ⚠️ Para crear órdenes se requiere:")
        print("   1. Usuario logueado (sesión activa)")
        print("   2. Email del usuario en la sesión")
        print("   3. Datos del usuario en la tabla 'usuarios'")
        
        # Verificar el código de creación de órdenes
        with open('main_sqlite.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "session['user_email']" in content:
            print("   ✅ El código usa session['user_email'] para obtener el email")
        else:
            print("   ❌ El código NO usa session['user_email']")
            
        if "usuario_email = session['user_email']" in content:
            print("   ✅ El email se obtiene de la sesión correctamente")
        else:
            print("   ⚠️ Verificar cómo se obtiene el email del usuario")
            
    except Exception as e:
        print(f"   ❌ Error al verificar proceso: {e}")

if __name__ == "__main__":
    print("🚀 Iniciando verificación de base de datos...")
    check_database()
    test_order_creation()
    
    print(f"\n" + "=" * 60)
    print("✅ VERIFICACIÓN COMPLETADA")
    print("=" * 60)
