import streamlit as st
import math

st.title("belajar berhitung :blue[dengan semangat] :rocket:")

Rp = number = st.number_input("Masukan jumlah belanja (Rp): ",0)
item = number = st.number_input("Masukan jumlah barang (Rp): ",0)

if st.button("Hitung jumlah", type="amount"):
  v = math.pi*(Rp**2)*item
  st.success(f"Jmlah belanja adalah {Rp:.2f}")
