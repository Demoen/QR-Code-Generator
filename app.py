from flask import Flask, render_template, request
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        img = qrcode.make(data)
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        qr_code = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return render_template('index.html', qr_code=qr_code)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
