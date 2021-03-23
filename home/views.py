from django.shortcuts import HttpResponse, redirect, render
from .forms import ContactInfo
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    post = Post.objects.all()[:3]
    context = {"posts": post}
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        author = request.POST["author"]
        slug = request.POST["slug"]
        post = Post(Title=title, Content=content, Author=author, slug=slug)
        post.save()
        messages.success(request,'Post added successfully')
    return render(request, "home/home.html", context)


def contact(request):
    forms = ContactInfo()
    if request.method == "POST":
        forms = ContactInfo(request.POST)
        if forms.is_valid():
            print("hfhhf", forms.cleaned_data)
            print(forms.is_valid())
            if forms.is_valid() != True:
                messages.error(request, "Some error occured.")
            forms.save()
            forms = ContactInfo()
            messages.success(request, "Your Message is successfully send.")
        else:
            print(forms.errors)
    context = {"form": forms}
    return render(request, "home/contact.html", context)


def about(request):
    return render(request, "home/about.html")


def search(request):
    query = request.GET["search"]
    if len(query) > 100:
        allPosts = Post.objects.none()
        messages.error(request, "No search result found !")
    else:
        allPostsTitle = Post.objects.filter(Title__icontains=query)
        allPostsContent = Post.objects.filter(Content__icontains=query)
        allPostsAuthor = Post.objects.filter(Author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent.union(allPostsAuthor))

    if allPosts.count() == 0:
        messages.warning(request, "No search result found !")
    else:
        messages.success(request, "Results found !")
    context = {"posts": allPosts, "query": query}
    return render(request, "home/search.html", context)


def handleSignup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect("Home")

        if not username.isalnum():
            messages.error(request, "Username can only contain charactes and numbers")
            return redirect("Home")

        if pass1 != pass2:
            messages.error(request, "Password do not match")
            return redirect("Home")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your account is successfully created.")
        return redirect("Home")
    else:
        return HttpResponse("404 - not found")


def handleLogin(request):
    if request.method == "POST":
        username = request.POST["loginusername"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("Home")
        else:
            messages.error(request, "Invalid credentials , please try again")
            return redirect("Home")
    else:
        return HttpResponse("404")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("Home")
