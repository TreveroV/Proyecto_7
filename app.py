import pandas as pd
import plotly.express as px
import streamlit as st
     
st.header('Analisis de venta de vehiculos usados')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
car_data_trans = car_data.groupby(['transmission','fuel'])['price'].mean().reset_index()
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Preci promedio por tipo de transmision y combustible')

    
    fig_2 = px.line(car_data_trans, x="fuel", y="price", color='transmission')
    st.plotly_chart(fig_2, use_container_width=True)
