# 🌐 WhatsLink - WhatsApp Group Link Validator
![WhatsLink](https://github.com/user-attachments/assets/56ec0346-98f4-4beb-b648-432e37370da1)

**WhatsLink** adalah aplikasi web modern yang memungkinkan pengguna untuk memeriksa apakah tautan grup WhatsApp valid atau tidak. Dibangun menggunakan Flask di backend dan Tailwind CSS di frontend, aplikasi ini menghadirkan pengalaman pengguna yang responsif dan mudah digunakan.

## 🎯 Fitur
- 🔗 **Validasi Link Grup WhatsApp**: Cek apakah sebuah link grup aktif dan dapat digunakan.
- 🖼️ **Informasi Grup**: Menampilkan nama dan gambar profil grup (_jika tersedia_).
- 🚀 **Responsif**: Desain responsif yang terlihat baik di perangkat mobile maupun desktop.
- ⚡ **Proses Cepat**: Hasil validasi link dalam hitungan detik.

## 🛠️ Teknologi yang Digunakan

- **Frontend**: HTML5, Tailwind CSS
- **Async**: Memanfaatkan `async` untuk pengecekan link yang lebih cepat
- **Backend**: Python (Flask)
- **Hosting**: AnymHost

## 📦 Instalasi Lokal
Jika Anda ingin menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:
1. **Clone repositori ini**:
    ```bash
    git clone https://github.com/RozhakXD/WhatsLink.git
    cd WhatsLink
    ```
2. **Buat environment virtual dan instal dependensi**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Untuk pengguna Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. **Jalankan aplikasi**:
    ```bash
    flask run
    ```
4. **Buka di browser**:  
   Akses aplikasi di `http://127.0.0.1:5000`

## 🚀 Deployment
WhatsLink telah di-hosting dan dapat diakses melalui URL berikut:

[WhatsLink - Live Demo](https://www.whatslink.rozhak-dev.my.id/)

## 🎨 Cuplikan Layar
![WhatsLink Image](https://github.com/user-attachments/assets/45d7c9f3-feb6-4cf7-b344-18ae5cb4dd9d)

## 🧑‍💻 Cara Penggunaan

1. Masukkan link grup WhatsApp di kolom yang disediakan.
2. Klik tombol "**Cek Link**".
3. Tunggu beberapa detik hingga aplikasi memproses link.
4. Aplikasi akan menampilkan nama grup, gambar profil, atau pesan error jika link tidak valid.

## ☕ Dukungan
Jika Anda menyukai proyek ini dan ingin mendukung pengembangannya, Anda dapat memberi donasi di platform berikut:

- [Trakteer](https://trakteer.id/rozhak_official/tip) | [PayPal](https://paypal.me/rozhak9) | [Saweria](https://saweria.co/rozhak9)

## 💡 Kontribusi
Ingin berkontribusi? Silakan fork repositori ini dan ajukan pull request dengan perubahan Anda. Setiap bantuan akan sangat dihargai!

## 📝 Lisensi
Proyek ini dilisensikan di bawah [MIT License](https://github.com/RozhakXD/WhatsLink/blob/main/LICENSE).
