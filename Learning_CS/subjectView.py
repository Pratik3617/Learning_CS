from django.shortcuts import render
from . import pool
import os
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def SubjectInterface(request):
    return render(request,"subjectInterface.html")

@xframe_options_exempt
def SubmitSubjects(request):
    try:
        db,cmd=pool.connectionPooling()
        categoryId=request.POST['categoryId']
        subjectName=request.POST['subjectName']
        description=request.POST['description']
        companyName=request.POST['companyName']
        website=request.POST['website']
        icon=request.FILES['icon']
        poster=request.FILES['poster']
        q="insert  into subjects (categoryId,subjectName,description,icon,poster,companyName,website) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(categoryId,subjectName,description,icon.name,poster.name,companyName,website)
        cmd.execute(q)
        db.commit()
        F=open("D:/Learning_CS/assets/"+icon.name,"wb")
        for chunk in icon.chunks():
            F.write(chunk)
        F.close()
        F = open("D:/Learning_CS/assets/" + poster.name, "wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request,'subjectInterface.html',{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request,'subjectInterface.html',{'status':False})

@xframe_options_exempt
def displayAllSubjects(request):
    try:
        db,cmd=pool.connectionPooling()
        q='select S.*,(select C.categoryName from category C where C.categoryId=S.categoryId) from subjects S'
        cmd.execute(q)
        rows =cmd.fetchall()
        db.close()
        return render(request,"displayAllSubjects.html",{'rows':rows})
    except Exception as e:
        print("error:",e)
        return render(request,"displayAllSubjects.html",{'rows':[]})

@xframe_options_exempt
def SubjectById(request):
    try:
        db,cmd=pool.connectionPooling()
        sid=request.GET['sid']
        q="select S.*,(select C.categoryName from category C where C.categoryId=S.categoryId) from subjects S where subjectId='{}'".format(sid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"SubjectById.html",{"row":row})
    except Exception as e:
        print("error:",e)
        return render(request,"SubjectById.html",{"row":[]})

@xframe_options_exempt
def EditDeleteSubjectData(request):
    try:
        btn=request.GET['btn']
        db,cmd=pool.connectionPooling()
        if(btn=="Edit"):
            categoryId = request.POST['categoryId']
            subjectId=request.GET['subjectId']
            subjectName = request.POST['subjectName']
            description = request.POST['description']
            companyName = request.POST['companyName']
            website = request.POST['website']
            q = "update subjects set(categoryId='{}',subjectName='{}',description='{}',companyName='{}',website='{}') where subjectId='{}'".format(categoryId, subjectName, description, subjectId,companyName,website)
            cmd.execute(q)
            db.commit()
            db.close()
        elif(btn=="Delete"):
            subjectId = request.GET['subjectId']
            q="delete from subjects where subjectId='{}'".format(subjectId)
            cmd.execute(q)
            db.commit()
            db.close()
        return render(request,"SubjectById.html",{"status":True})
    except Exception as e:
        print("error:",e)
        return render(request,"SubjectById.html",{"status":False})

@xframe_options_exempt
def EditSubjectIcon(request):
    try:
        db,cmd=pool.connectionPooling()
        subjectId=request.GET['subjectId']
        filename1=request.GET['filename1']
        icon=request.FILES['icon']
        q="update subjects set icon='{}' where subjectId='{}'".format(icon.name,subjectId)
        cmd.execute(q)
        db.commit()
        F=open("D:/Learning_CS/assets/"+icon.name)
        for chunk in icon.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/Learning_CS/assets/"+filename1)
        db.close()
        return render(request,"SubjectById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request,"SubjectById.html",{'status':False})

@xframe_options_exempt
def EditSubjectPoster(request):
    try:
        db,cmd=pool.connectionPooling()
        subjectId=request.GET['subjectId']
        filename2=request.GET['filename2']
        poster=request.FILES['poster']
        q="update subjects set poster='{}' where subjectId='{}'".format(poster.name,subjectId)
        cmd.execute(q)
        db.commit()
        F=open("D:/Learning_CS/assets/"+poster.name)
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/Learning_CS/assets/"+filename2)
        db.close()
        return render(request,"SubjectById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request,"SubjectById.html",{'status':False})


@xframe_options_exempt
def displayAllSubjectJSON(request):
    try:
        db,cmd=pool.connectionPooling()
        cid=request.GET['cid']
        q="select * from subjects where categoryId='{}'".format(cid)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("error:",e)
        return JsonResponse([],safe=False)








