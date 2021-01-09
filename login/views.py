from django.contrib.auth import logout
from django.views.generic import TemplateView, RedirectView


class Login(TemplateView):
    template_name = 'login/login.html'


class Logout(RedirectView):
    pattern_name = 'login:login_view'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
