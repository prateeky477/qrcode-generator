import streamlit as st
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import os


st.title("Welcome to this page it will help you to generate qr codes.")

a=st.text_input("Enter content here")
if (st.button("SUBMIT")):
    qr=pyqrcode.create(a)
    qr.png('Qcode.png',scale=8)

    os.system('Qcode.png')
