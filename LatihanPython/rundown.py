import streamlit as st
import pandas as pd

def main():
    st.title("Rundown Acara")

    # Tambahkan input untuk menambahkan item rundown dan jam
    item = st.text_input("Tambahkan item rundown:")
    time = st.text_input("Tambahkan waktu (jam:menit):")
    if st.button("Tambahkan"):
        if "rundown" not in st.session_state:
            st.session_state.rundown = []
            st.session_state.times = []
        st.session_state.rundown.append(item)
        st.session_state.times.append(time)

    # Tampilkan rundown
    if "rundown" in st.session_state:
        st.write("Rundown Acara:")
        df = pd.DataFrame({"Waktu": st.session_state.times, "Item Rundown": st.session_state.rundown})
        st.write(df)

        # Simpan ke dalam file CSV
        if st.button("Simpan ke CSV"):
            df.to_csv("rundown_acara.csv", index=False)
            st.success("Data berhasil disimpan ke dalam file CSV")

if __name__ == "_main_":
    main()
