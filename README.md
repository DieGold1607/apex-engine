
# APEX — Barcelona '92 Simulation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

Simulador interactivo de trayectorias parabólicas desarrollado con `streamlit` y `plotly`.

## Descripción

APEX es una aplicación didáctica para visualizar y experimentar con trayectorias parabólicas (proyectiles). Permite ajustar parámetros físicos como velocidad inicial, ángulo y gravedad, y ver los resultados en tiempo real.

## Tabla de contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación (Windows - PowerShell)](#instalación-windows---powershell)
- [Ejecución (desarrollo)](#ejecución-desarrollo)
- [Ejemplo de uso](#ejemplo-de-uso)
- [Estructura de archivos (resumen)](#estructura-de-archivos-resumen)
- [Contribuciones](#contribuciones)
- [Desarrolladores](#desarrolladores)
- [Changelog](#changelog)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Características

- Interfaz web con `streamlit`.
- Gráficas interactivas con `plotly`.
- Controles para parámetros físicos y visualización instantánea.

## Requisitos


- Python 3.8+ (recomendado 3.10+)
- Dependencias (desde `requirements.txt`):

```text
streamlit==1.51.0
numpy==2.3.5
matplotlib==3.10.7
plotly==6.5.0
```

## Instalación (Windows - PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

Nota: si quieres versiones concretas, usa el `requirements.txt` existente o genera uno nuevo con `pip freeze > requirements.txt` desde tu entorno virtual.

## Ejecución (desarrollo)

```powershell
streamlit run app.py
```

Abre el enlace que Streamlit proporcione en la terminal para ver la interfaz.

## Ejemplo de uso

1. Crea y activa el entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Instala dependencias:

```powershell
pip install -r requirements.txt
```

3. Ejecuta la app y abre la URL que Streamlit muestre:

```powershell
streamlit run app.py
```

4. En la interfaz, ajusta parámetros (velocidad, ángulo, gravedad) en la barra lateral y observa la gráfica interactiva.

<!-- Capturas removed: store screenshots in assets/ if needed -->
## Desarrolladores

- Recomendaciones de flujo: usar `develop` para trabajo diario y `main` solo para releases estables.
- Estilo: escribe commits pequeños y descriptivos. Sigue Semantic Versioning en el `CHANGELOG.md`.
- Para desarrollar localmente, activa el entorno y ejecuta `streamlit run app.py`.

## Changelog

Ver `CHANGELOG.md` para historial de cambios.

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

