from django.shortcuts import render
from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.http import Http404
from .models import Course
from .models import MCQ
from .models import Teacher,Student
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .models import Exam
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


from django.shortcuts import render_to_response
# Create your views here.
def index(request):

    #all_course = Course.objects.all()
    return render(request,'onlineEducation/index.html',{})

def login(request):
    if(request.method == "POST"):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            print("redirect")
            return redirect( "http://127.0.0.1:8000/onlineeducation/course/" )



        else:
            print("sabbir")
            return render(request,'onlineEducation/login.html',{})


    elif (request.method == "GET"):
        logout(request)
        return render(request,'onlineEducation/login.html',{})

    #all_course = Course.objects.all()


def home(request):
    all_course = Course.objects.all()
    context={
        "courses":all_course,
    }
    return render(request,'onlineEducation/home.html',context)


def exam(request):
    if(request.method=="GET"):
        print("pack")

    all_exam = Exam.objects.all()
    context={
        "exams":all_exam,
    }
    return render(request,'onlineEducation/exam.html',context)



def exam_detail(request,exam_id):
    #return HttpResponse("<h2> detail for exam"+str(exam_id)+ " </h2>")
    all_question = MCQ.objects.all()
   # print(all_question)
    context={
        "mcqs":all_question,
         "id":int(exam_id)
    }
    return render(request,'onlineEducation/exam_detail.html',context)



def course(request):
    all_course = Course.objects.all()
   # print(all_question)
    context={
        "courses":all_course,
    }

    return render(request,'onlineEducation/course.html',context)


def question(request):
    all_question = MCQ.objects.all()
   # print(all_question)
    data=0


    context={
        "mcqs":all_question,

    }

    return render(request,'onlineEducation/question.html',context)


def result(request):
    all_question = MCQ.objects.all()
    marks=0
    id=0
    if(request.method=="POST"):
        #print("in post request")
        #data =  request.POST.get('value')
        #print (data)




       # print(request.POST)
        for mcq in all_question:
            data=request.POST.get(str(mcq.id))
            #print(data)
            if(data==mcq.correctAnswer):
                marks += 1
                id=mcq.exam.id
    context={
        "marks":marks,
        "mcqs":all_question,
        "id":id,

    }

    return render(request,'onlineEducation/result.html',context)





def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return redirect('http://127.0.0.1:8000/onlineeducation/login/')
    else:
        form = UserCreationForm()
    return render(request, 'onlineEducation/signup.html', {'form': form})



def teacher(request):
    all_teacher = Teacher.objects.all()
   # print(all_question)
    context={
        "teachers":all_teacher,
    }

    return render(request,'onlineEducation/teacher.html',context)



def student(request):
    all_student = Student.objects.all()
   # print(all_question)
    context={
        "students":all_student,
    }

    return render(request,'onlineEducation/student.html',context)
