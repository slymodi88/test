import jwt
from django.contrib.auth.base_user import BaseUserManager

from Ecommerce import settings


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('username required')

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_token(self, user):
        payload = {'id': user.id, 'username': user.username}
        token = jwt.encode(
            payload, settings.SECRET_KEY)
        user.token = bytes.decode(token)
        user.save()
        return user

    # def create_token(self, user):
    #     token = Token.objects.create(user=user)
    #     user.token = token.key
    #     user.save()
    #     print(token.key)
    #     return user
