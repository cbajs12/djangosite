from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from users.forms import JoinForm, ChangeForm

Info = get_user_model()

def login(request):
	if request.method == 'POST':	
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user:
			auth_login(request,user)
			request.session['email'] = email
			return HttpResponseRedirect(reverse('main'))
		else:
			print "Invalid login details: {0}, {1}".format(email, password)
			return HttpResponseRedirect(reverse('users:login'))
	else:
		return render(request,'users/login.html')

@login_required	
def logout(request):
	auth.logout(request)
	try:
      		del request.session['email']
   	except KeyError:
        	pass
	return HttpResponseRedirect(reverse('main'))

def join(request):
	if request.method == 'POST':
		form = JoinForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect(reverse('main'))
		else:
			return HttpResponseRedirect(reverse('users:join',kwargs={'form':form}))

	else:
		form = JoinForm()
		return render(request,'users/join.html',{'form':form})

def check(request):
	email = request.GET['email']
	result = Info.objects.filter(email=email)
	if len(result) == 0: 
		return HttpResponse("1000")
	else:
		return HttpResponse("2000")
	
@login_required
def edit(request):
	if request.method == 'POST':
		email = request.session['email']
		#Info = get_user_model()
		info = Info.objects.get(email=email)
		form = ChangeForm(request.POST,instance=info)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			update_session_auth_hash(request, user)
			return HttpResponseRedirect(reverse('main'))

		else:
 			print form.errors
	else:
		form = ChangeForm()
		return render(request,'users/changeinfo.html',{'form':form})

@login_required
def delete(request):
	if request.method == 'POST':
		decide = request.POST['decide']
		if decide == 'yes':
			email = request.session['email']
			#Info = get_user_model()
			info = Info.objects.get(email=email)
			try:
      				del request.session['email']
   			except KeyError:
        			pass
			info.delete()
			return HttpResponseRedirect(reverse('main'))
		else:
			return HttpResponseRedirect(reverse('main'))
			
	else:
		return render(request,'users/delete.html')

@login_required
def show(request):
	#Info = get_user_model()
	user_list = Info.objects.all()
	paginator = Paginator(user_list,5)

	page = request.GET.get('page')
	try:
		paging = paginator.page(page)
	except PageNotAnInteger:
		paging = paginator.page(1)
	except EmptyPage:
		paging = paginator.page(paginator.num_pages)

	return render(request,'users/showuser.html',{"paging":paging})

'''class LoginView(FormView):
	template_name = 'users/login.html'
	form_class = LoginForm
	
	def get_success_url(self):
		return reverse('homepage')

	def form_valid(self,form):
		form.user.backend = 'django.contrib.auth.backends.ModelBackend'
		login(self.request,form.user)
		return super(LoginView,self).form_valid(form)'''
