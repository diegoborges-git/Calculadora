import streamlit as st
import math

st.set_page_config(page_title="Calculadora Hidráulica", layout="centered")

st.title("🧰 Assistência Técnica")

# Inputs
pressao = st.number_input("Pressão de Trabalho (bar)", min_value=0.0, format="%.1f")
diametro = st.number_input("Diâmetro da Camisa (mm)", min_value=0.0, format="%.1f")

if st.button("Calcular Força de Avanço"):
    if diametro > 0:
        # A = (pi * D^2) / 4
        area_mm2 = (math.pi * (diametro**2)) / 4
        # 1 bar = 10 N/cm^2 -> conversão direta para Kgf
        forca_kgf = (area_mm2 * pressao) / 100 
        
        st.success(f"Força de Avanço: **{forca_kgf:,.2f} kgf**")
    else:
        st.error("Insira um diâmetro válido.")