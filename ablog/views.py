from django.shortcuts import render
from django.views.generic import ListView,CreateView, DetailView, UpdateView, DeleteView
from .models import *
from .form import *
from django.urls import reverse_lazy

# def blog(request):
#     context = {}
#     return render(request,'index.html',context)


class Blog(ListView):
    model = Post
    template_name = 'index.html'
    # ordering = ['-id']
    ordering = ['-created']

    
class Article_Blog(DetailView):
    model = Post
    template_name = 'details.html'


class Add_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'host.html'

    # no need to use below lines because form.py takes care of it
    # fields = ('title','content')
    # fields = '__all__'


class update_post(UpdateView):
    model = Post
    form_class = updateform
    template_name = 'update.html'
    # fields = ['title','title_tag', 'content']


class destroy_post(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('my-blog')

    

