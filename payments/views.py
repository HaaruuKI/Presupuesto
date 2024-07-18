import sqlite3
from django.shortcuts import render

def update_account_balance(account_id, amount):
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "UPDATE Cuentas SET Saldo_actual = Saldo_actual - ? WHERE ID_cuenta = ?"
        datos = (amount, account_id)
        cursor.execute(consulta, datos)
        conexion.commit()

def add_transaction(date, description, amount, account, category):
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "INSERT INTO Transacciones (Fecha, Descripcion, Monto, ID_cuenta, ID_categoria) VALUES (?, ?, ?, ?, ?)"
        datos = (date, description, amount, account, category)
        cursor.execute(consulta, datos)
        conexion.commit()
        amount_replace = amount.replace("-", "")
        update_account_balance(account, amount_replace)
        


def get_categories():
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "SELECT ID_categoria, Nombre FROM Categorias"
        cursor.execute(consulta)
        return cursor.fetchall()

def get_accounts():
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "SELECT ID_cuenta, Nombre FROM Cuentas"
        cursor.execute(consulta)
        return cursor.fetchall()

def get_transactions():
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "SELECT Fecha, Descripcion, Monto, ID_cuenta, ID_categoria FROM Transacciones"
        cursor.execute(consulta)
        return cursor.fetchall()

def payments(request):
    if request.POST:
        date = request.POST['fecha']
        description = request.POST['descripcion']
        amount = request.POST['monto']
        account = request.POST['cuenta']
        category = request.POST['categoria']
        amount = f"-{amount}"
        add_transaction(date, description, amount, account, category)
    
    categories = get_categories()
    accounts = get_accounts()
    transactions = get_transactions()
    
    context = {
        'categories': categories,
        'accounts': accounts,
        'transactions': transactions,
    }
    return render(request, "payments.html", context)


























# import sqlite3
# from django.shortcuts import render

# def function_categories():
#     with sqlite3.connect('presupuesto.db') as conexion:
#         cursor = conexion.cursor()
#         consulta = """
#         SELECT ID_categoria, Nombre
#         FROM Categorias
#         """
#         cursor.execute(consulta)
#         return cursor.fetchall()

# def function_account():
#     with sqlite3.connect('presupuesto.db') as conexion:
#         cursor = conexion.cursor()
#         consulta = """
#         SELECT ID_cuenta, Nombre
#         FROM Cuentas
#         """
#         cursor.execute(consulta)
#         return cursor.fetchall()

# def function_add_trasaccion_sql(date, description, amount, account, category):
#     with sqlite3.connect('presupuesto.db') as conexion:
#         cursor = conexion.cursor()
#         consulta = """
#         INSERT INTO Transacciones (Fecha, Descripcion, Monto, ID_cuenta, ID_categoria
#         ) VALUES (?, ?, ?, ?, ?)
#         """
#         datos = (date, description, amount, account, category)
#         cursor.execute(consulta, datos)
#         conexion.commit()


# def function_view_trasacciones():
#     with sqlite3.connect('presupuesto.db') as conexion:
#         cursor = conexion.cursor()
#         consulta = """
#         SELECT Fecha, Descripcion, Monto, ID_cuenta, ID_categoria
#         FROM Transacciones
#         """
#         cursor.execute(consulta)        
#         return cursor.fetchall()

# def payments(request):
#     if request.POST:
#         date = request.POST['fecha']
#         description = request.POST['descripcion']
#         amount = request.POST['monto']
#         account = request.POST['cuenta']
#         category = request.POST['categoria']
#         amount = f"-{amount}"
#         function_add_trasaccion_sql(date, description, amount, account, category)
        
#     account_view = function_account()
#     categories_view = function_categories()
#     trasacciones_view = function_view_trasacciones()
    
#     context = {
#         'account_list': account_view,
#         'category_list': categories_view,
#         'trasacciones_view': trasacciones_view,
#         }
#     return render(request, "payments.html", context)