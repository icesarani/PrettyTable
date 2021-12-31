#Manejo de datos en tablas
#Petty Table se usa para tabular informacion
#pip install prettytable
from prettytable import PrettyTable
from prettytable import from_csv

#Creo la "tabla"
tabla = PrettyTable()

#Instancio las columnas y sus nombres
tabla.field_names = ['Nombre','Apellido','DNI']

#Relleno de Columna por Filas
#Agregado de filas
tabla.add_row(['Ignacio','Cesarani','43725126'])
tabla.add_row(['Jorge','Alcina','23725532'])
tabla.add_row(['Alberto','Muños','21938937'])

#Agregado de filas con listas anidadas
tabla.add_rows([['Juan','Romero','12332121'],['Carlos','Sandiego','32456132'],['Alan','Gomez','40765001']])

#Eliminar una Fila
tabla.del_row(2) #Se elimina la 2da fila

#Ingreso de datos por CSV (Uso la funcion from_csv)
with open("ejemplo.csv",'r') as fp:
    tabla = from_csv(fp)

#Printeo la tabla
print(tabla)