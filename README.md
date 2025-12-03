# APEX — Barcelona '92 Simulation

Simulador interactivo de trayectorias parabólicas desarrollado con Streamlit y Plotly.

## Descripción

APEX es una aplicación didáctica para visualizar y experimentar con trayectorias parabólicas (proyectiles). Permite ajustar parámetros físicos como velocidad inicial, ángulo y gravedad, y ver los resultados en tiempo real.

## Características

- Interfaz web con `streamlit`.
- Gráficas interactivas con `plotly`.
- Controles para parámetros físicos y visualización instantánea.

## Requisitos

- Python 3.8+ (recomendado 3.10+)
- Ver `requirements.txt` para las dependencias exactas

## Instalación (Windows - PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecución (desarrollo)

```powershell
streamlit run app.py
```

Abre el enlace que Streamlit proporcione en la terminal para ver la interfaz.

## Estructura de archivos (resumen)

- `app.py` — Archivo principal de la aplicación Streamlit.
- `requirements.txt` — Dependencias del proyecto.
- `Proyecto final de Cálculo I - calculos preliminares.py` — Cálculos auxiliares.
- `app (v1, antes de las correcciones mas elegantes).py` — Versión previa/experimental.

## Contribuciones

- Abrir issues para bugs o propuestas.
- Hacer fork y pull request para cambios. Mantener commits claros y breves.

## Licencia

Este proyecto está licenciado bajo la licencia **MIT**. Consulta el archivo `LICENSE` en la raíz del repositorio para ver el texto completo.

## Contacto

- Autor: Diego
- Email: diegold1607@gmail.com
- Repositorio: https://github.com/DieGold1607/apex-engine
