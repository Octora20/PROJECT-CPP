import streamlit as st
import pandas as pd
import re

def validate_time_format(time_string):
    """Validasi format waktu dengan format 'HH.MM-HH.MM'."""
    pattern = r'^\d{1,2}\.\d{2}-\d{1,2}\.\d{2}$'
    if re.match(pattern, time_string):
        return True
    return False

def main():
    st.title("Rundown Acara")

    # Load data dari file CSV (jika ada)
    try:
        data = pd.read_csv("data_rundown.csv")
    except FileNotFoundError:
        data = pd.DataFrame(columns=["No", "Agenda", "Jam"])

    # Tampilkan tabel rundown acara
    st.write("Rundown Acara Saat Ini:")
    st.write(data)

    st.write("Tambahkan Item Rundown Baru:")
    no = st.text_input("No")
    agenda = st.text_input("Agenda")
    jam = st.text_input("Jam (format: HH.MM-HH.MM)")

    if st.button("Tambahkan"):
        if no.strip() and agenda.strip() and jam.strip() and validate_time_format(jam.strip()):
            data.loc[len(data)] = [no, agenda, jam]
            data.to_csv("data_rundown.csv", index=False)
            st.success("Item Rundown Berhasil Ditambahkan!")
        else:
            st.error("Mohon isi semua kolom input dengan benar.")

    # Pilihan untuk mengedit rundown
    st.write("Edit Item Rundown:")
    if not data.empty:
        rundown_to_edit = st.selectbox("Pilih Item Rundown yang Ingin Diedit:", data["Agenda"])
        selected_row = data[data["Agenda"] == rundown_to_edit]
        if not selected_row.empty:
            new_no = st.text_input("No", value=selected_row["No"].iloc[0])
            new_agenda = st.text_input("Agenda", value=selected_row["Agenda"].iloc[0])
            new_jam = st.text_input("Jam", value=selected_row["Jam"].iloc[0])

            if st.button("Edit"):
                if validate_time_format(new_jam.strip()):
                    data.loc[data["Agenda"] == rundown_to_edit, "No"] = new_no
                    data.loc[data["Agenda"] == rundown_to_edit, "Agenda"] = new_agenda
                    data.loc[data["Agenda"] == rundown_to_edit, "Jam"] = new_jam
                    data.to_csv("data_rundown.csv", index=False)
                    st.success("Item Rundown Berhasil Diedit!")
                else:
                    st.error("Format waktu yang dimasukkan tidak valid.")
        else:
            st.warning("Tidak ada item rundown yang dipilih.")
    else:
        st.warning("Tidak ada item rundown untuk diedit.")

    # Pilihan untuk menghapus rundown
    st.write("Hapus Item Rundown:")
    if not data.empty:
        rundown_to_delete = st.selectbox("Pilih Item Rundown yang Ingin Dihapus:", data["Agenda"])
        if st.button("Hapus"):
            data = data[data["Agenda"] != rundown_to_delete]
            data.to_csv("data_rundown.csv", index=False)
            st.success("Item Rundown Berhasil Dihapus!")
    else:
        st.warning("Tidak ada item rundown untuk dihapus.")

if __name__ == "__main__":
    main()
