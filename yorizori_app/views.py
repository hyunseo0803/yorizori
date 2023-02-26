from itertools import count
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
    recipe= Recipe.objects.all().values()
    return render(request, 'home.html', {"recipe": recipe})


def login(request):  # 로그인 기능
    global memberinfo
    if request.method == "POST":
        u_id = request.POST.get('id')  # 사용자 입력 아이디=id
        u_password = request.POST.get('password')  # 사용자 입력 패스워드=password
        if MemberInfo.objects.filter(id=u_id).exists():
            memberinfo = MemberInfo.objects.get(id=u_id)
            if memberinfo.password == u_password:
                request.session['id'] = memberinfo.id
                return render(request, 'home2.html', {'user_is': memberinfo})
        else:
            res_data['error'] = '아이디 또는 비밀번호가 일치하지 않습니다.'
    return render(request, 'login.html', res_data)


def logout(request):
    request.session.flush()
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


def editmember(request, id):  # 회원정보 수정
    if request.method == "POST":
        print(id)
        member = MemberInfo.objects.get(id=id)
        print(member.id)
        print(member.password)
        print(member.email)
        # member.id = request.POST['id']
        member.password = request.POST['password']
        member.email = request.POST['email']
        member.save()
        return redirect("/home2/")
    else:
        member = MemberInfo()
        return render(request, 'EditMember.html', {'id': request.session['id']})


def Upload(request):
    global upload
    global memberinfo
    global source
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
        try:
            upload.img_url = request.FILES['image']
        except:
            pass
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
        return redirect('/MyRecipe/', {'recipe': recipe})
    else:
        recipe_a = Recipe.objects.get(recipe_id=recipe_id)
        return render(request, 'update.html', {'recipe': recipe_a})


def Delete(request, recipe_id):
    recipe = Recipe.objects.get(recipe_id=recipe_id)
    recipe.delete()
    return redirect("/MyRecipe/", {"request": request})


def MyRecipe(request):
    recipe = Recipe.objects.filter(id=request.session['id']).values()
    context = {'recipe': recipe}

    return render(request, 'MyRecipe.html', context)


crolw_ = []


def addSource(request):
    global recipe_c
    global crolw_
    global s
    global c
    if request.method == "GET":
        return render(request, 'addSource.html')
    elif request.method == "POST":
        mylist = request.POST.get("mylist")
        new_mylist = mylist.replace('"', '').replace(
            '[', '').replace(']', '').replace(',', '')
        print(new_mylist)
        url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=" + \
            new_mylist + "요리"
        print("생성url: ", url)
        # ConnectionError방지
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/100.0.48496.75"}
        original_html = requests.get(url, headers=headers)
        html = BeautifulSoup(original_html.text, "html.parser")
        # 검색결과
        articles = html.select(
            "div._list> panel-list >div._panel>more-contents>div._more_contents_event_base>ul.lst_total>li.bx>div.total_wrap>div.total_area>a")
        #main_pack > section > div > div._list > panel-list > div > more-contents > div > ul
        # main_pack > section > div > div._list > panel-list > div:nth-child(1) > more-contents > div > ul
        # print(f"articel: ============================{articles}")

        articles_img = html.select(
            "div._list > panel-list > div > more-contents > div > ul > li > div.total_wrap > div > div.api_pcpg_wrap._freescroll_wrap > div.api_flicking_wrap.review_thumb_group._svp_content._freescroll_flicking > div:nth-child(1) > a > img")
        # print(f"img:======================={articles_img}")
        # 제목 가져오기
        title = []
        blog_content = []

        t = html.find_all("a", {"class": "api_txt_lines"})
        for j in t:
            title.append(j.get_text())

        # 컨텐츠 가져오기
        c = html.find_all("a", {"class": "total_dsc _cross_trigger"})
        for i in c:
            blog_content.append(
                i.find("div", {"class": "api_txt_lines"}).get_text())

        # URL 가져오기
        url = []
        for i in articles:
            url.append(i.attrs['href'])

        img = []
        for i in articles_img:
            img.append(i.attrs['src'])
        # print(img)

        # title,info zip()내장함수로 리스트 합치기
        crolw = zip(title, blog_content, url, img)
        crolw_ = []
        crolw_ = list(crolw)

        # 반복문으로 title, info db에 insert
        # for t,c in crolw_:
        #     recipe_=AdminRecipe()
        #     recipe_.title=t
        #     recipe_.info=c
        #     recipe_.save()
        # db데이터 꺼내오기
        # recipe_c=AdminRecipe.objects.all()
        s = mylist.replace('"', '').replace('[', '').replace(']', '')
        n_s = s.split(',')
        for i in n_s:
            temp = Recipe.objects.all().filter(source__contains=i).values()
        c.clear()
        for i in temp:
            if len(set.intersection(set(map(lambda x: x.strip(), i["source"].split(','))), set(n_s))) > 0:
                c.append(i)
                print(c)
        return redirect("/search/", {"request": request})


def search(request):
    # print("테스트으으입니다")
    global crolw_
    global c
    return render(request, 'search.html', {"recipe_c": crolw_, "c": c})


def contents(request, recipe_id):
    global c
    content = Recipe.objects.filter(recipe_id=recipe_id).values()
    context = {"content": content}
    return render(request, 'contents.html', context)


def home2(request):
    recipe= Recipe.objects.all().values()
    request.session['id'] = memberinfo.id
    return render(request, 'home2.html', {"recipe": recipe})
