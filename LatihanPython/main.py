import streamlit as st

def page_one():
    st.write ("""
    # Selamat datang di program sederhana
    Pilih salah satu menu di bawah ini
    """)
    if st.button("Luas Segitiga"):
        st.session_state.page = "luas_segitiga"
    if st.button("Luas Persegi"):
        st.session_state.page = "luas_persegi"

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

    # Tombol untuk kembali ke page one
    if st.button("Kembali ke Menu Utama"):
        st.session_state.page = "welcome"

def page_three():
    st.write ("""
    # Aplikasi Luas Persegi
    Ini adalah aplikasi menghitung luas persegi sederhana
    """)

    sisi = st.number_input("Masukkan Panjang Sisi", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = sisi * sisi
        st.success(f"Luas persegi adalah {luas}")

    # Tombol untuk kembali ke page one
    if st.button("Kembali ke Menu Utama"):
        st.session_state.page = "welcome"

# Inisialisasi session state
if 'page' not in st.session_state:
    st.session_state.page = "welcome"

# Menampilkan halaman berdasarkan session state
if st.session_state.page == "welcome":
    page_one()
elif st.session_state.page == "luas_segitiga":
    page_two()
elif st.session_state.page == "luas_persegi":
    page_three()

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("Copyright @yohanoctora")
