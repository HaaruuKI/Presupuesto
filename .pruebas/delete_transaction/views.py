import sqlite3
from django.shortcuts import render

def get_categories():
    conexion = sqlite3.connect('presupuesto.db')
    cursor = conexion.cursor()
    consulta = "SELECT ID_Categoria, Nombre FROM Categorias"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    categories = [{"id": row[0], "name": row[1]} for row in resultados]
    cursor.close()
    conexion.close()
    return categories

def get_accounts():
    conexion = sqlite3.connect('presupuesto.db')
    cursor = conexion.cursor()
    consulta = "SELECT ID_Cuenta, Nombre FROM Cuentas"
    cursor.execute(consulta)
    resultados = cursor.fetchall()
    accounts = [{"id": row[0], "name": row[1]} for row in resultados]
    cursor.close()
    conexion.close()
    return accounts

def view_transaction_sql(id_trasaction):
    conexion = sqlite3.connect('presupuesto.db')
    cursor = conexion.cursor()
    consulta = """
    SELECT t.*, c.Nombre AS categoria_nombre, cu.Nombre AS cuenta_nombre
    FROM Transacciones t
    INNER JOIN Categorias c ON t.ID_Categoria = c.ID_Categoria
    INNER JOIN Cuentas cu ON t.ID_Cuenta = cu.ID_Cuenta
    WHERE t.ID_transaccion = ?;
    """
    cursor.execute(consulta, (id_trasaction,))
    resultados = cursor.fetchone()
    print(resultados)

    if resultados:
        transaction_data = {
            'id_transaccion': resultados[0],
            'fecha': resultados[1],
            'descripcion': resultados[2],
            'monto': resultados[3],
            'id_categoria': resultados[4],
            'id_cuenta': resultados[5],
            'categoria_nombre': resultados[6],
            'cuenta_nombre': resultados[7]
        }
    else:
        transaction_data = None

    cursor.close()
    conexion.close()
    return transaction_data 

def delete_transaction(request, id_trasaction):
    transaction_data =view_transaction_sql(id_trasaction)
    categories = get_categories()
    accounts = get_accounts()
    if transaction_data:
        id_trasaction_sql = transaction_data['id_transaccion']
        date_sql =transaction_data['fecha']
        description_sql = transaction_data['descripcion']
        amount_sql = transaction_data['monto']
        id_category_sql = transaction_data['id_categoria']
        id_account_sql = transaction_data['id_cuenta']
        name_category_sql = transaction_data['categoria_nombre']
        name_account_sql = transaction_data['cuenta_nombre']
        
    else:
        print("No se encontró la transacción")

    context = {'id': id_trasaction_sql, 
               'date':date_sql,
               'description':description_sql,
               'amount':amount_sql,
               'id_category':id_category_sql,
               'id_account':id_account_sql,
               'name_category':name_category_sql,
               'name_account':name_account_sql,
               'categories': categories,
               'accounts': accounts
               }
    return render(request, "delete_transaction.html", context)