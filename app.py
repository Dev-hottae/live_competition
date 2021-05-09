# /app.py
from flask import Flask, render_template, request

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/thanks', methods=['POST'])
def thanks():
    print("thanks")
    user_data = request.form
    user_name = user_data['name']
    user_email = user_data['email']
    user_phone = user_data['phone']
    user_text = user_data['comments']
    print(user_email)
    return render_template('thanks.html')

@app.route('/subscribe') # 접속하는 url
def signup():
    print("subscribe")
    return render_template('subscribe.html')

@app.route('/') # 접속하는 url
def index():
    return render_template('index.html')


if __name__=="__main__":
    # app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    app.run(host="0.0.0.0", port="80", debug=True)