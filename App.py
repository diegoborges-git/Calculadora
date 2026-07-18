import streamlit as st
import math

st.title("🧰 Assistência Técnica ")

# Criamos botões de rádio para escolher a operação
opcao = st.radio("O que você deseja calcular?", 
                 ["Força de Avanço", "Força de Recuo", "Velocidade"])

# A lógica abaixo só aparece se a opção for selecionada
if opcao == "Força de Avanço":
    st.subheader("Cálculo de Força de Avanço")
    pressao = st.number_input("Pressão (bar)", min_value=0.0)
    diametro = st.number_input("Diâmetro da Camisa (mm)", min_value=0.0)
    if st.button("Calcular"):
        area = (math.pi * (diametro/10)**2) / 4
        forca = area * pressao
        st.write(f"Força de Avanço: {forca:,.2f} kgf")

elif opcao == "Força de Recuo":
    st.subheader("Cálculo de Força de Recuo")
    pressao = st.number_input("Pressão (bar)", min_value=0.0)
    diametro = st.number_input("Diâmetro da Camisa (mm)", min_value=0.0)
    haste = st.number_input("Diâmetro da Haste (mm)", min_value=0.0)
    if st.button("Calcular"):
        area = (math.pi * ((diametro/10)**2 - (haste/10)**2)) / 4
        forca = area * pressao
        st.write(f"Força de Recuo: {forca:,.2f} kgf")

elif opcao == "Velocidade":
    st.subheader("Cálculo de Velocidade")
    vazao = st.number_input("Vazão (L/min)", min_value=0.0)
    diametro = st.number_input("Diâmetro da Camisa (mm)", min_value=0.0)
    if st.button("Calcular"):
        area_cm2 = (math.pi * (diametro/10)**2) / 4
        velocidade = (vazao * 1000) / (area_cm2 * 60)
        st.write(f"Velocidade: {velocidade:.2f} m/s")