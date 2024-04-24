from django.shortcuts import render
from django.views.generic import ListView
from car_app.models import Car
from car_brand_app.models import Brand



class CarListView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

    def get(self, request, *args, **kwargs):
        brand_slug = kwargs.get('brand_slug')
        self.object_list = self.model.objects.all()

        if brand_slug:
            brand = Brand.objects.get(slug=brand_slug)
            self.object_list = self.object_list.filter(brand=brand)

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        return context