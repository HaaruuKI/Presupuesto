from django.shortcuts import redirect, render
import sqlite3


def update_account_balance(account_id, amount, amount_sql):
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "SELECT Saldo_actual FROM Cuentas WHERE ID_cuenta = ?"
        cursor.execute(consulta, (account_id,))
        current_balance = cursor.fetchone()[0]
        
        balance = current_balance + float(amount) - float(amount_sql)
        
        if balance < current_balance:
            # print(f"{balance}, menos")
            new_balance = current_balance + float(amount_sql)
        else:
            # print(f"{balance}, mas")
            new_balance = current_balance - float(amount_sql)
        consulta = "UPDATE Cuentas SET Saldo_actual = ? WHERE ID_cuenta = ?"
        datos = (new_balance, account_id)
        cursor.execute(consulta, datos)
        conexion.commit()
        
def update_transaction_sql(date, amount, description, account, category, id_transaction):
    conexion = sqlite3.connect('presupuesto.db')
    cursor = conexion.cursor()
    consulta = """
    UPDATE Transacciones
    SET fecha = ?, descripcion = ?, monto = ?, ID_Categoria = ?, ID_Cuenta = ?
    WHERE ID_transaccion = ?;
    """
    datos = (date, description, amount, category, account, id_transaction)
    cursor.execute(consulta, datos)
    conexion.commit()
    cursor.close()
    conexion.close()

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

def edit_transaction(request, id_transaction):
    transaction_data =view_transaction_sql(id_transaction)
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

    if request.POST:
        date = request.POST['fecha']
        amount = request.POST['monto']
        description = request.POST['descripcion']
        account = request.POST['cuenta']
        category = request.POST['categoria']
            
        update_account_balance(account, amount, amount_sql)
        update_transaction_sql(date, amount, description, account, category, id_transaction)
        return redirect('trasacciones')
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
    return render(request, "edit_transaction.html", context)