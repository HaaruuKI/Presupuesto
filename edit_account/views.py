import sqlite3
from django.shortcuts import redirect, render

def update_account(name_account, type_account, current_balance, id_account):
    with sqlite3.connect("presupuesto.db") as conexion:
        cursor = conexion.cursor()
        consulta = """
        UPDATE Cuentas
        SET Nombre = ?, Tipo = ?, Saldo_actual = ? WHERE ID_cuenta = ?;
        """
        datos = [name_account, type_account, current_balance,id_account]
        cursor.execute(consulta, datos)
        conexion.commit()

def get_account(id_account):
    with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM Cuentas WHERE ID_cuenta = ?;"

        cursor.execute(consulta, [id_account])
        return cursor.fetchall()

def edit_account(request, id_account):
    if request.POST:
        name_account = request.POST['name_account']
        type_account = request.POST['type_account']
        current_balance = request.POST['current_balance'] 
        update_account(name_account, type_account, current_balance, id_account)
        return redirect('agregar_cuenta')
        
    get_accounts = get_account(id_account)
    context = {"id":id_account, "accounts": get_accounts}
    return render(request, "edit_account.html",context)