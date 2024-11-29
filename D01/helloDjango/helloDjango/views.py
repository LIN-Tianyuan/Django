from django.http import HttpResponse

def hello(request):

    return HttpResponse('<p><a href="/article/18.html">Root relative path</a></p><p><a href="article/19.html">Relative path (inaccessible)</a></p>',content_type="text/html;charset=utf-8",status=200)
   
def article(request,id):
    print(id)
    print(type(id))
    return HttpResponse(f"Details of Article No. {id}")
 
def user(request,username):
    return HttpResponse(f"username is: {username}")
    
    
def detail(request,path):
    return HttpResponse(f"path is: {path}")
    
def uuid(request,id):
    return HttpResponse(f"uuid is: {id}")
    
def search(request,year,month,day):
    return HttpResponse(f"This is : {year}-{month}-{day} news list")
    
def index(request):
    html = '''
        <html>
        <head>
        <title>Django Route</title>
        <style>
        ul,ol{
        list-style:none;
        }
        li{
        line-height:2em;
        }
        a{
        color:#900;
        text-decoration:none;
        }
        </style>
        </head>
        <body>
        <ul>
        <li><a href="/hello">hello</a></li>
        <li><a href="/article/12.html">Article Details</a></li>
        <li><a href="/user/alex">User information</a></li>
        <li><a href="/book/12345678-1234-1234-1234-012345678901">uuid</a></li>
        <li><a href="/search/2023/7/20">Check year, month and day news</a></li>
        </ul>
        </body>
        </html>
    '''
    return HttpResponse(html)
