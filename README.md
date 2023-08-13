# **Segmentación RFM**
El presente repositorio tiene como objetivo brindar una librería en Python que sea capaz de recibir input de las transacciones comerciales para brindar como output una segmentación RFM para la óptima toma de decisiones empresariales.


Debes renombrar las columnas que serán necesarias para el uso de la librería.
Debes identificar en las columnas del dataframe que hagan referencia a la identificación del consumidor, el día en que se ejecutó la venta del producto o el día en que se generó la fecha de orden, una columna de venta total (precio por cantidad) por registro, en el caso no se cuente la columna de venta total se debe generar una columna y, por último, elegir una columna que no tenga valores nulos, puede ser la columna de identificación del registro.

```python
data = data.rename(columns = {
    'Identificación del consumidor' : 'Customer ID',
    'Día en que se ejecutó la venta' : 'Date',
    'Venta Total' : 'Sales',
    'Identificación del registo' : 'Order ID'
})
```

```python
data["Order Date"] = pd.to_datetime(data["Order Date"]).dt.strftime("%Y%m%d")
data = data.rename(columns = {'Order Date':'Date'})
```

```python
rfm = Segmentation.RFM(data, '20190115', positions = [1,2,5,17])
Segmentation.RFMTable(rfm)
Segmentation.RFMAnalysis(rfm)
Segmentation.RFMFindClientsBySegment(rfm, "Hola")
```