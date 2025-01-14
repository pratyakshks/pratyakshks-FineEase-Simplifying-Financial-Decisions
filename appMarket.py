from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('indexMarket.html')  # Use a central template

if __name__ == "__main__":
   
    app.run(debug=True, host='0.0.0.0', port=5005)  # This runs the app on port 5001
