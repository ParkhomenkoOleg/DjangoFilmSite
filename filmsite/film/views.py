from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import RegisterUserForm, LoginUserForm
from .models import *
from .utils import DataMixin


class FilmHome(DataMixin, ListView):
    paginate_by = 12
    model = Film
    template_name = 'film/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ShowFilm(ListView):
    paginate_by = 12
    model = Film
    template_name = 'film/show_film.html'
    context_object_name = 'films'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curr_film'] = Film.objects.filter(title=self.kwargs['film_name'], is_published=True)
        return dict(list(context.items()))


class ShowFilmCategory(ListView):
    model = Film
    template_name = 'film/category.html'
    context_object_name = 'film'
    allow_empty = False

    def get_queryset(self):
        return Film.objects.filter(cat__name=self.kwargs['cat_name'], is_published=True).select_related('cat')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'film/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'film/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


def search_film(request):
    if request.method == "POST":
        searched = request.POST['searched']
        result = Film.objects.filter(title=searched)
        if len(result) == 0:
            return redirect('home')

        context = {
            'curr_film': result,
            'films': Film.objects.filter(is_published=True)
        }

        return render(request, 'film/show_film.html', context)
