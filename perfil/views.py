from django.shortcuts import render

# Create your views here.
from .models import Perfil_Hombre
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Perfil_Mujer
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PaisForm


from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required




def pais(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PaisForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            pais = "hola"
            return pais
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaisForm()

    return render(request, 'pais.html', {'form': form})






def inicio(request):


    queryset = Perfil_Hombre.objects.filter(activo=1).order_by('-id')
    context = {

    "queryset": queryset

    }

    return render(request, "inicio.html", context)




class HombresList(ListView):
    model = Perfil_Hombre

class HombresDetailList(DetailView):
    model = Perfil_Hombre

class MujeresList(ListView):
    model = Perfil_Mujer

class MujeresDetailList(DetailView):
    model = Perfil_Mujer