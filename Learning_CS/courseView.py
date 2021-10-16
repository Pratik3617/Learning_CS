from .import pool
import os
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import render

@xframe_options_exempt
def CourseInterface(request):
    return render(request,"courseInterface.html")


@xframe_options_exempt
def SubmitCourses(request):
    try:
        db, cmd = pool.connectionPooling()
        categoryId = request.POST['categoryId']
        subjectId = request.POST['subjectId']
        courseName = request.POST['courseName']
        courseOverview=request.POST['courseOverview']
        rating = request.POST['rating']
        length=request.POST['length']
        tutorName=request.POST['tutorName']
        price = request.POST['price']
        lectures = request.POST['lectures']
        description = request.POST['description']
        authorDetails = request.POST['authorDetails']
        icon = request.FILES['icon']
        poster = request.FILES['poster']
        q = "insert into course (categoryId, subjectId,courseName, courseOverview, rating, length, icon, poster, tutorName, price, lectures, description,authorDetails) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(categoryId, subjectId,courseName, courseOverview, rating, length, icon.name, poster.name, tutorName, price, lectures, description, authorDetails)
        cmd.execute(q)
        db.commit()
        F = open("D:/Learning_CS/assets/" + icon.name, "wb")
        for chunk in icon.chunks():
            F.write(chunk)
        F.close()
        F = open("D:/Learning_CS/assets/" + poster.name, "wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, 'courseInterface.html', {'status':True})
    except Exception as e:
        print("error:", e)
        return render(request, 'courseInterface.html', {'status': False})


@xframe_options_exempt
def displayAllCourses(request):
    try:
        db, cmd = pool.connectionPooling()
        q = 'select * from course'
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return render(request, "displayAllCourses.html", {'rows': rows})
    except Exception as e:
        print("error:", e)
        return render(request, "displayAllCourses.html", {'rows': []})

@xframe_options_exempt
def CourseById(request):
    try:
        db,cmd=pool.connectionPooling()
        coid=request.GET['coid']
        q="select Co.*,(select C.categoryName from category C where C.categoryId=Co.categoryId),(select S.subjectName from subjects S where S.subjectId=Co.subjectId) from course Co where courseId='{}'".format(coid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"CourseById.html",{"row":row})
    except Exception as e:
        print("error:",e)
        return render(request,"CourseById.html",{"row":[]})

@xframe_options_exempt
def EditDeleteCourseData(request):
    try:
        db,cmd=pool.connectionPooling()
        btn=request.GET['btn']
        if(btn=="Edit"):
            courseId=request.GET['courseId']
            categoryId = request.GET['categoryId']
            subjectId = request.GET['subjectId']
            courseName = request.GET['courseName']
            courseOverview = request.GET['courseOverview']
            rating = request.GET['rating']
            length = request.GET['length']
            tutorName = request.GET['tutorName']
            price = request.GET['price']
            lectures = request.GET['lectures']
            description = request.GET['description']
            authorDetails = request.GET['authorDetails']
            q="update course set categoryId='{}', subjectId='{}',courseName='{}',courseOverview='{}',rating='{}',length='{}',tutorName='{}',price='{}',lectures='{}',description='{}',authorDetails='{}' where courseId='{}'".format(categoryId,subjectId,courseName,courseOverview,rating,length,courseId,tutorName,price,lectures,description,authorDetails)
            cmd.execute(q)
            db.commit()
            db.close()
        elif(btn=='Delete'):
            courseId=request.GET['courseId']
            q="delete from course where courseId='{}'".format(courseId)
            cmd.execute(q)
            db.commit()
            db.close()
        return render(request,"CourseById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request, "CourseById.html", {'status': False})

@xframe_options_exempt
def EditCourseIcon(request):
    try:
        db,cmd=pool.connectionPooling()
        courseId=request.GET['courseId']
        icon=request.FILES['icon']
        filename1=request.GET['filename1']
        q="update course set icon='{}' where courseId='{}".format(icon.name,courseId)
        cmd.execute(q)
        db.commit()
        F=open("D:/Learning_CS/assets/"+icon.name,"wb")
        for chunk in icon.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/Learning_CS/assets/"+filename1)
        db.close()
        return render(request,"CourseById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request,"CourseById.html",{'status':False})


@xframe_options_exempt
def EditCoursePoster(request):
    try:
        db,cmd=pool.connectionPooling()
        courseId=request.GET['courseId']
        poster=request.FILES['poster']
        filename2=request.GET['filename2']
        q="update course set icon='{}' where courseId='{}".format(poster.name,courseId)
        cmd.execute(q)
        db.commit()
        F=open("D:/Learning_CS/assets/"+poster.name,"wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/Learning_CS/assets/"+filename2)
        db.close()
        return render(request,"CourseById.html",{'status':True})
    except Exception as e:
        print("error:",e)
        return render(request,"CourseById.html",{'status':False})

@xframe_options_exempt
def displayAllCourseJSON(request):
    try:
        sid=request.GET['sid']
        db,cmd=pool.connectionPooling()
        q="select * from course where subjectId='{}'".format(sid)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("error:",e)
        return JsonResponse([],safe=False)
