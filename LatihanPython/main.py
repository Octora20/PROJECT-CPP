import streamlit as st

def page_one():
    st.write ("""
    # Selamat datang di program sederhana
    Pilih salah satu menu di bawah ini
    """)
    if st.button("Luas Segitiga"):
        st.session_state.page = "luas_segitiga"

def page_two():
    st.write ("""
    # Aplikasi Luas Segitiga
    Ini adalah aplikasi menghitung luas segitiga sederhana
    """)

    alas = st.number_input("Masukkan Alas", 0)
    tinggi = st.number_input("Masukkan Tinggi", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 0.5 * alas * tinggi 
        st.success(f"Luas segitiganya adalah {luas}")



# Inisialisasi session state
if 'page' not in st.session_state:
    st.session_state.page = "welcome"

# Menampilkan halaman berdasarkan session state
if st.session_state.page == "welcome":
    page_one()
elif st.session_state.page == "luas_segitiga":
    page_two()
    
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Copyright @yohanoctora")