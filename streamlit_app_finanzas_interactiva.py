import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="App Educativa de Inversiones 💰", layout="wide")

# -----------------------------
# Título principal
# -----------------------------
st.title("App Educativa de Inversiones y Pensiones 💰🏡✈️")
st.markdown("Aprende a planificar tu futuro financiero con simulaciones interactivas y consejos personalizados.")

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
# Pestañas principales
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(["📊 Simulación", "✅ Consejos", "🌍 Impacto social", "📚 Tutorial educativo"])

# -----------------------------
# TAB 1: Simulación
# -----------------------------
with tab1:
    st.subheader("Simulación de tu ahorro 💰")
    st.line_chart(saldo)
    
    progreso = min(1.0, capital_final / (ahorro_mensual*meses*1.2))  # ejemplo de progreso dinámico
    st.progress(progreso)
    
    st.markdown(f"""
    - Objetivo: **{objetivo}**
    - Edad actual: {edad} años
    - Ahorro mensual: ${ahorro_mensual:,.0f}
    - Tiempo: {años} años
    - Interés anual aplicado: {interes_anual*100:.1f}%
    - Capital acumulado aproximado: ${capital_final:,.0f} 💵
    """)

# -----------------------------
# TAB 2: Consejos
# -----------------------------
with tab2:
    st.subheader("Consejos personalizados 🎯")
    if objetivo == "Viaje ✈️":
        st.success("Ahorra al menos un 10% más si tu meta es un viaje largo o internacional ✈️")
    elif objetivo == "Finca raíz / apartamento 🏡":
        st.warning("Considera inversiones adicionales si tu objetivo es una cuota inicial grande 🏡")
    else:
        st.info("Mantén la constancia y revisa tus opciones de inversión periódicamente 💡")
    
    if ahorro_mensual < ingreso_mensual * 0.2:
        st.error("💡 Estás ahorrando menos del 20% de tus ingresos. Considera aumentar tu ahorro para metas más seguras.")

# -----------------------------
# TAB 3: Impacto social
# -----------------------------
with tab3:
    st.subheader("Impacto de la baja natalidad en pensiones 🌍")
    st.markdown("""
    Si la natalidad baja, habrá menos cotizantes y menos dinero disponible para pensiones.  
    Por eso es importante planificar tu ahorro e inversión individualmente.
    """)
    
    ahorro_poco = [x*0.7 for x in saldo]
    ahorro_mucho = [x*1.3 for x in saldo]
    df_scenarios = pd.DataFrame({
        "Si todos ahorran poco 🐢": ahorro_poco,
        "Si todos ahorran más 🚀": ahorro_mucho,
        "Tu ahorro 💰": saldo
    })
    st.line_chart(df_scenarios)

# -----------------------------
# TAB 4: Tutorial educativo
# -----------------------------
with tab4:
    st.subheader("Mini tutorial educativo 📚")
    st.markdown("""
    **Tipos de inversión:**
    - Fondo de pensión voluntario 🏦: ahorro a largo plazo con beneficios fiscales.
    - CDT 💵: inversión fija con interés garantizado.
    - Finca raíz / apartamento 🏡: inversión en bienes raíces para aumentar patrimonio.
    - Viaje ✈️: planificación financiera para metas personales.
    
    **Riesgos:**
    - No ahorrar suficiente puede afectar tu futuro.
    - Empezar a invertir joven aprovecha el interés compuesto.
    
    **Motivación:**
    - Si eres menor de 30: 🌳 ¡Estás empezando en el mejor momento! Cada mes tu capital crece.
    - Si eres mayor de 30: 💪 Nunca es tarde para mejorar tu futuro financiero. ¡Comienza hoy!
    """)

st.markdown("¡Aprender a invertir y ahorrar puede ser divertido y seguro! 😄💰")
