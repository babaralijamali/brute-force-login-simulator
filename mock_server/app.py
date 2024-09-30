from flask import Flask, render_template, request

app = Flask(__name__)

# Mock credentials for testing brute force
USERNAME = 'admin'
PASSWORD = 'jamali'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            return "Login Successful"
        else:
            return "Login Failed"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
