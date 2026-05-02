import streamlit as st

st.set_page_config(page_title="Manual do Novo Alvinegro", page_icon="⭐")

st.title("⚽ Guia de Setores: Estádio Nilton Santos")
st.markdown("""Bem-vindo ao Manual Glorioso! Este guia vai te ajudar a escolher o setor perfeito 
    para assistir ao jogo do Fogão de acordo com o seu perfil.""")

st.header("1. O Estádio: Nilton Santos (Niltão)")
st.info("O Estádio Nilton Santos, carinhosamente conhecido como Niltão, é um dos complexos esportivos mais modernos e icônicos do Brasil. Localizado no Rio de Janeiro, destaca-se por sua arquitetura imponente com arcos monumentais e uma atmosfera vibrante que acolhe grandes eventos esportivos e shows internacionais. É um verdadeiro templo de paixão e superação, sendo um orgulho para a cidade e um ponto de encontro essencial para os amantes do esporte.")

st.image("https://fogonarede.com.br/wp-content/uploads/2024/05/show-numanice-estadio-nilton-santos-botafogo.jpg")

st.divider()

st.header("2. Qual é o seu estilo de torcer?")

setores = {
    "Leste Inferior": {
        "clima": "🔥 O Coração Pulsante",
        "descricao": "É o setor onde a torcida costuma ficar mais tempo em pé e cantando. Embora não seja o setor oficial das organizadas (que ficam na Norte), a Leste Inferior puxa muitas músicas e é onde o pulso do estádio bate mais forte.",
        "perfil": "É um público misto, mas predominantemente jovem e de média idade que quer uma experiência imersiva. Não é tão confortável quanto a Oeste (onde o pessoal assiste mais sentado), nem tão raiz quanto a Norte ou Leste Superior. É o equilíbrio perfeito para quem quer sentir a pressão da torcida.",
    },
    "Leste Superior": {
        "clima": "📸 Visão Panorâmica e Festa",
        "descricao": "Visão panorâmica total (estilo câmera tática de videogame). Por ser um setor muito amplo e alto, o som da torcida ecoa na cobertura, criando uma acústica poderosa. O clima é de engajamento coletivo, onde milhares de vozes se unem, mas com a vantagem de ter uma visão clara de todo o esquema tático do time.",
        "perfil": "O Analista de Bancada. Aquele que quer economizar no ingresso sem perder a festa, prefere uma visão privilegiada de todas as áreas do campo e gosta de fugir da chuva (por ser totalmente coberto).",
    },
    "Oeste Inferior/Superior": {
        "clima": "Conforto e Família",
        "descricao": "É a visão centralizada e mais nobre do estádio. Na Inferior, você está logo atrás dos bancos de reservas; na Superior, tem a visão da área de imprensa. O clima é de contemplação e conforto. É o setor mais silencioso, onde o foco é o jogo em si, com menos pessoas em pé ou bandeirões atrapalhando a vista.",
        "perfil": "O Tradicional/Família. Ideal para quem vai com crianças pequenas, idosos ou quer uma experiência mais premium. É perfeito para quem prefere assistir ao jogo sentado e valoriza facilidade de acesso e menos aglomeração nas filas.",
    },
    "Norte": {
        "clima": "🥁 O Setor Popular",
        "descricao": "Visão de fundo de gol (perspectiva de profundidade). O clima é Raiz e Explosivo. É onde ficam as principais Torcidas Organizadas e a bateria. O barulho é constante, o clima é de arquibancada clássica, com muita movimentação e energia do início ao fim. É o setor onde o ingresso costuma ser mais barato.",
        "perfil": "Aquele que quer o clima de organizada, não para de pular um segundo, gosta de estar perto da bateria e não liga para o ângulo da visão, desde que o apoio ao Botafogo seja incondicional."
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
   
