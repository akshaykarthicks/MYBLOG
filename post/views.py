from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_http_methods
from .models import Post
# Create your views here.
def index(request):
    posts=Post.objects.all()#this is used to get all the posts from the database
    return render(request, 'index.html', {'posts':posts}) #passing the posts to the template

def post(request, pk): #passing the post id to the post view for diff post
    posts=Post.objects.get(id=pk) #this is used to get the post from the database
    return render(request, 'posts.html', {'posts':posts}) #passing the post to the template

@require_http_methods(["GET", "POST"]) #this is used to check if the request is a post or get request
def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        
        if title and body:
            post = Post.objects.create(
                title=title,
                body=body
            )
            return redirect('index')
    
    return render(request, 'create_post.html')