from flask import Flask,request,jsonify
import sqlite3,json

Db='mydb.db'

def databasefunc():
    conn=sqlite3.connect(Db)
    conn.row_factory=sqlite3.Row
    return conn

app=Flask(__name__)

@app.route('/search',methods=['GET'])

def search():
    title=request.args.get('cpe_title')
    cpe_22uri=request.args.get('cpe_22_uri')
    cpe_23uri=request.args.get('ref_links')
    ref=request.args.get('ref_links')
    cpe_22=request.args.get('cpe_22')
    cpe_23=request.args.get('cpe_23')

    query="select * from CPE where 1=1"
    param=[]


    if title:
        query+=f" and cpe_title={title}"
        param.append(title)

    if cpe_22uri:
        query+=f"and cpe_22_uri={cpe_22uri}"
        param.append(cpe_22uri)

    if cpe_23uri:
        query+=f"and cpe_23_uri={cpe_23uri}"
        param.append(cpe_23uri)

    if ref:
        query+=f"and ref_links={ref}"
        param.append(ref)

    if cpe_22:
        query+=f"and cpe_22={cpe_22}"
        param.append(cpe_22)

    if cpe_23:
        query+=f"and cpe_23={cpe_23}"
        param.append(cpe_23)

    data=databasefunc()    
    cur=data.cursor()

    cur.execute(query,param)        

    cur.execute("select * from CPE")

    row=cur.fetchall()

    list1=[]

    for i in row:
        dict1=dict(i)

        dict1['cpe_title']=json.loads(dict1['cpe_title'])
        dict1['cpe_22_uri']=json.loads(dict1['cpe_22_uri'])
        dict1['cpe_23_uri']=json.loads(dict1['cpe_23_uri'])
        dict1['ref_links']=json.loads(dict1['ref_links'])
        dict1['cpe_22']=json.loads(dict1['cpe_22'])
        dict1['cpe_23']=json.loads(dict1['cpe_23'])

        list1.append(dict1)


    return jsonify(list1)

    



