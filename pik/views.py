from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PostForm, QuestionForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import DetailView, ListView, DeleteView, UpdateView


PRODUCT_CATEGORIES = (
		"Vozila",
		"Namještaj",
		"Bela tehnika",
		"Odjeća",
		"Tehnologija",
		"Igračke",
		"Literatura",
		"Nekretnine",
		"Ostalo",
	)


class HomeView(View):
	def get(self, request):
		post_list = Post.objects.all()
		paginator = Paginator(post_list, 6)
		categories = PRODUCT_CATEGORIES

		page = request.GET.get('page')
		page_obj = paginator.get_page(page)

		try:
			posts = paginator.page(page)
		except PageNotAnInteger:
			posts = paginator.page(1)
		except EmptyPage:
			posts = paginator.page(paginator.num_pages)

		context = {
			"posts":posts,
			"categories":categories,
			"page_obj":page_obj,
			"page":page
		}
		return render(self.request, "home.html", context)

class CreatePostView(View):
	template_name = "create_post.html"

	def get(self, request, *args, **kwargs):
		form = PostForm()
		context = {"form": form}
		return render(request, self.template_name, context)
	def post(self, request, *args, **kwargs):
		form = PostForm(self.request.POST or None, self.request.FILES or None)
		if form.is_valid():
			if self.request.user.is_authenticated:
				post = form.save(commit=False)
				post.user = self.request.user
				post.save()
				if post.price == "Iznos":
					return redirect("pik:determine-price")
				else:
					return redirect("/")
			else:
				return redirect("account_login")
		context = {
			"form":form,
		}
		return render(self.request, self.template_name, context)


class PostDetailView(DetailView):
	model = Post
	template_name = "post_view.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		pk = kwargs["object"]
		pk = pk.id
		context['post'] = Post.objects.get(id=pk)
		context['all_posts'] = Post.objects.all()
		return context



def category_view(request, cat):
	categories = PRODUCT_CATEGORIES
	category_posts = Post.objects.filter(category=cat)
	context = {
		"category_posts":category_posts,
		"categories":categories,
	}
	return render(request, "category_view.html", context)


class PostDeleteView(DeleteView):
	model = Post
	success_url = "/"
	template_name = "post_confirm_delete.html"


class PostUpdateView(UpdateView):
	model = Post
	form = PostForm
	fields = [
			"title",
			"price",
			"category",
			"description",
			"img",
			"replacement",
				]
	template_name = "create_post.html"
	success_url = "/"


def user_profile(request, id):
	user = User.objects.get(id=id)
	users_posts = Post.objects.filter(user=user)
	context = {
		"user": user,
		"users_posts": users_posts,
	}
	return render(request, "user_profile.html",context)


def search(request):
	posts_search = request.GET.get("search-site")
	posts = Post.objects.filter(
			Q(title__icontains=posts_search) |
			Q(description__icontains=posts_search)
		).distinct()
	
	context = {
		"posts": posts,
		"posts_search": posts_search
	}
	return render(request, "posts_search.html", context)


def questions(request, id):
	post = Post.objects.get(id=id)
	questions = Question.objects.filter(post=post)
	question_form = QuestionForm()
	if request.method == "POST":
		question_form = QuestionForm(request.POST)
		if question_form.is_valid():
			question = question_form.save(commit=False)
			question.user = request.user
			question.post = post
			question.save()
			return redirect("pik:post-questions", id=post.id)
		else:
			return redirect("/")
	context = {
		"question_form":question_form,
		"post":post,
		"questions":questions,
		}
	return render(request, "questions.html", context)


def delete_question(request, id):
	question = Question.objects.get(id=id)
	question.delete()
	return redirect("pik:post-questions", id=question.post.id)


def determine_price(request):
	post = Post.objects.all().order_by("-post_date")[0]
	if request.method == "POST":
		cijena = request.POST.get("cijena")
		post.price_int = cijena
		post.save()
		return redirect("pik:post-view", post.id) #TODO dodati redirect na post view
	else:
	context = {
	}
	return render(request, "determine_price.html", context)
