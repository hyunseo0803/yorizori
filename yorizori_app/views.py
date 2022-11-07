from multiprocessing import context
from django.shortcuts import render, redirect
from urllib import request
from .models import MemberInfo, Recipe
from bs4 import BeautifulSoup
import requests


memberinfo = MemberInfo()
upload = Recipe()
sl = []
res_data = {}


def index(request):
    return render(request, 'home.html')


def login(request):  # 로그인 기능
    global memberinfo
    if request.method == "POST":
        u_id = request.POST.get('id')  # 사용자 입력 아이디=id
        u_password = request.POST.get('password')  # 사용자 입력 패스워드=password
        if MemberInfo.objects.filter(id=u_id).exists():
            memberinfo = MemberInfo.objects.get(id=u_id)
            if memberinfo.password == u_password:
                request.session['id'] = memberinfo.id
                return render(request, 'home2.html', context={'user_is': memberinfo})
        else:
            res_data['error'] = '아이디 또는 비밀번호가 일치하지 않습니다.'
    return render(request, 'login.html', res_data)


def logout(request):
    logout(request)
    return render(request, 'home.html')


def singUp(request):
    global memberinfo
    if request.method == "POST":
        id = request.POST.get('id')  # 사용자 입력 아이디=id
        password = request.POST.get('password')  # 사용자 입력 패스워드=password
        email = request.POST.get('email')

        memberinfo = MemberInfo()
        memberinfo.id = id
        memberinfo.password = password
        memberinfo.email = email
        memberinfo.save()
    return render(request, 'singUp.html')


def Mrecipe(request):  # 회원정보 수정
    if request.method == 'GET':
        return render(request, 'recipe.html')

    elif request.method == 'POST':
        user = request.user

        id = request.POST.get('id')
        password = request.POST.get('password')
        email = request.POST.get('email')

        exist_id = MemberInfo.objects.filter(id=id)

        # 유저의 닉네임과 같다면 그대로 저장 필터에 걸린다면 리턴 = 유저닉네임과 입력닉네임이 같아도 저장,

        if exist_id and MemberInfo.id == id:
            MemberInfo.id = id
            MemberInfo.password = password
            MemberInfo.email = email
            MemberInfo.save()
            return redirect('/', MemberInfo.id)

        elif exist_id and MemberInfo.id != id:
            return render(request, 'recipe.html', {'error': '이미 사용중인 아이디 입니다.'})

        else:
            MemberInfo.id = id
            MemberInfo.password = password
            MemberInfo.email = email
            MemberInfo.save()
            return redirect('/', MemberInfo.id)


def Upload(request):
    global upload
    global memberinfo
    if request.method == "POST":
        memberinfo = MemberInfo()
        n_id = MemberInfo.objects.get(id=request.session['id'])
        # request.session['id'] = memberinfo.id
        # n_id=memberinfo.id
        title = request.POST.get('title')  # 사용자 입력
        info = request.POST.get('info')
        source = request.POST.get('source')
        ex = request.POST.get('ex')

        upload = Recipe()

        upload.id = n_id
        upload.title = title
        upload.info = info
        upload.source = source
        upload.ex = ex
        upload.save()
        return redirect("../MyRecipe/", request=request)
    return render(request, 'upload.html')


def Edit(request, recipe_id):
    if request.method == "POST":
        recipe = Recipe.objects.get(recipe_id=recipe_id)
        recipe.title = request.POST['title']
        recipe.info = request.POST['info']
        recipe.source = request.POST['source']
        recipe.ex = request.POST['ex']
        recipe.save()
        return redirect('/MyRecipe/',{'recipe':recipe})
    else:
        recipe = Recipe()
        return render(request, 'update.html', {'recipe': recipe})


def Delete(request, recipe_id):
    recipe = Recipe.objects.get(recipe_id=recipe_id)
    recipe.delete()
    return redirect("/MyRecipe/", {"request":request})



def MyRecipe(request):
    recipe = Recipe.objects.filter(id=request.session['id']).values()
    context = {'recipe': recipe}

    return render(request, 'MyRecipe.html', context)


def addSource(request):
    if request.method == "POST":
    # s=request.GET.get('s')
    # url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=" + s
    # print("생성url: ",url)
    # # ConnectionError방지
    # headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75" }
    # original_html = requests.get(url, headers=headers)
    # html = BeautifulSoup(original_html.text, "html.parser")
    # # 검색결과
    # articles = html.select("div._list > ul.lst_total _list_base > li div.total_area > a")
    # print(articles)
    # #제목 가져오기
    # title = []
    # for i in articles:
    #     title.append(i.attrs['title'])

    # #뉴스기사 URL 가져오기
    # url = []
    # for i in articles:
    #     url.append(i.attrs['href'])

    # #뉴스기사 내용 크롤링하기
    # contents = []
    # for i in url:
    #     #각 기사 html get하기
    #     cRecipe = requests.get(i)
    #     html = BeautifulSoup(cRecipe.text,"html.parser")
    #     #내용 가져오기 (p태그의 내용 모두 가져오기) 
    #     contents.append(html.find_all('p'))

        return redirect("/search/")
    return render(request,'addSource.html')


def search(request):
    return render(request, 'search.html')


def home2(request):
    return render(request, 'home2.html')


