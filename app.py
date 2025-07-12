import streamlit as st
import pandas as pd

# Título da página
st.set_page_config(page_title="Sorteador de Filmes", page_icon="🎬", layout="centered")

st.markdown("""
<style>
    .main {
        background-color: #f9f9f9;
        padding: 2rem;
        border-radius: 1rem;
    }
    h1 {
        color: #333333;
        font-family: 'Segoe UI', sans-serif;
    }
    .filme-box {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title('🎬 Sorteador de Filmes')

# Carrega o DataFrame
df = pd.read_csv('teste_filme_sem_india.csv', sep=';', dtype=str)

st.write("Clique no botão abaixo para sortear um filme aleatório (sem produções da Índia):")

if st.button('🎲 Sortear Filme'):
    filme = df.sample(n=1).iloc[0]

    st.markdown("""
    <div class="filme-box">
        <h2>{}</h2>
        <p><strong>• Ano:</strong> {}</p>
        <p><strong>• Nota IMDb:</strong> {} ({:,} votos)</p>
        <p><strong>• Gêneros:</strong> {}</p>
    </div>
    """.format(
        filme['title'],
        filme['startYear'],
        filme['averageRating'],
        int(filme['numVotes'].replace(',', '')) if filme['numVotes'].replace(',', '').isdigit() else 0,
        filme['genres']
    ), unsafe_allow_html=True)
else:
    st.info("Nenhum filme sorteado ainda. Clique no botão acima para sortear um!")
