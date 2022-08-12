from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
f_name =''
l_name =''
email =''
pwd =''
# Create your views here.
def signup_action(request):
    global f_name, l_name, email, pwd
    if request.method =='POST':
        m= sql.connect(host="localhost", user="root", passwd="dheeraj1902", database="user_info")
        cursor = m.cursor()
        d= request.POST
        for key, value in d.items():
            if key == "first_name":
                f_name = value
            if key == "last_name":
                l_name = value
            if key == "email":
                email = value
            if key == "password":
                pwd = value
        c="insert into users values('{}','{}','{}','{}')".format(f_name, l_name, email, pwd)
        cursor.execute(c)
        m.commit()
    
    return render(request, 'signup_page.html')

