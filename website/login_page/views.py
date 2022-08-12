from django.shortcuts import render
import mysql.connector as sql
email =''
pwd = ''

# Create your views here.
def login_action(request):
    global email, pwd
    if request.method =="POST":
        m= sql.connect(host="localhost", user="root", passwd="dheeraj1902", database="user_info")
        cursor = m.cursor()
        d= request.POST
        for key, value in d.items():
            if key == "email":
                email = value
            if key == "password":
                pwd = value
        c="select * from users where email='{}' and password='{}'".format(email, pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            return render(request, 'wlc.html')
            
    return render(request, 'login_page.html')