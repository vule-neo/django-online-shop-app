from django import forms
from django.forms import ModelForm
from .models import Post, Question
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
	class Meta:
		model = Post
		exclude = ["post_date", "user", "price_int"]
		widgets = {
				'description': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
			}
		labels = {
				'title': _('Ime artikla '),
				'price': _('Cijena '),
				'description': _('Opis '),
				'img': _('Dodajte fotografiju '),
				'replacement': _('Da li želite zamjenu za ovaj artikal '),
				'category': _('Izaberite kategoriju '),
				"price_int": _("Unesite cijenu ")
			}


class QuestionForm(ModelForm):
	class Meta:
		model = Question
		fields = ['text',]

		widgets = {
				'text': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
			}

		labels = {
				'text': _('Postavi pitanje '),
				}