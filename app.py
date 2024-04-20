# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Route to render a styled 'Hello World!' message."""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello Solitics!</title>
        <style>
            body {
                background-color: #f0f0f0;
                font-family: 'Arial', sans-serif;
                text-align: center;
                margin-top: 200px;
                color: #333;
            }
            h1 {
                color: #0066ff;
            }
        </style>
    </head>
    <body>
        <h1>Hello Solitics!</h1>
        <p>Welcome to my Test for Solitics-DevOps!</p>
    </body>
    </html>
    """
    return html_content

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
