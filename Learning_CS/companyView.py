from .import pool
import os
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.shortcuts import render

@xframe_options_exempt
def CompanyInterface(request):
    return render(request,"CompanyInterface.html")


@xframe_options_exempt
def SubmitCompany(request):
    try:
        db, cmd = pool.connectionPooling()
        subjectId = request.POST['subjectId']
        companyName = request.POST['companyName']
        website=request.POST['website']
        q = "insert into company (subjectId,companyName,website) values('{0}','{1}','{2}')".format(subjectId,companyName,website)
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request, 'CompanyInterface.html', {'status':True})
    except Exception as e:
        print("error:", e)
        return render(request, 'CompanyInterface.html', {'status': False})


@xframe_options_exempt
def displaySubjectJSON(request):
    try:
        db,cmd=pool.connectionPooling()

        q="select * from subjects"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("error:",e)
        return JsonResponse([],safe=False)

@xframe_options_exempt
def ProblemsInterface(request):
    return render(request,"ProblemsInterface.html")


@xframe_options_exempt
def SubmitProblems(request):
    try:
        db, cmd = pool.connectionPooling()
        courseId = request.POST['courseId']
        link = request.POST['link']
        q = "insert into problems (courseId,link) values('{0}','{1}')".format(courseId,link)
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request, 'ProblemsInterface.html', {'status':True})
    except Exception as e:
        print("error:", e)
        return render(request, 'ProblemsInterface.html', {'status': False})



@xframe_options_exempt
def displayCourseJSON(request):
    try:
        db,cmd=pool.connectionPooling()

        q="select * from course"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("error:",e)
        return JsonResponse([],safe=False)