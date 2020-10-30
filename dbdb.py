import pymysql

def dbcon():
    return pymysql.connect(host='mysql.pythonanywhere-services.com',
                   user='', password='',
                   db='$myai', charset='utf8',
                   cursorclass=pymysql.cursors.DictCursor
                   )

def create_table():
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE search (data varchar(255))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(data):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (data,)
        c.execute("INSERT INTO search VALUES (%s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM search')
        ret = c.fetchall()
        # for row in c.execute('SELECT * FROM search'):
        #     ret.append(row)
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

# insert_data('asdf')
# retdata = select_all()
# print(retdata)
