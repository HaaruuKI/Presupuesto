import sqlite3
from django.shortcuts import render

def add_account(account, type_account, current_balance):
  with sqlite3.connect("presupuesto.db") as conexion:
    cursor = conexion.cursor()
    consulta = """
    INSERT INTO Cuentas (Nombre, Tipo, Saldo_actual)
    VALUES (?, ?, ?);
    """
    datos = (account, type_account, float(current_balance))
    cursor.execute(consulta, datos)
    conexion.commit()

def get_account():
      with sqlite3.connect('presupuesto.db') as conexion:
        cursor = conexion.cursor()
        consulta = "SELECT Nombre, Tipo, Saldo_actual FROM Cuentas"
        cursor.execute(consulta)
        return cursor.fetchall()
      
def add_accounts(request):
    if request.POST:
        account = request.POST['cuenta']
        type_account = request.POST['tipo']
        current_balance = request.POST['saldo_actual']
        print( type(account), type(type_account), type(current_balance) )
        print( account, type_account, current_balance )
        add_account(account, type_account, current_balance)
    
    accounts = get_account()

    context= {'accounts': accounts }
    return render(request, 'add_accounts.html', context)