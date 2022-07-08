from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .models import Category, Manufacturer, Product, Comment


# Create your views here.
class HomeView(ListView):
    template_name = 'shop/home.html'
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manufactories'] = Manufacturer.objects.all()
        return context


class ProductList(ListView):
    template_name = 'shop/products.html'
    model = Product

    def get_queryset(self):
        queryset = Product.objects.filter(count__gt=0)
        if self.request.GET.getlist('category'):
            queryset = queryset.filter(category_id__in=self.request.GET.getlist('category'))
        if self.request.GET.getlist('manuf'):
            queryset = queryset.filter(manufacturer_id__in=self.request.GET.getlist('manuf'))
        if self.request.GET.get('minValue'):
            queryset = queryset.filter(price__gte=self.request.GET.get('minValue'))
        if self.request.GET.get('maxValue'):
            queryset = queryset.filter(price__lte=self.request.GET.get('maxValue'))
        if self.request.GET.get('search'):
            queryset = queryset.filter(title__icontains=self.request.GET.get('search'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = Category.objects.all()
        context['manufs'] = Manufacturer.objects.all()
        context['catFilter'] = self.request.GET.getlist('category')
        context['manufFilter'] = self.request.GET.getlist('manuf')
        context['otherFilters'] = self.request.GET

        return context


class ProductDetail(DetailView):
    template_name = 'shop/productDetail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(product_id=self.kwargs.get('pk'))
        return context

    def post(self, request, *args, **kwargs):
        comment = Comment.objects.create(
            content=self.request.POST.get('content'),
            product_id=kwargs.get('pk'),
            user_id=self.request.user.id
        )
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))


class ChackOutView(View):
    def get(self, request):
        context = {'products': Product.objects.filter(id__in=request.GET.getlist('product'))}
        return render(request, 'shop/chackout.html', context)

    def post(self, request):
        # Make chackout
        pass
