from .models import CustomUser
from django.contrib.auth.backends import  ModelBackend

from django.contrib.auth.models import User


class EmailAuthBackend(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


'''class EmailAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        print(10000)
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = CustomUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            print(111)
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None'''