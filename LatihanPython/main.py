import streamlit as st

# Daftar menu minuman dan harganya
daftar_minuman = {
    'Espresso': 15000,
    'Cappuccino': 20000,
    'Latte': 20000,
    'Americano': 25000,
    'Macchiato': 25000
}

# Daftar menu makanan dan harganya
daftar_makanan = {
    'Nasi Goreng': 20000,
    'Mie Goreng': 15000,
    'Nasi Rawon': 25000,
    'Sate Ayam': 25000,
    'Bakso': 15000
}

# Fungsi untuk menghitung total biaya pembelian
def hitung_total(pesanan):
    total = 0
    for item, harga in pesanan.items():
        total += harga
    return total

def main():
    st.title('Kasir Kafe')

    nama_pelanggan = st.text_input('Nama Pelanggan', '')

    st.header('Menu Minuman')
    minuman_jumlah = {}
    for minuman, harga in daftar_minuman.items():
        minuman_jumlah[minuman] = st.number_input(f'{minuman} (Rp{harga})', min_value=0, step=1)

    st.header('Menu Makanan')
    makanan_jumlah = {}
    for makanan, harga in daftar_makanan.items():
        makanan_jumlah[makanan] = st.number_input(f'{makanan} (Rp{harga})', min_value=0, step=1)

    st.header('Ringkasan Pesanan')
    for minuman, jumlah in minuman_jumlah.items():
        if jumlah > 0:
            st.write(f'Minuman: {minuman}, Jumlah: {jumlah}, Harga: Rp{daftar_minuman[minuman] * jumlah}')

    for makanan, jumlah in makanan_jumlah.items():
        if jumlah > 0:
            st.write(f'Makanan: {makanan}, Jumlah: {jumlah}, Harga: Rp{daftar_makanan[makanan] * jumlah}')

    total_harga = sum([daftar_minuman[minuman] * jumlah for minuman, jumlah in minuman_jumlah.items()]) + \
                  sum([daftar_makanan[makanan] * jumlah for makanan, jumlah in makanan_jumlah.items()])
    st.write(f'Total Pembayaran: Rp{total_harga}')

    st.write(f'Pesanan atas nama: {nama_pelanggan}')

    if st.button('Cetak Nota'):
        st.write('--- Nota Pesanan ---')
        st.write(f'Nama Pelanggan: {nama_pelanggan}')
        st.write('--- Daftar Pesanan ---')
        for minuman, jumlah in minuman_jumlah.items():
            if jumlah > 0:
                st.write(f'{jumlah}x {minuman} (Rp{daftar_minuman[minuman] * jumlah})')
        for makanan, jumlah in makanan_jumlah.items():
            if jumlah > 0:
                st.write(f'{jumlah}x {makanan} (Rp{daftar_makanan[makanan] * jumlah})')
        st.write('---------------------')
        st.write(f'Total Pembayaran: Rp{total_harga}')

if __name__ == '__main__':
    main()
