from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from raquel.models import Curso
from .forms import CustomUserCreationForm
from .views import SignUpView

# Create your tests here.


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='prueba',
                                        email='prueba@user.com', password='prueba1234')
        self.assertEqual(user.email, 'prueba@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

# verificar que la vista redirigirá a una página de inicio de sesión si el usuario no ha iniciado sesión
    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse(' my-manualidad '))
        self.assertRedirects(resp, '/users/login/?next=/raquel/curso/')

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse(' my-manualidad '))
        self.assertRedirects(resp, '/users/login/?next=/raquel/manualidades/')

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse(' my-manualidad '))
        self.assertRedirects(resp, '/users/login/?next=/raquel/epocas/')

    def test_login(self):
        self.common_user.set_password('raquel-admin')
        self.common_user.save()
        response = self.client.login(
            username='raquel-admin', password='raquel1234')
        self.assertEquals(response, True)

    def test_login_fail(self):
        self.common_user.set_password('oliver')
        self.common_user.save()
        response = self.client.login(username='oliver', password='oliver1')
        self.assertEquals(response, False)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup/')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, '¡Hola! No debería estar en la página.')

    def test_signup_form(self):  # new
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):  # new
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SignUpView.as_view().__name__
        )


class CursoTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='adminuser',
            email='adminuser@email.com',
            password='testpass123'
        )
        self.special_permission = Permission.objects.get(
            codename='special_status')  # new
        self.curso = Curso.objects.create(
            title='	Origami fácil para niños',
            impartidor='admin', price='250.00',
        )
        self.review = Curso.objects.create(
            curso=self.curso,
            impartidor=self.user,
            review='An excellent review',
        )

    def test_curso_list_view_for_logged_out_user(self):  # new
        self.client.logout()
        response = self.client.get(reverse('curso_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '%s?next=/cursos/' % (reverse('account_login')))
        response = self.client.get(
            '%s?next=/cursos/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')

    def test_curso_detail_view_with_permissions(self):  # new
        self.client.login(email='adminuser@email.com', password='testpass123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.curso.get_absolute_url())
        no_response = self.client.get('/cursos/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Origami fácil para niños')
        self.assertContains(response, 'An excellent review')
        self.assertTemplateUsed(response, 'cursos/cursos_detalle.html')
