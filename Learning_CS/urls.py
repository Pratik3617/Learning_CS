"""Learning_CS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import categoryView
from . import subjectView
from .import courseView
from .import lectureView
from .import adminView
from . import userView
from .import companyView
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),

    #admin
    path('adminlogin/',adminView.AdminLogin),
    path('checklogin/',adminView.CheckLogin),

    #category
    path('categoryInterface/',categoryView.CategoryInterface),
    path('submitCategory',categoryView.SubmitCategory),
    path('displayallCategories/',categoryView.displayAllCategories),
    path('categorybyid/',categoryView.CategoryById),
    path('displayallCategoryjson/',categoryView.displayAllCategoryJSON),
    path('editdeletecategorydata/',categoryView.EditDeleteCategoryData),
    path('editicon/',categoryView.EditIcon),
    path('displayallCategories/', categoryView.displayAllCategories),

    #subject
    path('subjectInterface/',subjectView.SubjectInterface),
    path('submitSubjects', subjectView.SubmitSubjects),
    path('displayallSubjects/',subjectView.displayAllSubjects),
    path('subjectbyid/',subjectView.SubjectById),
    path('editdeletesubjectdata/', subjectView.EditDeleteSubjectData),
    path('editsubjecticon/', subjectView.EditSubjectIcon),
    path('editdsubjectposter/', subjectView.EditSubjectPoster),
    path('displayallSubjectjson/', subjectView.displayAllSubjectJSON),

    #course
    path('courseInterface/',courseView.CourseInterface),
    path('submitCourses', courseView.SubmitCourses),
    path('displayallCourses/',courseView.displayAllCourses),
    path('editdeletecoursedata/', courseView.EditDeleteCourseData),
    path('coursebyid/', courseView.CourseById),
    path('editcourseicon/', courseView.EditCourseIcon),
    path('editcourseposter/', courseView.EditCoursePoster),
    path('displayallCoursejson/', courseView.displayAllCourseJSON),

    #lecture
    path('lectureInterface/',lectureView.LectureInterface),
    path('submitLectures', lectureView.SubmitLectures),
    path('displayallLectures/',lectureView.displayAllLectures),
    path('lecturebyid/', lectureView.LectureById),
    path('editdeletelecturedata/', lectureView.EditDeleteLectureData),
    path('editlectureicon/', lectureView.EditLectureIcon),

    # company
    path('companyInterface/',companyView.CompanyInterface),
    path('submitCompany', companyView.SubmitCompany),
    path('displaysubjectjson/', companyView.displaySubjectJSON),
    path('problemInterface/',companyView.ProblemsInterface),
    path('submitProblems', companyView.SubmitProblems),
    path('displaycoursejson/', companyView.displayCourseJSON),


    path('user/',userView.UserView),
    path('gate/',userView.Gate),
    path('competitiveprogramming/',userView.CompetitiveProgramming),
    path('artificialIntelligence/',userView.ArtificialIntelligence),
    path('machineLearning/',userView.MachineLearning),
    path('dataScience/',userView.DataScience),
    path('webTechnologies/',userView.WebTechnologies),
    path('dataStructures/',userView.DataStructures),
    path('C/', userView.C),
    path('C++/', userView.CPlus),
    path('python/', userView.Python),
    path('java/', userView.Java),
    path('javascript/', userView.JavaScript),
    path('sql/', userView.SQL),
    path('jquery/', userView.JQuery),
    path('html/', userView.HTML),
    path('css/', userView.CSS),
    path('php/', userView.Php),
    path('dbms/', userView.DBMS),
    path('cso/', userView.CSO),
    path('mathematics/', userView.Mathematics),
    path('computerNetwork/', userView.ComputerNetwork),
    path('compilerDesign/', userView.CompilerDesign),
    path('operatingSystem/', userView.OperatingSystem),
    path('digitalLogics/', userView.DigitalLogics),

    path('coursePreview/',userView.CoursePreview),
    path('lecturePreview/',userView.LecturePreview),
    path('subjectPreview/', userView.SubjectPreview),
    path('searching/', userView.Searching),
    path('addnotes', userView.AddNotes),
    path('displayAllNotes/', userView.DisplayAllNotes),

    path('userdetailsubmit/',userView.UserDetailSubmit),
    path('checkuserlogin/',userView.CheckUserLogin),
    path('usersession/',userView.UserSession),
    path('userlogout/', userView.UserLogout),


    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]
