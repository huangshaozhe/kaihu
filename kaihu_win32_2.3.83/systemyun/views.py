from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
import requests
from systemyun import models
from django.forms.models import model_to_dict

# Create your views here.
def hello(request):

    return render(request,'home.html')
    #return render(request,'dddd.html')

def forgot(request):
    import os
    if request.method == 'POST':
        account = request.POST['username']
        password = request.POST['password']
        pin = request.POST["pin"]
        for looper in account:
            if looper == ' ':
                return render(request, 'error.html')
            else :
                continue
        for looper in password:
            if looper == ' ':
                return render(request, 'error.html')
            else :
                continue
        for looper in pin:
            if looper == ' ':
                return render(request, 'error.html')
            else :
                continue
        user_list = models.Account.objects.all()
        print(user_list)
        for row in user_list:
            if row.name == name:
                return render(request, 'error.html')
            else:
                continue
        
        models.Account.objects.create(name=name)
        models.Account.objects.create(password=password)
        models.Account.objects.create(pin = pin)
        

def add_account(request):
    import os
    if request.method == 'POST': 
        name = request.POST['username']
        password=request.POST['password']
        for looper in name:
            if looper == ' ':
                return render(request, 'error.html')
            elif looper == '。':
                return render(request, 'error.html')
            elif looper == '。':
                return render(request, 'error.html')
            elif looper == '\\':
                return render(request, 'error.html')
            elif looper == '/':
                return render(request, 'error.html')
            elif looper == '"':
                return render(request, 'error.html')
            elif looper == '[':
                return render(request, 'error.html')
            elif looper == ']':
                return render(request, 'error.html')
            elif looper == ':':
                return render(request, 'error.html')
            elif looper == '|':
                return render(request, 'error.html')
            elif looper == '<':
                return render(request, 'error.html')
            elif looper == '>':
                return render(request, 'error.html')
            elif looper == '+':
                return render(request, 'error.html')
            elif looper == '=':
                return render(request, 'error.html')
            elif looper == ';':
                return render(request, 'error.html')
            elif looper == ',':
                return render(request, 'error.html')
            elif looper == '?':
                return render(request, 'error.html')
            elif looper == '*':
                return render(request, 'error.html')
            elif looper == '@':
                return render(request, 'error.html')
            else:
                continue
        for passwd in password:
            if passwd == ' ':
                return render(request, 'error.html')
            else:
                continue
        pin = request.POST["pin"]
        for looper in pin:
            if looper == ' ':
                return render(request, 'error.html')
            else:
                continue
        user_list = models.Account.objects.all()
        print(user_list)
        for row in user_list:
            if row.name == name:
                return render(request, 'error.html')
            else:
                continue
        models.Account.objects.create(name=name,password=password,pin=pin)
        user_list = models.Account.objects.all()
        print(user_list)
        os.system(f'net user {name} {password} /add')
        return render(request, 'ok.html')
    else:
        return render(request, 'index.html')

def del_account(request):
    import os
    if request.method == 'POST': 
        name = request.POST['username']
        password=request.POST['password']
        for looper in name:
            if looper == ' ':
                return render(request, 'error_del.html')
            elif looper == '。':
                return render(request, 'error_del.html')
            elif looper == '。':
                return render(request, 'error_del.html')
            elif looper == '\\':
                return render(request, 'error_del.html')
            elif looper == '/':
                return render(request, 'error_del.html')
            elif looper == '"':
                return render(request, 'error_del.html')
            elif looper == '[':
                return render(request, 'error_del.html')
            elif looper == ']':
                return render(request, 'error_del.html')
            elif looper == ':':
                return render(request, 'error_del.html')
            elif looper == '|':
                return render(request, 'error_del.html')
            elif looper == '<':
                return render(request, 'error_del.html')
            elif looper == '>':
                return render(request, 'error_del.html')
            elif looper == '+':
                return render(request, 'error_del.html')
            elif looper == '=':
                return render(request, 'error_del.html')
            elif looper == ';':
                return render(request, 'error_del.html')
            elif looper == ',':
                return render(request, 'error_del.html')
            elif looper == '?':
                return render(request, 'error_del.html')
            elif looper == '*':
                return render(request, 'error_del.html')
            elif looper == '@':
                return render(request, 'error_del.html')
            else:
                continue
        for passwd in password:
            if passwd == ' ':
                return render(request, 'error_del.html')
            else:
                continue
        pin = request.POST["pin"]
        for looper in pin:
            if looper == ' ':
                return render(request, 'error_del.html')
            else:
                continue
        userssss = models.Account.objects.get(name=name)
        users = model_to_dict(userssss)
        print(users)
        if users['password'] == str(password):
            if users['pin'] == str(pin):
                models.Account.objects.filter(name=f"{name}").delete()
                os.system(f'net user {name} /del')
                return render(request, 'ok_del.html')
            else:
                return render(request, 'error_del.html')
        else:
            return render(request, 'error_del.html')
    else:
        return render(request, 'del_account.html')


def revise(request):
    return render(request, 'revise.html')

def purchase_admin(request):
    return render(request, 'purchase_admin.html')

def donate(request):
    return render(request, 'donate.html')

def human_services(request):
    return render(request, 'human_services.html')

def db_handle(request):
    user_list_obj = models.Demo.objects.all()
    return render(request, 't1.html', {'li': user_list_obj})

def login(request):
    if request.method == 'POST':
        #获取数据 
        account = request.POST['name']
        password=request.POST['password']
        user_list = models.UserIfo.objects.all()
        #print(user_list)
        for row in user_list:
            if row.name ==  account:
                if row.password == password:
                    """设置cookie"""
                    response = HttpResponse("设置cookie")
                    ''' max_age 设置过期时间，单位是秒 '''
                    # response.set_cookie('name', 'tong', max_age=14 * 24 * 3600)
                    ''' expires 设置过期时间，是从现在的时间开始到那个时间结束 '''
                    response.set_cookie(name, password, expires=datetime.now()+timedelta(days=14))
                    return response
                else:
                    return render(request, 'login.html')
            else:
                continue
    else:
        return render(request, 'login.html')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'sign-up.html')
    else:
        name = request.POST['name']
        password = request.POST['password']
        rePassword = request.POST['rePassword']
        if password == rePassword:
            user_list = models.UserIfo.objects.all()
            #print(user_list)
            for row in user_list:
    #通过关联ut字段取关联表----正向操作
                if row.name == name:
                    return HttpResponse('名称已被占用')
                else:
                    continue
            else:
                models.UserType.objects.create(name=name)
                models.UserType.objects.create(password=password)
                """设置cookie"""
                response = HttpResponse("设置cookie")
                ''' max_age 设置过期时间，单位是秒 '''
                # response.set_cookie('name', 'tong', max_age=14 * 24 * 3600)
                ''' expires 设置过期时间，是从现在的时间开始到那个时间结束 '''
                response.set_cookie(name, password, expires=datetime.now()+timedelta(days=14))
                return response

