import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
    
hist_button = st.checkbox('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma del modelo año de los autos')
            
    # crear un histograma
    fig = px.histogram(car_data, x="model_year")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

esc_button = st.checkbox('Grafica por dispersión') # Boton # 2
    
if esc_button:
    # escribir un mensaje
    st.write('Diagrama por dispersion, relacion precio modelo-año')
            
    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x="model_year", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    