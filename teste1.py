import streamlit as st

# Configurações iniciais da página
st.set_page_config(page_title="Manual do Novo Alvinegro", page_icon="⭐")

# Título e Introdução
st.title("⚽ Guia de Setores: Estádio Nilton Santos")
st.markdown("""Bem-vindo ao Glorioso! Este guia vai te ajudar a escolher o lugar perfeito 
    para assistir ao jogo do Fogão de acordo com o seu perfil.""")

# --- SEÇÃO 1: O ESTÁDIO ---
st.header("1. O Palco: Nilton Santos (Niltão)")
st.info("Localizado no Engenho de Dentro, o estádio é a nossa casa. Possui tecnologia de gramado sintético de última geração.")

# Espaço para uma imagem geral do estádio
# st.image("https://fogonarede.com.br/wp-content/uploads/2024/05/show-numanice-estadio-nilton-santos-botafogo.jpg", caption="O Templo Alvinegro")

st.divider()

# --- SEÇÃO 2: IDENTIFICADOR DE PERFIL ---
st.header("2. Qual é o seu estilo de torcer?")

# Dicionário com as informações dos setores
setores = {
    "Leste Inferior": {
        "clima": "🔥 O Coração Pulsante",
        "descricao": "Onde a festa acontece. Setor mais próximo do campo, com bandeirões e cantoria ininterrupta.",
        "perfil": "Torcedor que quer cantar os 90 minutos e não se importa de ficar em pé.",
        "video_placeholder": "Insira aqui o link de um vlog ou vídeo da bateria."
    },
    "Leste Superior": {
        "clima": "📸 Visão Panorâmica e Festa",
        "descricao": "Excelente custo-benefício. Você vê o jogo de cima (tática perfeita) e a torcida também é muito engajada.",
        "perfil": "Torcedor que gosta de ver o desenho do time em campo e participar da festa.",
        "video_placeholder": "Insira aqui um vídeo da vista superior."
    },
    "Oeste Inferior/Superior": {
        "clima": "☕ Conforto e Família",
        "descricao": "Setores mais tranquilos, com cadeiras estofadas (na Inferior) e acesso mais rápido. Geralmente onde ficam as cabines de imprensa.",
        "perfil": "Famílias com crianças, idosos ou quem prefere assistir ao jogo sentado com mais calma.",
        "video_placeholder": "Insira aqui um vídeo da entrada da Oeste."
    },
    "Norte": {
        "clima": "🥁 O Setor Popular",
        "descricao": "O setor atrás do gol. É o local das organizadas e de ingressos mais acessíveis.",
        "perfil": "Torcedor raiz que quer o clima das organizadas e energia máxima.",
        "video_placeholder": "Insira aqui um vídeo da entrada da Norte."
    }
}

# Selectbox para o usuário escolher
escolha = st.selectbox("Escolha um setor para conhecer os detalhes:", list(setores.keys()))

# Exibição dos detalhes com base na escolha
if escolha:
    st.subheader(f"Setor {escolha}")
    st.write(f"**Clima:** {setores[escolha]['clima']}")
    st.write(setores[escolha]['descricao'])
    st.write(f"👉 **Ideal para:** {setores[escolha]['perfil']}")
    
    # Espaço para Mídia (Imagens ou Vídeos)
    col1, col2 = st.columns(2)
    with col1:
        st.warning("📸 [Lugar para foto da vista do setor]")
        # st.image("caminho/para/foto_setor.jpg")
    with col2:
        st.warning("🎥 [Lugar para vídeo do clima]")
        # st.video("link_do_youtube_ou_arquivo")

st.divider()

# --- SEÇÃO 3: CONCLUSÃO ---
if st.button("Finalizar Guia: Onde encontro ingressos?"):
    st.success("Acesse o site oficial: **https://www.ingresse.com/**")
    st.balloons()
