from flask import Flask, send_from_directory
import os

app = Flask(__name__)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_FILE = "schedule.pdf"

@app.route('/')
def show_pdf():
    path = os.path.join(PROJECT_DIR, PDF_FILE)
    if not os.path.exists(path):
        return f"<h1>Nie znaleziono pliku {PDF_FILE}</h1>", 404

    return f"""
    <!DOCTYPE html>
    <html lang='pl'>
    <head>
        <meta charset='UTF-8'>
        <title>Harmonogram Silowni</title>
        <meta http-equiv='refresh' content='600'>
        <style>
            body {{ margin:0; padding:0; height:100vh; }}
            iframe {{ width:100%; height:100%; border:none; }}
        </style>
    </head>
    <body>
        <iframe src='/schedule.pdf'></iframe>
    </body>
    </html>
    """

@app.route('/schedule.pdf')
def get_pdf():
    return send_from_directory(PROJECT_DIR, PDF_FILE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
