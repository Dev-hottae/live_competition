from app import *


@app.route('/signup')
def signup():
    return render_template('register.html')

@app.route('/signup_pro', methods=['GET', 'POST'])
def signup_pro():

    if request.method == 'POST':
        req = request.form
        user_name = req['user_name']
        user_id = req['user_id']
        user_pw = req['user_pw']

        # check unique

        # save ibks_user
        sql = '''
            INSERT INTO ibks_user(user_name, user_id, user_pw)
            VALUES(%s, %s, %s)
        '''
        cursor.execute(sql, (user_name, user_id, user_pw))
        conn.commit()

        # session conn
        session['user_name'] = req['user_name']
        session['user_id'] = req['user_id']

        data = {
            "msg" : "sign up complete!"
        }

        return render_template('alert.html', data=data)

    else:
        return render_template('register.html') 

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_pro', methods=['GET', 'POST'])
def login_pro():

    if request.method == 'POST':

        # check database
        sql = '''
            select user_name, user_id
            from ibks_user
            where user_id=%s and user_pw=%s
        '''
        cursor.execute(sql, (request.form['user_id'], request.form['user_pw']))
        row = cursor.fetchall()

        # create session
        session['user_name'] = row[0][0]
        session['user_id'] = row[0][1]
        
        return redirect(url_for('index'))
    
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the user_id from the session if it's there
    session.clear()

    return redirect(url_for('index'))