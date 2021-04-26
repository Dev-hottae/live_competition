# /app.py
from flask import Flask, render_template, request

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/signin',methods=['POST'])
def signin():
    user_data = request.form
    user_email = user_data['user_email']
    print(user_email)
    return render_template('thanks.html')

@app.route('/') # 접속하는 url
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    # app.run(host="127.0.0.1", port="5000", debug=True)