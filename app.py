
import streamlit as st
import pandas as pd

# Título e layout
st.set_page_config(page_title="Sorteador de Filmes", page_icon="🎬", layout="centered")
st.title('🎬 Sorteador de Filmes')

# Carrega os dados
df = pd.read_csv('teste_filme_sem_india.csv', sep=';', dtype=str)

# Trata colunas numéricas
df['startYear'] = pd.to_numeric(df['startYear'], errors='coerce')
df['averageRating'] = pd.to_numeric(df['averageRating'], errors='coerce')
df['numVotes'] = pd.to_numeric(df['numVotes'].str.replace(',', ''), errors='coerce')

# Extrai todos os gêneros possíveis
todos_generos = sorted(set(g for sub in df['genres'].dropna().str.split(',') for g in sub))

# Filtros
ano_minimo = st.slider('Ano mínimo de lançamento', min_value=int(df['startYear'].min()), max_value=int(df['startYear'].max()), value=2000)
genero_selecionado = st.selectbox('Selecione um gênero', options=['Todos'] + todos_generos)

# Aplica filtros
df_filtrado = df[df['startYear'] >= ano_minimo].copy()

if genero_selecionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['genres'].str.contains(genero_selecionado, na=False)]

# Botão para sortear
if st.button('🎲 Sortear Filme'):
    if not df_filtrado.empty:
        filme = df_filtrado.sample(n=1).iloc[0]

        st.subheader(filme['title'])
        st.write(f"• Ano: {int(filme['startYear'])}")
        st.write(f"• Nota IMDb: {filme['averageRating']} ({int(filme['numVotes'])} votos)")
        st.write(f"• Gêneros: {filme['genres']}")
    else:
        st.warning("Nenhum filme encontrado com os critérios selecionados.")
else:
    st.info("Use os filtros e clique no botão para sortear um filme.")
