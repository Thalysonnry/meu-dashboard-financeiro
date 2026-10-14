import streamlit as st
import yfinance as yf

# Configuração da página
st.set_page_config(page_title="Meu Primeiro Dashboard", layout="wide")

# Título do aplicativo
st.title("📊 Dashboard de Cotações em Tempo Real")
st.write("Projeto desenvolvido em Python para acompanhamento de ativos.")

# Criar uma barra lateral para interação do usuário
st.sidebar.header("Opções")
ativo = st.sidebar.text_input("Digite o código do ativo:", value="BTC-USD")
periodo = st.sidebar.selectbox("Escolha o período:", ["1mo", "6mo", "1y"], index=1)

# Buscar e exibir os dados
if ativo:
    try:
        dados = yf.download(ativo, period=periodo)
        
        if not dados.empty:
            st.subheader(f"Gráfico de Preço do Ativo: {ativo.upper()}")
            st.line_chart(dados['Close'])
        else:
            st.warning("Código de ativo inválido ou sem dados.")
            
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")