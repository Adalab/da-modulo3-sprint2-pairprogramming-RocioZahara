pip install pandas
import pandas as pd

# Lee los archivos CSV
ventas = pd.read_csv('ventas.csv')
productos = pd.read_csv('productos.csv')
clientes = pd.read_csv('clientes.csv')

# Muestra las primeras filas de cada conjunto de datos para comprender su estructura
print("Datos de Ventas:")
print(ventas.head())

print("\nDatos de Productos:")
print(productos.head())

print("\nDatos de Clientes:")
print(clientes.head())

# Información sobre las columnas y tipos de datos
print("\nInformación de Ventas:")
print(ventas.info())

print("\nInformación de Productos:")
print(productos.info())

print("\nInformación de Clientes:")
print(clientes.info())

# Estadísticas descriptivas para entender los datos numéricos (si los hay)
print("\nEstadísticas de Ventas:")
print(ventas.describe())

# También puedes explorar columnas específicas y su contenido
print("\nColumnas de Productos:")
print(productos.columns)

# Para ver los tipos de datos de una columna particular
print("\nTipos de datos de la columna 'Nombre' en Clientes:")
print(clientes['Nombre'].dtype)
