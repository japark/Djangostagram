from django.db import models
from dsuser.models import Dsuser
from tag.models import Tag

# Create your models here.


class Post(models.Model):
	user = models.ForeignKey(Dsuser, on_delete=models.CASCADE, verbose_name='작성자')
	img_url = models.URLField(max_length=512, verbose_name='이미지주소')
	contents = models.TextField(verbose_name='내용')
	tags = models.ManyToManyField(Tag, verbose_name="태그")
	registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

	def __str__(self):
		return self.contents

	class Meta:
		db_table = 'post'
		verbose_name = '게시글'
		verbose_name_plural = '게시글목록'