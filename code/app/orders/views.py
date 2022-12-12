from django.views.generic import TemplateView, DetailView
from django.conf import settings
import stripe
from django.shortcuts import render
from django.contrib.auth.models import Permission
from raquel.models import Curso
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.


class OrdersCurso(LoginRequiredMixin, DetailView):
    template_name = 'orders/pago_cursos.html'
    model = Curso
    context_object_name = 'Todos_Cursos'
    login_url = 'account_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context['api_key'] = settings.STRIPE_TEST_SECRET_KEY
        return context


class OrdersPageView(DetailView):
    template_name = 'orders/purchase.html'
    model = Curso
    context_object_name = 'Todos_Cursos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context['api_key'] = settings.STRIPE_TEST_SECRET_KEY
        return context


def charge(request):
    if request.method == 'POST':
        Precio = int(request.POST['precio'])*100
        nombre = request.POST['nombre']
        charge = stripe.Charge.create(
            amount=Precio,
            currency='usd',
            description='El pago de la peliculas ' +
            nombre + ' es de:' + str(Precio),
            source=request.POST['stripeToken'],
            api_key=settings.STRIPE_TEST_SECRET_KEY)
    return render(request, 'orders/charge.html')
