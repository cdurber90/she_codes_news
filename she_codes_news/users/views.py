from typing import Any
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic

from news.models import NewsStory
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserAccountView(generic.DetailView):
    model = CustomUser
    template_name = 'users/myAccount.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['user_stories'] = NewsStory.objects.filter(author=user)
        return context