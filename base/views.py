
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import todo

# Create your views here.
class todos(ListView):
    model = todo
    template_name = 'base/home.html'
    context_object_name = 'todos'





class todocreate(CreateView):
    model = todo
    template_name = 'base/form.html'
    fields = ['title','desc','complete']
    success_url = reverse_lazy('todo')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(todocreate,self).form_valid(form)

class edit(UpdateView):
    model = todo
    template_name = 'base/form.html'
    fields = ['title','desc','complete']
    success_url = reverse_lazy('todo')

class delete(DeleteView):
    model = todo
    context_object_name = 'todo'
    template_name = 'base/confirm.html'
    success_url = reverse_lazy('todo')


