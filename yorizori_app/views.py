from aifc import Error
import email
from django.shortcuts import render,redirect
from urllib import request
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib import auth 
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

memberinfo=MemberInfo()
sl=[]
res_data={}

def index(request):
    return render(request, 'home.html' )

def login(request):  #로그인 기능
    global memberinfo
    if request.method == "POST":
        u_id=request.POST.get('id')   #사용자 입력 아이디=id
        u_password=request.POST.get('password')#사용자 입력 패스워드=password  
        if MemberInfo.objects.filter(id=u_id).exists():
            memberinfo = MemberInfo.objects.get(id = u_id)
            if memberinfo.password==u_password:
                request.session['id'] = memberinfo.id
                return render(request,'home2.html', context={'user_is':memberinfo})
        else:
            res_data['error'] = '아이디 또는 비밀번호가 일치하지 않습니다.'
    return render(request,'login.html',res_data) 

        
def logout(request):
    logout(request)
    return render(request, 'home.html')

def singUp(request):
    global memberinfo
    if request.method == "POST":
        id=request.POST.get('id')   #사용자 입력 아이디=id
        password=request.POST.get('password')#사용자 입력 패스워드=password  
        email=request.POST.get('email')
        
        memberinfo=MemberInfo()
        memberinfo.id=id 
        memberinfo.password=password
        memberinfo.email=email
        memberinfo.save()
    return render(request, 'singUp.html')
            
def Mupdate(request):  #회원정보 수정
    if request.method == 'GET':
        return render(request, 'update.html')

    elif request.method == 'POST':
        user = request.user

        id = request.POST.get('id')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        exist_id= MemberInfo.objects.filter(id=id)

        #유저의 닉네임과 같다면 그대로 저장 필터에 걸린다면 리턴 = 유저닉네임과 입력닉네임이 같아도 저장,
            
        if exist_id and MemberInfo.id == id:
            MemberInfo.id = id
            MemberInfo.password = password
            MemberInfo.email = email
            MemberInfo.save()
            return redirect('/', MemberInfo.id)
        
        elif exist_id and MemberInfo.id != id:
            return render(request, 'update.html', {'error': '이미 사용중인 아이디 입니다.'})
        
        else:
            MemberInfo.id = id
            MemberInfo.password = password
            MemberInfo.email = email
            MemberInfo.save()
            return redirect('/', MemberInfo.id)
        
def upload(request):
    if request.method == "GET":
        return render(request, 'views/index2.html') 
    elif request.method == "POST":
        title=request.POST.get('title')   #사용자 입력
        info=request.POST.get('info')   
        source=request.POST.get('source')
        ex=request.POST.get('ex')
        
        recipeUpload=Recipe.objects.get(title,info,source,ex) #Recipe 테이블
        recipeUpload.save()
        
        return render(request,'repository.html')
    
    
def addSource(request):
    return render(request,'addSource.html')

def search(request):
    return render(request,'search.html')

def home2(request):
    return render(request,'home2.html')


# def login(request):
#     return render(request,'login.html')


# def register(request):
#     return render(request,'register.html')

    
    