from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('indexServices.html')  # Use a central template

if __name__ == "__main__":
    app.run(port=5000)  # The gateway runs on port 5000
