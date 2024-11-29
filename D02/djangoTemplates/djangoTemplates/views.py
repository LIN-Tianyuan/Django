from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def variable(request):
    username = 'Tom'
    age = 23
    sex = True
    score = {
        'chinese': 128,
        'math': 149,
        'english': 122
    }
    friends = ['John', 'Rose', 'Tom']
    return render(request, 'variable.html', locals())


def forloop(request):
    books = [
        {
            'id': 5,
            'bookname': '孙子兵法大全集（超值金版）',
            'price': 18.4,
            'publishing': '新世界出版社',
            'category': '历史'
        },
        {
            'id': 11,
            'bookname': '甲骨文丛书·拿破仑大帝(全2册) ',
            'price': 119.5,
            'publishing': '中信出版集团',
            'category': '传记'
        },
        {
            'id': 22,
            'bookname': 'JavaScript DOM编程艺术（第2版）',
            'price': 42.70,
            'publishing': '人民邮电出版社',
            'category': '计算机'
        },
        {
            'id': 23,
            'bookname': '精通iOS开发 第8版',
            'price': 102.20,
            'publishing': '人民邮电出版社',
            'category': '计算机'
        },
        {
            'id': 26,
            'bookname': 'UNIX网络编程 卷1 套接字联网API（第3版）',
            'price': 102.9,
            'publishing': '人民邮电出版社',
            'category': '计算机'
        },
        {
            'id': 31,
            'bookname': '曾国藩的正面与侧面：1+2（套装共两册）',
            'price': 59.30,
            'publishing': '岳麓书社',
            'category': '传记'
        },
        {
            'id': 40,
            'bookname': '普京传：不可替代的俄罗斯硬汉 [Mr.Putin: Operative In The Kremlin]  ',
            'price': 39,
            'publishing': '红旗出版社',
            'category': '传记'
        },
    ]

    students = [
        {
            'name': '王伟',
            'age': 21,
            'sex': True,
            'education': 3
        },
        {
            'name': '张敏',
            'age': 19,
            'sex': False,
            'education': 4
        },
        {
            'name': '李静',
            'age': 22,
            'sex': False,
            'education': 3
        },
        {
            'name': '李强',
            'age': 22,
            'sex': True,
            'education': 1
        },
        {
            'name': '王磊',
            'age': 25,
            'sex': True,
            'education': 5
        },
        {
            'name': '李娟',
            'age': 23,
            'sex': False,
            'education': 2
        },
    ]

    context = {
        'books': books,
        'students': students
    }
    return render(request, 'forloop.html', context)


def delete_book(request, id):
    return HttpResponse(f"{id} delete.")


def get_book(request, id):
    return HttpResponse(f"{id} get.")


def ifcond(request):
    students = [
        {
            'name': '王伟',
            'age': 21,
            'sex': True,
            'education': 3
        },
        {
            'name': '张敏',
            'age': 19,
            'sex': False,
            'education': 4
        },
        {
            'name': '李静',
            'age': 22,
            'sex': False,
            'education': 3
        },
        {
            'name': '李强',
            'age': 22,
            'sex': True,
            'education': 1
        },
        {
            'name': '王磊',
            'age': 25,
            'sex': True,
            'education': 5
        },
        {
            'name': '李娟',
            'age': 23,
            'sex': False,
            'education': 2
        },
    ]
    return render(request, 'ifcond.html', locals())


def filter(request):
    html = '''
    This is a recap of the HTML content you learned today:
Heading 1 with <h1>... </h1> to indicate
Paragraphs are denoted by <p>... </p>.
    '''
    link = '<p><a href="http://www.baidu.com">Baidu</a></p>'

    content = 'In this article, you learned how to use Python to interact with Freshdesk to fetch, create, and update tickets. You also learned how to use a webhook with Freshdesk to get real-time updates of when changes occur on Freshdesk tickets.If you need to build and maintain several integrations, you can build one integration with Merge and connect with hundreds of platforms—including Freshdesk, Zendesk, and Salesforce Service Cloud—through a Helpdesk and Ticketing Unified API. Instead of building and maintaining integrations with various tools and services, Merge allows you to easily implement new technologies and stay up-to-date with industry trends, all while staying focused on your core operations.Learn more about Merge by scheduling a demo with one of our integration experts.'
    return render(request, 'filter.html', locals())


def register(request):
    return render(request, 'register.html')
