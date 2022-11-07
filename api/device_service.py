from flask import Flask, Blueprint, request, jsonify
import sqlite3

device = Blueprint('device',__name__)

def conectar():
    return sqlite3.connect('database/data.db')

@device.route('/', methods=['GET'])
def get_all():
    device = []
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_device")

        for i in cur.fetchall():
            devices = {}
            device["id"] = i["id"]
            device["nome"] = i["nome"]
            device["ssid"] = i["ssid"]
            device["mac"] = i["mac"]
            device["senha"] = i["senha"]
            device["lock"] = i["lock"]
            device.append(device)
    except Exception as e:
        print(e)
        devices = []

    return jsonify(devices)
