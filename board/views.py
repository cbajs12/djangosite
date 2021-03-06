from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from board.models import Boards
from board.forms import WriteForm, CommentForm

Info = get_user_model()

def lists(request):
	board_lists = Boards.objects.filter(board_pid=0).order_by('board_id').reverse()
	paginator = Paginator(board_lists,5)
	
	page = request.GET.get('page')
	try:
		paging = paginator.page(page)
	except PageNotAnInteger:
		paging = paginator.page(1)
	except EmptyPage:
		paging = paginator.page(paginator.num_pages)

	return render(request,'board/list.html',{"paging":paging})

@login_required
def write(request):
	if request.method == 'POST':
		form = WriteForm(request.POST)
		if form.is_valid():
			email = request.session['email']
			info = Info.objects.get(email=email)
			nform = form.save(commit=False)
			nform.user_id = email
			nform.user_name = info.last_name
			nform.hits = 0
			nform.save()
			return HttpResponseRedirect(reverse('board:lists'))
		else:
			print form.errors
	else:
		return render(request,'board/write.html')

def view(request,board_id):
	boards = Boards.objects.get(board_id=board_id)
	if request.method == 'POST':
		content = request.POST.get('comment_contents',None)
		email = request.session['email']
		info = Info.objects.get(email=email)
		comment = Boards()
		comment.board_pid = board_id
		comment.user_id = email
		comment.user_name = info.last_name
		comment.subject = ""
		comment.contents = content
		comment.hits = 0
		comment.save()
		lists = Boards.objects.all().filter(board_pid=board_id)
		return render(request,'board/view.html',{"lists":lists,"bd":boards})
	else:
		boards.hits += 1
		boards.save()
		comment = Boards.objects.all().filter(board_pid=board_id)
		return render(request,'board/view.html',{"lists":comment,"bd":boards})
	#return HttpResponseRedirect(reverse('board:views',args=(board_id,)),{"bd",boards}) -> should use redirect after update DB

def delComment(request,board_id):
	boards = Boards.objects.get(board_id=board_id)
	email = request.session['email']
	bemail = boards.user_id
	if email == bemail:
		boards.delete()	
	bdId = request.GET['id']
	board = Boards.objects.get(board_id=bdId)
	comment = Boards.objects.all().filter(board_pid=bdId)
	return render(request,'board/view.html',{"lists":comment,"bd":board})

@login_required
def update(request,board_id):
	email = request.session['email']
	userid = request.GET['id']
	if email != userid:
		return HttpResponseRedirect(reverse('board:lists'))
	else:	
		boards = Boards.objects.get(board_id=board_id)
		if request.method == 'POST':	
			form = WriteForm(request.POST,instance=boards)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(reverse('board:view',args=(board_id,)))
			else:
				print form.errors
		else:
			return render(request,'board/update.html',{"bd":boards})

@login_required
def delete(request,board_id):
	email = request.session['email']
	userid = request.GET['id']
	if email != userid:
		return HttpResponseRedirect(reverse('board:lists'))
	else:
		boards = Boards.objects.get(board_id=board_id)
		boards.delete()
		boards = Boards.objects.all().filter(board_pid=board_id)
		boards.delete()
		return HttpResponseRedirect(reverse('board:lists'))
	

	
	
	
