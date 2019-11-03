from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Blog
from .models import Comment
from time import strftime
from django.http import HttpResponseRedirect
import random
from django.urls import reverse

def index(request):
    latest_post_list = Blog.objects.order_by('-posted_date')[:3]
    comments = {}
    for b in latest_post_list:
        b.commentNumber = Comment.objects.filter(blog=b).count()
    currtime = strftime("%h %d, %Y, %I:%M:%S %Z")
    context = {'latest_post_list':latest_post_list,
               'time':currtime}
    return render(request, 'blog/index.html', context)

def bio(request):
    currtime = strftime("%h %d, %Y, %I:%M:%S %Z")
    context = {'time':currtime,}
    return render(request, 'blog/bio.html', context)
    
def tech(request):
    currtime = strftime("%h %d, %Y, %I:%M:%S %Z")
    context = {'time':currtime,}
    return render(request, 'blog/tech.html', context)
    
def detail(request, blog_id):
    currtime = strftime("%h %d, %Y, %I:%M:%S %Z")
    try:
        post = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    post.comments = Comment.objects.filter(blog=blog_id).order_by('-posted_date')
    context = {'time':currtime,
               'post':post,}
    return render(request, 'blog/detail.html', context)

def comments(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    c = Comment()
    c.author_nickname = request.POST.get("author_nickname")
    c.email = request.POST.get("email")
    c.content = request.POST.get("content")
    c.posted_date = strftime("%Y-%m-%d %H:%M:%S")
    c.blog_id = blog_id
    c.save()   
    return HttpResponseRedirect(reverse('blog:detail',args=(blog.id,)))

def blogArchive(request):
    latest_post_list = Blog.objects.order_by('-posted_date')
    for b in latest_post_list:
        b.commentNumber = Comment.objects.filter(blog=b).count()
    currtime = strftime("%h %d, %Y, %I:%M:%S %Z")
    context = {'latest_post_list':latest_post_list,
               'time':currtime}
    return render(request, 'blog/blogArchive.html', context)

def nuke(request):
    for b in Blog.objects.all():
        b.delete()
    return HttpResponseRedirect('/blog/')

def init(request):
    nuke(request)
    for i in range(0,10):
        b=Blog()
        b.title = 'Post number ' + str(i)
        b.author = 'Bob ' + str(i)
        b.posted_date = strftime("%Y-%m-%d %H:%M:%S")
        b.content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sed lorem eget diam tristique tempor. Vivamus in purus eu orci placerat fermentum. Aenean non placerat diam, id commodo ante. Aenean sagittis velit a nulla tristique, at suscipit nisl consectetur. Donec consectetur, arcu id tempus ullamcorper, est massa laoreet eros, in ornare ipsum purus in quam. Praesent nec dolor non nibh mollis pharetra eget ut nisl. Sed convallis convallis felis pulvinar viverra. Aliquam sed sem turpis. Quisque consectetur molestie aliquam. Cras lacinia vitae sem nec fermentum. Proin finibus leo in venenatis venenatis. Phasellus fringilla, lacus rhoncus porttitor mollis, orci felis facilisis mauris, id tempus libero nisi id erat.Etiam vitae egestas massa. Aenean pulvinar sit amet mi id porttitor. Quisque purus ipsum, fermentum quis augue in, accumsan varius ipsum. Fusce velit metus, congue et lacinia ut, molestie ac est. Ut non nisi id mauris lacinia aliquam. Morbi nec ex lorem. Sed placerat a magna sit amet fermentum. Duis malesuada et nisi eu semper. Donec ornare, mauris sit amet imperdiet mattis, mi leo imperdiet sapien, nec faucibus eros elit a nibh.Nam porta feugiat magna, sit amet varius orci scelerisque quis. Praesent ac sodales ante. Proin blandit porta nibh, vel varius est sollicitudin vel. Donec sollicitudin aliquam metus sit amet finibus. Sed urna nunc, tristique ut tellus id, volutpat lacinia diam. Nunc dignissim ex quis purus congue, sit amet aliquet turpis tincidunt. Pellentesque tempor gravida ligula, ac lobortis orci malesuada a. Vivamus gravida massa neque, eu consequat sapien eleifend a. Vivamus pulvinar tortor ex, ac placerat arcu consequat ut. Donec aliquam urna ut eros vestibulum pharetra. Proin molestie tortor vitae mauris consequat ultricies. Cras est ante, accumsan in varius sit amet, pellentesque quis enim. Donec lacinia interdum purus a pellentesque. Maecenas non risus dolor. Vestibulum eget molestie tortor. Morbi condimentum venenatis felis."
        b.save()
        for j in range(1, random.randint(3,10)):
            c=Comment()
            c.author_nickname = 'Jack' + str(j)
            c.email = 'email' + str(j) + '@gmail.com'
            c.posted_date = strftime("%Y-%m-%-d %H:%M:%S")
            c.blog = b
            c.content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sed lorem eget diam tristique tempor. Vivamus in purus eu orci placerat fermentum. Aenean non placerat diam, id commodo ante. Aenean sagittis velit a nulla tristique, at suscipit nisl consectetur. Donec consectetur, arcu id tempus ullamcorper, est massa laoreet eros, in ornare ipsum purus in quam. Praesent nec dolor non nibh mollis pharetra eget ut nisl. Sed convallis convallis felis pulvinar viverra. Aliquam sed sem turpis. Quisque consectetur molestie aliquam. Cras lacinia vitae sem nec fermentum. Proin finibus leo in venenatis venenatis. Phasellus fringilla, lacus rhoncus porttitor mollis, orci felis facilisis mauris, id tempus libero nisi id erat.Etiam vitae egestas massa. Aenean pulvinar sit amet mi id porttitor. Quisque purus ipsum, fermentum quis augue in, accumsan varius ipsum. Fusce velit metus, congue et lacinia ut, molestie ac est. Ut non nisi id mauris lacinia aliquam. Morbi nec ex lorem. Sed placerat a magna sit amet fermentum. Duis malesuada et nisi eu semper. Donec ornare, mauris sit amet imperdiet mattis, mi leo imperdiet sapien, nec faucibus eros elit a nibh.Nam porta feugiat magna, sit amet varius orci scelerisque quis. Praesent ac sodales ante. Proin blandit porta nibh, vel varius est sollicitudin vel. Donec sollicitudin aliquam metus sit amet finibus. Sed urna nunc, tristique ut tellus id, volutpat lacinia diam. Nunc dignissim ex quis purus congue, sit amet aliquet turpis tincidunt. Pellentesque tempor gravida ligula, ac lobortis orci malesuada a. Vivamus gravida massa neque, eu consequat sapien eleifend a. Vivamus pulvinar tortor ex, ac placerat arcu consequat ut. Donec aliquam urna ut eros vestibulum pharetra. Proin molestie tortor vitae mauris consequat ultricies. Cras est ante, accumsan in varius sit amet, pellentesque quis enim. Donec lacinia interdum purus a pellentesque. Maecenas non risus dolor. Vestibulum eget molestie tortor. Morbi condimentum venenatis felis."
            c.save()
    return HttpResponseRedirect('/blog/')

