from django.shortcuts import render
from . import pool
import os
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def LectureInterface(request):
    return render(request,"lectureInterface.html")

@xframe_options_exempt
def SubmitLectures(request):
    try:
        db, cmd = pool.connectionPooling()
        categoryId = request.POST['categoryId']
        subjectId = request.POST['subjectId']
        courseId = request.POST['courseId']
        lectureName = request.POST['lectureName']

        length = request.POST['length']
        icon = request.FILES['icon']

        q = "insert  into lecture (categoryId,,subjectId,courseName,courseOverview,rting,length,icon,poster) values('{0}','{1}','{2}','{3}','{4}','{5}')".format(categoryId, subjectId,courseId, lectureName,  length, icon.name)
        cmd.execute(q)
        db.commit()
        F=open("D:/Learning_CS/assets/"+icon.name,"wb")
        for chunk in icon.chunk():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, 'lectureInterface.html', {'status', True})
    except Exception as e:
        print("error:", e)
        return render(request, 'lectureInterface.html', {'status', False})

@xframe_options_exempt
def displayAllLectures(request):
    try:
        db,cmd=pool.connectionPooling()
        q='select * from lecture'
        cmd.execute(q)
        rows =cmd.fetchall()
        db.close()
        return render(request,"displayAllLectures.html",{'rows':rows})
    except Exception as e:
        print("error:",e)
        return render(request,"displayAllLectures.html",{'rows':[]})

@xframe_options_exempt
def LectureById(request):
    try:
        db,cmd=pool.connectionPooling()
        lid=request.GET['lid']
        q="select L. * ,(select C.categoryName from category C where C.categoryId=L.categoryId),(select S.subjectName from subjects S where S.subjectId=L.subjectId),(select Co.courseName from Course Co where Co.courseId=L.courseId) from lecture L where lectureId='{}'".format(lid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"LectureById.html",{"row":row})
    except Exception as e:
        print("error:",e)
        return render(request,"LectureById.html",{"row":[]})

@xframe_options_exempt
def EditDeleteLectureData(request):
    try:
        db,cmd=pool.connectionPooling()
        btn=request.GET['btn']
        if(btn=="Edit"):
            lectureId=request.GET['lectureId']
            categoryId = request.GET['categoryId']
            subjectId = request.GET['subjectId']
            courseId = request.GET['courseId']
            lectureName = request.GET['lectureName']
            length = request.POST['length']
            q="update lecture set categoryId='{}',subjectId='{}',courseId='{}',lectureName='{}',length='{}' where lectureId='{}'".format(categoryId,subjectId,courseId,lectureName,length,lectureId)
            cmd.execute(q)
            db.commit()
            db.close()
        elif(btn=="Delete"):
            lectureId = request.GET['lectureId']
            q="delete from lecture where lectureId='{}'".format(lectureId)
            cmd.execute(q)
            cmd.execute()
            db.commit()
            db.close()
        return render(request,"LectureById.html",{"status":True})
    except Exception as e:
        print("error:",e)
        return render(request,"LectureById.html",{"status":False})

@xframe_options_exempt
def EditLectureIcon(request):
    try:
        db,cmd=pool.connectionPooling()
        lectureId=request.GET['lecturId']
        icon=request.FILES["icon"]
        filename1=request.GET['filename1']
        q="update lecture set icon='{}' where lectureId='{}'".format(icon.name,lectureId)
        cmd.execute(q)
        db.commit()
        F=open("D:/Learning_CS/assets/"+icon.name)
        for chunk in icon.chunk():
            F.write(chunk)
        F.close()
        os.remove("D:/Learning_CS/assets/"+filename1)
        db.close()
        return render(request,"LectureById.html",{"status":True})
    except Exception as e:
        print("error:",e)
        return render(request,"LectureById.html",{"status":False})










