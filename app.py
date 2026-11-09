from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Project</title>
            <style>
                body {
                    background: #eef2ff;
                    font-family: Arial;
                    text-align: center;
                    padding-top: 100px;
                }
                .container {
                    background: white;
                    padding: 40px;
                    margin: auto;
                    width: 70%;
                    border-radius: 15px;
                    box-shadow: 0 4px 12px #cccccc;
                }
                h1 {
                    color: #2563eb;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>CI/CD Pipeline Successful!</h1>
                <h2>Welcome to My Docker Project</h2>
                <p>Application deployed using GitHub Actions,
                Docker and Kubernetes.</p>
                <p>Status: Running Successfully</p>
            </div>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
