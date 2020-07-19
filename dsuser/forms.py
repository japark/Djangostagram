from django import forms
from django.contrib.auth.hashers import check_password

from dsuser.models import Dsuser


class RegisterForm(forms.Form):
	username = forms.CharField(max_length=32, label="아이디")
	email = forms.EmailField(max_length=128, label='이메일')
	password = forms.CharField(widget=forms.PasswordInput, label='비밀번호')
	re_password = forms.CharField(widget=forms.PasswordInput, label='비밀번호확인')

	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		email = cleaned_data.get('email')
		password = cleaned_data.get('password')
		re_password = cleaned_data.get('re_password')

		if not (username and email and password and re_password):
			self.add_error(None, "모든 값을 입력해야 합니다.")
		else:
			if not password == re_password:
				self.add_error(None, "비밀번호가 다릅니다.")


class LoginForm(forms.Form):
	username = forms.CharField(max_length=32, label="아이디")
	password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")

	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get('username')
		password = cleaned_data.get('password')

		if username and password:
			try:
				user = Dsuser.objects.get(username=username)
			except Dsuser.DoesNotExist:
				self.add_error(None, "아이디가 없습니다.")
			else:
				if not check_password(password, user.password):
					self.add_error(None, "비밀번호를 틀렸습니다.")
		else:
			self.add_error(None, "아이디와 비밀번호를 모두 입력하세요.")