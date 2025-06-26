import streamlit as st
import mlflow.sklearn
import pandas as pd
import mlflow
import pickle
import os

# Adicione esta linha logo no início!
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# Dicionário: Nome da especiaria -> (run_id, nome legível)
MODELOS = {
    "Canela e flores de caneleira": ("556c193e934f4e7e8e3ce7c6dfe3cc4b", "Cinnamon and cinnamon-tree flowers, raw"),
    "Gengibre": ("53e609e56830437aaf96c7b807ae8c44", "Ginger, raw"),
    "Pimentas secas (Capsicum/Pimenta)": ("3f573c665d8d4a98a5f93c3058acd7a2", "Chillies and peppers, dry (Capsicum spp., Pimenta spp.), raw"),
    "Baunilha": ("e32d84b590814e4eb905f96fec0d0c91", "Vanilla, raw"),
    "Cravo (talos inteiros)": ("d7cb0fc26a024ad788ba216bd59f3cf5", "Cloves (whole stems), raw"),
    "Pimenta (Piper spp.)": ("633d2b39cf11413ca219ebcabb410ffc", "Pepper (Piper spp.), raw"),
    "Noz-moscada, macis e cardamomos": ("3bbcdd438c75459ca2b2c101ba81f52a", "Nutmeg, mace, cardamoms, raw"),
    "Pimentas verdes (Capsicum/Pimenta)": ("8acef88689474cdfbdda4bc5ea7f6038", "Chillies and peppers, green (Capsicum spp. and Pimenta spp.)"),
    "Anis, badiana, coentro, cominho, alcaravia, funcho e zimbro": ("cd92e19fd5cd4451b00d8f7f85091da8", "Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw"),
}

st.title("Predição de Importação de Especiarias com MLflow")

# Escolha da especiaria
escolha = st.selectbox("Escolha a especiaria:", list(MODELOS.keys()))
run_id, item_value = MODELOS[escolha]

# Carrega o modelo correspondente
@st.cache_resource
def carregar_modelo(run_id):
    model_uri = f"runs:/{run_id}/best_model"
    return mlflow.sklearn.load_model(model_uri)

modelo = carregar_modelo(run_id)

# Carregue as colunas do treinamento (você deve salvar isso ao treinar o modelo)
# Exemplo: com pickle, salve as colunas do X_train antes do fit
# with open("colunas_treinamento.pkl", "rb") as f:
#     colunas_treinamento = pickle.load(f)
# Para este exemplo, vamos simular:
colunas_treinamento = modelo.feature_names_in_ if hasattr(modelo, "feature_names_in_") else None

# Entradas do usuário
st.header("Preencha os dados para previsão:")

# Exemplo de campos (ajuste conforme seu dataset real)
area = st.text_input("Área (país/região, igual ao treinamento)")
ano = st.number_input("Ano", min_value=1900, max_value=2100, value=2022)

if st.button("Prever"):
    df = pd.DataFrame([{
        "Area": area,
        "Year": ano,
        "Item": item_value,  # Fixo conforme a especiaria escolhida
    }])
    df = pd.get_dummies(df)
    # Alinha as colunas
    if colunas_treinamento is not None:
        for col in colunas_treinamento:
            if col not in df.columns:
                df[col] = 0
        df = df[colunas_treinamento]
    try:
        pred = modelo.predict(df)
        st.success(f"Previsão: {pred[0]:,.2f}")
    except Exception as e:
        st.error(f"Erro ao prever: {e}")
        st.info("Verifique se os valores de entrada estão corretos e compatíveis com o modelo.")

st.caption("Baseado nos modelos salvos via MLflow.")