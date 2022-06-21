from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, is_verified, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            is_verified=is_verified,

            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True,True, **extra_fields)
        return user

class User_info(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=250)
    phone = models.BigIntegerField()
    mother_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    gender = models.CharField(max_length=7)
    religion = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    qualification = models.CharField(max_length=250)
    marital_status = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    weight = models.BigIntegerField(max_length=50)
    body_type = models.CharField(max_length=50)
    physical_status = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    smoking = models.CharField(max_length=50)
    drinking = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='images/', blank=True, default='')

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    user_info = models.OneToOneField(User_info,null=True,blank=True,on_delete=models.CASCADE)
    token = models.CharField(default=None,null=True,max_length=200)
    gender = models.CharField(max_length=50)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

class Profile_views(models.Model):
    visited_user = models.CharField(max_length=250)
    user = models.CharField(max_length=250)