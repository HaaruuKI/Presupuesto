from django.shortcuts import render
import sqlite3

def delete_transaccion_sql(id_tran):
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "DELETE FROM Transacciones WHERE ID_transaccion = ?;"
        cursor.execute(consulta, [id_tran])
        conexion.commit()

def get_transactions(fecha_desde=None, fecha_hasta=None):
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        if fecha_desde and fecha_hasta:
            consulta = """
                SELECT t.Fecha, t.Descripcion, t.Monto, c.Nombre_cuenta, ca.Nombre_categoria, t.ID_transaccion 
                FROM Transacciones t 
                INNER JOIN Cuentas c ON t.ID_cuenta = c.ID_cuenta 
                INNER JOIN Categorias ca ON t.ID_categoria = ca.ID_categoria 
                WHERE t.Fecha BETWEEN ? AND ?;
            """
            cursor.execute(consulta, [fecha_desde, fecha_hasta])
        elif fecha_desde:
            consulta = """
                SELECT t.Fecha, t.Descripcion, t.Monto, c.Nombre as nombre_cuenta, ca.Nombre as nombre_categoria, t.ID_transaccion 
                FROM Transacciones t 
                INNER JOIN Cuentas c ON t.ID_cuenta = c.ID_cuenta 
                INNER JOIN Categorias ca ON t.ID_categoria = ca.ID_categoria 
                WHERE t.Fecha >= ?;
            """
            cursor.execute(consulta, [fecha_desde])
        else:
            consulta = """
                SELECT t.Fecha, t.Descripcion, t.Monto, c.Nombre as nombre_cuenta, ca.Nombre as nombre_categoria, t.ID_transaccion 
                FROM Transacciones t 
                INNER JOIN Cuentas c ON t.ID_cuenta = c.ID_cuenta 
                INNER JOIN Categorias ca ON t.ID_categoria = ca.ID_categoria;
            """            
            cursor.execute(consulta)
        return cursor.fetchall()

def trasacciones(request):
    if request.POST:
        id_tran = request.POST['id_transaccion']
        delete_transaccion_sql(id_tran)
    fecha_hasta = request.GET.get('hasta_input')
    fecha_desde = request.GET.get('de_input')
    if fecha_hasta and fecha_desde:
        transactions_view = get_transactions(fecha_desde, fecha_hasta)
    elif fecha_desde:
        transactions_view = get_transactions(fecha_desde, None)
    else:
        transactions_view = get_transactions()    
    context= {'transactions': transactions_view}
    return render(request, 'trasacciones.html', context)