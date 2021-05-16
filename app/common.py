from functools import wraps
from app import *

import pandas as pd


@app.route('/')
def index():
    
    # get stock_changes
    sql = '''
        select s.user_id, u.user_name, s.stock_name, s.stock_code, s.changes
        from stock_change as s
        join ibks_user as u
        on s.user_id = u.user_id
        order by s.changes desc
    '''

    cursor.execute(sql)
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=['user_id', 'user_name', 'stock_name', 'stock_code', 'changes'])
    change_top = df[df['changes'] == df['changes'].max()]

    data = {
        "top_name": change_top['user_name'].tolist()[0],
        "top_stock": change_top['stock_name'].tolist()[0],
        "top_change_rate": round(change_top['changes'].tolist()[0], 2),
        "competitors": len(df),
        "average_profit": round(df['changes'].mean(), 2),
        "top3": df[:3]
    }

    return render_template('index.html', data=data)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None or session.get('user_id') == "":
            print("here")
            return redirect(url_for("login", next_url=request.url))
        return f(*args, **kwargs)
    return decorated_function