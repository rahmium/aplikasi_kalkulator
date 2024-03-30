import streamlit as st
st.header('_Aplikasi Penjumlahan Bilangan Numerik_', divider='violet')
number_one = st.number_input('**Masukkan angka pertama**')
st.write('Angka pertamanya adalah', number_one)

number_two = st.number_input('Masukkan angka kedua')
st.write('Angka keduanya adalah', number_two)

operasi_matematika= number_one * number_two
st.write(f'Angka pertama {number_one} x Angka kedua {number_two} = {operasi_matematika}')


