from flask import Flask ,render_template, request ,jsonify

app=Flask(__name__)

USER_EMAIL = "test@gmail.com"
USER_PASSWORD = "123456"

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
   
    if email == USER_EMAIL and password == USER_PASSWORD:
        return jsonify({"message": "Login successful", "status": "success"})
    else:
        return jsonify({"message": "Invalid email or password", "status": "error"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  
