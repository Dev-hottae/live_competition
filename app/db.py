from app import *

def execute(query, args={}):
    cursor.execute(query, args)

def executeOne(query, args={}):
    cursor.execute(query, args)
    row = cursor.fetchone()
        return row

def executeAll(query, args={}):
    cursor.execute(query, args)
    row = cursor.fetchall()
    return row

def commit():
    db.commit()