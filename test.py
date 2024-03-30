import streamlit as st

st.header('JAMAL KALKULATOR', divider='rainbow')

angka_pertama = st.number_input('nmasukan angka pertama')
st.write('The current number is ', angka_pertama)

angka_kedua = st.number_input('masukan angka kedua')
st.write('thecurrent number is ', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua


st.write(f'angka pertama {angka_pertama} x {angka_kedua} = {operasi_matematika}')

warna = st.color_picker('pilih waarna', '#00f900')
st.write('warnanya ini', warna)

