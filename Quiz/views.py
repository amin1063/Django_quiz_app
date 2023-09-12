from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from rest_framework import viewsets
# from .serializers import GeeksSerializer
from .models import QuesModel


from rest_framework import viewsets

from Quiz.serializers import PersonSerializer, SpeciesSerializer
from Quiz.models import Person, Species



# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context) 

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')


# class GeeksViewSet(viewsets.ModelViewSet):
#     # define queryset
#     queryset = QuesModel.objects.all()
#     # specify serializer to be used
#     serializer_class = GeeksSerializer    



class PersonViewSet(viewsets.ModelViewSet):
   queryset = Person.objects.all()
   serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Species.objects.all()
   serializer_class = SpeciesSerializer
