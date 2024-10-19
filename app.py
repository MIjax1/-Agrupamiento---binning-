import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Cargar el archivo CSV (usando coma como separador)
file_path = 'customers.csv'
data = pd.read_csv(file_path, sep=',')  # Aseguramos que es separado por comas

# Limpiar los nombres de las columnas para eliminar espacios en blanco
data.columns = data.columns.str.strip()

# Mostrar los datos originales (primeras 5 filas)
print("Datos originales (primeras 5 filas):")
print(data.head())

# Definir los límites de los bins y las etiquetas para 'product_weight_g'
bins_weight = [0, 2000, 4000, 5000, float('inf')]  # Ajustados según lo solicitado
labels_weight = ['Ligero', 'Medio', 'Pesado', 'Muy pesado']

# Agrupar la columna 'product_weight_g' en bins
data['weight_category'] = pd.cut(data['product_weight_g'], bins=bins_weight, labels=labels_weight)

##  rangos para la longitud
bins_length = [0, 25, 50, 75, 105]
labels_length = ['Pequeño', 'Mediano', 'Grande', 'Muy Grande']


# Agrupar la columna 'product_length_cm' en bins
data['length_category'] = pd.cut(data['product_length_cm'], bins=bins_length, labels=labels_length)

# Mostrar las categorías aplicadas
print("\nDatos con categorías de peso y longitud (primeras 5 filas):")
print(data[['product_id', 'product_weight_g', 'weight_category', 'product_length_cm', 'length_category']].head())

# Guardar el DataFrame actualizado con las nuevas columnas en un archivo CSV
output_file_path = 'customers_with_categories.csv'
data.to_csv(output_file_path, index=False)
print(f"\nArchivo CSV actualizado guardado en: {output_file_path}")

# Crear subplots: uno debajo del otro
fig = make_subplots(rows=2, cols=1, subplot_titles=('Distribución de Categorías de Peso', 'Distribución de Categorías de Longitud'))

# Agregar el gráfico de categorías de peso
fig.add_trace(
    go.Histogram(x=data['weight_category'], marker_color='#636EFA'),
    row=1, col=1
)

# Agregar el gráfico de categorías de longitud
fig.add_trace(
    go.Histogram(x=data['length_category'], marker_color='#EF553B'),
    row=2, col=1
)

# Actualizar el layout de los gráficos para centrar y ampliar de manera proporcional
fig.update_layout(
    title_text='Distribución de Categorías de Peso y Longitud',
    showlegend=False,
    height=1200,  # Aumentar la altura total
    width=800,    # Aumentar el ancho para hacerlo más grande
    margin=dict(l=100, r=100, t=100, b=100),  # Centrar los gráficos ajustando márgenes
)

# Mostrar el gráfico
fig.show()
