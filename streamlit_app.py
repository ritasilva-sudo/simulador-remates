
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador de Remates", page_icon="⚽")

st.title("⚽ Simulador de Remates")
st.write("Será que consegues marcar um golo?")

st.subheader("Configuração do remate")

velocidade = st.slider("Velocidade (km/h)", 40, 130, 85)
angulo = st.slider("Ângulo de elevação (graus)", 1, 45, 16)
distancia = st.slider("Distância à baliza (m)", 5, 30, 11)

# Conversão de unidades
v = velocidade / 3.6
theta = np.radians(angulo)
g = 9.81

# Trajetória parabólica (sem resistência do ar)
x = np.linspace(0, distancia, 150)
y = x * np.tan(theta) - (
    g * x**2 / (2 * v**2 * np.cos(theta)**2)
)

altura = y[-1]

st.subheader("📈 Trajetória da bola")

fig, ax = plt.subplots()
ax.plot(x, y, color="royalblue", linewidth=2, label="Bola")
ax.axvline(distancia, color="gray", linestyle="--", label="Baliza")
ax.plot(
    [distancia, distancia],
    [0, 2.44],
    color="red",
    linewidth=5,
    label="Altura da baliza",
)
ax.set_xlabel("Distância (m)")
ax.set_ylabel("Altura (m)")
ax.set_ylim(bottom=0)
ax.grid(alpha=0.3)
ax.legend()

st.pyplot(fig)
plt.close(fig)

st.subheader("🎯 Resultado")

if altura < 0:
    st.error("A bola toca no chão antes da baliza!")
elif altura > 2.44:
    st.warning("A bola passa por cima da barra!")
elif altura >= 1.8:
    st.success("Remate alto! Pode ser uma bola à gaveta! ⚽")
else:
    st.info("Remate dentro da altura da baliza!")

st.caption(
    "Modelo físico simplificado: não considera resistência do ar, "
    "direção lateral nem movimento do guarda-redes."
)
