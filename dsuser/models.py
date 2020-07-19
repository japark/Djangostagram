from django.db import models

# Create your models here.


class Dsuser(models.Model):
	username = models.CharField(max_length=32, verbose_name='아이디')
	password = models.CharField(max_length=64, verbose_name='비밀번호')
	email = models.EmailField(max_length=128, verbose_name='이메일')
	registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')

	def __str__(self):
		return self.username

	class Meta:
		db_table = 'member'
		verbose_name = '회원'
		verbose_name_plural = '회원목록'
