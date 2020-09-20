from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password,**extra_fields):

        extra_fields.setdefault('is_admin',False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password, **extra_fields)


class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='이메일')
    nickname = models.CharField(unique=True, verbose_name='닉네임', max_length=50)
    is_admin = models.BooleanField(default=False, verbose_name='관리자여부')
    is_staff = models.BooleanField(default=False, verbose_name='스태프권한')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    objects = UserManager()






