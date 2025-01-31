import zipfile
import os

# Path file yang akan dikompres
file_to_zip = '/var/lib/marzban/db.sqlite3'  # Ganti dengan path file Anda

# Path file ZIP output
zip_output = 'backup.zip'  # Ganti dengan path output ZIP yang diinginkan

# Membuat file ZIP dan menambahkan file ke dalamnya
with zipfile.ZipFile(zip_output, 'w') as zipf:
    zipf.write(file_to_zip, arcname=os.path.basename(file_to_zip))

print(f"File {file_to_zip} berhasil dikompres menjadi {zip_output}")
import requests

# Ganti dengan token bot dan chat ID Anda
TOKEN = "6757695853:AAEL0FTOL1Nhhcc7xnoE4RGzX0iPG4Dct5M"
CHAT_ID = "2074448736"

# Path file yang ingin dikirim
file_path = "backup.zip"

# URL API Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

# Kirim file
with open(file_path, "rb") as file:
    files = {"document": file}
    data = {"chat_id": CHAT_ID}
    response = requests.post(url, files=files, data=data)

# Cek respons
if response.status_code == 200:
    print("File berhasil dikirim!")
else:
    print("Gagal mengirim file:", response.text)
