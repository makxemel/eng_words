from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Word, Student
from django.views.generic import ListView, CreateView
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout


class MainPageView(TemplateView):
    template_name = 'main_page.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            return redirect('login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = '/'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    # success_url = '/'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class TenWordsList(ListView):
    template_name = 'words_mode.html'
    paginate_by = 1

    def get_queryset(self):
        user = Student.objects.get(user=self.request.user)
        queryset = user.words.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        return context


def word_list_rand(request):
    template_name = 'word_random_list.html'
    word = Word.objects.order_by('?').first()

    return render(request, template_name, {'card': word})


def delete_student_word(request, word_id):
    new_word = Word.objects.order_by('?').first()
    student = Student.objects.get(user__pk=request.user.id)
    student.words.remove(word_id)
    student.words.add(new_word)
    return redirect('words_mode')



    
