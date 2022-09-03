from django.db.models import Count

from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('film'))

        context['cats'] = cats
        return context
