from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class CaseInsensitiveModelBackend(ModelBackend):
    """Class to make usernames case insensitive"""
    # Source: https://stackoverflow.com/questions/70713647/

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get(username__iexact=username)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
