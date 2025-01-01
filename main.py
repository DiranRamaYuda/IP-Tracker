# KODE PROGRAM INI MEMILIKI LISENSI DARI PEMBUATNYA

# Route utama untuk halaman web
@app.route("/", methods=["GET"])
def home():
    # Ambil IP pengunjung
    visitor_ip = get_visitor_ip()

    # Ambil detail IP dari API eksternal
    ip_details = get_ip_details(visitor_ip)

    # Tambahkan timestamp
    ip_details["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simpan data ke file JSON
    save_to_file(ip_details)

    # Tampilkan halaman web dengan informasi
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TES</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 20%;
            }}
            h1 {{
                color: #333;
            }}
        </style>
    </head>
    <body>
        <h1>KAMU ANAK BAIK</h1>
    </body>
    </html>
    """
    return render_template_string(html_content)

# Route untuk API (hanya JSON)
@app.route("/api", methods=["GET"])
def api_proxy():
    # Ambil IP pengunjung
    visitor_ip = get_visitor_ip()

    # Ambil detail IP dari API eksternal
    ip_details = get_ip_details(visitor_ip)

    # Tambahkan timestamp
    ip_details["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Simpan data ke file JSON
    save_to_file(ip_details)

    # Kirimkan data kembali ke klien
    return jsonify(ip_details)

# Route untuk debugging header
@app.route("/headers", methods=["GET"])
def debug_headers():
    return jsonify(dict(request.headers))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
