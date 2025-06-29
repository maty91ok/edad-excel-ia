
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de ejemplo para entrenar el modelo (usamos un pequeño dataset simulado)
data = {
    'uso_vlookup': [1, 0, 1, 1, 0, 0, 1, 0],
    'uso_atajos': [1, 1, 1, 0, 0, 0, 1, 0],
    'errores_frecuentes': [0, 1, 0, 2, 3, 2, 0, 3],
    'uso_macros': [1, 0, 1, 0, 0, 0, 1, 0],
    'edad': [35, 22, 40, 28, 19, 25, 38, 21]
}
df = pd.DataFrame(data)

# Entrenar modelo
X = df.drop("edad", axis=1)
y = df["edad"]
modelo = LinearRegression()
modelo.fit(X, y)

# Título
st.title("🧠 Estimador de Edad por Uso de Excel")
st.write("Ajustá los controles y la IA predecirá tu edad estimada según tu estilo de uso de Excel.")

# Entradas del usuario
uso_vlookup = st.checkbox("¿Usás VLOOKUP o funciones de búsqueda?", value=True)
uso_atajos = st.checkbox("¿Usás atajos de teclado?", value=True)
errores = st.slider("Errores frecuentes al usar Excel", 0, 5, 1)
uso_macros = st.checkbox("¿Creás o usás macros?", value=False)

# Botón para predecir
if st.button("🔍 Estimar Edad"):
    datos_usuario = pd.DataFrame([{
        "uso_vlookup": int(uso_vlookup),
        "uso_atajos": int(uso_atajos),
        "errores_frecuentes": errores,
        "uso_macros": int(uso_macros)
    }])
    prediccion = modelo.predict(datos_usuario)[0]
    st.success(f"🧓 Edad estimada: {prediccion:.1f} años")
