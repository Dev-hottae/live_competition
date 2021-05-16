from app import *
import pandas as pd

@app.route('/status')
@login_required
def status():

    # get applications
    sql = '''
        select s.user_id, s.stock_name, s.stock_code, s.changes, u.user_name
        from stock_change as s
        join ibks_user as u
        on s.user_id = u.user_id
        order by s.changes desc
    '''
    
    cursor.execute(sql)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['user_id', 'stock_name', 'stock_code', 'changes', 'user_name'])
    return render_template('status.html', data=df)