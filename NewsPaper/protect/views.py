from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import Post,Author
@login_required
def dashboard_view(request):
    try: author=Author.objects.get(authorUser=request.user)
    except Author.DoesNotExist: return render(request,'protect/dashboard.html',{'error':'Вы не являетесь автором'})
    posts=Post.objects.filter(author=author).order_by('-dateCreation')
    return render(request,'protect/dashboard.html',{'posts':posts,'author':author})
