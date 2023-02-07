from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Blog,Category
# Create your views here.
def main(request):
    return render(request,'index.html')

def culture(request):
    return render(request,'culture.html')

def culture_topic(request,tID):
    return render(request,'culturetopic.html')


def listBlogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs" : blogs
    }
    return render(request,'listblogs.html',context)

def spBlog(request,id):
    blog = Blog.objects.get(id = id)
    context = {
        "blog" : blog
    }
    return render(request,'spblog.html',context)
def addBlog(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        text = request.POST['text']
        Blog.objects.create(blog_name=name,blog_category=Category.objects.get(cat_name=category),blog_text=text)
        return HttpResponseRedirect(reverse('list'))
    return render(request,'addBlog.html')

def delBlog(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return HttpResponseRedirect(reverse('list'))
    #return render(request, 'listblogs.html')

def editBlog(request,id):
    blog = Blog.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        text = request.POST['text']
        Blog.objects.filter(id=id).update(blog_name=name,blog_category=Category.objects.get(cat_name=category),blog_text=text)
        return HttpResponseRedirect(reverse('list'))
    else:
        # request.POST['name'] = blog.blog_name
        # request.POST['category'] = blog.blog_category
        # request.POST['text'] = blog.blog_text
        context = {
            'cat' : blog
        }
        return render(request,'editBlog.html',context)

