import os
import hashlib
import random
import string
from functools import wraps
from datetime import datetime
from flask_mysqldb import MySQL
import MySQLdb
from urllib.parse import quote_plus
from mysql.connector import errorcode
from flask import Flask, request,send_from_directory, jsonify, abort, Response
import time
import json

app = Flask(__name__)

AUTH_TOKEN = 'your_auth_token'

mx1=0
mx2=0
mx3=0
mx4=0
mx5=0
mx6=0

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'eris4x'
app.config['MYSQL_PASSWORD'] = 'rexis4x@33#'
app.config['MYSQL_DB'] = 'skenmc'

mysql = MySQL(app)

def tokenize(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        t = request.headers.get('Authorization')
        if t is None or not t.startswith('Bearer '):
            return jsonify({'e': 'unauthorized'}), 401
        t = t.split(' ')[1]
        if t != AUTH_TOKEN:
            return jsonify({'e': 'unauthorized'}), 401
        return f(*args, **kwargs)
    return decorated_function


@app.route('/qrc', methods=['GET'])
def qrc():
    global mx1
    global mx2
    global mx3
    global mx4
    global mx5
    global mx6

    cur = mysql.connection.cursor()
    cur.execute("SELECT COUNT(*) FROM all_skn")
    mx1 = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM new")
    mx2 = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM t100")
    mx3 = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM gskins")
    mx4 = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM bskins")
    mx5 = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM hdskins")
    mx6 = cur.fetchone()[0]
    cur.close()
    
    return f"{mx1}::{mx2}::{mx3}::{mx4}::{mx5}::{mx6}", 200



@app.route('/skinz', methods=['POST'])
@tokenize
def skinz():
    d=request.get_json()
    if d is None:
        return jsonify({'error': 'unable to query'}), 400

    m = 20 # max query
    c = d.get('c') # category
    n = d.get('n') # already query count
    l = False #last item

    sq = mysql.connection.cursor()


    if c == "mx1":
        t = mx1-n #to
        f = t-m #from

        if f < 1:
            f = 0
            mx = t
            l = True
        try:
            sq.execute("SELECT * FROM all_skn ORDER BY sn DESC LIMIT %s OFFSET %s", (mx, f))
            rs = sq.fetchall()
            if rs:
                z = [desc[0] for desc in sq.description]
                if not l:
                    j = [{"END": "NO"},*[dict(zip(z, row)) for row in rs]]
                else:
                    j = [{"END": "YES"},*[dict(zip(z, row)) for row in rs]]
                return json.dumps(j), 200
            else:
                return jsonify({'m': 'no skin found'}), 204
        except Exception as e:
            print(e)
            return jsonify({'m': 'query error'}), 404
        finally:
            sq.close()
    elif c == "mx2":
        t = mx2-n #to
        f = t-m #from

        if f < 1:
            f = 0
            mx = t
            l = True
        try:
            sq.execute("SELECT * FROM new ORDER BY sn DESC LIMIT %s OFFSET %s", (mx, f))
            rs = sq.fetchall()
            if rs:
                z = [desc[0] for desc in sq.description]
                if not l:
                    j = [{"END": "NO"},*[dict(zip(z, row)) for row in rs]]
                else:
                    j = [{"END": "YES"},*[dict(zip(z, row)) for row in rs]]
                return json.dumps(j), 200
            else:
                return jsonify({'m': 'no skin found'}), 204
        except Exception as e:
            print(e)
            return jsonify({'m': 'query error'}), 404
        finally:
            sq.close()
    elif c == "mx3":
        t = mx3-n #to
        f = t-m #from

        if f < 1:
            f = 0
            mx = t
            l = True
        try:
            sq.execute("SELECT * FROM t100 ORDER BY sn DESC LIMIT %s OFFSET %s", (mx, f))
            rs = sq.fetchall()
            if rs:
                z = [desc[0] for desc in sq.description]
                if not l:
                    j = [{"END": "NO"},*[dict(zip(z, row)) for row in rs]]
                else:
                    j = [{"END": "YES"},*[dict(zip(z, row)) for row in rs]]
                return json.dumps(j), 200
            else:
                return jsonify({'m': 'no skin found'}), 204
        except Exception as e:
            print(e)
            return jsonify({'m': 'query error'}), 404
        finally:
            sq.close()
    elif c == "mx4":
        t = mx4-n #to
        f = t-m #from

        if f < 1:
            f = 0
            mx = t
            l = True
        try:
            sq.execute("SELECT * FROM gskins ORDER BY sn DESC LIMIT %s OFFSET %s", (mx, f))
            rs = sq.fetchall()
            if rs:
                z = [desc[0] for desc in sq.description]
                if not l:
                    j = [{"END": "NO"},*[dict(zip(z, row)) for row in rs]]
                else:
                    j = [{"END": "YES"},*[dict(zip(z, row)) for row in rs]]
                return json.dumps(j), 200
            else:
                return jsonify({'m': 'no skin found'}), 204
        except Exception as e:
            print(e)
            return jsonify({'m': 'query error'}), 404
        finally:
            sq.close()
    elif c == "mx5":
        t = mx5-n #to
        f = t-m #from

        if f < 1:
            f = 0
            mx = t
            l = True
        try:
            sq.execute("SELECT * FROM bskins ORDER BY sn DESC LIMIT %s OFFSET %s", (mx, f))
            rs = sq.fetchall()
            if rs:
                z = [desc[0] for desc in sq.description]
                if not l:
                    j = [{"END": "NO"},*[dict(zip(z, row)) for row in rs]]
                else:
                    j = [{"END": "YES"},*[dict(zip(z, row)) for row in rs]]
                return json.dumps(j), 200
            else:
                return jsonify({'m': 'no skin found'}), 204
        except Exception as e:
            print(e)
            return jsonify({'m': 'query error'}), 404
        finally:
            sq.close()
    elif c == "mx6":
        t = mx6-n #to
        f = t-m #from

        if f < 1:
            f = 0
            mx = t
            l = True
        try:
            sq.execute("SELECT * FROM hdskins ORDER BY sn DESC LIMIT %s OFFSET %s", (mx, f))
            rs = sq.fetchall()
            if rs:
                z = [desc[0] for desc in sq.description]
                if not l:
                    j = [{"END": "NO"},*[dict(zip(z, row)) for row in rs]]
                else:
                    j = [{"END": "YES"},*[dict(zip(z, row)) for row in rs]]
                return json.dumps(j), 200
            else:
                return jsonify({'m': 'no skin found'}), 204
        except Exception as e:
            print(e)
            return jsonify({'m': 'query error'}), 404
        finally:
            sq.close()
    else:
        return "unable to query", 404


@app.route('/search', methods=['POST'])
@tokenize
def search():
    s = "%"+request.data.decode('utf-8')+"%"
    sq = mysql.connection.cursor()
    try:
        sq.execute("SELECT * FROM all_skn WHERE skn_nm LIKE %s LIMIT 60", (s,))
        rs = sq.fetchall()
        if rs:
            z = [desc[0] for desc in sq.description]
            j = [dict(zip(z, row)) for row in rs]
            return json.dumps(j)
        else:
            return jsonify({'m': 'no skin found'}), 404
    except Exception as e:
        return "unable to query"+str(e), 403


@app.route('/mfav', methods=['POST'])
@tokenize
def zx():
    s = request.get_json()
    sq = mysql.connection.cursor()
    p = ', '.join('%s' for _ in s)
    q = f"""
        SELECT * 
        FROM all_skn 
        WHERE skn_sm IN ({p})
        ORDER BY FIELD(skn_sm, {', '.join('%s' for _ in s)})
    """
    try:
        sq.execute(q, s+s)
        rs = sq.fetchall()
        if rs:
            r = [desc[0] for desc in sq.description]
            j = [dict(zip(r, row)) for row in rs]
            return json.dumps(j)
        else:
            return jsonify({'m': 'no skin found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        sq.close()

    return "unable to query", 200
    

@app.route('/skin')
def skin():
    d = request.args.get('d')
    s = request.args.get('s')

    if not d:
        abort(404)
    if not s:
        abort(404)

    vx(s)

    p = f"skenmc/{d}/skins/"
    if not os.path.exists(os.path.join(p, s)):
        abort(404)
    return send_from_directory(p, s),200


@app.route('/dl', methods=['POST'])
@tokenize
def dl():
    sq = mysql.connection.cursor()
    t = ['all_skn', 'new', 't100', 'gskins', 'bskins','hdskins']
    skn_sm= request.data.decode('utf-8')
    try:
        for table in t:
            query = f"""
            UPDATE {table}
            SET skn_dl = skn_dl + 1
            WHERE skn_sm = %s
            """
            sq.execute(query, (skn_sm,))
            mysql.connection.commit()
    except Exception as e:
        print("DL ERROR")
        print(e)
    finally:
        sq.close()
    return Response(status=200)


def vx(skin_sm):
    sq = mysql.connection.cursor()
    t = ['all_skn', 'new', 't100', 'gskins', 'bskins','hdskins']
    try:
        for table in t:
            query = f"""
            UPDATE {table}
            SET skn_vw = skn_vw + 1
            WHERE skn_sm = %s
            """
            sq.execute(query, (skin_sm,))
            mysql.connection.commit()
    except Exception as e:
        print("VX ERROR")
    finally:
        sq.close()


@app.route('/preview')
def preview():
    d = request.args.get('u')
    f = request.args.get('q')
    p = f"skenmc/{d}/preview/"
    if not os.path.exists(os.path.join(p, f)):
        return jsonify({'m': 'no skin found'}), 404
    return send_from_directory(p, f),200

@app.route('/upload', methods=['POST'])
@tokenize
def upx():
    sq = mysql.connection.cursor()

    fd = datetime.now().strftime("%d%Y%m")
    
    cs = "skenmc/"+fd
    pv = cs+"/preview/"
    sk = cs+"/skins/"

    if not os.path.exists(cs):
        os.makedirs(cs)
        os.makedirs(sk)
        os.makedirs(pv)

    s1 = request.files['skin']
    p1 = request.files['preview']

    skn_hash = SHA512Checksum(s1)
    skn_nm = request.form['skn_nm']
    skn_sm = request.form['skn_sm']
    skn_qs = fd
    skn_uid1 = request.form['skn_uid1']
    skn_uid2 = request.form['skn_uid2']
    skn_dl = 0
    skn_vw = 0


    try:
        sq.execute("INSERT INTO all_skn (skn_hash,skn_nm,skn_sm,skn_qs,skn_uid1,skn_uid2,skn_dl,skn_vw) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (skn_hash,skn_nm,skn_sm,skn_qs,skn_uid1,skn_uid2,skn_dl,skn_vw))
        mysql.connection.commit()
        s1.seek(0)
        s1.save(sk+skn_sm)
        p1.save(pv+skn_sm)
        print("success")
        return jsonify({'message': 'File successfully uploaded'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'File successfully uploaded'}), 401
    finally:
        sq.close()

def SHA512Checksum(file):
    """Calculate the SHA-512 checksum of a file."""
    sha512 = hashlib.sha512()
    for chunk in iter(lambda: file.read(4096), b""):
        sha512.update(chunk)
    return sha512.hexdigest()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
