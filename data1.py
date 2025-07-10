import sqlite3
from xml.etree import ElementTree as e


data=e.parse('xmldata.xml')
root=data.getroot()

conn=sqlite3.connect("mydb.db")
cur=conn.cursor()

cur.execute('''create table if not exists CPE(
            cpe_title VARCHAR,
            cpe_22_uri TEXT,
            cpe_23_uri TEXT,
            ref_links TEXT,
            cpe_22 DATE,
            cpe_23 DATE
            )'''
        )

for i in root.findall('cpe_item'):
    dc=[]
    title=i.find('title').text
    uri22=i.find('cpe-22-uri').text
    uri23=i.find('cpe-23-uri').text
    ref=[j.text for j in root.find('references').findall('reference')]
    cpe22=i.find('cpe-22').text
    cp23=i.find('cpe-23').text

    if len(title)>0 and len(uri22)>0 and len(uri23)>0 and len(ref)>0 and len(cp23) or len(cpe22)==0:
        dc.append(title)
        dc.append(uri22)
        dc.append(uri23)
        dc.append(ref)
        dc.append(0)
        dc.append(cp23)


    cur.execute("insert into CPE (cpe_title,ref_links,cpe_23) values (?,?,?,?,?,?)",dc)

    conn.commit()

cur.execute("select * from CPE")

conn.close()   
  
