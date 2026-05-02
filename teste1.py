import streamlit as st


st.set_page_config(page_title="Manual do Novo Alvinegro", page_icon="⭐")

st.title("⚽ Guia de Setores: Estádio Nilton Santos")
st.markdown("""Bem-vindo ao Manual Glorioso! Este guia vai te ajudar a escolher o lugar perfeito 
    para assistir ao jogo do Fogão de acordo com o seu perfil.""")

st.header("1. O Palco: Nilton Santos (Niltão)")
st.info("O Estádio Nilton Santos, carinhosamente conhecido como Niltão, é um dos complexos esportivos mais modernos e icônicos do Brasil. Localizado no Rio de Janeiro, destaca-se por sua arquitetura imponente com arcos monumentais e uma atmosfera vibrante que acolhe grandes eventos esportivos e shows internacionais. É um verdadeiro templo de paixão e superação, sendo um orgulho para a cidade e um ponto de encontro essencial para os amantes do esporte.")

st.image("https://fogonarede.com.br/wp-content/uploads/2024/05/show-numanice-estadio-nilton-santos-botafogo.jpg", caption="O Templo Alvinegro")

st.divider()

st.header("2. Qual é o seu estilo de torcer?")

setores = {
    "Leste Inferior": {
        "clima": "🔥 O Coração Pulsante",
        "descricao": "Onde a festa acontece. Setor mais próximo do campo, com bandeirões e cantoria ininterrupta.",
        "perfil": "Torcedor que quer cantar os 90 minutos e não se importa de ficar em pé.",
    },
    "Leste Superior": {
        "clima": "📸 Visão Panorâmica e Festa",
        "descricao": "Excelente custo-benefício. Você vê o jogo de cima (tática perfeita) e a torcida também é muito engajada.",
        "perfil": "Torcedor que gosta de ver o desenho do time em campo e participar da festa.",
    },
    "Oeste Inferior/Superior": {
        "clima": "Conforto e Família",
        "descricao": "Setores mais tranquilos e acesso mais rápido. Geralmente onde ficam as cabines de imprensa e a área kids.",
        "perfil": "Famílias com crianças, idosos ou quem prefere assistir ao jogo sentado com mais calma.",
    },
    "Norte": {
        "clima": "🥁 O Setor Popular",
        "descricao": "O setor atrás do gol. É o local das organizadas e de ingressos mais acessíveis.",
        "perfil": "Torcedor raiz que quer o clima das organizadas e energia máxima."
    }
}
escolha = st.selectbox("Escolha um setor para conhecer os detalhes:", list(setores.keys()))


if escolha:
    st.subheader(f"Setor {escolha}")
    st.write(f"**Clima:** {setores[escolha]['clima']}")
    st.write(setores[escolha]['descricao'])
    st.write(f"👉 **Ideal para:** {setores[escolha]['perfil']}")

st.divider()

if st.button("Finalizar Guia: Onde encontro ingressos?"):
    st.success("Acesse o site oficial: **https://www.ingresse.com/**")
   
