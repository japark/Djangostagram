from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView

from dsuser.forms import RegisterForm, LoginForm
from dsuser.models import Dsuser

# Create your views here.


class RegisterView(FormView):
	template_name = 'dsuser/register.html'
	form_class = RegisterForm
	success_url = '/'

	def form_valid(self, form):
		member = Dsuser(
			username=form.data.get('username'),
			email=form.data.get('email'),
			password=make_password(form.data.get('password')),
		)
		member.save()
		return super().form_valid(form)


class LoginView(FormView):
	template_name = 'dsuser/login.html'
	form_class = LoginForm
	success_url = '/'

	def form_valid(self, form):
		self.request.session['user'] = form.data.get('username')
		return super().form_valid(form)


def logout(request):
	if request.session.get('user'):
		del request.session['user']
	return redirect('/')