import os
import zipfile

def zip_folder(folder_path, output_path):
    """
    Mengompres folder ke file .zip.

    :param folder_path: Path folder yang akan dikompres.
    :param output_path: Path file .zip yang akan dibuat.
    """
    try:
        # Membuat file .zip
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk melalui folder dan tambahkan semua file ke .zip
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, start=folder_path)
                    zipf.write(file_path, arcname)
        print(f"Folder '{folder_path}' berhasil dikompres ke '{output_path}'.")
    except Exception as e:
        print(f"Gagal mengompres folder: {e}")

# Contoh penggunaan
folder_to_zip = "/var/lib/marzban"  # Ganti dengan path folder yang ingin dikompres
output_zip_file = "backup.zip"  # Ganti dengan path file .zip output

zip_folder(folder_to_zip, output_zip_file)

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
