from django.shortcuts import render
from . import pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt


def UserView(request):
    try:
        ses = ''
        user = ''
        try:

            if(request.session['USER']):
                ses=True
                user=request.session['USER']
            else:
                ses=False
                user=[]
            print('USER',user)

        except:
            pass

        db,cmd=pool.connectionPooling()
        q="select * from course"
        cmd.execute(q)
        rows=cmd.fetchall()

        q="select * from subjects where categoryId=3"
        cmd.execute(q)
        srows=cmd.fetchall()

        q = "select * from subjects where categoryId=4"
        cmd.execute(q)
        Crows = cmd.fetchall()


        q = "select * from subjects where categoryId=5"
        cmd.execute(q)
        wrows = cmd.fetchall()


        q = "select * from subjects where categoryId=6"
        cmd.execute(q)
        prows = cmd.fetchall()


        return render(request,"userInterface.html",{'rows':rows,'srows':srows,'Crows':Crows,'wrows':wrows,'prows':prows,'ses':ses,'user':user})
    except Exception as e:
        print("error:",e)
        return render(request,"userInterface.html",{'rows':[],'srows':[],'Crows':[],'wrows':[],'prows':[],'ses':[],'user':[]})


def CoursePreview(request):
    try:
        ses = ''
        user = ''
        try:
            if(request.session['USER']):
                ses=True
                user=request.session['USER']
            else:
                ses=False
                user=[]
            print('USER',user)

        except:
            pass


        row=request.GET['row']
        row=eval(row)
        cid=row[2]
        db, cmd = pool.connectionPooling()
        q = "select * from course"
        cmd.execute(q)
        rows = cmd.fetchall()

        q = "select * from lecture where courseId='{}'".format(cid)
        cmd.execute(q)
        lrows = cmd.fetchall()

        q = "select * from course where courseId='{}'".format(cid)
        cmd.execute(q)
        orow = cmd.fetchone()

        q="select * from company where subjectId='{}'".format(row[1])
        cmd.execute(q)
        srows = cmd.fetchall()

        db.close()
        return render(request,'CoursePreview.html',{'row':row,'rows':rows,'lrows':lrows,'orow':orow,'srows':srows,'ses':ses,'user':user})
    except Exception as e:
        print("error:",e)
        return render(request,'CoursePreview.html', {'row': [],'rows':[],'lrows':[],'orow':[],'srows':[],'ses':[],'user':[]})


def LecturePreview(request):
    try:
        ses = ''
        user = ''
        try:

            if(request.session['USER']):
                ses=True
                user=request.session['USER']
            else:
                ses=False
                user=[]
            print('USER',user)

        except:
            pass

        db,cmd=pool.connectionPooling()
        lrow=request.GET['lrow']
        lrow=eval(lrow)

        q = "select * from lecture where courseId='{}'".format(lrow[2])
        cmd.execute(q)
        rows = cmd.fetchall()

        q = "select * from problems where courseId='{}'".format(lrow[2])
        cmd.execute(q)
        prows = cmd.fetchall()

        db.close()
        return render(request,'LecturePreview.html',{'lrow':lrow,'rows':rows,'prows':prows,'ses':ses,'user':user})
    except Exception as e:
        print("err:",e)
        return render(request,'LecturePreview.html',{'lrow':[],'rows':[],'prows':[],'ses':[],'user':[]})

def SubjectPreview(request):
    try:
        ses = ''
        user = ''
        try:

            if(request.session['USER']):
                ses=True
                user=request.session['USER']
            else:
                ses=False
                user=[]
            print('USER',user)

        except:
            pass


        db,cmd=pool.connectionPooling()
        srow = request.GET['srow']
        srow = eval(srow)

        q="select * from course where subjectId='{}'".format(srow[1])
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"SubjectPreview.html",{'srow':srow,'rows':rows,'ses':ses,'user':user})
    except Exception as e:
        print("er:",e)
        return render(request, "SubjectPreview.html",{'srow':[],'rows':[],'ses':[],'user':[]})

def AddNotes(request):
    try:
        db,cmd=pool.connectionPooling()
        courseId=request.GET['cid']
        heading=request.GET['heading']
        text=request.GET['text']
        q="insert into notes (courseId,heading,text) values('{0}','{1}','{2}')".format(courseId,heading,text)
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request,"LecturePreview.html")
    except Exception as e:
        print("e:",e)
        return render(request,"LecturePreview.html")


def DisplayAllNotes(request):
    try:
        db,cmd=pool.connectionPooling()
        courseId=request.GET['courseId']
        q="select * from notes where courseId='{}'".format(courseId)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllNotes.html",{'rows':rows})
    except Exception as e:
        print("E",e)
        return render(request, "DisplayAllNotes.html", {'rows': []})


