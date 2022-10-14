import re
from sqlite3 import IntegrityError
from django.shortcuts import render,redirect
from urllib import request
from .models import *
from django.contrib.auth.hashers import check_password

sl=[]

def index(request):
    return render(request, 'search.html')

def login(Request,id):  #로그인 기능
    if request.method == "GET":
        return render(request, 'views/login.html') 
    elif request.method == "POST":
        id=request.POST.get('id')   #사용자 입력 아이디=id
        password=request.POST.get('password')   #사용자 입력 패스워드=password  
        
        res_data={}   #유효성 처리 
        memberinfo=MemberInfo.objects.get(id=id) #MemberInfo 테이블의 id와 사용자 아이디 입력 id 일치하는 것 가져오기
        if check_password(password, memberinfo.password): #패스워드 확인 
            request.session['id']=memberinfo.id    #세션 유지 처리 
            
            return  redirect('/')   #index 로 리다이렉트
        else:
            res_data['error']="비밀번호가 틀립니다." #에러 처리 
        
def logout(request):
    logout(request)
    return render(request, 'index2.html')

def singup(request):
    if request.method == 'POST':
        id=request.POST.get('id')   #사용자 입력
        password=request.POST.get('password')  
        email=request.POST.get('email')
        
        try:
            memberInfo=MemberInfo.objects.get(id,password,email)
            memberInfo.save()
        except IntegrityError:
            return render(
                request,'singup.html',{"massage":"Id already taken."}
                
            )
        login(request,memberInfo)
        return render(request,'login.html')
            
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
    