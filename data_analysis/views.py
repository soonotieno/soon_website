from django.shortcuts import render
import pymysql
import pandas as pd
import re


def home(request):
    conn = pymysql.connect(host='localhost', user='root', password='tjqltm12@@', db='soon', charset='utf8')
    curs = conn.cursor()
    sql = 'SELECT company,code FROM company_info '
    curs.execute(sql)
    values = curs.fetchall()
    conn.close()

    return render(
        request, 'data_analysis/home.html', {'values': values})
