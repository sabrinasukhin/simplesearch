from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count, Q

from .models import Product, Category, Tag


def index(request):
    search = request.GET.get('search', None)
    category = request.GET.get('category', None)
    tags_selected = request.GET.getlist('tags', [])

    filters = Q()
    tag_filter = Q()
    if search != '' and search is not None:
        filters &= Q(name__icontains=search)
    if category != '' and category is not None:
        filters &= Q(category_id=category)
    if tags_selected != [] and tags_selected is not None:
        tag_filter &= Q(tags__in=tags_selected)
        filters &= Q(num_tag_match=len(tags_selected))
    results = Product.objects.annotate(num_tag_match=Count('tags', filter=tag_filter)).filter(filters)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        "categories": categories,
        "tags": tags,
        "results": results,
    }
    return render(request, "searchapp/index.html", context)
