from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

def redirect_to_threads(request):
    return redirect('thread_list')

def thread_list(request):
    threads = Thread.objects.all()
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            thread_form.save()
            return redirect('thread_list')
    else:
        thread_form = ThreadForm()

    return render(request, 'post/thread_list.html', {'threads': threads, 'thread_form': thread_form})

def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = thread.posts.all()

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=id)
    else:
        post_form = PostForm()

    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'post_form': post_form})

def delete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()

    return redirect('thread_list')

def edit_thread(request, id):
    thread =get_object_or_404(Thread, id=id)

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=id)
    else:
        form = ThreadForm(instance=thread)

    return render(request, 'post/edit_thread.html', {'form': form})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()

    return redirect('thread_detail', id=thread_id)

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'post/edit_post.html', {'form': form})