from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from car_app.models import Car
from car_app.forms import CarModelForm,CommentForm
from django.contrib import messages

# Create your views here.

# Add Car implementation
class AddCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_app/add_car.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["type"] = "Add"
        return context
    
    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong. your car not added in the list.')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Car added successful')
        return super().form_valid(form)
    
# Car details views
class CarDetailsView(DetailView):
    model = Car
    template_name = 'car_app/car_details.html'
    
    def post(self,request,*args, **kwargs):
        car = self.get_object()
        if self.request.method == 'POST':
            comment_form = CommentForm(data= self.request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.car = car
                new_comment.save()
                messages.success(self.request, 'Thanks for your opinion!')
            return self.get(request,*args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['car'] = self.get_object()
        context['comments'] = comments
        context['form'] = comment_form

        return context
    



    
