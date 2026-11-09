import os
from flask import Flask, jsonify


app= Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "greeting": os.getenv("GREETING", "Hello"),
        "student": os.getenv("STUDENT", "Student"),
        "variant": os.getenv("VARIANT", "7")
    })
    
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
