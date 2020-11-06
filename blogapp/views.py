from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *
from django.shortcuts import redirect
# Create your views here.

def index(request):
	postitem = Post.objects.all()
	form = BlogForm()
	context = {'postitem':postitem, 'form':form}
	
	return render(request,'blog/home.html',context)


def create(request):
	form = BlogForm()
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {
		'form':form
	}
	return render(request, 'blog/create.html',context)


def update(request,pk):

	postitem = Post.objects.get(id=pk)
	form = BlogForm(instance= postitem)
	if request.method == "POST":
		form = BlogForm(request.POST, instance= postitem)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form':form,'postitem':postitem}
	return render(request, 'blog/update.html',context)


def delete(request,pk):
	postitem = Post.objects.get(id=pk)
	context = {'postitem':postitem}
	if request.method == "POST":
		postitem.delete()
		return redirect('/')

	return render(request, 'blog/delete.html',context)
