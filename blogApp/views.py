from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Post
from.forms import PostEdit
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    '''This function shows all post in the home page'''
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'blogApp/home.html', context)


@login_required(login_url='/login')
def postDetail(request, id):
    '''This function gets the specific detail of a specific post'''
    posts = Post.objects.get(pk=id)
    context = {
        'posts':posts
    }
    return render(request, 'blogApp/post_detail.html', context)


def postCreate(request):
    '''This function allows the user to create a new post'''
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image-file')
        Post.objects.create(
            author = request.user,
            title = data['title'],
            content = data['content'],
            image = image
        )
        return redirect('home')
    return render(request, 'blogApp/post_create.html')


def postUpdate(request, id):
    '''This function updates the post of a specific user.'''
    post = Post.objects.get(pk=id)
    form = PostEdit(instance=post)

    if request.method == 'POST':
        form = PostEdit(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Successfull')
            return redirect('home')
        else:
            form = PostEdit(instance=post)
    context = {'form': form}
    return render(request, 'blogApp/post_update.html', context)



def postDelete(request, id):
    '''This function deletes specific post for users.'''
    posts = Post.objects.get(pk=id)

    if request.user != posts.author:
        return HttpResponse('<h3> Hey! You are not allowed here')
    if request.method == 'POST':
        posts.delete()
        return redirect('home')
    return render(request, 'blogApp/post_delete.html')