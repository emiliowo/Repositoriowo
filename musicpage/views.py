from django.shortcuts import render
from .models import Review
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio.
    
    """
    #Renderiza la Plantilla HTML index.html con los datos en la variable contexto

    return render(
        request,
        'index.html',
        
    )

def contact(request):
    """
    Función vista para la página inicio del sitio.
    
    """
    #Renderiza la Plantilla HTML index.html con los datos en la variable contexto

    return render(
        request,
        'contact.html',
        
    )

def about(request):
    """
    Función vista para la página inicio del sitio.
    
    """
    #Renderiza la Plantilla HTML index.html con los datos en la variable contexto

    return render(
        request,
        'about.html',
        
    )

class ListaReviewVista(generic.ListView):
    model	=	Review
    context_object_name ='review_list' 
    template_name =	'musicpage/review_list.html'


class ReviewCreate(CreateView):
    model = Review
    fields= '__all__'


class ReviewUpdate(UpdateView):
    model = Review
    fields = ['nombre','email','review']


class ReviewDelete(DeleteView):
    model = Review
    success_url= reverse_lazy('review')

class ReviewDetailView(generic.DeleteView):
    model = Review    