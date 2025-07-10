from flask import Flask,request,jsonify
import sqlite3,json

Db='mydb.db'

def databasefunc():
    conn=sqlite3.connect(Db)
    conn.row_factory=sqlite3.Row
    return conn

app=Flask(__name__)

@app.route('/u',methods=['GET'])

def pagination():
    page=request.args.get('page',1)
    limit=request.args.get('limit',10)

    data=databasefunc()
    cur=data.cursor()

    ofset=(page-1)*limit

    cur.execute("select * from CPE limit ? offset ?",(limit,ofset))

    rows=cur.fetchall()

    data.close()

    list1=[]

    for i in rows:
        dict1=dict(i)

        dict1['cpe_title']=json.loads(dict1['cpe_title'])
        dict1['cpe_22_uri']=json.loads(dict1['cpe_22_uri'])
        dict1['cpe_23_uri']=json.loads(dict1['cpe_23_uri'])
        dict1['ref_links']=json.loads(dict1['ref_links'])
        dict1['cpe_22']=json.loads(dict1['cpe_22'])
        dict1['cpe_23']=json.loads(dict1['cpe_23'])

        list1.append(dict1)

    return jsonify(list1) 

if __name__=='__main__':
    app.run(debug=True)





    








