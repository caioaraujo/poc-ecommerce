from django.contrib.auth import logout, login
from django.views.generic import RedirectView, FormView

from .forms import UserForm


class Login(FormView):
    form_class = UserForm
    template_name = 'login/login.html'
    success_url = '/produtos/'

    def form_valid(self, form):
        login(self.request, form.user)
        return super(Login, self).form_valid(form)


class Logout(RedirectView):
    pattern_name = 'login:login_view'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
