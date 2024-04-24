from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,View,UpdateView
from django.contrib.auth.views import LoginView,PasswordChangeView
from auth_app.forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from car_app.models import Order,Car

# Create your views here.

# User register implementation 
class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'auth_app/form.html'
    success_url = reverse_lazy('user_login')

    def form_invalid(self, form):
        messages.error(self.request, 'user register failed. try again!')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'user register successful!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Register"
        return context
    
    
# User login implementation 
class UserLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'auth_app/form.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'user logged in failed. please, provide valid information!')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'user logged in successful!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context
    
# User  logout implementation
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'logged out successfully')
        return redirect('user_login')

#Profile view  
@method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    def get(self,request):
        orders = Order.objects.filter(user = request.user)
        return render(request, 'auth_app/profile.html', {'orders': orders})
    
# Edit Profile
@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    template_name = 'auth_app/form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    fields = ['username', 'first_name', 'last_name', 'email']

    def form_valid(self, form):
        messages.success(self.request, 'User Updated SuccessFully Done!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong. try again.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Update"
        return context

@method_decorator(login_required, name='dispatch')
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'auth_app/change_password.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'User Password SuccessFully changed!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Something went wrong. try again.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Change Password"
        return context



# Buy Now    
def buy_now(request,id):
    ordered_car = Car.objects.get(id = id)

    if ordered_car.quantity > 0:
        ordered_car.quantity -= 1
        ordered_car.save()

        req_car = Order.objects.filter(user=request.user, car=ordered_car)

        if req_car.exists():
            order = req_car.first()
            order.quantity += 1
            order.save()
            messages.success(request, 'Order placed succesfully')
            return redirect('profile')
        else:
            order = Order.objects.create(user=request.user, car=ordered_car,quantity = 1)
            messages.success(request, 'Order placed succesfully')
            return redirect('profile')
    else:
        messages.error(request, 'Car is not available due to low quantity.')
        return render(request, 'car_app/car_details.html')
    
    