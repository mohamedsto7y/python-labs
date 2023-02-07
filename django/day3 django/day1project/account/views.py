from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from  django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import ListView
# Create your views here.

class List(ListView):
    model = MyUser

class Loginview(View):
    def get(self,req):
        return render(req, 'login.html')
    def post(self,req):
        u = MyUser.objects.filter(username=req.POST['username'], password=req.POST['password'])
        authuser = authenticate(username=req.POST['username'], password=req.POST['password'])
        print(authuser)
        if (u[0] is not None and authuser is not None):
            req.session['userid'] = u[0].id
            req.session['username'] = u[0].username
            login(req, authuser)
            return HttpResponseRedirect('/home')
        else:
            context = {}
            context['error'] = 'username or password wong'
            return render(req, 'login.html', context)

def login1(req):
    if (req.method == 'GET'):
        return render(req, 'login.html')
    else:
        u = MyUser.objects.filter(username=req.POST['username'], password=req.POST['password'])
        authuser=authenticate(username=req.POST['username'],password=req.POST['password'])
        print(authuser)
        if (u[0] is not None and authuser is not None):
            req.session['userid'] = u[0].id
            req.session['username'] = u[0].username
            login(req,authuser)
            return HttpResponseRedirect('/home')
        else:
            context = {}
            context['error'] = 'username or password wong'
            return render(req, 'login.html', context)

@require_http_methods(['GET'])
def logout1(request):
    request.session.clear()
    return HttpResponseRedirect('/home')


def register1(req):
    if(req.method=='POST'):
        x=MyUser.objects.create(
            username=req.POST['username'],
            password=req.POST['password'],
            email=req.POST['email']
        )
        User.objects.create_superuser(username=req.POST['username']
                                      , password=req.POST['password'],

                                      email=req.POST['email'])
        req.session['username'] = x.username
        req.session['email'] = x.email
        context ={
            'username' : x.username
        }
        return render(req, 'index.html',context)
    else:
        return render(req, 'register.html')
