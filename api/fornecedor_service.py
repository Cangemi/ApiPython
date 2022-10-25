from flask import Flask, Blueprint, request, jsonify
import sqlite3

fornecedor = Blueprint('fornecedor',__name__)

@fornecedor.route('/', methods=['GET'])
def teste():
    return 'Fornecedores'
