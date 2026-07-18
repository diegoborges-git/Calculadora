import streamlit as st
import math

st.title("🧰 Assistência Técnica ")
st.header("🧰 Assistênciaaaaaaa Técnica ")
st.subheader("🧰 Assistência Técnica ")

# Criamos botões de rádio para escolher a operação
opcao = st.radio("O que você deseja calcular?", 
                 ["Força de Avanço do Cilindro", "Força de Recuo do Cilindro", "Velocidade de Avanço do Cilindro", "Cálculos de Motor Hidráulico"], index=None)



if opcao == "Cálculos de Motor Hidráulico":
    st.subheader("Cálculos de Motor Hidráulico")
    
    # Slider para eficiência (isso facilita muito para o técnico)
    eficiencia = st.slider("Eficiência do motor (%)", 0, 100, 85)
    fator = 456 * (eficiencia / 100)
    
    sub_opcao = st.radio("O que deseja calcular?", ["Vazão máxima", "Pressão máxima", "Potência mínima"],index=None )
    
    if sub_opcao == "Vazão máxima":
        potencia = st.number_input("Potência (CV)", min_value=0.0)
        pressao = st.number_input("Pressão (bar)", min_value=0.0)
        if st.button("Calcular"):
            vazao = (fator * potencia) / pressao if pressao != 0 else 0
            st.write(f"Vazão máxima: {vazao:.2f} L/min")
            
    elif sub_opcao == "Pressão máxima":
        potencia = st.number_input("Potência (CV)", min_value=0.0)
        vazao = st.number_input("Vazão (L/min)", min_value=0.0)
        if st.button("Calcular"):
            pressao = (fator * potencia) / vazao if vazao != 0 else 0
            st.write(f"Pressão máxima: {pressao:.2f} bar")
            
    elif sub_opcao == "Potência mínima":
        vazao = st.number_input("Vazão (L/min)", min_value=0.0)
        pressao = st.number_input("Pressão (bar)", min_value=0.0)
        if st.button("Calcular"):
            potencia = (vazao * pressao) / fator
            st.write(f"Potência mínima: {potencia:.2f} CV")

# A lógica abaixo só aparece se a opção for selecionada
if opcao == "Força de Avanço do Cilindro":
    st.subheader("Cálculo de Força de Avanço")
    pressao = st.number_input("Pressão (bar)", min_value=0.0)
    pressao_kgf = pressao*1.02
    diametro = st.number_input("Diâmetro da Camisa (mm)", min_value=0.0)
    if st.button("Calcular"):
        area_cm2 = (math.pi * (diametro/10)**2) / 4
        forca = area_cm2 * pressao_kgf
        st.write(f"Área Total: {area_cm2:,.3f} cm²")
        st.write(f"Força de Avanço: {forca:,.3f} kgf")

elif opcao == "Força de Recuo do Cilindro":
    st.subheader("Cálculo de Força de Recuo")
    pressao = st.number_input("Pressão (bar)", min_value=0.0)
    pressao_kgf = pressao*1.02
    diametro = st.number_input("Diâmetro da Camisa (mm)", min_value=0.0)
    haste = st.number_input("Diâmetro da Haste (mm)", min_value=0.0)
    if st.button("Calcular"):
        area_cm2 = (math.pi * ((diametro/10)**2 - (haste/10)**2)) / 4
        forca = area_cm2 * pressao_kgf
        st.write(f"Área da Coroa: {area_cm2:,.3f} cm²")
        st.write(f"Força de Recuo: {forca:,.3f} kgf")

elif opcao == "Velocidade de Avanço do Cilindro":
    st.subheader("Cálculo de Velocidade")
    vazao = st.number_input("Vazão (L/min)", min_value=0.0)
    diametro = st.number_input("Diâmetro da Camisa (mm)", min_value=0.0)
    if st.button("Calcular"):
        area_cm2 = (math.pi * (diametro/10)**2) / 4
        velocidade = (vazao) / (area_cm2 * 0.006)
        st.write(f"Área Total: {area_cm2:,.3f} cm²")
        st.write(f"Velocidade: {velocidade:.3f} m/s")
