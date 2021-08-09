from django.contrib.auth.models import PermissionsMixin
from users.manager import UserManager
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True)
    phonenumber = models.CharField(max_length=255)
    token = models.CharField(max_length=255, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    city = models.ForeignKey('branches.City', on_delete=models.CASCADE, default=1)
    address = models.ForeignKey('locations.Location', on_delete=models.CASCADE, default=1)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    # @property
    # def token(self):
    #     payload = {'id': User.id, 'username': User.username}
    #     token = jwt.encode({'id': self.id, 'username': self.username,'exp':datetime.utcnow()+timedelta(hours=24)}
    #                        , settings.SECRET_KEY, algorithm='HS256')
    #     return token
