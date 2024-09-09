import urllib.parse

def decode_url_part(encoded_url, start_param='user%', end_param='&tgWebAppVersion=7'):
    # Mencari bagian URL yang dimulai dari parameter 'user%'
    start_index = encoded_url.find(start_param)
    
    if (start_index == -1):
        raise ValueError(f"Parameter '{start_param}' tidak ditemukan dalam URL.")
    
    # Mengambil substring yang dimulai dari 'user%'
    encoded_part = encoded_url[start_index:]
    
    # Melakukan decoding URL
    decoded_part = urllib.parse.unquote(encoded_part)
    
    # Mencari bagian untuk dihapus dari decoded_part
    end_index = decoded_part.find(end_param)
    if end_index != -1:
        decoded_part = decoded_part[:end_index]
    
    return decoded_part

def main():
    urls = []
    print("Masukkan URL yang ingin didecode (ketik 'selesai' untuk mengakhiri):")
    
    while True:
        encoded_url = input()
        if encoded_url.lower() == 'selesai':
            break
        urls.append(encoded_url)
        print("Masukkan URL selanjutnya atau ketik 'selesai' untuk mengakhiri:")

    decoded_urls = []
    for url in urls:
        try:
            decoded_part = decode_url_part(url)
            decoded_urls.append(decoded_part)
        except ValueError as e:
            print(f"Error: {e}")
            decoded_urls.append("")

    # Menyimpan hasil decoding ke dalam file .txt
    output_filename = "decoded_urls.txt"
    with open(output_filename, 'w') as file:
        for decoded_url in decoded_urls:
            if decoded_url:
                file.write(decoded_url + "\n")
    
    print(f"\nHasil URL decoding telah disimpan dalam file '{output_filename}'.")

if __name__ == "__main__":
    main()
