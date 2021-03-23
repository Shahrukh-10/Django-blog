from django.shortcuts import HttpResponse, redirect, render
from .models import Post
from blog.models import BlogComment
from django.contrib import messages
from blog.templatetags import get_dict

# Create your views here.
def blog(request):
    allpost = Post.objects.all()
    context = {"posts": allpost}
    return render(request, "blog/bloghome.html", context)


def blogpost(request, slug):
    # return HttpResponse(f'MERI STRING - > - > {slug}')
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    repdict = {}
    for reply in replies:
        if reply.sno not in repdict.keys():
            repdict[reply.parent.sno] = [reply]
        else:
            repdict[reply.parent.sno].append(reply)
    context = {
        "post": post,
        "repdict": repdict,
        "comments": comments,
        "user": request.user,
    }
    return render(request, "blog/blogpost.html", context)


def postComment(request):
    if request.method == "POST":
        comment = request.POST["comment"]
        user = request.user
        postno = request.POST["postsno"]
        post = Post.objects.get(sno=postno)
        parentsno = request.POST["parentsno"]

        if parentsno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentsno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            messages.success(request, "Your reply has been posted successfully")
        comment.save()
    return redirect(f"/blog/{post.slug}")