def Gate(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db,cmd=pool.connectionPooling()
        q="select * from course where categoryId=1"
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,"Gate.html",{'rows':rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:",e)
        return render(request, "Gate.html",{'rows':[],'ses':[],'user':[]})


def CompetitiveProgramming(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db,cmd=pool.connectionPooling()
        q="select * from course where categoryId=7"
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request, "CompetitiveProgramming.html",{'rows':rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:",e)
        return render(request, "CompetitiveProgramming.html",{'rows':[],'ses':[],'user':[]})


def ArtificialIntelligence(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where categoryId=8"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "ArtificialIntelligence.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "ArtificialIntelligence.html", {'rows': [],'ses':[],'user':[]})

def MachineLearning(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where categoryId=3"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "MachineLearning.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "MachineLearning.html", {'rows': [],'ses':[],'user':[]})

def DataScience(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where categoryId=10"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "DataScience.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "DataScience.html", {'rows': [],'ses':[],'user':[]})

def WebTechnologies(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where categoryId=5"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "WebTechnologies.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "WebTechnologies.html", {'rows': [],'ses':[],'user':[]})

def DataStructures(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where categoryId=11"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "DataStructures.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "DataStructures.html", {'rows': [],'ses':[],'user':[]})

def C(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=39"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "C.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "C.html", {'rows': [],'ses':[],'user':[]})

def CPlus(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=40"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "C++.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "C++.html", {'rows': [],'ses':[],'user':[]})

def Python(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=42"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "python.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "python.html", {'rows': [],'ses':[],'user':[]})

def Java(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=41"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "Java.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "Java.html", {'rows': [],'ses':[],'user':[]})

def JavaScript(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=30"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "JavaScript.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "JavaScript.html", {'rows': [],'ses':[],'user':[]})

def SQL(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=33"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "SQL.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "SQL.html", {'rows': [],'ses':[],'user':[]})

def JQuery(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=34"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "JQuery.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "JQuery.html", {'rows': [],'ses':[],'user':[]})

def HTML(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=28"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "HTML.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "HTML.html", {'rows': [],'ses':[],'user':[]})

def CSS(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=29"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "CSS.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "CSS.html", {'rows': [],'ses':[],'user':[]})

def Php(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=31"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "Php.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "Php.html", {'rows': [],'ses':[],'user':[]})


def DBMS(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=20"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "DBMS.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "DBMS.html", {'rows': [],'ses':[],'user':[]})

def CSO(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=2"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "CSO.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "CSO.html", {'rows': [],'ses':[],'user':[]})

def Mathematics(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=25"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "Mathematics.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "Mathematics.html", {'rows': [],'ses':[],'user':[]})

def ComputerNetwork(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=18"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "ComputerNetworks.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "ComputerNetworks.html", {'rows': [],'ses':[],'user':[]})


def CompilerDesign(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=19"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "CompilerDesign.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "CompilerDesign.html", {'rows': [],'ses':[],'user':[]})

def DigitalLogics(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=23"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "DigitalLogics.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "DigitalLogics.html", {'rows': [],'ses':[],'user':[]})

def OperatingSystem(request):
    try:
        ses = ''
        user = ''
        try:

            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses = False
                user = []
            print('USER', user)

        except:
            pass
        db, cmd = pool.connectionPooling()
        q = "select * from course where subjectId=16"
        cmd.execute(q)
        rows = cmd.fetchall()
        return render(request, "OperatingSystem.html", {'rows': rows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "OperatingSystem.html", {'rows': [],'ses':[],'user':[]})

def Searching(request):
    try:
        db,cmd=pool.connectionPooling()
        search=request.GET['search']
        if(search==""):
            return JsonResponse(safe=False)
        else:
            q="select * from course where courseName like '{}%'".format(search)
            cmd.execute(q)
            rows=cmd.fetchall()
            db.close()
            return JsonResponse(rows,safe=False)
    except Exception as e:
        print("err:",e)
        return JsonResponse([],safe=False)


def UserDetailSubmit(request):
    try:
        db,cmd=pool.connectionPooling()
        name=request.GET['name']
        email = request.GET['email']
        password = request.GET['password']
        q="insert into userlogin (name,email,password) values('{0}','{1}','{2}')".format(name,email,password)
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse("Registration Successful",safe=False)
    except Exception as e:
        print("Err:",e)
        return JsonResponse("Registration Failed",safe=False)

def CheckUserLogin(request):
    try:
        db, cmd = pool.connectionPooling()
        email = request.GET['email']
        q="select * from userlogin where email='{}'".format(email)
        print(q)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return JsonResponse(row, safe=False)
    except Exception as e:
        print("errrr:",e)
        return JsonResponse(None,safe=False)

def UserSession(request):
    try:
        email = request.GET['email']
        name=request.GET['name']

        request.session["USER"]=[email,name]
        return JsonResponse(True, safe=False)
    except Exception as e:
        print("errrr",e)
        return JsonResponse(False,safe=False)


def UserLogout(request):
    try:
        del request.session['USER']
        return UserView(request)
    except Exception as e:
        print("er:",e)


