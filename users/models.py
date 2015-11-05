from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
	def create_user(self,email,first_name,last_name,country,comment,password=None):
		if not email and first_name and last_name and password:
		 raise ValueError('Users must have an email address')
	
		user = self.model(
			email=self.normalize_email(email),
			first_name=first_name,
			last_name=last_name,
			country=country,
			comment=comment,
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,email,first_name,last_name,password):
		user = self.model(
			email=self.normalize_email(email),
			first_name=first_name,
			last_name=last_name,
			password=password,
			)
		user.is_admin=True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(unique=True)
	country = models.CharField(max_length=50,blank=True)
	comment = models.TextField(blank=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name']

	def __unicode__(self):
		return self.email

