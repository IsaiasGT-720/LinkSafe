from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
##from django.contrib.auth import login
from .models import Link
#import uuid



## RENDER DE LA DASHBOARD, QUIEN SABE, QUIZAS SE ARREGLE
@login_required
def dashboard(request):
    element = Link.objects.filter(user=request.user)
    print("ya agarré los links")
    return render(request, "CentralLinks/dashboard.html", {"elementos": element})



## CRUD DE LOS LINKS
# OPERACION CREAR
@login_required
def create_link(request):
   if request.method == "POST":
      URLs = request.POST.get("url")
      titulo = request.POST.get("title")
      if URLs and titulo:
        Link.objects.create(
            URL=URLs,
            title=titulo,
            user=request.user
        )
        print("Listo mi rey, ya creé el link 😏")
        return redirect('dashboard')
      else:
        print("cagaste la lata papito 😥")
        return redirect('dashboard')



#OPERACION DE BUSQUEDA
@login_required
def search_links(request):
    query = request.GET.get("q", "")

    links = Link.objects.filter(
        user=request.user
    ).filter(
        Q(title__icontains=query) |
        Q(URL__icontains=query)
    )

    return render(
        request,
        "CentralLinks/dashboard.html",
        {
            "list": links,
            "search": query
        }
    )
    #return redirect("dashboard")


@login_required
@require_http_methods(["POST"])
def modify_link(request, link_id):
    link = get_object_or_404(Link, id=link_id, user=request.user)
    link.title = request.POST.get("title", link.title)
    link.URL = request.POST.get("url", link.URL)
    link.save()

    return JsonResponse({"message": "Link actualizado"})


# OPERACION ELIMINAR
@login_required
def delete_link(request, link_id):
    link = get_object_or_404(Link, id=link_id, user=request.user)
    link.delete()
    return redirect("dashboard")



##INICIO DE SESION
def login_view(request):
    if request.method == "POST":
        print("PETICION TOMADA")
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        print("USER AUTENTICADO")
        print("USER:", user)
        if user:
            login(request, user)
            return redirect("dashboard")
        print("CAGASTE LA LATA")

        return render(request, "CentralLinks/login.html", {
            "error": "Invalid credentials"
        })
       

    return render(request, "CentralLinks/login.html")
## CIERRE DEL LOG IN



## ESTO ES EL SIGN IN
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm  = request.POST.get("confirm")
        # 1. Verificar passwords
        if password != confirm:
            return render(request, "CentralLinks/register.html", {
                "error": "Las contraseñas no coinciden"
            })
        # 2. Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            return render(request, "CentralLinks/register.html", {
                "error": "Este nombre de usuario ya existe"
            })
        # 3. Crear usuario
        user = User.objects.create_user(
            username=username,
            password=password
        )
        return redirect("login")
    return render(request, "CentralLinks/register.html")


# UN TEXTO BONITO
print("""
      ------------------
      CREATED WITH LOVE
      EVERYTING  IS  OK,
      GO AHEAD!
      ------------------
      """)