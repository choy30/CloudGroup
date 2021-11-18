from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.forms import BoatForm, UpdateBoatForm, RentForm
from blog.models import Boat, Rent


class HomeView(ListView):
    model = Boat
    template_name = 'home.html'
class BoatDetail(DetailView):
    model = Boat
    template_name = 'boat/boat_detail.html'
class MyBoat(ListView):
    model = Boat
    template_name = 'boat/myboat.html'
class AddBoatView(CreateView):
    model = Boat
    form_class = BoatForm
    template_name = 'boat/add_boat.html'
    success_url = reverse_lazy('my-boat')
class UpdateBoatView(UpdateView):
    model = Boat
    form_class = UpdateBoatForm
    template_name = 'boat/update_boat.html'
    success_url = reverse_lazy('my-boat')
class DeleteBoatView(DeleteView):
    model = Boat
    template_name = 'boat/delete_boat.html'
    success_url = reverse_lazy('my-boat')
class RentBoatView(DetailView,CreateView):
    model = Boat
    form_class = RentForm
    template_name = 'rent/rent_boat.html'
    success_url = reverse_lazy('rent-success')
def rent_success(request):
    return render(request, 'rent/rent_success.html')
class RentListView(ListView):
    model = Rent
    template_name = 'rent/rent_list.html'
    ordering = ['-id']
class DeleteRentView(DeleteView):
    model = Rent
    template_name = 'rent/rent_delete.html'
    success_url = reverse_lazy('rent-list')