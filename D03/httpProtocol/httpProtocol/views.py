from django.shortcuts import render
from django.http import HttpResponseRedirect


def redirect(request):
    return HttpResponseRedirect('http://www.baidu.com')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        love = request.POST.getlist('love')
        provinces = request.POST.getlist('provinces')
        return render(request, 'registerinfo.html', locals())


def link(request):
    username = request.GET.get('username')
    age = request.GET.get('age')
    return render(request, 'link.html', locals())


def search(request):
    print(request.GET.get('keywords'))
    print(request.GET.get('category'))
    return render(request, 'search.html')


def index(request):
    products = [
        {
            'id': 455,
            'price': 5566.69,
            'name': 'Huawei 5',
            'image': '5.jpg'
        },
        {
            'id': 5899,
            'price': 7788.89,
            'name': 'Huawei 6',
            'image': '6.jpg'
        }
    ]
    return render(request, 'index.html', locals())