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
    return redirect(YOUTUBE_URL, code=302)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
