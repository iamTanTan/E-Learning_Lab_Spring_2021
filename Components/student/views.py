from django.shortcuts import render
from Components.student.models import Post, WelcomePage,ReadingMaterial, Connect
from django.contrib.auth.decorators import login_required
from Components.quizapp.models import Quiz
@login_required
def class_index(request, id_field):
    posts = Post.objects.all().filter(courses = (str)(id_field) )
    
    if (not posts.exists()):
        return render(request, "not_exists.html", {})

    context = {
        "posts": posts,
    }
    print(context)
    return render(request, "class_index.html", context)


@login_required
def class_detail(request, id_field, pk):
    posts = Post.objects.all().filter(courses = (str)(id_field) )

    if (not posts.exists()):
        return render(request, "not_exists.html", {})

    detail = posts.get( pk=pk)
  
    context = {
        "post": detail,
     
    }

    return render(request, "class_detail.html", context)


@login_required
def welcome_page(request, id_field):
    page = WelcomePage.objects.all().filter(courses = (str)(id_field) )

    if (not page.exists()):
        return render(request, "not_exists.html", {})

    context = {
        "page": page,
    }

    return render(request, "welcome_page.html", context)

@login_required
def reading_material(request, id_field):
    page = ReadingMaterial.objects.all().filter(courses = (str)(id_field) )
    
    if (not page.exists()):
        return render(request, "not_exists.html", {})
   
    context = {
        "page": page,
    }

    return render(request, "reading_material.html", context)


@login_required
def connect(request, id_field):
    page = Connect.objects.all().filter(courses = (str)(id_field) )
    if (not page.exists()):
        return render(request, "not_exists.html", {})
   
    context = {
        "page": page,
    }

    return render(request, "connect.html", context)


@login_required
def quizzes(request, id_field):
    posts = Quiz.objects.all().filter(courses = (str)(id_field) )
    #detail = posts.get(id="1df92740-5fb8-46c8-9f7c-25c56d5d34f1")
    if (not posts.exists()):
        return render(request, "not_exists.html", {})
   
    context = {
        "posts": posts,
    }

    return render(request, "quizzes.html", context)


@login_required
def quizzes_index(request, id_field, id):
    posts = Quiz.objects.all().filter(courses = (str)(id_field))
    detail = posts.get(id=id)
  
    if (not posts.exists()):
        return render(request, "not_exists.html", {})

    context = {
        "page": detail,
     
    }

    return render(request, "quizzes_index.html", context)