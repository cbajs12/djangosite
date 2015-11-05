from django.db import models

class Boards(models.Model):
	board_id = models.AutoField(primary_key=True)
	board_pid = models.IntegerField(null=True,default=0)
	user_id = models.EmailField(null=True)
	user_name = models.CharField(max_length=30)
	subject = models.CharField(max_length=50)
	contents = models.TextField()
	hits = models.IntegerField()
	reg_date = models.DateField(auto_now=True,auto_now_add=True,editable=False,blank=True)

	def __unicode__(self):
		return self.user_name
	
	
