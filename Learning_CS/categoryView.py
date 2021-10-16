from django.shortcuts import render
from . import pool
import os
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def CategoryInterface(request):
    return render(request,"categoryInterface.html")

@xframe_options_exempt
def SubmitCategory(request):
    try:
        db,cmd=pool.connectionPooling()
        categoryName=request.POST['categoryName']
        description=request.POST['description']
        icon=request.FILES['icon']
        q="insert into category (categoryName,description,icon) values('{0}','{1}','{2}')".format(categoryName,description,icon.name)
        F=open("D:/Learning_CS/assets/"+icon.name,"wb")
        for chunk in icon.chunks():
            F.write(chunk)
        F.close()
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request,'categoryInterface.html',{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request,'categoryInterface.html',{'status':False})

@xframe_options_exempt
def displayAllCategories(request):
    try:
        db,cmd=pool.connectionPooling()
        q='select * from category'
        cmd.execute(q)
        rows =cmd.fetchall()
        db.close()
        return render(request,"displayAllCategories.html",{'rows':rows})
    except Exception as e:
        print("error:",e)
        return render(request,"displayAllCategories.html",{'rows':[]})


@xframe_options_exempt
def CategoryById(request):
    try:
        db,cmd=pool.connectionPooling()
        cid=request.GET['cid']
        q="select * from category where categoryId='{}'".format(cid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"CategoryById.html",{"row":row})
    except Exception as e:
        print("error:",e)
        return render(request,"CategoryById.html",{"row":[]})


@xframe_options_exempt
def EditDeleteCategoryData(request):
    try:
        btn=request.GET['btn']
        db,cmd=pool.connectionPooling()
        if(btn=='Edit'):
            categoryId = request.GET['categoryId']
            categoryName = request.GET['categoryName']
            description = request.GET['description']
            q = "update category set categoryName='{}',description='{}' where categoryId='{}'".format(categoryName,description,categoryId)
            cmd.execute(q)
            db.commit()
            db.close()
        elif(btn=="Delete"):
            categoryId = request.GET['categoryId']
            q = "delete from category where categoryId='{}'".format(categoryId)
            cmd.execute(q)
            db.commit()
            db.close()
        return render(request,"CategoryById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request,"CategoryById.html",{'status':False})


@xframe_options_exempt
def EditIcon(request):
    try:
        db,cmd=pool.connectionPooling()
        categoryId=request.GET['categoryId']
        filename=request.GET['filename']
        icon=request.FILES['icon']
        q="update category set icon='{}' where categoryId='{}'".format(icon.name,categoryId)
        cmd.execute(q)
        db.commit()
        F = open("D:/Learning_CS/assets/" + icon.name, "wb")
        for chunk in icon.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/" + filename)
        db.close()
        return render(request,"CategoryById.html",{"status":True})
    except Exception as e:
        print("error:",e)
        return render(request,"CategoryById.html",{"status":False})


@xframe_options_exempt
def displayAllCategoryJSON(request):
    try:
        db,cmd=pool.connectionPooling()
        q='select * from category'
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("error:",e)
        return JsonResponse([],safe=False)


