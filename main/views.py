import decimal
import sqlite3
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def update_account(income, account):
  with sqlite3.connect("presupuesto.db") as conexion:
    cursor = conexion.cursor()
    query_view = "SELECT Saldo_actual FROM Cuentas WHERE ID_cuenta = ?"
    data = [account]
    cursor.execute(query_view, data)
    current_balance = cursor.fetchone()
  
    try:
      query_update = "UPDATE Cuentas SET Saldo_actual = ? WHERE ID_cuenta = ?"
      new_balance = current_balance[0] + round(float(income),2)
      data = (new_balance, account)
      cursor.execute(query_update, data)
      conexion.commit()
      print("Exito")
    except Exception as e:
      print(f"Error: {e}")

def get_accounts():
  with sqlite3.connect("presupuesto.db") as conexion:
    cursor = conexion.cursor()
    query = "SELECT ID_cuenta, Nombre FROM Cuentas"
    cursor.execute(query)
    accounts = cursor.fetchall()
    return accounts
  
@login_required
def main(request):
  user = request.user
  
  get_acccounts = get_accounts()
  
  if request.POST:
    income = request.POST["income"]
    account = request.POST["account"]
    update_account(income, account)
  
  context = {'user':user, 'accounts':get_acccounts}
  return render(request, "main.html", context)

def logout_view(request):
    logout(request)
    return redirect('/')
  