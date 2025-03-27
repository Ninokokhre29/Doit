from lib2to3.fixes.fix_input import context

from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.db.models import Q
from .models import Products, Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class ProductView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query')
        selected_categories = request.GET.getlist('category')

        products = Products.objects.all()

        if query:
            products = products.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query)
            ).distinct()

        if selected_categories:
            products = products.filter(category__id__in=selected_categories).distinct()

        paginator = Paginator(products, 4)

        page_num = request.GET.get('page')

        try:
            products = paginator.page(page_num)
        except PageNotAnInteger:
            products =paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        categories = Category.objects.all().order_by('category_type')

        categories_by_type = {}
        for category in categories:
            categories_type = category.category_type
            if categories_type not in categories_by_type:
                categories_by_type[categories_type] = []

            categories_by_type[categories_type].append(category)

        return render(request, self.template_name, {
            'products': products,
            'categories_by_type': categories_by_type,
            'selected_categories': selected_categories
        })

class ProductDetailView(DetailView):
    template_name = 'details.html'
    model = Products
    context_object_name = 'product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        related_products = Products.objects.filter(
            category__in=product.category.all()
        ).exclude(id=product.id).distinct()[:4]

        context['related_products'] = related_products
        return context

class AboutUsView(TemplateView):
    template_name = 'about.html'