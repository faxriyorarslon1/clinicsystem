from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


GENDER_CHOICES = (
    ('Erkak', 'Erkak'),
    ('Ayol', 'Ayol')
)

DOCTOR_TYPE = (
    ('Terapevt', 'Terapevt'),
    ('Lor', 'Lor'),
    ('Okulist', 'Okulist'),
    ('Pulmonolog', 'Pulmonolog'),
    ('Stomotolog', 'Stomotolog')
)

DOCTOR_DEGREE = (
    ("Amaliyotchi shifokor", 'Amaliyotchi shifokor'),
    ('Bosh shifokor', 'Bosh shifokor'),
    ('Yordamchi shifokor', 'Yordamchi shifokor'),
)

BEMOR_TYPE = (
    ("Og'ir holatda", "Og'ir holatda"),
    ("O'rta holatda" , "O'rta holatda"),
    ("Yengil holatda", "Yengil holatda")
)



class User(AbstractUser):
    username = models.CharField('First name',
                                max_length=20, unique=False)
    last_name = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=12, unique=True)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'last_name', 'middlename','email', 
                        'gender','password']

    def __str__(self):
        return "{} {}".format(self.username, self.last_name)

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'



class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=DOCTOR_TYPE)
    degree = models.CharField(max_length=20, choices=DOCTOR_DEGREE)

    def __str__(self):
        return "{} {} ## {}".format(self.user.username, self.user.last_name, self.type)

    class Meta:
        verbose_name = 'Shifokor'
        verbose_name_plural = 'Shifokorlar'


class Bemor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=BEMOR_TYPE)

    def __str__(self):
        return "{} {} ## {}".format(self.user.username, self.user.last_name, self.type)

    class Meta:
        verbose_name = 'Bemor'
        verbose_name_plural = 'Bemorlar'



