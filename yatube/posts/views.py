from posts.models import comment
from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')
def about(request):
    return render(request, 'posts/about.html')
comments=[
    {'author':'Иван Петрович','date':'2.11.24;15:24','text':'все проверил, спасибо'},
    {'author': 'Иван Иванов', 'date': '01-12-2023', 'text': 'Отличная статья!'},
    {'author': 'Петр Петров 2', 'date': '02-12-2023', 'text': 'Спасибо за полезную информацию.'},
    {'author': 'Анна Сидорова', 'date': '03-12-2023', 'text': 'Очень понравилось! Буду ждать новых статей.'}
]
context = {'comments': comments}
def posts(request):
    comments=comment.objects.all()
    print(comments[0].author)
    return render(request, 'posts/posts.html',context={'comments': comments})
def register(request):
    return render(request, 'posts/register.html')
def login(request):
    return render(request, 'posts/login.html')