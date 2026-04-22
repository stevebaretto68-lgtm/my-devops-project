from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 My DevOps App is Live!</h1>"

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"})

@app.route("/info")
def info():
    return jsonify({
        "app": "my-devops-app",
        "stack": ["Flask", "Docker", "Azure", "Terraform", "Ansible"],
        "environment": "production"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)