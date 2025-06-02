from flask import Flask, redirect, request, render_template_string

app = Flask(__name__)

YOUTUBE_URL = "https://youtu.be/7nSr2P6blYM?si=Lxte8Q4MKw0Zea5-"

@app.route('/')
def index():
    # Page HTML qui auto-submit un POST
    return render_template_string("""
    <html>
    <head><title>VMascourse Redirect</title></head>
    <body>
        <form id="redirectForm" method="POST" action="/redirect-to-song">
        </form>
        <script>
            document.getElementById("redirectForm").submit();
        </script>
    </body>
    </html>
    """)

@app.route('/redirect-to-song', methods=['POST'])
def redirect_to_song():
    return redirect(YOUTUBE_URL, code=302)

@app.route('/go')
def go():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>VMascourse - Préparation de la mission</title>
        <meta charset="UTF-8">
        <style>
            body {
                background-color: #0f0f0f;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .loader {
                border: 8px solid #f3f3f3;
                border-top: 8px solid #3498db;
                border-radius: 50%;
                width: 60px;
                height: 60px;
                animation: spin 1s linear infinite;
                margin-top: 20px;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
        <script>
            setTimeout(function() {
                window.location.href = "{{ url }}";
            }, 120000); // 2 minutes = 120000 ms
        </script>
    </head>
    <body>
        <h1>Chargement de votre mission...</h1>
        <p>Merci de patienter pendant l'initialisation de l'environnement virtuel.</p>
        <div class="loader"></div>
        <p style="margin-top: 30px;">Redirection automatique dans 2 minutes.</p>
    </body>
    </html>
    """, url=YOUTUBE_URL)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
