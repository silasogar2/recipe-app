from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        '''Test Creating a user'''
        email = 'test@silasogar.tech'
        password = 'Silas'
        username = 'Silasogar'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Ensuring email is normalized'''
        email = 'test2@SILASOGAR.tech'
        # email = 'test@silasogar.tech'
        user = get_user_model().objects.create_user(email, 'Silas123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test that email is not invalid'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123') 

    def test_super_user_is_created(self):
        '''Test creating a super user'''
        user = get_user_model().objects.create_superuser(
            'aurelia@silasogar.tech',
            'Aurelia'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


        
