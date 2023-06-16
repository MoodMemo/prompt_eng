# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 11:38:23 2023

@author: juLeena
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return 'This is My Page!'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
