from django.shortcuts import render
import sqlite3


def add_category_sql(category, description):
  with sqlite3.connect("presupuesto.db") as conexion:
    cursor = conexion.cursor()

    consulta = """
    INSERT INTO Categorias (Nombre, Descripcion)
    VALUES (?, ?)
    """
    datos = (category, description)
    cursor.execute(consulta, datos)
    conexion.commit()

def function_view_categories():
  conexion = sqlite3.connect('presupuesto.db')
  cursor = conexion.cursor()
  consulta = """
  SELECT Nombre, Descripcion
  FROM Categorias
  """
  cursor.execute(consulta)
  resultados = cursor.fetchall()

  cursor.close()
  conexion.close()
  return resultados

def add_category(request):
    if request.POST:
        category = request.POST['category']
        description = request.POST['description']
        add_category_sql(category,description)
        
    categories = function_view_categories()
    
    context= {'categories': categories}
    return render(request, 'add_categories.html', context)