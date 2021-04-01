import mysql.connector
import json


def sql_connection():
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 password="",
                                 database="db_idha")
    return db


def input_suhu_kelembapan(suhu, kelembapan):
    db = sql_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO `suhu`(`suhu`, `kelembapan`) VALUES (%s,%s)",
                   (suhu, kelembapan))
    db.commit()


def input_cahaya(cahaya):
    db = sql_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO `cahaya`(`cahaya`) VALUES (%s)", (cahaya, ))
    db.commit()


def input_hujan(hujan):
    db = sql_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO `hujan`(`hujan`) VALUES (%s)", (hujan, ))
    db.commit()


def get_suhu_kelembapan():
    db = sql_connection()
    cursor = db.cursor()
    cursor.execute("SELECT `suhu`, `kelembapan` FROM `suhu`")
    rows = [x for x in cursor]
    cols = [x[0] for x in cursor.description]
    datas = []
    for row in rows:
        data = {}
        for prop, val in zip(cols, row):
            data[prop] = val
        datas.append(data)
    dataJson = json.dumps(datas)
    return dataJson


def get_cahaya():
    db = sql_connection()
    cursor = db.cursor()
    cursor.execute("SELECT `cahaya` FROM `cahaya`")
    rows = [x for x in cursor]
    cols = [x[0] for x in cursor.description]
    datas = []
    for row in rows:
        data = {}
        for prop, val in zip(cols, row):
            data[prop] = val
        datas.append(data)
    dataJson = json.dumps(datas)
    return dataJson


def get_hujan():
    db = sql_connection()
    cursor = db.cursor()
    cursor.execute("SELECT `hujan` FROM `hujan`")
    rows = [x for x in cursor]
    cols = [x[0] for x in cursor.description]
    datas = []
    for row in rows:
        data = {}
        for prop, val in zip(cols, row):
            data[prop] = val
        datas.append(data)
    dataJson = json.dumps(datas)
    return dataJson