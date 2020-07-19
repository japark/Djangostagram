from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView

from dsuser.models import Dsuser
from dsuser.decorators import login_required
from post.forms import PostForm
from post.models import Post
from tag.models import Tag

# Create your views here.


@method_decorator(login_required, name='dispatch')
class PostCreate(FormView):
	template_name = 'post/post_create.html'
	form_class = PostForm
	success_url = '/'

	def form_valid(self, form):
		username = self.request.session.get('user')
		post = Post(
			user=Dsuser.objects.get(username=username),
			img_url=form.cleaned_data.get('img_url'),
			contents=form.data.get('contents'),
		)
		post.save()
		tags = form.cleaned_data["tags"].split(",")
		for tag in tags:
			tag = tag.strip()
			if not tag: continue
			_tag, _ = Tag.objects.get_or_create(name=tag)
			post.tags.add(_tag)
		return super().form_valid(form)


class PostList(ListView):
	queryset = Post.objects.all().order_by('-registered_dttm')
	paginate_by = 4
	# context_object_name = 'product_list'


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'post/post_detail.html', {'post':post})