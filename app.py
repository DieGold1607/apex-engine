import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- 1. CONFIGURACIÓN DEL SISTEMA ---
st.set_page_config(
    page_title="APEX | Barcelona '92 Simulation",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS "LUMINA ULTIMATE" ---
st.markdown("""
<style>
    /* FUENTES */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Space+Grotesk:wght@300;500;700&display=swap');

    :root {
        --bg-void: #020204;
        --neon-cyan: #00F5A0;
        --neon-purple: #9D00FF;
        --glass-bg: rgba(255, 255, 255, 0.03);
        --glass-border: 1px solid rgba(255, 255, 255, 0.08);
        --text-main: #FFFFFF;
        --text-dim: #94A3B8;
    }

    html { scroll-behavior: smooth; }

    .stApp {
        background-color: var(--bg-void);
        background-image: 
            radial-gradient(circle at 50% -10%, rgba(0, 245, 160, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 80% 60%, rgba(157, 0, 255, 0.08) 0%, transparent 40%),
            radial-gradient(circle at 10% 90%, rgba(0, 245, 160, 0.05) 0%, transparent 40%);
        font-family: 'Inter', sans-serif;
    }

    /* TIPOGRAFÍA */
    h1, h2, h3, h4 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: var(--text-main) !important;
        letter-spacing: -0.02em;
    }
    
    .big-title {
        font-size: 4.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #fff 30%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.1;
        margin-bottom: 20px;
    }
    
    .subtitle {
        color: var(--neon-cyan);
        font-family: 'Space Grotesk';
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 0.8rem;
        margin-bottom: 20px;
        border-left: 2px solid var(--neon-cyan);
        padding-left: 10px;
    }

    /* SUBTÍTULOS */
    .section-header {
        font-family: 'Space Grotesk';
        font-size: 2rem;
        color: white;
        margin-top: 60px;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .section-number {
        color: var(--neon-purple);
        font-size: 1rem;
        border: 1px solid var(--neon-purple);
        padding: 5px 10px;
        border-radius: 50px;
    }

    /* TARJETAS GLASSMORPHISM */
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: var(--glass-border);
        border-radius: 24px;
        padding: 30px;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .glass-card:hover {
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }

    /* TABLAS */
    .tech-table {
        width: 100%;
        border-collapse: collapse;
        color: #ccc;
        font-size: 0.9rem;
    }
    .tech-table td {
        padding: 12px 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    .tech-value {
        text-align: right;
        color: white;
        font-family: 'Space Grotesk', monospace;
        font-weight: bold;
    }

    /* MODIFICACIÓN DE EXPANDER PARA LA NOTA */
    .streamlit-expanderHeader {
        font-family: 'Space Grotesk';
        color: #94A3B8;
        font-size: 0.9rem;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stSlider > div > div > div > div {
        background-color: var(--neon-cyan) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. HERO SECTION ---
c1, c2 = st.columns([1.5, 1])
with c1:
    st.markdown('<div class="subtitle">PROYECTO FINAL CÁLCULO I</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="big-title">EL TIRO IMPOSIBLE:<br>BARCELONA \'92</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size: 1.1rem; color: #94A3B8; max-width: 600px; line-height: 1.6;">
        Análisis diferencial y simulación física del encendido del pebetero olímpico. 
        Desmitificando la leyenda con cálculo vectorial y optimización industrial.
    </p>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: right;">
        <span style="background: rgba(255,255,255,0.1); padding: 8px 16px; border-radius: 20px; font-family: Space Grotesk; font-size: 0.8rem; color: white;">
            EQUIPO ALFA & GAMMA
        </span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 4. SECCIÓN 1: CONTEXTO ---
col_text, col_data = st.columns([1.2, 1])

with col_text:
    st.markdown("""
    <div class="section-header">
        <span class="section-number">01</span>
        <span>CONTEXTO HISTÓRICO</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: white; margin-bottom: 15px;">¿MITO O REALIDAD?</h3>
        <p style="color: #94A3B8; line-height: 1.6;">
            El encendido del pebetero en 1992 por <strong>Antonio Rebollo</strong> es icónico. 
            Sin embargo, la física dictaba un riesgo inaceptable: si la flecha intentaba entrar y golpeaba el borde, 
            podía rebotar hacia la multitud.
        </p>
        <p style="color: #94A3B8; line-height: 1.6;">
            <strong>La solución:</strong> Un truco de perspectiva. El objetivo real era pasar 
            <span style="color: #00F5A0;">por encima</span> del pebetero, cruzando una nube de gas.
        </p>
    </div>
    
    <div class="glass-card">
        <h4 style="color: #fff; margin-bottom: 10px;">EL "BOTÓN DE PÁNICO"</h4>
        <p style="font-size: 0.9rem; color: #94A3B8;">
            Investigaciones revelan que existía un mecanismo de seguridad. Si el viento desviaba la flecha, 
            un técnico detonaría el gas manualmente para asegurar el espectáculo.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_data:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="glass-card">
        <h3 style="color: #00F5A0; margin-bottom: 20px; font-size: 1.2rem;">PARÁMETROS REALES</h3>
        <table class="tech-table">
            <tr><td>PESO FLECHA</td><td class="tech-value">100 - 120 g</td></tr>
            <tr><td>ÁNGULO REQUERIDO</td><td class="tech-value">~48° - 52°</td></tr>
            <tr><td>VELOCIDAD INICIAL</td><td class="tech-value">~29 - 32 m/s</td></tr>
            <tr><td>OBJETIVO REAL</td><td class="tech-value">Pasar >2m Alto</td></tr>
        </table>
        <div style="margin-top: 20px; font-size: 0.75rem; color: #666; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px;">
            DATOS RECUPERADOS DE ANÁLISIS FORENSE DEL EVENTO
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 5. SECCIÓN 2: SIMULADOR ---
st.markdown("""
<div class="section-header">
    <span class="section-number">02</span>
    <span>SIMULADOR DE TRAYECTORIA</span>
</div>
""", unsafe_allow_html=True)

c_ctrl, c_viz = st.columns([1, 2.5])

# --- CONTROLES ---
with c_ctrl:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h4 style="color: #00F5A0; margin-bottom: 15px;">CONFIGURACIÓN</h4>', unsafe_allow_html=True)
    
    velocidad = st.slider("Velocidad Inicial (m/s)", 20.0, 60.0, 31.5, 0.1) 
    angulo = st.slider("Ángulo de Elevación (°)", 30.0, 80.0, 50.0, 0.5)
    
    # Cálculos
    theta_rad = np.radians(angulo)
    vx_val = velocidad * np.cos(theta_rad)
    vy_val = velocidad * np.sin(theta_rad)
    
    st.markdown('<div style="margin: 20px 0; border-top: 1px solid rgba(255,255,255,0.1);"></div>', unsafe_allow_html=True)
    st.markdown('<h4 style="color: #9D00FF; margin-bottom: 10px;">VECTORES (DERIVADA)</h4>', unsafe_allow_html=True)
    
    c_vx, c_vy = st.columns(2)
    with c_vx: st.metric("Vx (Horizontal)", f"{vx_val:.1f} m/s")
    with c_vy: st.metric("Vy (Vertical)", f"{vy_val:.1f} m/s")
    
    st.markdown('</div>', unsafe_allow_html=True) 
    
    # --- AQUI ESTÁ LA JUSTIFICACIÓN DE TRANSPARENCIA ---
    with st.expander("ℹ️ NOTA TÉCNICA: MODELO IDEAL VS. REALIDAD"):
        st.markdown("""
        <div style="font-size: 0.85rem; color: #ccc; line-height: 1.5; font-family: Inter;">
            <strong style="color: #fff;">Justificación del Modelo:</strong><br>
            Para este proyecto de <em>Cálculo Diferencial I</em>, utilizamos un modelo físico de <strong>vacío ideal</strong> (sin resistencia del aire). 
            Esto permite demostrar el uso exacto de derivadas en componentes vectoriales ($v_x, v_y$) sin la complejidad de Ecuaciones Diferenciales no lineales.<br><br>
            <strong style="color: #fff;">Compensación:</strong> En la realidad, la fricción frenaría la flecha. Por ello, el simulador utiliza una velocidad inicial efectiva ($31.5$ m/s) ligeramente superior a la histórica ($~29$ m/s) para compensar matemáticamente la pérdida de energía y lograr la trayectoria geométrica correcta.
        </div>
        """, unsafe_allow_html=True)

# --- FÍSICA ---
g = 9.81
h_inicial = 1.7
distancia_pebetero = 66.0
altura_pebetero = 27.0
t = np.linspace(0, 8.0, 400) 
x = vx_val * t
y = h_inicial + (vy_val * t) - (0.5 * g * t**2)

mask = (y >= 0) & (x <= 100)
x_plot = x[mask]
y_plot = y[mask]

if vx_val > 0:
    t_impacto = distancia_pebetero / vx_val
    y_impacto = h_inicial + (vy_val * t_impacto) - (0.5 * g * t_impacto**2)
else:
    y_impacto = 0

# VEREDICTO
diferencia = y_impacto - altura_pebetero
veredicto_color = "#FF2E2E"
veredicto_text = "FALLO DE TRAYECTORIA"

if y_impacto < 0:
    veredicto_text = "IMPACTO EN SUELO"
elif y_impacto < altura_pebetero:
    veredicto_text = f"COLISIÓN CON MURO ({y_impacto:.2f}m)"
elif 0 <= diferencia <= 8: 
    veredicto_color = "#00F5A0"
    veredicto_text = f"OBJETIVO ALCANZADO (+{diferencia:.2f}m)"
else:
    veredicto_color = "#FFBA00"
    veredicto_text = f"SOBREPASO EXCESIVO (+{diferencia:.2f}m)"

# --- VISUALIZACIÓN ---
with c_viz:
    st.markdown('<div class="glass-card" style="padding: 0; overflow: hidden;">', unsafe_allow_html=True)
    
    fig = go.Figure(
        data=[
            go.Scatter(x=[66, 66], y=[0, 27], mode="lines", line=dict(color="rgba(255,255,255,0.2)", width=2), name="Muro"),
            go.Scatter(x=[66], y=[27], mode="markers", marker=dict(color="white", size=12, symbol="diamond"), name="Pebetero"),
            go.Scatter(x=[x_plot[0]], y=[y_plot[0]], mode="markers", marker=dict(color="#00F5A0", size=10), name="Flecha"),
            go.Scatter(x=[x_plot[0]], y=[y_plot[0]], mode="lines", line=dict(color="#00F5A0", width=4), name="Trayectoria")
        ],
        layout=go.Layout(
            xaxis=dict(range=[0, 90], showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Distancia (m)", zeroline=False, color="#94A3B8"),
            yaxis=dict(range=[0, 55], showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Altura (m)", zeroline=False, color="#94A3B8"),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            height=500,
            margin=dict(l=20, r=20, t=20, b=20),
            hovermode="x unified",
            updatemenus=[dict(
                type="buttons",
                showactive=False,
                x=0.05, y=0.95,
                bgcolor="rgba(0,0,0,0.5)",
                font=dict(color="white"),
                buttons=[dict(
                    label="INICIAR SIMULACIÓN",
                    method="animate",
                    args=[None, dict(frame=dict(duration=10, redraw=False), fromcurrent=True, mode='immediate')]
                )]
            )]
        ),
        frames=[go.Frame(
            data=[
                go.Scatter(x=[66, 66], y=[0, 27]), 
                go.Scatter(x=[66], y=[27]),        
                go.Scatter(x=[x_plot[k]], y=[y_plot[k]]), 
                go.Scatter(x=x_plot[:k], y=y_plot[:k])    
            ]
        ) for k in range(1, len(x_plot), 5)] 
    )
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    st.markdown('</div>', unsafe_allow_html=True)

# --- KPI FINAL ---
st.write("")
k1, k2, k3 = st.columns(3)

with k1:
    st.markdown(f"""
    <div class="glass-card" style="text-align: center; padding: 20px;">
        <div style="font-size: 0.8rem; color: #888; letter-spacing: 1px;">ALTURA AL CRUZAR</div>
        <div style="font-family: Space Grotesk; font-size: 2rem; color: white;">{y_impacto:.2f}m</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="glass-card" style="text-align: center; padding: 20px; border-color: {veredicto_color};">
        <div style="font-size: 0.8rem; color: {veredicto_color}; letter-spacing: 1px;">VEREDICTO</div>
        <div style="font-family: Space Grotesk; font-size: 1.5rem; font-weight: bold; color: {veredicto_color};">{veredicto_text}</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="glass-card" style="text-align: center; padding: 20px;">
        <div style="font-size: 0.8rem; color: #888; letter-spacing: 1px;">TIEMPO DE VUELO</div>
        <div style="font-family: Space Grotesk; font-size: 2rem; color: white;">{t_impacto:.2f}s</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><div style='text-align:center; color:#555; font-size:0.8rem;'>APEX ENGINE V12.0 | EQUIPO ALFA & GAMMA</div>", unsafe_allow_html=True)