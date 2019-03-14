from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import *
import datetime
# Create your views here.
def index(request):
    return render(request,'Todo/index.html')

def register(request):
	form=UserForm()
	return render(request,'Todo/register.html',context={"form":form})

def login_user(request):
	form=LoginForm()
	return render(request,'Todo/login.html',context={"form":form,"error_message":""})

def reg(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		email=request.POST['email']
		user=User(username=username,email=email,password=password)
		user.save()
		#return render(request,'Todo/dashboard.html',context={"todos":None,"user":user.id})
	return render(request,'Todo/index.html')

def log(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		print(username,password)
		user = User.objects.get(username=username,password=password)
		login(request,user)
		todos=ToDo.objects.filter(user=user)
		print(todos)
		return render(request,'Todo/dashboard.html',context={"todos":todos,"user":user.id})
	return render(request,'Todo/index.html')
def logout_user(request):
	logout(request)
	return render(request,'Todo/index.html')
@login_required
def addTodo(request):
	if request.method=="POST":
		task=request.POST['task']
		description=request.POST['description']
		time=request.POST['time']
		user_id=request.POST['user']
		user=User.objects.get(pk=user_id)
		todo=ToDo(task=task,description=description,user=user,time=time)
		todo.save()
		todos=ToDo.objects.filter(user=user)
		return render(request,'Todo/dashboard.html',context={"todos":todos,"user":user.id})
	form=TodoForm()
	return render(request,'Todo/todo.html',context={"form":form,"user":request.user.id})
@login_required
def deleteTodo(request):
	if request.method=="POST":
		tid=request.POST['tid']
		ToDo.objects.get(pk=tid).delete()
		user=request.user
		todos=ToDo.objects.filter(user=user)
		return render(request,'Todo/dashboard.html',context={"todos":todos,"user":user.id})
@login_required
def edit(request,tid):
	todo=ToDo.objects.get(pk=tid)
	print(tid)
	print(todo.time.time())
	return render(request,'Todo/edit.html',context={"todo":todo,"tid":tid,"time":todo.time.strftime("%Y-%m-%d %H:%M:%S") })
@login_required
def editTodo(request):
	if request.method=="POST":
		tid=request.POST["tid"]
		task=request.POST["task"]
		description=request.POST["description"]
		time=request.POST["time"]
		todo=ToDo.objects.get(pk=tid)
		todo.task=task
		todo.description=description
		todo.time=time
		todo.save()
		todos=ToDo.objects.filter(user=request.user)
		return render(request,'Todo/dashboard.html',context={"todos":todos,"user":request.user.id})