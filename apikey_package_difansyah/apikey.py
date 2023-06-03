import json

# Fungsi untuk membaca dan mendekripsi kunci API dari file JSON
def get_decrypted_api_key(json_file, keyword):
    with open(json_file, 'r') as file:
        data = json.load(file)

    encrypted_api_key = data["encrypted_key"]

    decrypted_key = decrypt_key(encrypted_api_key, keyword)
    return decrypted_key

# Fungsi untuk mendekripsi kunci
def decrypt_key(encrypted_key, keyword):
    decrypted_key = ""
    keyword_index = 0

    for char in encrypted_key:
        if char.isalpha():
            # Menghitung offset ASCII berdasarkan huruf besar atau kecil
            ascii_offset = ord('A') if char.isupper() else ord('a')

            # Mendapatkan karakter kunci untuk dekripsi berdasarkan indeks kata kunci
            key_char = keyword[keyword_index % len(keyword)]

            # Menghitung pergeseran berdasarkan huruf besar dari karakter kunci
            key_offset = ord(key_char.upper()) - ord('A')

            # Melakukan dekripsi dengan pergeseran sesuai karakter kunci
            decrypted_char = chr((ord(char) - ascii_offset - key_offset) % 26 + ascii_offset)
            decrypted_key += decrypted_char

            # Mengupdate indeks kata kunci
            keyword_index += 1
        else:
            decrypted_key += char

    return decrypted_key

json_file = 'encrypted_api_key.json'
keyword = 'KUNCI_API_KEY'
decrypted_api_key = get_decrypted_api_key(json_file, keyword)
