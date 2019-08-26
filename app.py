from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['Get','Post'])
def home():
    return render_template('home.html')

@app.route("/signin",methods=['Get'])
def signin_form():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return render_template('success.html')
    return render_template('fail.html')

if __name__ == "__main__":
    app.debug = True  # 开启调试模式 app.run(debug=True)
    app.run()
