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
    return {"status": "healthy"}, 200

@app.route('/generate', methods=['POST'])
def generate_qr():
    # Get data from request
    content = request.json.get('data')
    
    # Validate input
    if not content:
        return {"error": "No 'data' field provided"}, 400

    # Generate QR Code
    img = qrcode.make(content)
    
    # Save to memory buffer
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)

    # Return image
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
