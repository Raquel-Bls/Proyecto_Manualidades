from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

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
