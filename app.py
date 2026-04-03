from flask import Flask, request, jsonify

app = Flask(__name__)

KULLANICILAR = {
    "ahmet": "1234",
    "mehmet": "5678"
}

@app.route("/giris", methods=["POST"])
def giris():
    data = request.json
    kullanici_adi = data.get("kullanici_adi")
    sifre = data.get("sifre")

    if KULLANICILAR.get(kullanici_adi) == sifre:
        return jsonify({"sonuc": True})
    else:
        return jsonify({"sonuc": False})

if __name__ == "__main__":
    app.run()
