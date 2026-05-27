import streamlit as st  # Librería para crear aplicaciones web en Python
import time  # Librería para medir tiempos de ejecución

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(  # Configura la página de Streamlit
    page_title="Búsqueda y Ordenamiento",  # Título de la pestaña
    page_icon="🔵",  # Ícono de la pestaña
    layout="centered"  # Diseño centrado
)

# =====================================================
# ESTILOS
# =====================================================

st.markdown("""  
<style>

/* Fondo principal de la aplicación */
.stApp{
    background: linear-gradient(to bottom, #071120, #0b1730);
}

/* Estilo general del texto */
html, body, [class*="css"]{
    color:white;
    font-family:Arial;
}

/* Colores de los títulos */
h1, h2, h3{
    color:white;
}

/* TITULO PRINCIPAL */

.main-title{
    font-size:55px; /* Tamaño grande */
    font-weight:bold; /* Negrilla */
    color:#60a5fa; /* Azul */
}

/* SUBTITULO */

.sub-title{
    font-size:20px;
    color:#94a3b8;
}

/* INPUT */

.stTextInput input{
    background-color:#10233f !important; /* Fondo del input */
    color:white !important; /* Texto blanco */
    border-radius:15px !important; /* Bordes redondos */
    border:1px solid #2563eb !important; /* Borde azul */
    height:60px; /* Altura */
    font-size:24px; /* Tamaño texto */
}

/* BOTONES */

.stButton > button{
    background-color:#10233f; /* Fondo botón */
    color:white; /* Texto blanco */
    border:1px solid #2563eb; /* Borde azul */
    border-radius:15px; /* Bordes redondos */
    width:180px; /* Ancho */
    height:70px; /* Alto */
    font-size:22px; /* Tamaño letra */
    transition:0.3s; /* Animación */
}

/* EFECTO HOVER DEL BOTÓN */

.stButton > button:hover{
    background-color:#2563eb; /* Cambia color */
    color:white;
    border:1px solid #60a5fa;
}

/* TARJETAS */

.card{
    background-color:#0f1c35; /* Fondo tarjeta */
    padding:25px; /* Espaciado interno */
    border-radius:20px; /* Bordes redondos */
    border:1px solid #1d4ed8; /* Borde azul */
    margin-top:20px; /* Separación arriba */
}

/* TEXTO RESUMEN */

.resumen{
    color:#60a5fa;
    font-size:40px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)  # Permite usar HTML y CSS

# =====================================================
# ALGORITMOS DE ORDENAMIENTO
# =====================================================

def burbuja(lista):
    # Función Bubble Sort

    n = len(lista)  # Guarda tamaño de la lista

    for i in range(n):  # Recorre toda la lista

        for j in range(0, n - i - 1):  # Recorre comparando elementos

            if lista[j] > lista[j + 1]:  # Si el actual es mayor al siguiente

                # Intercambia posiciones
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista  # Retorna lista ordenada


def insercion(lista):
    # Función Insertion Sort

    for i in range(1, len(lista)):  # Empieza desde el segundo elemento

        actual = lista[i]  # Guarda valor actual

        j = i - 1  # Posición anterior

        # Mientras el anterior sea mayor
        while j >= 0 and lista[j] > actual:

            lista[j + 1] = lista[j]  # Mueve elemento a la derecha

            j -= 1  # Retrocede posición

        lista[j + 1] = actual  # Inserta valor correcto

    return lista  # Retorna lista ordenada


def mezcla(lista):
    # Función Merge Sort simplificada

    return sorted(lista)  # Usa sorted de Python

# =====================================================
# ALGORITMOS DE BÚSQUEDA
# =====================================================

def busqueda_lineal(lista, objetivo):
    # Busca recorriendo uno por uno

    for i in range(len(lista)):  # Recorre lista

        if lista[i] == objetivo:  # Si encuentra el objetivo

            return i  # Devuelve posición

    return -1  # Si no encuentra retorna -1


def busqueda_binaria(lista, objetivo):
    # Busca dividiendo la lista a la mitad

    izquierda = 0  # Inicio
    derecha = len(lista) - 1  # Final

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2  # Calcula centro

        if lista[medio] == objetivo:  # Si encuentra el valor

            return medio  # Retorna posición

        elif lista[medio] < objetivo:
            # Busca en la derecha

            izquierda = medio + 1

        else:
            # Busca en la izquierda

            derecha = medio - 1

    return -1  # Si no encuentra retorna -1

# =====================================================
# SESSION STATE
# =====================================================

# Guarda información para que no se reinicie la aplicación

if "lista_ordenada" not in st.session_state:
    st.session_state.lista_ordenada = None

if "algoritmo_ordenamiento" not in st.session_state:
    st.session_state.algoritmo_ordenamiento = None

if "tiempo_orden" not in st.session_state:
    st.session_state.tiempo_orden = None

if "algoritmo_busqueda" not in st.session_state:
    st.session_state.algoritmo_busqueda = None

if "tiempo_busqueda" not in st.session_state:
    st.session_state.tiempo_busqueda = None

if "posicion" not in st.session_state:
    st.session_state.posicion = None

# =====================================================
# TITULO
# =====================================================

st.markdown(
    '<p class="main-title">🔵 Búsqueda y Ordenamiento</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Sistema de análisis de algoritmos</p>',
    unsafe_allow_html=True
)

st.write("")  # Espacio vacío

# =====================================================
# PASO 1
# =====================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("1️⃣ ¿Cuál es el objetivo?")

objetivo = st.text_input(
    "Ingresa un número de 4 dígitos",
    max_chars=4,  # Máximo 4 caracteres
    placeholder="Ejemplo: 0001"
)

valido = False  # Variable de validación

if objetivo:

    if not objetivo.isdigit():
        # Verifica si son números

        st.error("❌ Solo puedes ingresar números")

    elif len(objetivo) < 4:
        # Verifica longitud

        st.warning("⚠️ Debes ingresar exactamente 4 dígitos")

    else:

        valido = True  # Activa validación

        st.success(f"✅ Objetivo válido: {objetivo}")

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# CONTINUAR SOLO SI ES VALIDO
# =====================================================

if valido:

    # Genera lista desde 0000 hasta 9999
    lista = [str(i).zfill(4) for i in range(0, 10000)]

    # =====================================================
    # ORDENAMIENTO
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("2️⃣ Elige el algoritmo de ordenamiento")

    # Divide pantalla en 3 columnas
    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("Burbuja"):

            inicio = time.perf_counter()  # Inicia cronómetro

            # Ejecuta algoritmo
            st.session_state.lista_ordenada = burbuja(lista.copy())

            # Calcula tiempo en microsegundos
            st.session_state.tiempo_orden = (
                time.perf_counter() - inicio
            ) * 1000000

            # Guarda nombre del algoritmo
            st.session_state.algoritmo_ordenamiento = "Burbuja"

    with col2:

        if st.button("Inserción"):

            inicio = time.perf_counter()

            st.session_state.lista_ordenada = insercion(lista.copy())

            st.session_state.tiempo_orden = (
                time.perf_counter() - inicio
            ) * 1000000

            st.session_state.algoritmo_ordenamiento = "Inserción"

    with col3:

        if st.button("Mezcla"):

            inicio = time.perf_counter()

            st.session_state.lista_ordenada = mezcla(lista.copy())

            st.session_state.tiempo_orden = (
                time.perf_counter() - inicio
            ) * 1000000

            st.session_state.algoritmo_ordenamiento = "Mezcla"

    # Verifica si ya se ordenó
    if st.session_state.lista_ordenada is not None:

        st.success(
            f"✅ {st.session_state.algoritmo_ordenamiento} completado"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # BUSQUEDA
    # =====================================================

    if st.session_state.lista_ordenada is not None:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("3️⃣ Elige el algoritmo de búsqueda")

        col4, col5 = st.columns(2)

        with col4:

            if st.button("Lineal"):

                inicio = time.perf_counter()

                # Ejecuta búsqueda lineal
                st.session_state.posicion = busqueda_lineal(
                    st.session_state.lista_ordenada,
                    objetivo
                )

                # Tiempo búsqueda
                st.session_state.tiempo_busqueda = (
                    time.perf_counter() - inicio
                ) * 1000000

                st.session_state.algoritmo_busqueda = "Lineal"

        with col5:

            if st.button("Binaria"):

                inicio = time.perf_counter()

                # Ejecuta búsqueda binaria
                st.session_state.posicion = busqueda_binaria(
                    st.session_state.lista_ordenada,
                    objetivo
                )

                st.session_state.tiempo_busqueda = (
                    time.perf_counter() - inicio
                ) * 1000000

                st.session_state.algoritmo_busqueda = "Binaria"

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # RESUMEN FINAL
    # =====================================================

    if st.session_state.algoritmo_busqueda is not None:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("🏆 Resumen Final")

        st.write("")

        st.write("Ordenamiento")

        # Muestra algoritmo usado
        st.markdown(
            f'<p class="resumen">{st.session_state.algoritmo_ordenamiento}</p>',
            unsafe_allow_html=True
        )

        # Muestra tiempo ordenamiento
        st.write(
            f"⏱ Tiempo Ordenamiento: {st.session_state.tiempo_orden:,.1f} μs"
        )

        st.write("")

        st.write("Búsqueda")

        # Muestra algoritmo búsqueda
        st.markdown(
            f'<p class="resumen">{st.session_state.algoritmo_busqueda}</p>',
            unsafe_allow_html=True
        )

        # Muestra tiempo búsqueda
        st.write(
            f"⏱ Tiempo Búsqueda: {st.session_state.tiempo_busqueda:,.1f} μs"
        )

        st.write("")

        # =====================================================
        # SUMAR 1 A LA POSICIÓN
        # =====================================================

        if st.session_state.posicion != -1:

            # Suma 1 porque las listas empiezan en 0
            posicion_real = st.session_state.posicion + 1

            st.success(
                f"🎯 Objetivo {objetivo} encontrado en la posición {posicion_real}"
            )

        else:

            st.error(
                f"❌ Objetivo {objetivo} no encontrado"
            )

        st.write("")

        # =====================================================
        # REINICIAR
        # =====================================================

        if st.button("🔄 Reiniciar"):

            # Reinicia variables
            st.session_state.lista_ordenada = None
            st.session_state.algoritmo_ordenamiento = None
            st.session_state.tiempo_orden = None
            st.session_state.algoritmo_busqueda = None
            st.session_state.tiempo_busqueda = None
            st.session_state.posicion = None

            st.rerun()  # Recarga aplicación

        st.markdown('</div>', unsafe_allow_html=True)