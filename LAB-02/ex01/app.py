from flask import Flask, request, render_template, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
import subprocess
import os

app = Flask(__name__)
import time




@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

# @app.route("/caesar")
# def caesar():
#     filename = request.args.get("file", "caesar_cipher.py")  # Mặc định chạy script.py nếu không có file

#     # Định nghĩa đường dẫn thư mục chứa file
#     script_dir = r"D:\Users\Documents\Code\Python\bmttnc-hutech-2280603477\LAB-03"
    
#     # Ghép đường dẫn đúng
#     script_path = os.path.join(script_dir, filename)

#     # Kiểm tra file có tồn tại không
#     if not os.path.isfile(script_path):
#         return f"File {script_path} không tồn tại!", 404

#     # Chạy file Python
#     result = subprocess.run(["python", script_path], capture_output=True, text=True)
#     return render_template('index.html')

# @app.route("/vigenere")
# def vigenere():
#     filename = request.args.get("file", "vigenere_cipher.py")  # Mặc định chạy script.py nếu không có file

#     # Định nghĩa đường dẫn thư mục chứa file
#     script_dir = r"D:\Users\Documents\Code\Python\bmttnc-hutech-2280603477\LAB-03"
    
#     # Ghép đường dẫn đúng
#     script_path = os.path.join(script_dir, filename)

#     # Kiểm tra file có tồn tại không
#     if not os.path.isfile(script_path):
#         return f"File {script_path} không tồn tại!", 404

#     # Chạy file Python
#     result = subprocess.run(["python", script_path], capture_output=True, text=True)
#     return render_template('index.html')

# @app.route("/railfence")
# def railfence():
#     filename = request.args.get("file", "railfence_cipher.py")  # Mặc định chạy script.py nếu không có file

#     # Định nghĩa đường dẫn thư mục chứa file
#     script_dir = r"D:\Users\Documents\Code\Python\bmttnc-hutech-2280603477\LAB-03"
    
#     # Ghép đường dẫn đúng
#     script_path = os.path.join(script_dir, filename)

#     # Kiểm tra file có tồn tại không
#     if not os.path.isfile(script_path):
#         return f"File {script_path} không tồn tại!", 404

#     # Chạy file Python
#     result = subprocess.run(["python", script_path], capture_output=True, text=True)
#     return render_template('index.html')

# @app.route("/playfair")
# def playfair():
#     filename = request.args.get("file", "playfair_cipher.py")  # Mặc định chạy script.py nếu không có file

#     # Định nghĩa đường dẫn thư mục chứa file
#     script_dir = r"D:\Users\Documents\Code\Python\bmttnc-hutech-2280603477\LAB-03"
    
#     # Ghép đường dẫn đúng
#     script_path = os.path.join(script_dir, filename)

#     # Kiểm tra file có tồn tại không
#     if not os.path.isfile(script_path):
#         return f"File {script_path} không tồn tại!", 404

#     # Chạy file Python
#     result = subprocess.run(["python", script_path], capture_output=True, text=True)
#     return render_template('index.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Playfair = PlayFairCipher()
    encrypted_text = Playfair.playfair_encrypt(text, Playfair.create_playfair_matrix(key))
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Playfair = PlayFairCipher()
    decrypted_text = Playfair.playfair_decrypt(text, Playfair.create_playfair_matrix(key))
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Railfence = RailFenceCipher()
    encrypted_text = Railfence.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Railfence = RailFenceCipher()
    decrypted_text = Railfence.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/vigenere/encrypt", methods=['POST'])
def vingenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vingenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    
@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

#main function
if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5050, debug=True)
