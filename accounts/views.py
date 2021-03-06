from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, FormView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm

from .models import User
from .forms import UserAdminCreationForm
from checkout.models import Order

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/index.html'

class RegisterView(CreateView):

    model = User
    template_name = 'accounts/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')

class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    fields = ['name', 'email', 'cpf', 'gender', 'telephone', 'birth']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user

class UpdateAddressView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_address.html'
    fields = ['street', 'number', 'complement', 'district', 'city', 'state', 'zipcode']
    success_url = reverse_lazy('accounts:index')

    def get_object(self):
        return self.request.user

class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)

class OrderListView(LoginRequiredMixin, ListView):

    template_name = 'accounts/order_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetailView(LoginRequiredMixin, DetailView):

    template_name = 'accounts/order_detail.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_address = UpdateAddressView.as_view()
update_password = UpdatePasswordView.as_view()
order_list = OrderListView.as_view()
order_detail = OrderDetailView.as_view()