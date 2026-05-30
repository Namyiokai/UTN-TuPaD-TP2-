"Análisis de Ventas de Pequeña Empresa"
"Script desarrollado por Paco (P2) - Análisis de datos de ventas"


import pandas as pd
import matplotlib.pyplot as plt
import os

datos_ventas = {
    'fecha': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05',
              '2024-01-06', '2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10'],
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Laptop', 'Mouse', 
                 'Teclado', 'Laptop', 'Mouse', 'Teclado', 'Laptop'],
    'cantidad': [2, 5, 3, 1, 4, 2, 3, 6, 2, 4],
    'precio_unitario': [800, 25, 45, 800, 25, 45, 800, 25, 45, 800]
}

df = pd.DataFrame(datos_ventas)
df['fecha'] = pd.to_datetime(df['fecha'])
df['venta_total'] = df['cantidad'] * df['precio_unitario']

print("Primeras 5 filas del dataset:")
print(df.head())

ventas_totales = df['venta_total'].sum()
producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
cantidad_mas_vendida = df.groupby('producto')['cantidad'].sum().max()
ventas_por_producto = df.groupby('producto')['venta_total'].sum()

print(f"Ventas totales: ${ventas_totales:,.2f}")
print(f"Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")
print("Ventas por producto:")
print(ventas_por_producto)

plt.figure(figsize=(10, 6))
ventas_diarias = df.groupby('fecha')['venta_total'].sum()
plt.plot(ventas_diarias.index, ventas_diarias.values, marker='o', linewidth=2, markersize=8)
plt.title('Evolución de Ventas Diarias', fontsize=14, fontweight='bold')
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Ventas Totales ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('resultados/evolucion_ventas.png', dpi=150)
print("Gráfico guardado en: resultados/evolucion_ventas.png")


with open('resultados/resumen_ventas.txt', 'w', encoding='utf-8') as f:
    f.write("Resúmen de análisis de ventas")
    f.write(f"Ventas Totales: ${ventas_totales:,.2f}")
    f.write(f"Producto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")
    f.write("Ventas por producto:")
    for producto, venta in ventas_por_producto.items():
        f.write(f"  - {producto}: ${venta:,.2f}")

print("Resumen guardado en: resultados/resumen_ventas.txt")
print("Análisis completo")
