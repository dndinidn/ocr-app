import streamlit as st
from PIL import Image
import pytesseract
import io
import platform   # <== ini penting supaya 'platform.system()' bisa jalan

# 🔧 Gunakan path dinamis
if platform.system() == "Windows":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
else:
    pytesseract.pytesseract.tesseract_cmd = "tesseract"

st.set_page_config(page_title="OCR App", page_icon="🖼️", layout="wide")

st.title("🖼️ Aplikasi Pengenalan Teks dari Gambar (OCR)")
st.caption("Konversi teks pada gambar menjadi teks digital menggunakan Python + pytesseract")

# Sidebar
with st.sidebar:
    st.header("Pengaturan")
    lang = st.selectbox("Pilih bahasa OCR", ["eng", "ind"], index=1)
    st.info("Pastikan bahasa sudah terinstal di Tesseract. Default: English & Indonesian.")

uploaded = st.file_uploader("Unggah gambar berisi teks (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Gambar Diupload", use_column_width=True)

    if st.button("🔍 Jalankan OCR"):
        with st.spinner("Memproses gambar..."):
            text = pytesseract.image_to_string(image, lang=lang)
        st.success("Selesai!")
        st.subheader("📄 Hasil Teks:")
        st.text_area("Teks terdeteksi", text, height=200)
        
        # Tombol download hasil teks
        buf = io.BytesIO(text.encode('utf-8'))
        st.download_button(
            "💾 Download hasil sebagai .txt", 
            data=buf, 
            file_name="hasil_ocr.txt", 
            mime="text/plain"
        )
else:
    st.info("Silakan unggah gambar terlebih dahulu.")
