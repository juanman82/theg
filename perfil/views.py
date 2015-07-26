from django.shortcuts import render

# Create your views here.
from .models import Perfil


def inicio(request):


    queryset = Perfil.objects.filter(activo=1).order_by('-id')
    context = {

    "queryset": queryset

    }

    return render(request, "inicio.html", context)
