from app import *
import pandas as pd

@app.route('/allApplication')
@login_required
def allApplication():
    # get applications
    sql = '''
        select a.stock_name, a.stock_code, a.stock_reason, a.user_id, u.user_name
        from application as a
        join ibks_user as u
        on a.user_id = u.user_id
    '''
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['stock_name', 'stock_code', 'stock_reason', 'user_id', 'user_name'])
    print(df)
    return render_template('allApplication.html', data=df)

@app.route('/joinCompete')
@login_required
def joinCompete():
    return render_template('application.html')

@app.route('/joinCompete_pro', methods=['GET', 'POST'])
@login_required
def joinCompete_pro():
    if request.method == 'POST':
        form_data = request.form

        # check code
        stock_code = form_data['stock_code']
        
        naver_url = "https://finance.naver.com/item/main.nhn?code={}".format(stock_code)
        
        try:
            res = requests.get(url=naver_url).text
            soup = BeautifulSoup(res, 'html.parser')
            stock_name = soup.select('#middle .wrap_company h2')[0].text
        except:
            return render_template('application.html')

        # save application to db
        sql = '''
            insert into application (stock_name, stock_code, stock_reason, user_id)
            values(%s, %s, %s, %s)
        '''
        cursor.execute(sql, (stock_name, stock_code, form_data['stock_reason'], session['user_id']))
        conn.commit()

        data = {
            "msg" : "application submited!"
        }

        return render_template('alert.html', data=data)

    else:
        return render_template('application.html') 

@app.route('/modifyApp')
@login_required
def modifyApp():

    # get my application
    sql = '''
        select *
        from application
        where user_id=%s
    '''
    cursor.execute(sql, (session['user_id']))
    row = cursor.fetchall()

    data = {
        'stock_name' : row[0][1],
        'stock_id' : row[0][2],
        'stock_reason' : row[0][3]
    }

    return render_template('modify_app.html', data=data)

# dup_error
@app.errorhandler(pymysql.err.IntegrityError)
def handle_dup_sql_insert(e):
    data = {
        "msg" : "ONLY 1 Application possible!!"
    }
    return render_template('error_and_return.html', data=data)