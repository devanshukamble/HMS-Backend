from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

# custome user manager class copied from documentation


class UserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname,dateofbirth, gender, address1, address2, city, state, country, zipcode, password=None, password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            dateofbirth = dateofbirth,
            gender=gender,
            address1=address1,
            address2=address2,
            city=city,
            state=state,
            country=country,
            zipcode=zipcode
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,firstname,lastname,gender,dateofbirth, password=None, password2=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            firstname=firstname,
            lastname=lastname,
            gender=gender,
            dateofbirth=dateofbirth,
            password=password,
            address1="",
            address2="",
            city="", 
            state="",
            country="",
            zipcode="",           
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# custome user model copied from documentation
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dateofbirth = models.DateField()
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=255,)
    state = models.CharField(max_length=255,)
    country = models.CharField(max_length=255,)
    zipcode = models.CharField(max_length=12)
    is_doctor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["firstname","lastname","gender","dateofbirth"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
