import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="App Educativa de Inversiones 💰", layout="wide")

# -----------------------------
# Título y descripción
# -----------------------------
st.title("App Educativa de Inversiones y Pensiones 💰🏡✈️")
st.markdown("""
Bienvenido/a a la app interactiva para aprender sobre **inversiones y ahorro pensional**.  
Aquí podrás simular cómo tu dinero puede crecer con el tiempo y alcanzar tus metas.
""")

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("Tus datos")
ahorro_mensual = st.sidebar.number_input("Ahorro mensual ($)", min_value=0, value=500000, step=10000)
años = st.sidebar.number_input("Años de ahorro", min_value=1, max_value=50, value=10)
objetivo = st.sidebar.selectbox("Objetivo financiero", ["Fondo de pensión 🏦", "CDT 💵", "Finca raíz / apartamento 🏡", "Viaje ✈️"])
edad = st.sidebar.number_input("Edad actual", min_value=15, max_value=70, value=25)
ingreso_mensual = st.sidebar.number_input("Ingreso mensual ($)", min_value=0, value=2000000, step=10000)

# -----------------------------
# Cálculos de ahorro
# -----------------------------
interes_anual = 0.05  # 5% anual
meses = años * 12
saldo = []
capital = 0

for i in range(1, meses+1):
    capital = capital + ahorro_mensual
    capital = capital * (1 + interes_anual/12)
    saldo.append(capital)

capital_final = saldo[-1]

# -----------------------------
# Simulación y resultados
# -----------------------------
st.subheader("📊 Simulación de tu ahorro")
st.line_chart(saldo)

st.subheader("💡 Resumen")
st.markdown(f"""
- Objetivo: **{objetivo}**
- Edad actual: {edad} años
- Ahorro mensual: ${ahorro_mensual:,.0f}
- Tiempo: {años} años
- Interés anual aplicado: {interes_anual*100:.1f}%
- Capital acumulado aproximado: ${capital_final:,.0f}
""")

# -----------------------------
# Recomendaciones inteligentes
# -----------------------------
st.subheader("✅ Consejos personalizados")
if objetivo == "Viaje ✈️":
    st.markdown("Ahorra al menos un 10% más si tu meta es un viaje largo o internacional ✈️")
elif objetivo == "Finca raíz / apartamento 🏡":
    st.markdown("Considera inversiones adicionales si tu objetivo es una cuota inicial grande 🏡")
else:
    st.markdown("Mantén la constancia y revisa tus opciones de inversión periódicamente 💡")

if ahorro_mensual < ingreso_mensual * 0.2:
    st.markdown("💡 Estás ahorrando menos del 20% de tus ingresos. Considera aumentar tu ahorro para metas más seguras.")

# -----------------------------
# Simulación de impacto social
# -----------------------------
st.subheader("🌍 Impacto de la baja natalidad en pensiones")
st.markdown("""
Si la natalidad baja, habrá menos cotizantes y menos dinero disponible para pensiones.  
Por eso es importante **planificar tu ahorro e inversión individualmente**.
""")

# Escenarios
ahorro_poco = [x*0.7 for x in saldo]
ahorro_mucho = [x*1.3 for x in saldo]
st.line_chart({
    "Si todos ahorran poco": ahorro_poco,
    "Si todos ahorran más": ahorro_mucho,
    "Tu ahorro": saldo
})

# -----------------------------
# Mini tutorial educativo
# -----------------------------
st.subheader("📚 Mini tutorial educativo")
st.markdown("""
**Tipos de inversión:**
- Fondo de pensión voluntario 🏦: ahorro a largo plazo con beneficios fiscales.
- CDT 💵: inversión fija con interés garantizado.
- Finca raíz / apartamento 🏡: inversión en bienes raíces para aumentar patrimonio.
- Viaje ✈️: planificación financiera para metas personales.

**Riesgos:**
- No ahorrar suficiente puede afectar tu futuro.
- Empezar a invertir joven aprovecha el interés compuesto.
""")

# -----------------------------
# Motivación
# -----------------------------
st.subheader("🎯 Mensaje motivacional")
if edad < 30:
    st.markdown("¡Estás empezando en el mejor momento! Cada mes tu capital crece como un árbol 🌳")
else:
    st.markdown("Nunca es tarde para mejorar tu futuro financiero 💪. ¡Comienza hoy!")

st.markdown("¡Aprender a invertir y ahorrar puede ser divertido y seguro! 😄💰")
