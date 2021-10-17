from django.shortcuts import render
from . import pool

def AdminLogin(request):
    return render(request,"adminLogin.html",{'msg':""})

def CheckLogin(request):
    try:
        db,cmd=pool.connectionPooling()
        email=request.GET['email']
        password=request.GET['password']
        q="select * from admin where email='{}' and password='{}'".format(email,password)
        cmd.execute(q)
        row=cmd.fetchone()
        if(row):
            return render(request,"Dashboard.html",{'row':row})
        else:
            return render(request,"adminLogin.html",{'msg':"Pls Input Valid Email and Password"})
    except Exception as e:
        print("error:",e)
        return render(request,"adminLogin.html",{"msg":"Server Error....."})