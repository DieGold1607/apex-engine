import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. DATOS REALES (Recopilados por César)
# ==========================================
v0 = 36.0           # Velocidad (m/s) calculada de 130 km/h
g = 9.8             # Gravedad
h_inicial = 1.7     # Ajuste: Altura de disparo (arquero promedio)

# Los 3 ángulos que propuso César
angulos = [22, 23, 25] 
colores = ['#ff0055', '#ffff00', '#00ffcc'] # Colores neón para cada intento

# Datos del Objetivo (Pebetero - Estimado para que cuadre)
distancia_pebetero = 70.0  # La distancia real solía ser ~70m
altura_pebetero = 21.0     # Altura aproximada del pebetero real

# ==========================================
# 2. SIMULACIÓN Y GRÁFICAS
# ==========================================
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

t_max = 3.5 # Tiempo de simulación suficiente para ver la caída
t = np.linspace(0, t_max, 500)

print(f"--- RESULTADOS DE SIMULACIÓN (V0 = {v0} m/s) ---")

for i, ang in enumerate(angulos):
    theta_rad = np.radians(ang)
    
    # Ecuaciones de Movimiento
    vx = v0 * np.cos(theta_rad)
    vy = v0 * np.sin(theta_rad)
    
    x = vx * t
    y = h_inicial + (vy * t) - (0.5 * g * t**2)
    
    # Filtramos para que no grafique bajo tierra
    mask = y >= 0
    
    # GRÁFICA 1: TRAYECTORIA
    label_text = f'Ángulo {ang}°'
    ax1.plot(x[mask], y[mask], color=colores[i], linewidth=2, label=label_text)
    
    # Calcular altura exacta al pasar por el pebetero (x=70)
    t_impacto = distancia_pebetero / vx
    y_impacto = h_inicial + (vy * t_impacto) - (0.5 * g * t_impacto**2)
    print(f"Ángulo {ang}° -> Altura a los 70m: {y_impacto:.2f} m")

# Dibujar el Pebetero (Meta)
ax1.plot(distancia_pebetero, altura_pebetero, 'wo', markersize=12, markeredgecolor='white', label='Pebetero')
ax1.vlines(distancia_pebetero, 0, altura_pebetero, colors='white', linestyles='dashed', alpha=0.3)

ax1.set_title(f'Análisis de Trayectoria (v0={v0} m/s)', fontsize=14, color='white')
ax1.set_xlabel('Distancia (m)')
ax1.set_ylabel('Altura (m)')
ax1.legend()
ax1.grid(True, alpha=0.2)

# ==========================================
# 3. ILUSIÓN ÓPTICA (Usando el ángulo de 25° que es el más alto)
# ==========================================
theta_best = np.radians(25)
x_best = (v0 * np.cos(theta_best)) * t
y_best = h_inicial + (v0 * np.sin(theta_best)) * t - (0.5 * g * t**2)

# Ángulo visual phi = arctan(y/x)
# Evitamos división por cero sumando un epsilon pequeño
phi = np.degrees(np.arctan2(y_best, x_best + 0.001))

ax2.plot(t[mask], phi[mask], color='#00ffcc', linewidth=2)
ax2.set_title('Ilusión Óptica: Ángulo Visual del Espectador', fontsize=14, color='white')
ax2.set_xlabel('Tiempo de vuelo (s)')
ax2.set_ylabel('Ángulo Aparente (Grados)')
ax2.grid(True, alpha=0.2)

# Zona crítica
ax2.axvspan(1.5, 2.5, color='red', alpha=0.1, label='Zona de "Enceste Visual"')
ax2.legend()

plt.tight_layout()
plt.show()