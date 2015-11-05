from django import forms

from board.models import Boards

class WriteForm(forms.ModelForm):
	subject = forms.CharField(max_length=50)
	contents = forms.CharField()

	class Meta:
		model = Boards
		fields = ('subject', 'contents')

class CommentForm(forms.ModelForm):
	contents = forms.CharField()
	
	class Meta:
		model = Boards
		fields = ('contents',)
