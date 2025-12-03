import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- CONFIGURACIÓN DE LA PÁGINA (Título y Layout) ---
st.set_page_config(
    page_title="Simulador Barcelona 92 - Equipo Alfa",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏹"
)

# Estilo CSS para forzar modo oscuro y fuentes tipo "Hacker"
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    h1, h2, h3 {
        font-family: 'Courier New', monospace;
        color: #00ffcc;
    }
    .stSlider > div > div > div > div {
        background-color: #ff0055;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (CONTROLES DEL USUARIO) ---
st.sidebar.header("🎛️ Panel de Control")
st.sidebar.markdown("Ajusta los parámetros para simular el tiro:")

# Sliders interactivos
velocidad = st.sidebar.slider("Velocidad Inicial (m/s)", 20.0, 45.0, 29.5, 0.5)
angulo = st.sidebar.slider("Ángulo de Disparo (°)", 10.0, 80.0, 50.0, 1.0)
h_inicial = 1.7
distancia_pebetero = 66.0
altura_pebetero = 27.0

st.sidebar.markdown("---")
st.sidebar.markdown("**Datos Técnicos:**")
st.sidebar.info(f"🏹 Flecha: Easton X7 (100g)\n🎯 Objetivo: {distancia_pebetero}m / {altura_pebetero}m")
st.sidebar.text("Desarrollado por: Equipo Alfa")

# --- LÓGICA MATEMÁTICA ---
g = 9.81
theta_rad = np.radians(angulo)
t_max = 5.0
t = np.linspace(0, t_max, 500)

vx = velocidad * np.cos(theta_rad)
vy = velocidad * np.sin(theta_rad)
x = vx * t
y = h_inicial + (vy * t) - (0.5 * g * t**2)

# Filtrar suelo
mask = y >= 0
x_plot = x[mask]
y_plot = y[mask]
t_plot = t[mask]

# Calcular altura exacta en el muro (x=66)
if vx > 0:
    t_impacto = distancia_pebetero / vx
    y_impacto = h_inicial + (vy * t_impacto) - (0.5 * g * t_impacto**2)
else:
    y_impacto = 0

# --- INTERFAZ PRINCIPAL ---
st.title("🏹 PROYECTO BARCELONA '92: ANÁLISIS BALÍSTICO")
st.markdown("### ¿Fue un tiro real o una ilusión óptica? Compruébalo tú mismo.")

# Columnas para las gráficas
col1, col2 = st.columns(2)

# GRÁFICA 1: TRAYECTORIA
with col1:
    plt.style.use('dark_background')
    fig1, ax1 = plt.subplots(figsize=(10, 6), facecolor='#0f172a')
    ax1.set_facecolor('#1e293b')
    
    # Trayectoria
    ax1.plot(x_plot, y_plot, color='#00ffcc', linewidth=3, label=f'Tiro a {angulo}°')
    
    # Muro y Pebetero
    ax1.fill_between([66, 70], 0, 27, color='#64748b', alpha=0.5, label='Muro Estadio')
    ax1.plot(distancia_pebetero, altura_pebetero, 'wo', markersize=15, markeredgecolor='white')
    
    # Estética
    ax1.set_title(f"TRAYECTORIA FÍSICA (V={velocidad} m/s)", fontsize=12, color='white')
    ax1.set_xlabel("Distancia (m)")
    ax1.set_ylabel("Altura (m)")
    ax1.grid(True, alpha=0.2, linestyle='--')
    ax1.set_ylim(0, max(35, max(y_plot)+5))
    ax1.legend()
    
    st.pyplot(fig1)

# GRÁFICA 2: ILUSIÓN ÓPTICA
with col2:
    fig2, ax2 = plt.subplots(figsize=(10, 6), facecolor='#0f172a')
    ax2.set_facecolor('#1e293b')
    
    # Cálculo de ángulo visual
    phi = np.degrees(np.arctan2(y_plot, x_plot + 0.001))
    
    ax2.plot(t_plot, phi, color='#ff00ff', linewidth=3)
    ax2.set_title("ILUSIÓN ÓPTICA (PERSPECTIVA)", fontsize=12, color='white')
    ax2.set_xlabel("Tiempo (s)")
    ax2.set_ylabel("Ángulo Visual (°)")
    ax2.grid(True, alpha=0.2, linestyle='--')
    
    st.pyplot(fig2)

# --- VEREDICTO AUTOMÁTICO ---
st.markdown("---")
st.subheader("📢 VEREDICTO DEL SISTEMA:")

margen_error = 2.0 # metros
diferencia = y_impacto - altura_pebetero

if y_impacto < 0:
    st.error(f"❌ FALLO TOTAL: La flecha no llegó al muro. Cayó al suelo antes.")
elif y_impacto < altura_pebetero:
    st.error(f"❌ IMPACTO EN MURO: La flecha chocó contra la pared a {y_impacto:.2f}m de altura. (Faltaron {abs(diferencia):.2f}m)")
elif y_impacto > (altura_pebetero + 4):
    st.warning(f"⚠️ DEMASIADO ALTO: La flecha pasó {diferencia:.2f}m por encima. Riesgo de caer en la grada opuesta.")
else:
    st.success(f"✅ ¡TIRO PERFECTO! La flecha pasó {diferencia:.2f}m por encima del pebetero, encendiendo el gas.")
    st.balloons() # EFECTO DE FIESTA SI ACIERTAN