from flask import Flask, render_template, request
from password import generate_password

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    password = generate_password(length)
    
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=False)