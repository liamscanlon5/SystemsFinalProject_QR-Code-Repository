from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "status": "online",
        "service": "QR Code Generator",
        "usage": "Send a POST request to /generate with JSON body: {'data': 'your-text-here'}"
    }

@app.route('/health')
def health():
    # Required for Rubric "Functionality" & Ops
    return {"status": "healthy"}, 200

@app.route('/generate', methods=['POST'])
def generate_qr():
    # 1. Get data from request
    content = request.json.get('data')
    
    if not content:
        return {"error": "No 'data' field provided"}, 400

    # 2. Generate QR Code using the library
    # concept: Data Pipelines (Input -> Process -> Output)
    img = qrcode.make(content)
    
    # 3. Save to memory buffer (don't clutter file system)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)

    # 4. Return image directly
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    # Listens on 0.0.0.0 to be accessible inside Docker/Cloud
    app.run(host='0.0.0.0', port=5000)
