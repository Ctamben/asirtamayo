import streamlit as st

st.title("🎈 Mi aplicación")
st.write("Esto es una prueba")

st.header("Esto es una cabecera")

cantidad = st.slider("Elija un valor ")

print(f' el identificador de cantidad es {id(cantidad)}')

for i in range(cantidad):
    st.button(f'Botón {i}')
    st.checkbox(f'Opcion {i}')