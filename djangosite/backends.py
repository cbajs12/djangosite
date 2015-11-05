from django.contrib.auth.models import check_password
from django.contrib.auth import get_user_model

class EmailAuthBackend(object):
	
	def authenticate(self,username=None,password=None):
		try:
			User = get_user_model()
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None

	def get_user(self,user_id):
		try:
			User = get_user_model()
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
