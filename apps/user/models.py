from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from SpywareBackendServer.settings import AUTH_USER_MODEL


# Base model


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, **extra_fields)
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    unique_code = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=254, blank=True, null=True, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    user_image = models.ImageField(upload_to='assets/', default='assets/no_image.png', null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    type = models.PositiveSmallIntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User', null=True, blank=True, related_name="user_created_by_fk",
                                   on_delete=models.PROTECT)
    modified_by = models.ForeignKey('User', blank=True, related_name="user_modified_by_fk",
                                    null=True, on_delete=models.PROTECT)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    sort = models.CharField(max_length=20, null=True, blank=True)
    status = models.PositiveSmallIntegerField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self):
        return self.email

    def __str__(self):
        try:
            return self.first_name + "-" + self.last_name
        except:
            return "Hello"


class UserPermissions(models.Model):
    user = models.ForeignKey(User, related_name='user_permission_fk', null=True, blank=True, on_delete=models.PROTECT)

    created_by = models.ForeignKey(User, null=True, blank=True,
                                   related_name="%(app_label)s_%(class)s_created_by", on_delete=models.PROTECT)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, blank=True, related_name="%(app_label)s_%(class)s_modified_by",
                                    null=True, on_delete=models.PROTECT)
    modified_datetime = models.DateTimeField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'user_permission'
        verbose_name_plural = 'user_permissions'

    def __str__(self):
        return self.user.first_name + '-' + self.user.last_name

